
"""
script Lvtemplate 
---------------------------------------------------------------

* Firewall Live View filter templates
* Classes: ['_templates', '_template']
"""

class _templates:    
    """
    class _templates
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Lvtemplate/_templates  
     
    :param (list[_template]) _template: A list of _template instances.                    
    
        """   
    def __init__(self,  _template, ):
            self._template = _template  
            
class _template:    
    """
    class _template
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Lvtemplate/_template  
    
    :param (str) _name: Text 
           Required               
    
    :param (bool) _or:  
           Required, Default= 0               
    
    :param (str) _filters: CSVList 
           Required               
    
        """   
    def __init__(self,  _name,  _filters, _or='0', ):
            if _name is None:
                raise Exception("Required argument _name is missing")
            
            self._name = _name  
            
            if _or is None:
                raise Exception("Required argument _or is missing")
            
            self._or = _or  
            
            if _filters is None:
                raise Exception("Required argument _filters is missing")
            
            self._filters = _filters  
            