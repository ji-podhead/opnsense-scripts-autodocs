
"""
script Netflow 
---------------------------------------------------------------

* OPNsense Netflow
* Classes: ['_capture', '_collect']
"""

class _capture:    
    """
    class _capture
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Netflow/_capture  
    
    :param (list[str]) _interfaces: Interface               
    
    :param (list[str]) _egress_only: Interface               
    
    :param (str) _version:  
           Required, Default= v9, Options= ['v5', 'v9']               
    
    :param (str) _targets: IPPort               
    
        """   
    def __init__(self,  _interfaces,  _egress_only,  _targets, _version='v9', ):
            self._interfaces = _interfaces  
            
            self._egress_only = _egress_only  
            
            if _version is None:
                raise Exception("Required argument _version is missing")
            
            self._version = _version  
            
            self._targets = _targets  
            
class _collect:    
    """
    class _collect
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Netflow/_collect  
    
    :param (bool) _enable:  
           Required, Default= 0               
    
        """   
    def __init__(self, _enable='0', ):
            if _enable is None:
                raise Exception("Required argument _enable is missing")
            
            self._enable = _enable  
            