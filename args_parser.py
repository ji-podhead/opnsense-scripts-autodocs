import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--cache', help='Dump cache', action="store_true", default=False)
parser.add_argument('-i', '--infra', help='Dump infrastructure cache', action="store_true", default=False)
parser.add_argument('-s', '--stats', help='Dump stats', action="store_true", default=False)
parser.add_argument('-l', '--list-local-zones', help='List local Zones', action="store_true", default=False)
parser.add_argument('-I', '--list-insecure', help='List Domain-Insecure Zones', action="store_true", default=False)
parser.add_argument('-d', '--list-local-data', help='List local data', action="store_true", default=False)


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
