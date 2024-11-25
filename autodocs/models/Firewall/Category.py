
"""
script Category 
---------------------------------------------------------------

* Firewall categories
* Classes: ['_categories', '_category']
"""

class _categories:    
    """
    class _categories
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Category/_categories  
     
    :param (list[_category]) _category: A list of _category instances.                    
    
        """   
    def __init__(self,  _category, ):
            self._category = _category  
            
class _category:    
    """
    class _category
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Category/_category  
    
    :param (str) _name: Text 
           Required               
    
    :param (bool) _auto:                
    
    :param (str) _color: Text               
    
        """   
    def __init__(self,  _name,  _auto,  _color, ):
            if _name is None:
                raise Exception("Required argument _name is missing")
            
            self._name = _name  
            
            self._auto = _auto  
            
            self._color = _color  
            