import argparse
import os
import re
import shutil
import pathlib

import yaml
import markdown

from collections import namedtuple
import urllib.parse
import urllib.request

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


ALERT_TYPES = {
    "NOTE": ("Note", "<svg viewBox=\"0 0 16 16\" width=\"16\" height=\"16\" fill=\"currentColor\"><path d=\"M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25V8.5h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z\"></path></svg>"),
    "TIP": ("Tip", "<svg viewBox=\"0 0 16 16\" width=\"16\" height=\"16\" fill=\"currentColor\"><path d=\"M8 1.5c-2.363 0-4 1.69-4 3.75 0 .984.424 1.625.984 2.304l.214.253c.223.264.47.556.673.868.347.533.629 1.157.629 1.825v.75h3v-.75c0-.668.282-1.292.629-1.825.203-.312.45-.604.673-.868l.214-.253c.56-.679.984-1.32.984-2.304 0-2.06-1.637-3.75-4-3.75ZM4.5 11.75c0-.138.112-.25.25-.25h6.5a.25.25 0 0 1 .25.25v.5a.25.25 0 0 1-.25.25h-6.5a.25.25 0 0 1-.25-.25v-.5ZM6 13.75c0-.138.112-.25.25-.25h3.5a.25.25 0 0 1 .25.25v.25a1.25 1.25 0 0 1-1.25 1.25h-1.5A1.25 1.25 0 0 1 6 14.00v-.25Z\"></path></svg>"),
    "IMPORTANT": ("Important", "<svg viewBox=\"0 0 16 16\" width=\"16\" height=\"16\" fill=\"currentColor\"><path d=\"M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z\"></path></svg>"),
    "WARNING": ("Warning", "<svg viewBox=\"0 0 16 16\" width=\"16\" height=\"16\" fill=\"currentColor\"><path d=\"M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z\"></path></svg>"),
    "CAUTION": ("Caution", "<svg viewBox=\"0 0 16 16\" width=\"16\" height=\"16\" fill=\"currentColor\"><path d=\"M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.141.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z\"></path></svg>")
}

import xml.etree.ElementTree as ET

class GitHubAlertsTreeprocessor(Treeprocessor):
    def run(self, root):
        for bq in root.iter("blockquote"):
            first_p = bq.find("p")
            if first_p is not None and first_p.text:
                text = first_p.text.strip()
                for alert_key, (title, svg) in ALERT_TYPES.items():
                    tag = f"[!{alert_key}]"
                    if text.startswith(tag):
                        bq.attrib["class"] = f"markdown-alert markdown-alert-{alert_key.lower()}"
                        remainder = text[len(tag):].lstrip()
                        first_p.text = remainder
                        
                        title_p = ET.Element("p", {"class": "markdown-alert-title"})
                        svg_elem = ET.fromstring(svg)
                        title_p.append(svg_elem)
                        svg_elem.tail = f" {title}"
                        bq.insert(0, title_p)
                        break

class GitHubAlertsExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(GitHubAlertsTreeprocessor(md), "github_alerts", priority=20)


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
            GitHubAlertsExtension(),
            RemoveMdExtension(
                page_context.get("base_url"), page_context.get("dir_path")
            ),
        ],
        extension_configs={
            "toc": {
                "toc_depth": "3-3",
            }
        },
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

    # Fetch latest cosigners.json at build time for fallback
    try:
        req = urllib.request.Request("https://www.gstatic.com/mtcs/cosigners/v1/cosigners.json", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            fallback_bytes = resp.read()
            static_dir = os.path.join(config.get("output_dir"), "static")
            os.makedirs(static_dir, exist_ok=True)
            with open(os.path.join(static_dir, "cosigners_fallback.json"), "wb") as f:
                f.write(fallback_bytes)
            print("Successfully saved static/cosigners_fallback.json for build fallback")
    except Exception as e:
        print(f"Warning: Could not fetch cosigners.json at build time ({e})")

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
        output_policy = os.path.join(config.get("output_dir"), "crp", "policy", "index.html")
        print(f"Will copy {output_policy} to {output_path}")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        shutil.copy(output_policy, output_path)

if __name__ == "__main__":
    main()
