"""Generate the Sphinx notebook pages from the canonical example notebooks."""

import copy
import glob
import os
import re
import warnings

import nbformat
from nbconvert.exporters import rst


warnings.simplefilter("ignore")


GENERATED_SOURCE_DIR = "examples/generated"
NBVIEWER_BASE_URL = (
    "https://nbviewer.org/github/Unidata/python-awips/blob/v23/examples/notebooks/"
)
PUBLISHED_BASE_URL = "https://unidata.github.io/python-awips/examples/generated"

_HEADING_RE = re.compile(r"^(#{2,4})\s+(.+?)\s*$", re.MULTILINE)
_ALERT_RE = re.compile(
    r'<div\s+class=["\\]*alert-(?:info|warning|danger|success)["\\]*>\s*'
    r"(.*?)\s*</div>",
    re.DOTALL | re.IGNORECASE,
)


def setup(app):
    app.connect("builder-inited", generate_rst)

    return {
        "version": "0.2",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def _canonical_notebook_dir():
    """Return the repository-level examples/notebooks directory."""
    repository_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    )
    return os.path.join(repository_root, "examples", "notebooks")


def _normalise_markdown(source):
    """Normalise escaped HTML stored by some notebook editors."""
    return source.replace(r'\"', '"').replace(r"\n", "\n")


def _slugify(title):
    """Create the same simple section fragment used by the generated pages."""
    title = re.sub(r"<[^>]+>", "", title)
    title = re.sub(r"[*_`]", "", title)
    title = re.sub(r"[^A-Za-z0-9\s-]", "", title).strip().lower()
    return re.sub(r"[\s-]+", "-", title)


def _number_headings(notebook):
    """Number level 2-4 Markdown headings and return their TOC entries."""
    counters = [0, 0, 0]
    entries = []

    for cell in notebook.cells:
        if cell.cell_type != "markdown":
            continue

        def replace_heading(match):
            level = len(match.group(1))
            title = match.group(2).strip()
            index = level - 2
            counters[index] += 1
            for deeper in range(index + 1, len(counters)):
                counters[deeper] = 0

            number = ".".join(str(value) for value in counters[: index + 1])
            entries.append((level, number, title, _slugify(title)))
            return f"{'#' * level} {number} {title}"

        cell.source = _HEADING_RE.sub(replace_heading, cell.source)

    return entries


def _make_toc(entries, page_url):
    """Build the website table of contents used by the current pages."""
    lines = ["## Table of Contents", ""]
    for level, number, title, fragment in entries:
        indent = "&nbsp;" * (4 * (level - 2))
        lines.append(
            f"{indent}[{number} {title}]({page_url}#{fragment})<br>  "
        )
    return "\n".join(lines)


def _convert_alert(match):
    """Convert notebook HTML alert boxes to Markdown block quotes for RST."""
    body = match.group(1)
    body = body.replace(r'\"', '"').replace(r"\n", "\n")
    body = re.sub(r"<b>(.*?)</b>", r"**\1**", body, flags=re.DOTALL)
    body = re.sub(r"<code>(.*?)</code>", r"``\1``", body, flags=re.DOTALL)
    body = re.sub(r"<i>(.*?)</i>", r"*\1*", body, flags=re.DOTALL)
    body = re.sub(
        r'<a\s+href="([^"]+)">\s*(.*?)\s*</a>',
        r"[\2](\1)",
        body,
        flags=re.DOTALL,
    )
    body = re.sub(r"</?li>", "", body)
    body = re.sub(r"<br\s*/?>", "\n", body)
    body = re.sub(r"<[^>]+>", "", body)
    body = "\n".join(line.strip() for line in body.splitlines()).strip()
    return "\n".join(f"> {line}" if line else ">" for line in body.splitlines())


def _prepare_notebook(notebook, basename):
    """Create an in-memory website version without changing the notebook."""
    notebook = copy.deepcopy(notebook)
    page_url = f"{PUBLISHED_BASE_URL}/{basename}.html"
    toc_cell_index = None

    for index, cell in enumerate(notebook.cells):
        if cell.cell_type != "markdown":
            continue

        cell.source = _normalise_markdown(cell.source)

        # Sphinx supplies the page title. Retain only the tutorial subtitle and
        # the Objectives section from the notebook's branded opening cell.
        if index == 0 and "# Objectives" in cell.source:
            objectives = cell.source.split("# Objectives", 1)[1]
            cell.source = (
                "Python-AWIPS Tutorial Notebook\n\n---\n\n"
                f"# Objectives{objectives}"
            )

        if "<h1>Table of Contents" in cell.source:
            toc_cell_index = index

        cell.source = re.sub(
            r'<a\s+href="#top">Top</a>',
            f"[Top]({page_url})",
            cell.source,
            flags=re.IGNORECASE,
        )
        cell.source = _ALERT_RE.sub(_convert_alert, cell.source)

    entries = _number_headings(notebook)
    if toc_cell_index is not None:
        notebook.cells[toc_cell_index].source = _make_toc(entries, page_url)

    # A final Markdown horizontal rule becomes an invalid trailing RST
    # transition. Remove it from the website-only notebook copy.
    for cell in reversed(notebook.cells):
        if cell.cell_type == "markdown":
            cell.source = re.sub(r"\n\s*---\s*$", "", cell.source).rstrip()
            break
    return notebook


def nb_to_rst(nb_path):
    """Convert a canonical example notebook to reStructuredText."""
    basename = os.path.splitext(os.path.basename(nb_path))[0]
    with open(nb_path, encoding="utf-8") as notebook_file:
        notebook = nbformat.read(notebook_file, as_version=4)

    notebook = _prepare_notebook(notebook, basename)
    exporter = rst.RSTExporter()
    output, resources = exporter.from_notebook_node(notebook)

    image_directory = basename + "_files"
    image_prefix = os.path.join(image_directory, basename + "_")
    resources["metadata"]["basename"] = basename
    resources["metadata"]["name"] = basename.replace("_", " ")
    resources["metadata"]["imgdir"] = image_directory

    notebook_url = NBVIEWER_BASE_URL + os.path.basename(nb_path)
    output_lines = [f"`Notebook <{notebook_url}>`_"]
    for line in output.split("\n"):
        if line.startswith(".. image:: "):
            line = line.replace("output_", image_prefix)
        output_lines.append(line)

    return "\n".join(output_lines), resources


def write_nb(destination, output, resources):
    os.makedirs(destination, exist_ok=True)
    rst_file = os.path.join(
        destination,
        resources["metadata"]["basename"] + resources["output_extension"],
    )
    name = resources["metadata"]["name"]
    with open(rst_file, "w", encoding="utf-8") as rst_file_handle:
        header = "=" * len(name)
        rst_file_handle.write(header + "\n")
        rst_file_handle.write(name + "\n")
        rst_file_handle.write(header + "\n")
        rst_file_handle.write(output)

    image_directory = os.path.join(
        destination, resources["metadata"]["imgdir"]
    )
    os.makedirs(image_directory, exist_ok=True)
    basename = resources["metadata"]["basename"]
    for filename, image_data in resources["outputs"].items():
        image_file = os.path.join(
            image_directory, filename.replace("output_", basename + "_")
        )
        with open(image_file, "wb") as image_file_handle:
            image_file_handle.write(image_data)


def generate_rst(app):
    destination = os.path.join(app.srcdir, GENERATED_SOURCE_DIR)
    notebook_pattern = os.path.join(_canonical_notebook_dir(), "*.ipynb")
    for filename in sorted(glob.glob(notebook_pattern)):
        write_nb(destination, *nb_to_rst(filename))

