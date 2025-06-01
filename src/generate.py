import argparse
import os
import re
import shutil
import pathlib

import yaml
import markdown

from collections import namedtuple
import urllib.parse

from jinja2 import Environment, FileSystemLoader


class Filters:

    @classmethod
    def join_paths(cls, a, b):
        a = pathlib.Path(a)
        b = pathlib.Path(b)
        return str(a.joinpath(b.relative_to(b.anchor) if b.is_absolute() else b))

    @classmethod
    def absolute_url(cls, base_url, path):
        parsed_url = urllib.parse.urlparse(base_url, allow_fragments=False)
        new_path = cls.join_paths(parsed_url.path, path)
        return urllib.parse.urlunparse(
            (
                parsed_url.scheme or "http",
                parsed_url.netloc,
                new_path,
                parsed_url.params,
                parsed_url.query,
                parsed_url.fragment,
            )
        )


from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension


class RemoveMdExtensionTreeprocessor(Treeprocessor):

    def __init__(self, md, base_url, dir_path):
        super().__init__(md)
        self.base_url = urllib.parse.urlparse(base_url)
        self.dir_path = dir_path

    def run(self, root):
        """Iterate over all <a> tags in the HTML tree and remove `.md` from
        their href. If the link is in a relative directory, resolve the full
        link using base URL"""
        for element in root.iter("a"):
            href = element.get("href")
            if href and href.endswith(".md") and not href.startswith("http"):
                full_path = os.path.normpath(
                    os.path.join(self.base_url.path, self.dir_path, href)
                )
                print("href, full_path:", href, full_path)
                target = urllib.parse.urlunparse(
                    (
                        self.base_url.scheme or "http",
                        self.base_url.netloc,
                        full_path,
                        self.base_url.params,
                        self.base_url.query,
                        self.base_url.fragment,
                    )
                )
                if target.endswith("/index.md"):
                    target = target[:-9]
                else:
                    # Strip off the last 3 chars (".md")
                    target = target[:-3]
                element.set("href", target)


class RemoveMdExtension(Extension):

    def __init__(self, base_url, dir_path):
        super().__init__()
        self.base_url = base_url
        self.dir_path = dir_path

    def extendMarkdown(self, md):
        print("base_url, dir_path", self.base_url, self.dir_path)
        md.treeprocessors.register(
            RemoveMdExtensionTreeprocessor(md, self.base_url, self.dir_path),
            "remove_md_extension",
            priority=15,
        )


def replace_extension(filename, old, new):
    parts = filename.rsplit(
        f".{old}", 1
    )  # Split from the right, at most once, gives [name, '']
    return f".{new}".join(parts)


def title_from_filename(filename):
    return replace_extension(filename, "md", "")


def render_file(input_path, output_path, env, page_context={}):
    filename = os.path.basename(input_path)

    # Create necessary subdirectories in output_path
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to detect YAML front matter
    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)

    # Parse the front matter
    if match:
        front_matter = yaml.safe_load(match.group(1))  # Parse YAML
        md_content = match.group(2)  # Extract Markdown part
    else:
        front_matter = {}
        md_content = content

    # Get the template from the front matter
    template_name = front_matter.get("template", "base.html")
    template = env.get_template(template_name)

    # Convert Markdown to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=[
            "tables",
            "toc",
            "attr_list",
            RemoveMdExtension(
                page_context.get("base_url"), page_context.get("dir_path")
            ),
        ],
    )

    # Wrap with a template
    page_context = page_context.copy()
    page_context.update(
        {
            "content": html_content,
            "title": front_matter.get("title", title_from_filename(filename)),
        }
    )
    final_html = template.render(**page_context)

    # Write to output file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)


ConversionResult = namedtuple("ConversionResult", ["converted", "skipped"])


import os
import shutil


def render_markdown(input_dir, output_dir, env, page_context={}) -> ConversionResult:
    converted = 0
    skipped = 0

    for root, _, files in os.walk(input_dir):
        for filename in files:
            input_path = os.path.join(root, filename)
            # Determine the relative path (directory structure under input_dir).
            relative_path = os.path.relpath(os.path.dirname(input_path), input_dir)

            # Decide how to handle the file.
            if filename == "index.md":
                # Special case index.md to turn into index.html in the exact same location
                output_path = os.path.join(output_dir, relative_path, "index.html")
                should_render = True
            elif filename.endswith(".md"):
                # Instead of simply replacing .md with .html, place it in:
                #
                #   output_dir / relative_path / [filename-without-.md] / index.html
                #
                folder_name = os.path.splitext(filename)[0]  # remove .md
                output_path = os.path.join(
                    output_dir, relative_path, folder_name, "index.html"
                )
                should_render = True

            elif filename.endswith(".jinja2"):
                # No change for jinja2 behavior:
                output_filename = filename[:-7]  # remove '.jinja2'
                output_path = os.path.join(output_dir, relative_path, output_filename)
                should_render = True

            else:
                # All other files are copied as-is (unchanged behavior):
                output_path = os.path.join(output_dir, relative_path, filename)
                should_render = False

            # Normalize the path (important on Windows, but generally good practice).
            output_path = os.path.normpath(output_path)

            # Render if needed; otherwise just copy the file.
            if should_render:
                # Ensure the parent directory (or in the case of .md, the subfolder) exists.
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                context = page_context.copy()
                context["dir_path"] = relative_path
                render_file(input_path, output_path, env, page_context=context)
                converted += 1
            else:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                shutil.copy(input_path, output_path)
                skipped += 1

    return ConversionResult(converted, skipped)


def main():
    # Default paths and context
    CONFIG_PATH_DEFAULT = "config.yaml"
    INPUT_DIR_DEFAULT = "content"
    TEMPLATE_DIR_DEFAULT = "templates"
    OUTPUT_DIR_DEFAULT = "output_html"
    CONTEXT_DEFAULT = {"base_url": "http://localhost:8000"}

    # Argument parsing
    parser = argparse.ArgumentParser(
        description="Process configuration and override context values."
    )
    parser.add_argument(
        "--config",
        type=str,
        default=CONFIG_PATH_DEFAULT,
        help="Path to the config file.",
    )
    parser.add_argument(
        "--input-dir", type=str, default=None, help="Path to the input directory."
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Path to the output directory for rendering.",
    )
    parser.add_argument(
        "--template-dir",
        type=str,
        default=None,
        help="Path to the directory containing jinja2 templates.",
    )
    parser.add_argument(
        "--context",
        nargs=2,
        action="append",
        metavar=("KEY", "VALUE"),
        help="Override context values in config, e.g., --context base_url example.com",
    )
    args = parser.parse_args()

    # Load YAML config
    print(f"Loading configuration from {args.config}")
    with open(args.config, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # Set defaults
    config.setdefault("input_dir", INPUT_DIR_DEFAULT)
    config.setdefault("template_dir", TEMPLATE_DIR_DEFAULT)
    config.setdefault("output_dir", OUTPUT_DIR_DEFAULT)
    config.setdefault("context", CONTEXT_DEFAULT.copy())

    # Override directories from config root with CLI args, if given
    if args.input_dir:
        config["input_dir"] = args.input_dir
    if args.template_dir:
        config["template_dir"] = args.template_dir
    if args.output_dir:
        config["output_dir"] = args.output_dir

    # Override context values if provided
    if args.context:
        for key, value in args.context:
            config["context"][key] = value

    # Load Jinja2 templates
    env = Environment(loader=FileSystemLoader(config["template_dir"]))
    env.filters["absolute_url"] = lambda x: Filters.absolute_url(
        config["context"]["base_url"], x
    )

    # Ensure output directory exists
    os.makedirs(config.get("output_dir"), exist_ok=True)

    # Render the markdow and copy assets
    res = render_markdown(
        config.get("input_dir"),
        config.get("output_dir"),
        env,
        page_context=config.get("context"),
    )
    print(f"Converted {res.converted} files, copied {res.skipped} non-input files")

    versions = config["context"].get("versions", [])
    current_version = config["context"].get("current_version", "")
    for version in versions:
        if current_version and version.get("version", "") != current_version:
            continue
        print(version)
        output_path = os.path.join(config.get("output_dir"), version["path"], "index.html")
        output_index = os.path.join(config.get("output_dir"), "index.html")
        print(f"Will copy {output_index} to {output_path}")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        shutil.copy(output_index, output_path)

if __name__ == "__main__":
    main()
