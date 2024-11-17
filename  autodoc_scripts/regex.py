import os
import re
from pathlib import Path
import ast#import shutil
import shutil
import json
output = "/home/ji/Dokumente/ji-podhead/opnsense-scripts-autodoc/results"
php_path="/home/ji/Dokumente/ji-podhead/opnsense-scripts-autodoc/php_docstrings"
bashscript_path="/home/ji/Dokumente/ji-podhead/opnsense-scripts-autodoc/src/opnsense_scripts_autodoc/bashcripts"
def create_main_function(directory):
    for root, dirs, files in os.walk(directory):
        print("------------------------")
        print(root)
        print("------------------------")
        subfolder_path = os.path.join(output, root.split("/")[-1])
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        for file in files:
            print("-------------")
            script_path = os.path.join(root, file)

            if file.endswith('.py'):
                print(file)
                parameters = []
                with open(script_path, 'r') as f:
                    content = f.read()
                    tree = ast.parse(content)

                    for node in ast.walk(tree):
                        if node.__dict__ != {}: 
                            #print(node.__dict__)
                            if "id"  in node.__dict__.keys():
                              if (node.__dict__["id"] == 'parser'):#or node.__dict__["id"] == 'argparse' or node.__dict__["id"] == 'args':
                                #print(node.__dict__)
                                startline=node.__dict__["lineno"]
                                endline=node.__dict__["end_lineno"]
                                lines = content.split('\n')[startline-1:endline]
                                text = '\n'.join(lines)
                                match = re.search(r'^parser\.add_argument\(\'.*\)', text, re.MULTILINE)
                                if match:

                                    result = match.group()
                                    pattern_alias = r"'-([^']*)'," # add --
                                    matches = re.findall(pattern_alias, result)
                                    if matches:
                                        argument={
                                                "arg":None,
                                                "alias": None,
                                            }
                                        for res in matches:
                                            if("-" in res):
                                                argument["alias"]="-"+res
                                            else:
                                                argument["arg"]="-"+res
                                            res="\'-"+res+"\',"
                                            result=result.replace(res,"")
                                        
                                        result=result.replace("parser.add_argument(","")
                                        
                                        result=(result[:-1]).split(",")
                                        print(result)
                                        for res in result:
                                            
                                            print(res)
                                            if("=" in res):
                                                res=res.split("=")
                                                argument[res[0].replace(" ","")]=res[1].replace("\"","").replace("\'","")

                                        print("-------------------")
                                        # print(result)
                                        # result=json.loads(result)
                                        # print(result)
                                        # print(matches)
                                        #print(argument)
                                            
                                        
                                      

                                       # print(argument)
                                        parameters.append(argument)

                print(parameters)
                string="\"\"\""
                string +=  f"""
script {file}
------------------------------------------

*Parameters*

"""
                if(len(parameters)>0):
                    for parameter in parameters:
                        string +=  f"""
*{parameter["arg"]}* : {parameter["type"] if "type" in parameter and parameter["type"]!= None  else "str"}
    { ("Alias: " + parameter["alias"]) if "alias" in parameter and parameter["alias"]!= None  else "" }
    { ("info: " + parameter["help"]) if "help" in parameter and parameter["help"]!= None   else ""}
    {  ( "required: "+ parameter["required"]) if "required" in parameter and parameter["required"]!= None else ""}
    { ("default: " + parameter["default"]) if "default" in parameter and parameter["default"]!= None  else  ""}
"""
                               
                else:
                    string +=  f"""
None

"""    
                string += "\"\"\""

                with open(subfolder_path+"/"+file, 'w') as f:
                    f.write(string)
            elif file.endswith('.sh'):
                shutil.copy(bashscript_path+"/"+file, subfolder_path)
            elif file.endswith('.php'):
                shutil.copy(php_path+"/"+file,subfolder_path)

                # Finden Sie die Zeilen, die mit "parser.add_argument" beginnen
                # arg_lines = [line.strip() for line in content.split('\n') if line.startswith('parser.add_argument')]

                # # Extrahieren Sie die Argumentnamen und Default-Werte
                # args = []
                # for line in arg_lines:
                #     #^wp.*php$
                #     match = re.search(r'^parser\.add_argument\(\'.*\)',line)
                #     #re.search(r'parser\.add_argument(.+?)#', line, re.DOTALL)
                #     #match = re.search(r'parser\.add_argument\((\'|")(.+?)\'|\"),\s*help\s*=\s*(\'|")(.+?)\s*,\s*default\s*=\s*(.+?)\s*\)', line)
                #     #match = re.search(r'--(\w+),\s*help\s*=\s*(\'|")(.+?)\s*,\s*default\s*=\s*(.+?)\s*\)', line)
                    
                #     if match:
                #          print(match.group(0))
                #         args.append({
                #             'name': match.group(1),
                #             'help': match.group(2).strip("'"),
                #             'default': match.group(3)
                #         })
                # print(args)
                # # Erstellen Sie die main() Funktion
                # new_content = f"""  {', '.join([{arg["name"]}, {arg["help"]}, {arg["default"]}] for arg in args)}"""
                # print(file)
                # print(new_content)
# if __name__ == '__main__':
#     main()
# """

#                 # Überprüfen Sie, ob eine main() Funktion bereits existiert
#                 if 'def main():' in content:
#                     print(f"Ungültiges Skript gefunden: {script_path}")
#                     continue

#                 # Schreiben Sie die neue main() Funktion ins Skript
#                 with open(script_path, 'w') as f:
#                     f.write(new_content)

#                 print(f"Neue main() Funktion erstellt für: {script_path}")

# Verwendung des Skripts
directory = "./" #input("Geben Sie den Pfad zum Hauptverzeichnis ein: ")
create_main_function(directory)