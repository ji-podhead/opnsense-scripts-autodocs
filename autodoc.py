import os
from pathlib import Path
import ast
import shutil
import subprocess
import json

output = "/home/ji/Dokumente/ji-podhead/opnsense-scripts-autodoc/autodocs/autodocs"
php_path="/home/ji/Dokumente/ji-podhead/opnsense-scripts-autodoc/php_docstrings"
bashscript_path="/home/ji/Dokumente/ji-podhead/opnsense-scripts-autodoc/bashcript_docstrings"

argparse_process = """
import argparse
argObjects={}
ignoredkeys=["metavar", "container","nargs"]
replacements={
    "option_strings":"options",
    "action":"action",
    "const":"const",
    "default":"default",
    "type":"type",
    "choices":"choices",
    "help":"descriptions",
    "required":"required"
}
actions=parser.__dict__['_action_groups'][1].__dict__["_actions"]
for action in actions:
    if isinstance(action, argparse._StoreAction):
        action=action.__dict__
        argObjects[action["dest"]]=new_obj = {replacements.get(k, k): v for k, v in action.items() if k not in ignoredkeys}

print(json.dumps(argObjects))
"""


def create_main_function(directory):
    auto_module="""
    """
    for root, dirs, files in os.walk(directory):
        print("------------------------")
        print(root)
        print("------------------------")
        subfolder_path = os.path.join(output, root.split("/")[-1])
        module_path = subfolder_path.split("/")[-1]
        print(module_path)
        if (module_path!="opnsense_scripts_autodoc"):
            auto_module+=f"""
.. toctree:: {module_path}

{module_path}
======================================

        """ 
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        for file in files:
            print("-------------")
            script_path = os.path.join(root, file)
            if file.endswith('.py') and file != "args_parser.py":
                print(file)
                parsecode = []
                with open(script_path, 'r') as f:
                    content = f.read()
                    tree = ast.parse(content)
                    for node in ast.walk(tree):
                        if node.__dict__ != {}: 
                            if "id"  in node.__dict__.keys():
                              if (node.__dict__["id"] == 'parser' ):#or node.__dict__["id"] == 'argparse' or node.__dict__["id"] == 'args':
                                print("----------------------------------")
                                #print(node.__dict__)
                                startline=node.__dict__["lineno"]
                                endline=node.__dict__["end_lineno"]
                                lines = content.split('\n')[startline-1:endline]
                                text = '\n'.join(lines)
                                if("subparser" not in text and "print_help()" not in text):
                                    parsecode.append(text.lstrip())
                if len(parsecode)>0 :
                    print(parsecode)
                    parsecode.insert(0, "import argparse")
                    parsecode.insert(0, "import json")
                    parsecode.append(argparse_process)
                    parsecode="\n".join(parsecode).replace("args = parser.parse_args()","")
                    parsecode=parsecode.lstrip()
                    print(parsecode)
                    with open("args_parser.py", "w") as f:
                        f.write(parsecode)
                    try:      
                        parameters = subprocess.check_output(["python", "args_parser.py"]).decode("utf-8")
                        parameters=json.loads(parameters)
                        print((parameters))
                        string="\"\"\""
                        string +=  f"""
script {file}
------------------------------------------

*Parameters*
                        """
                        if(len(parameters)>0):
                            for name,parameter in parameters.items():
                                string +=  f"""
* {name} : {parameter["type"] if "type" in parameter and parameter["type"]!= None  else "str"}
    * Description: {parameter["descriptions"] if "descriptions" in parameter else "-"}""" 
                                for key,value in parameter.items():
                                    if(key in ["descriptions","type","dest"] or value == None):continue
                                    string +=  f""" 
    * {key} : {value}"""
                                                          
                        else:
                            string +=  f"""
None
                        """    
                        string += """
\"\"\"                  """
                        with open(subfolder_path+"/"+file, 'w') as f:
                            f.write(string)
                        auto_module += f"""    
.. automodule:: {module_path}.{file.replace(".py","")}
"""
                    except(subprocess.CalledProcessError) as err:
                        print( err)
            elif file.endswith('.sh'):
                with open(bashscript_path+"/"+file, 'r') as f:
                    content = f.read()
                    string="""
\"\"\""""
                    string += content.replace("# ","").replace("#","")
                    string = string.replace("!/bin/sh","")
                    string = string.replace("---------------","------------------------------")
                    string = string.replace(" script","script")
                    string = string.replace(" --","--")
                    string+="""
\"\"\""""
                    with open(subfolder_path+"/"+file.replace(".sh",".py"), 'w') as f:
                        f.write(string)
                #shutil.copy(bashscript_path+"/"+file, subfolder_path)
                auto_module += f"""    
.. automodule:: {module_path}.{file.replace(".sh","")}
"""
            elif file.endswith('.php'):
                with open(php_path+"/"+file, 'r') as f:
                    content = f.read()
                    content = content.split("\n")
                    content= [line for line in content if line not in ["#!/usr/local/bin/php","<?php","/**"," */"]]
                    content = [line.replace(" *", "", 1)[1:] for line in content]
                    
                    content.insert(0,"\"\"\"")
                    string="\n".join(content)
                    string =string.replace(" ---","---")
                    string =string.replace("-------","----------------------------------").lstrip()
                    
                    # string =string.replace("Description*","*Description*").replace("Arguments","*Arguments*").replace("Returns","*Returns*")
                    string+="""
\"\"\""""
                    with open(subfolder_path+"/"+file.replace(".php",".py"), 'w') as f:
                        f.write(string)
                #shutil.copy(php_path+"/"+file,subfolder_path)
                auto_module += f"""
.. automodule:: {module_path+"."+file.replace(".php","")}
"""
    print(auto_module)
    with open(".docs/docs.rst", 'w') as f:
        f.write(auto_module)
directory = "./src/opnsense_scripts_autodoc" #input("Geben Sie den Pfad zum Hauptverzeichnis ein: ")
create_main_function(directory)