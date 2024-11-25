from opnsense_helper.config_manager.DHCRelay.DHCRelay import destinations

"""
script DHCRelay 
---------------------------------------------------------------

* DHCRelay configuration
* Classes: ['_relays', '_destinations']
"""

class _relays:    
    """
    class _relays
    ---------------------------------------------------------------
    
    Mount: /OPNsense/DHCRelay/_relays  
    
    :param (bool) _enabled:  
           Required               
    
    :param (str) _interface: Interface 
           Required               
     
    :param (DHCRelay) _destination: An instance of the DHCRelay class. 
           Required                
    
    :param (bool) _agent_info:  
           Required               
    
        """   
    def __init__(self,  _enabled,  _interface,  _destination,  _agent_info, ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _interface is None:
                raise Exception("Required argument _interface is missing")
            
            self._interface = _interface  
            
            if _destination is None:
                raise Exception("Required argument _destination is missing")
            
            self._destination = _destination  
            
            if _agent_info is None:
                raise Exception("Required argument _agent_info is missing")
            
            self._agent_info = _agent_info  
            
class _destinations:    
    """
    class _destinations
    ---------------------------------------------------------------
    
    Mount: /OPNsense/DHCRelay/_destinations  
     
    :param (list[_destination]) _destination: A list of _destination instances.                    
    
        """   
    def __init__(self,  _destination, ):
            self._destination = _destination  
            