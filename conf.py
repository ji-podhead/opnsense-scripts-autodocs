import os
import sys
sys.path.insert(0, os.path.abspath('./'))  # Source code dir relative to this file

extensions = [
    'sphinx.ext.autodoc',  # Core library for html generation from docstrings
    'sphinx.ext.autosummary',  # Create neat summary tables
'myst_parser',
    'sphinxarg.ext','sphinxcontrib.autoprogram']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
autosummary_generate = True  # Turn on sphinx.ext.autosummary
autodoc_mock_imports = ["queryInstalledRules",
                        "opnsense_scripts_autodoc.suricata.queryInstalledRule", 
                        "listRuleMetadata","listInstallableRulesets","installRules",
                        "interfaces","queryInstalledRules","queryAlertLog","listRuleMetadata",
                        "opnsense_scripts_autodoc.suricata.rule","opnsense_scripts_autodoc.surica",
                        "ujson","params" 'lib',"opnsense_scripts_autodoc.netflow.lib",
                        "opnsense_scripts_autodoc.suricata.lib","netaddr","log_helper",
                        "ping","list_arp","import opnsense_scripts_autodoc.suricata.queryAlertLog","results.scripts"
                        
                        ]
templates_path = ['_templates']

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "rightsidebar": "true",
    "relbarbgcolor": "black"
}

project = 'opnsense_helper'
copyright = '2024, ji-podhead'
author = 'ji-podhead'
release = '0.1.20'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


