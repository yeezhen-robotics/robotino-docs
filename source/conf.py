# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import datetime

project = 'Robotino-PicoScan-Quickstart-Guide'
copyright = '2026, Bristol Robotics Laboratory'
author = 'Khoo Yee Zhen'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = ['custom.css']
html_favicon = '_static/images/favicon.ico'

# -- Extras ------------------------------------------------------------------
# This block adds the block to automatically display the current date
html_last_updated_fmt = None  # disable the default
rst_epilog = f"""
.. |last_updated| replace:: {datetime.now().strftime("%d/%m/%Y %H:%M")}
"""