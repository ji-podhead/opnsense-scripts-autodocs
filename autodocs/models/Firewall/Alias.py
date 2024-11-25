
"""
script Alias 
---------------------------------------------------------------

* Firewall aliases
* Classes: ['_geoip', '_aliases']
"""

class _geoip:    
    """
    class _geoip
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Alias/_geoip  
    
    :param (str) _url: Url               
    
        """   
    def __init__(self,  _url, ):
            self._url = _url  
            
class _aliases:    
    """
    class _aliases
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Alias/_aliases  
     
    :param (list[_alias]) _alias: A list of _alias instances.                    
    
        """   
    def __init__(self,  _alias, ):
            self._alias = _alias  
            