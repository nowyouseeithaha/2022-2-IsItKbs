# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'IsItKbs'
copyright = '2023, Douglas Alves, Sidney Fernando, Gabriel Campello, Rafael Ferreira, Arthur Grandao, Arthur de Melo, Paulo Victor'
author = 'Douglas Alves, Sidney Fernando, Gabriel Campello, Rafael Ferreira, Arthur Grandao, Arthur de Melo, Paulo Victor'
release = '1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys, os

# sys.path.append(os.path.abspath('isitkbs\\ks.py'))
sys.path.append(os.path.abspath('..\\..'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.todo']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
