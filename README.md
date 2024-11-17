# OPNsense-scripts-autodocs
### ***automatially created docs for opnsense 24 core***
- [docs can be found here](https://ji-podhead.github.io/opnsense-scripts-autodocs/.docs/_build/html/index.html)
- the original opnsense core scripts [can be found here](https://github.com/opnsense/core/tree/master/src/opnsense/scripts)

### created using:
  - ast parser for the python scripts that use the argParse class
    - objects where replicated using subprocess and the code provided by ast
  - php and bash script autodocs where created using regex and codeium
    - those files where also manually overlooked and scanned for required parameters and flags 

### backend api implementation
- my backend api implementation called [opnsense-helper](https://github.com/ji-podhead/opnsense-helper) (pip package) can call all those scripts via ssh.
- you can also apply call every pluginctl and configctl command
- the config manager lets you apply configurations via xml in runtime
  - so far you can set vlans, phys. interfaces and dhcpd
    - more will be comming as well as an ansible collection  
