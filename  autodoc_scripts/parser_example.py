import argparse
import pprint
import json
parser = argparse.ArgumentParser(    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--proto', help='protocol to fetch', choices=['inet', 'inet6'], default='inet')
parser.add_argument('-a','--aaa', help='aaa', choices=['a', 'a2'], default='a')

args = parser.parse_args()

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
        print((type(action)))
        print((action))
        action=action.__dict__
        argObjects[action["dest"]]=new_obj = {replacements.get(k, k): v for k, v in action.items() if k not in ignoredkeys}

print(json.dumps(argObjects))