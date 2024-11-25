
"""
script Loopback 
---------------------------------------------------------------

* Loopback configuration
* Classes: ['_loopback']
"""

class _loopback:    
    """
    class _loopback
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Interfaces/loopbacks/_loopback  
    
    :param (str) _deviceId: AutoNumber 
           Required               
    
    :param (str) _description: Description 
           Required               
    
        """   
    def __init__(self,  _deviceId,  _description, ):
            if _deviceId is None:
                raise Exception("Required argument _deviceId is missing")
            
            self._deviceId = _deviceId  
            
            if _description is None:
                raise Exception("Required argument _description is missing")
            
            self._description = _description  
            