import os
import sys
sys.path.insert(0, os.path.abspath('../autodocs/autodocs'))  # Source code dir relative to this file

extensions = [
    'sphinx.ext.autodoc',  # Core library for html generation from docstrings
    'sphinx.ext.autosummary',  # Create neat summary tables
    'myst_parser',
    'sphinxarg.ext','sphinxcontrib.autoprogram',

    ]
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
autosummary_generate = True  # Turn on sphinx.ext.autosummary
#autodoc_mock_imports = [                        ]
templates_path = ['_templates']

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "rightsidebar": "true",
    "relbarbgcolor": "black"
}

project = 'opnsense-scripts-autodoc'
author = 'ji-podhead'
release = '0.1.0'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
