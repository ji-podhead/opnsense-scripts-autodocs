
"""
script KeaCtrlAgent 
---------------------------------------------------------------

* Kea Control Agent configuration
* Classes: ['_general']
"""

class _general:    
    """
    class _general
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Kea/ctrl_agent/_general  
    
    :param (bool) _enabled:  
           Required, Default= 0               
    
    :param (str) _port: Port 
           Required, Default= 53               
    
    :param (bool) _stats:                
    
    :param (list[str]) _active_interface: UnboundInterface               
    
    :param (bool) _dnssec:                
    
    :param (bool) _dns64:                
    
    :param (str) _dns64prefix: Network               
    
    :param (bool) _noarecords:                
    
    :param (bool) _regdhcp:                
    
    :param (str) _regdhcpdomain: Text               
    
    :param (bool) _regdhcpstatic:                
    
    :param (bool) _noreglladdr6:                
    
    :param (bool) _noregrecords:                
    
    :param (bool) _txtsupport:                
    
    :param (bool) _cacheflush:                
    
    :param (str) _local_zone_type:  
           Required, Default= transparent, Options= ['transparent', 'always_nxdomain', 'always_refuse', 'always_transparent', 'deny', 'inform', 'inform_deny', 'nodefault', 'refuse', 'static', 'typetransparent']               
    
    :param (list[str]) _outgoing_interface: UnboundInterface               
    
    :param (bool) _enable_wpad:                
    
        """   
    def __init__(self,  _stats,  _active_interface,  _dnssec,  _dns64,  _dns64prefix,  _noarecords,  _regdhcp,  _regdhcpdomain,  _regdhcpstatic,  _noreglladdr6,  _noregrecords,  _txtsupport,  _cacheflush,  _outgoing_interface,  _enable_wpad, _enabled='0', _port='53', _local_zone_type='transparent', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _port is None:
                raise Exception("Required argument _port is missing")
            
            self._port = _port  
            
            self._stats = _stats  
            
            self._active_interface = _active_interface  
            
            self._dnssec = _dnssec  
            
            self._dns64 = _dns64  
            
            self._dns64prefix = _dns64prefix  
            
            self._noarecords = _noarecords  
            
            self._regdhcp = _regdhcp  
            
            self._regdhcpdomain = _regdhcpdomain  
            
            self._regdhcpstatic = _regdhcpstatic  
            
            self._noreglladdr6 = _noreglladdr6  
            
            self._noregrecords = _noregrecords  
            
            self._txtsupport = _txtsupport  
            
            self._cacheflush = _cacheflush  
            
            if _local_zone_type is None:
                raise Exception("Required argument _local_zone_type is missing")
            
            self._local_zone_type = _local_zone_type  
            
            self._outgoing_interface = _outgoing_interface  
            
            self._enable_wpad = _enable_wpad  
            