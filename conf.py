# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'flmidi-101'
copyright = '2020, Hobyst & flmidi-101 contributors'
author = 'Hobyst & flmidi-101 contributors'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.githubpages', 'sphinx.ext.autodoc', 'recommonmark', 'sphinx_markdown_tables']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Typlog theme
html_theme = 'sphinx_typlog_theme'

html_theme_options = {
    'logo': 'icon.svg',
    'color': '#e96915',
    'description': 'A comprehensive guide for FL Studio MIDI scripting',
    'github_user': 'hobyst',
    'github_repo': 'flmidi-101',
    'meta_html': '<meta name="generator" content="sphinx">',
    'warning': 'This guide is still under-development.',
}

html_sidebars = {
    '**': [
        'logo.html',
        'github.html',
        'globaltoc.html',
        'searchbox.html',
    ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']