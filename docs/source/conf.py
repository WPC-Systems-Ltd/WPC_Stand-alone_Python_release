# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import datetime
#from WPC_config import __version__
sys.path.append('.')

# -- Project information -----------------------------------------------------

project = 'WPC Stand-alone Python'
copyright = '2023, WPC Systems Ltd.'
author = 'WPC Systems Ltd.'

# The full version, including alpha/beta/rc tags
version = "0.0.13"
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'numpydoc',
  'sphinx.ext.duration',
  'sphinx.ext.githubpages',
  'breathe',
]
################################################################################
## Options for breathe

breathe_projects = {project: '../xml/'}
breathe_default_project = project
breathe_default_members = ('members', 'undoc-members')
breathe_show_define_initializer = True
breathe_show_enumvalue_initializer = True
breathe_show_include = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo = "images/WPC-logo.PNG"
html_favicon =  "images/WPC-trademark.jpg"
html_theme_options = {
    'logo_only': False,
    'display_version': True,
}

html_show_sourcelink = False
# html_context = {
#   'display_github': True,
#   'github_user': 'WPC-Systems-Ltd',
#   'github_repo': 'WPC_Device_Driver',
#   'github_version': 'main/docs/source/',
# }

def setup(app):
    app.add_css_file('custom_sphinx.css')

html_static_path = ['_static']
numpydoc_show_class_members = False
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
