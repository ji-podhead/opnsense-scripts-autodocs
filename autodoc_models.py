import json
import xml.etree.ElementTree as ET
import os
import logging
import pprint
import datetime as dt
root_dir = './opnsense_models/Firewall'
result_dir = './autodocs/models'
class_infos = {}
subclasses={}
scripts=[]
children=[]
ignore=["Constraints","Mask","ValidationMessage","Multiple","Required","Default"]
def check_if_exists(class_name):
     if class_name in class_infos:
        return logging.error(f"script is overwriting class: {class_name}")
     else:
        return False

def recursive_iterate_xml_files(xml_root, classProto, script):
                
    def re(obj,elem):
        obj["value"]["instance"]="_"+elem.tag
        obj["type"]="instance_list"
        proto={
        "name": dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        "id":"_"+elem.tag,
        "proto_attrib": xml_root.attrib,
        "subelements":[],
        }
        
        class_infos[name]=proto
        script["classes"].append(obj["name"])
        print(elem.text)
        recursive_iterate_xml_files(elem,proto,script)
    for elem in xml_root:
            
        name = "_"+elem.tag
        obj={
                'name':  name,
                'type':  elem.attrib.get('type'),
                'default':  elem.find('Default').text if elem.find('Default') is not None else False,
                'required':  elem.find('Required').text if elem.find('Required') is not None else False,
                'multiple':  elem.find('Multiple').text if elem.find('Multiple') is not None else False,
                "value": {},
                "info": "",
                "subclasses":[]
            }
        if obj["name"] not in ignore:
            if(obj["required"]=="Y"):   
                obj["required"] = True
            else:
                obj["required"] = False
            child=elem.find("Model")
            child and print(f"""child:  {child}""")
            text=(elem.text.split("\n")[0].split(" ")[0]) if elem.text is not None else ''
            if  child is not None:
                obj["type"] = "instance"
                import_element={
                     "source":child[0].find('source').text,
                     "items":child[0].find('items').text,
                     "display":child[0].find('display').text,
                }
                obj["value"]["instance"]=import_element["source"].split(".")[-1]# child[0].tag
                obj["value"]["parent"] = child[0].tag
                script["imports"].append(import_element)
            elif obj["type"] == "IntegerField":
                    obj["type"]="int"
                    min=elem.find('MinimumValue')
                    max=elem.find('MaximumValue')
                    obj["value"]["min"] = min.text if min is not None else None
                    obj["value"]["max"] = max.text if max is not None else None
            elif obj["type"]== "OptionField":
                    obj["type"]="str"
                    obj["value"]["options"]={"values":[],"description":[]}
                    options=elem.find('OptionValues')
                    for key in options.findall('*'):
                         value=key.attrib.get('value')
                         text=key.text
                         if(value!=None):
                            obj["value"]["options"]["values"].append(value)
                            if text != None:
                                obj["value"]["options"]["description"].append(text) 
                         else:
                            if text != None:
                                obj["value"]["options"]["values"].append(text)
            elif obj["type"] =="BooleanField":
                    obj["type"]="bool"
            elif obj["type"]!="ArrayField"  and (obj['default'] is not False or obj['required'] is not False or len(elem)<=1):
                 print("len" + str(len(elem)))
                 multi=obj["multiple"]
                 obj["info"]=obj["type"]
                 if(multi=="Y"):
                    obj["type"]="list[str]"
                 else:
                    obj["type"]="str"
            else: # obj["type"] == None and ( text is ''):
                re(obj,elem)
            classProto["subelements"].append(obj)
def create_python_classes(script):
    code =""
    for import_element in reversed(script["imports"]):
        _from=import_element['source'].replace("OPNsense","opnsense_helper.config_manager")
        code += f"from {_from} import {import_element['items']}\n"
        script["imports"]=filter(lambda n: n != import_element, script["imports"])
    code += f"""
\"\"\"
script {script["name"]} 
---------------------------------------------------------------

* {script["description"]}
* Classes: {script["classes"]}
\"\"\"
"""
    for _class in script["classes"]:
        obj = class_infos[_class]
        subelements = obj["subelements"]
        code += f"""
class {obj["name"]}:    
    \"\"\"
    class {obj["name"]}
    ---------------------------------------------------------------
    
    Mount: {obj["mount"]}  
    """
        # Füge die Subelemente hinzu
        for subelement in subelements:
        # Meta
            meta=""      
            if(subelement["required"] == True):
                meta+="Required, "
            if subelement["default"] != False:
                meta+=f"Default= {subelement['default']}, "                 
            if subelement["type"] == "int" and "min" in subelement["value"].keys() and "max" in subelement["value"].keys():
                meta+=f"Min= {subelement['value']['min']}, Max= {subelement['value']['max']}, "
            if("options" in subelement["value"]):
                meta += f"Options= {subelement['value']['options']['values']}, "
            if(meta != ""):
                meta=" \n           "+ meta[:-2]
        # Info
            if subelement["info"] != "" and subelement["info"] != None:
                print(subelement)
                info = subelement["info"].split("Field")[0].split(".\\")[-1]
            else:
                info = ""
        # Field
            if(subelement["type"] not in ["instance","instance_list"]):
                code += f"""
    :param ({subelement["type"]}) {subelement["name"]}: {info}{meta}               
    """
        # Instance_list
            elif subelement["type"] == "instance_list": 
                code+=f""" 
    :param (list[{subelement["value"]["instance"]}]) {subelement["name"]}: A list of {subelement["value"]["instance"]} instances.{meta}                    
    """
    #   instance
            elif subelement["type"] == "instance":
      
                code+=f""" 
    :param ({subelement["value"]["instance"]}) {subelement["name"]}: An instance of the {subelement["value"]["instance"]} class.{meta}                
    """
        
        
        code += f"""
        \"\"\""""
        constructor=""
        for subelement in (subelements):
            if(subelement["default"] == False):
                constructor += f" {subelement['name']}, "
        for subelement in (subelements):
            if(subelement["default"] != False):
                default = subelement["default"] if type(subelement["default"]) == int else f"'{subelement['default']}'"
                constructor += f"{subelement['name']}={default}, "
                
        code+=f"""   
    def __init__(self, {constructor}):"""
        
        for subelement in subelements:
            if(subelement["required"] == True):
                code += f"""
            if {subelement["name"]} is None:
                raise Exception("Required argument {subelement['name']} is missing")
            """
            
            code += f"""
            self.{subelement["name"]} = {subelement["name"]}  
            """
    target=script["__path"] + f"/{script['name']}.py"
    print(target)
    with open(target, "w") as f:
        f.write(code)
            
def iterate_xml_files(dir_path):
    protos={}
    for root, dirs, files in os.walk(dir_path):
        print(root)
        folder=root.split("/")[-1]
        result_folder=result_dir+"/"+folder
        print(result_folder)

        for file in files:
            if file.endswith('.xml'):
                
                file_path = os.path.join(root, file)
                tree = ET.parse(file_path)
                name=file.split(".")[0]
                xml_root = tree.getroot()
                items=xml_root.find("items") # select the prototype item
                if(items):
                     items=items
                else:
                     continue
                class_proto={
                     "name":name,
                     "proto_attrib": items.attrib,
                     "subelements":[],
                }
                script={
                    "name":name,
                    "classes":[],
                    "imports":[],
                }
                #class_infos[name]=class_proto
                #script["classes"].append(name)
                script["__path"]=result_folder
                script["mount"]=xml_root.find("mount").text if xml_root.find("description") is not None else None
                script["description"]=xml_root.find("description").text if xml_root.find("description") is not None else None
                scripts.append(script)
                recursive_iterate_xml_files(items, class_proto, script)
    for script in scripts:
        print(f"""--------------------------{script["name"]}----------------------""")
        pprint.pprint(script["name"],width=80)
        if not os.path.exists(script["__path"]):
                os.mkdir(script["__path"])
                print(f"Der Ordner {script['name']} wurde erstellt.")
        else:
                print(f"Der Ordner {script['name']} existiert bereits.")

        for _class in script["classes"]:
                obj=class_infos[_class]
                obj["mount"]= (script["mount"][1:] +"/"+obj["name"]) if script["mount"] is not None else None
                print(f"""       -----------{_class}------------""")
                script[_class]=obj
        print(script["__path"])
       
        create_python_classes(script)
iterate_xml_files(root_dir)



 
        # with open(script["__path"]+"/"+script["name"]+".json", 'w') as f:
        #     json.dump(script, f)