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
        return urllib.parse.urlunparse((
            parsed_url.scheme or "http",
            parsed_url.netloc,
            new_path,
            parsed_url.params,
            parsed_url.query,
            parsed_url.fragment,
        ))

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
    html_content = markdown.markdown(md_content, extensions=['tables', 'toc', 'attr_list'])

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


def render_markdown(input_dir, output_dir, env, page_context={}) -> ConversionResult:
    converted = 0
    skipped = 0
    for root, _, files in os.walk(input_dir):
        for filename in files:
            # Only Markdown files will have their extension changed, everything
            # else is copied.
            input_path = os.path.join(root, filename)
            should_render = False
            if filename.endswith(".md"):
                output_filename = replace_extension(filename, "md", "html")
                should_render = True
            elif filename.endswith(".jinja2"):
                should_render = True
                output_filename = filename[:-7]
            else:
                output_filename = filename
            relative_path = os.path.relpath(os.path.dirname(input_path), input_dir)
            output_path = os.path.normpath(
                os.path.join(output_dir, relative_path, output_filename)
            )

            # Only Markdown files are rendered.
            if should_render:
                render_file(input_path, output_path, env, page_context=page_context)
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
    parser = argparse.ArgumentParser(description="Process configuration and override context values.")
    parser.add_argument("--config", type=str, default=CONFIG_PATH_DEFAULT, help="Path to the config file.")
    parser.add_argument("--input-dir", type=str, default=None, help="Path to the input directory.")
    parser.add_argument("--output-dir", type=str, default=None, help="Path to the output directory for rendering.")
    parser.add_argument("--template-dir", type=str, default=None, help="Path to the directory containing jinja2 templates.")
    parser.add_argument("--context", nargs=2, action="append", metavar=("KEY", "VALUE"),
                        help="Override context values in config, e.g., --context base_url example.com")
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
        config['input_dir'] = args.input_dir
    if args.template_dir:
        config['template_dir'] = args.template_dir
    if args.output_dir:
        config['output_dir'] = args.output_dir


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


if __name__ == "__main__":
    main()
