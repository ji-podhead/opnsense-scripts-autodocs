
"""
script Syslog 
---------------------------------------------------------------

* None
* Classes: ['_general', '_destinations', '_destination']
"""

class _general:    
    """
    class _general
    ---------------------------------------------------------------
    
    Mount: None  
    
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
            
class _destinations:    
    """
    class _destinations
    ---------------------------------------------------------------
    
    Mount: None  
     
    :param (list[_destination]) _destination: A list of _destination instances.                    
    
        """   
    def __init__(self,  _destination, ):
            self._destination = _destination  
            
class _destination:    
    """
    class _destination
    ---------------------------------------------------------------
    
    Mount: None  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (str) _transport:  
           Required, Default= udp, Options= ['UDP(4)', 'TCP(4)', 'UDP(6)', 'TCP(6)', 'TLS(4)', 'TLS(6)']               
    
    :param (list[str]) _program: JsonKeyValueStore               
    
    :param (str) _level:  
           Options= ['debug', 'info', 'notice', 'warn', 'error', 'critical', 'alert', 'emergency']               
    
    :param (str) _facility:  
           Options= ['kernel messages', 'user-level messages', 'mail system', 'system daemons', 'security/authorization messages', 'messages generated internally by syslogd', 'line printer subsystem', 'network news subsystem', 'UUCP subsystem', 'clock daemon', 'security/authorization messages', 'FTP daemon', 'NTP subsystem', 'log audit', 'log alert', 'locally used (0)', 'locally used (1)', 'locally used (2)', 'locally used (3)', 'locally used (4)', 'locally used (5)', 'locally used (6)', 'locally used (7)']               
    
    :param (str) _hostname: Hostname 
           Required               
    
    :param (str) _certificate: Certificate               
    
    :param (str) _port: Port 
           Required, Default= 514               
    
    :param (bool) _rfc5424:  
           Required, Default= 0               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _program,  _level,  _facility,  _hostname,  _certificate,  _description, _enabled='1', _transport='udp', _port='514', _rfc5424='0', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _transport is None:
                raise Exception("Required argument _transport is missing")
            
            self._transport = _transport  
            
            self._program = _program  
            
            self._level = _level  
            
            self._facility = _facility  
            
            if _hostname is None:
                raise Exception("Required argument _hostname is missing")
            
            self._hostname = _hostname  
            
            self._certificate = _certificate  
            
            if _port is None:
                raise Exception("Required argument _port is missing")
            
            self._port = _port  
            
            if _rfc5424 is None:
                raise Exception("Required argument _rfc5424 is missing")
            
            self._rfc5424 = _rfc5424  
            
            self._description = _description  
            