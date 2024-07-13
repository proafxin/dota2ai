# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import tomllib
from datetime import datetime
from os.path import abspath, dirname, join

cwd = dirname(abspath(__file__))
root = join(cwd, "../..")

sys.path.insert(0, root)


toml_file = join(root, "pyproject.toml")

with open(toml_file, "rb") as f:
    data = tomllib.load(f)
    project_data = data.get("project")
    if not isinstance(project_data, dict):
        raise ValueError("Check your pyproject.toml file")

    authors: list[dict[str, str]] = project_data["authors"]
    author_names = [author["name"] for author in authors]
    project: str = project_data["name"].upper()


VERSION = "1.1.0"
release = VERSION


author = ", ".join(author_names)
year = datetime.now().year
copyright = f"{year}, {author}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]

templates_path = ["_templates"]
exclude_patterns: list[str] = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"

html_theme_options: dict[str, str] = {}
html_context = {"default_mode": "dark"}

html_static_path: list[str] = []
