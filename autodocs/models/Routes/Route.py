
"""
script Route 
---------------------------------------------------------------

* None
* Classes: ['_route']
"""

class _route:    
    """
    class _route
    ---------------------------------------------------------------
    
    Mount: None  
    
    :param (str) _network: Network 
           Required               
    
    :param (str) _gateway: JsonKeyValueStore 
           Required               
    
    :param (str) _descr: Description               
    
    :param (bool) _disabled:  
           Required, Default= 0               
    
        """   
    def __init__(self,  _network,  _gateway,  _descr, _disabled='0', ):
            if _network is None:
                raise Exception("Required argument _network is missing")
            
            self._network = _network  
            
            if _gateway is None:
                raise Exception("Required argument _gateway is missing")
            
            self._gateway = _gateway  
            
            self._descr = _descr  
            
            if _disabled is None:
                raise Exception("Required argument _disabled is missing")
            
            self._disabled = _disabled  
            