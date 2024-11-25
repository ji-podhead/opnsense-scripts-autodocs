#!/usr/local/bin/python3.11
import ast
import re
import shlex
import subprocess
import sys
import tempfile
from ast import unparse
import os
import astpretty
import rich
from cleez.colors import red

from php2py.parser import parse
from php2py.translator import Translator

#with open("/home/ji/Dokumente/ji-podhead/opnsense-scripts-autodoc/src/opnsense_scripts_autodoc/health/updaterrd.php", 'r') as f:
script_path = os.path.join(os.getcwd(), "")
print(script_path)
#content = f.read()
#php_ast = ast.parse(content)
php_ast=parse(script_path)
translator= Translator().translate_root(php_ast)
print(translator)

