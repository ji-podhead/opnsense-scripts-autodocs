from opnsense_helper.config_manager.monit.monit import service
from opnsense_helper.config_manager.monit.monit import test

"""
script Monit 
---------------------------------------------------------------

* Monit settings
* Classes: ['_general', '_alert', '_service', '_test']
"""

class _general:    
    """
    class _general
    ---------------------------------------------------------------
    
    Mount: /OPNsense/monit/_general  
    
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
            
class _alert:    
    """
    class _alert
    ---------------------------------------------------------------
    
    Mount: /OPNsense/monit/_alert  
    
    :param (bool) _enabled:  
           Required, Default= 0               
    
    :param (str) _recipient: Email 
           Required, Default= root@localhost.local               
    
    :param (bool) _noton:  
           Required, Default= 0               
    
    :param (str) _events: CSVList               
    
    :param (str) _format: Text               
    
    :param (int) _reminder:  
           Min= 0, Max= 86400               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _events,  _format,  _reminder,  _description, _enabled='0', _recipient='root@localhost.local', _noton='0', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _recipient is None:
                raise Exception("Required argument _recipient is missing")
            
            self._recipient = _recipient  
            
            if _noton is None:
                raise Exception("Required argument _noton is missing")
            
            self._noton = _noton  
            
            self._events = _events  
            
            self._format = _format  
            
            self._reminder = _reminder  
            
            self._description = _description  
            
class _service:    
    """
    class _service
    ---------------------------------------------------------------
    
    Mount: /OPNsense/monit/_service  
    
    :param (bool) _enabled:  
           Required, Default= 0               
    
    :param (str) _name: Text 
           Required               
    
    :param (str) _description: Description               
    
    :param (str) _type:  
           Required, Options= ['Process', 'File', 'Fifo', 'Filesystem', 'Directory', 'Remote Host', 'System', 'Custom', 'Network']               
    
    :param (str) _pidfile: Text               
    
    :param (str) _match: Text               
    
    :param (str) _path: Text               
    
    :param (int) _timeout:  
           Required, Default= 300, Min= 1, Max= 86400               
    
    :param (int) _starttimeout:  
           Required, Default= 30, Min= 0, Max= 86400               
    
    :param (str) _address: Hostname               
    
    :param (str) _interface: Interface               
    
    :param (str) _start: Text               
    
    :param (str) _stop: Text               
     
    :param (monit) _tests: An instance of the monit class.                
     
    :param (monit) _depends: An instance of the monit class.                
    
    :param (str) _polltime: Text               
    
        """   
    def __init__(self,  _name,  _description,  _type,  _pidfile,  _match,  _path,  _address,  _interface,  _start,  _stop,  _tests,  _depends,  _polltime, _enabled='0', _timeout='300', _starttimeout='30', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _name is None:
                raise Exception("Required argument _name is missing")
            
            self._name = _name  
            
            self._description = _description  
            
            if _type is None:
                raise Exception("Required argument _type is missing")
            
            self._type = _type  
            
            self._pidfile = _pidfile  
            
            self._match = _match  
            
            self._path = _path  
            
            if _timeout is None:
                raise Exception("Required argument _timeout is missing")
            
            self._timeout = _timeout  
            
            if _starttimeout is None:
                raise Exception("Required argument _starttimeout is missing")
            
            self._starttimeout = _starttimeout  
            
            self._address = _address  
            
            self._interface = _interface  
            
            self._start = _start  
            
            self._stop = _stop  
            
            self._tests = _tests  
            
            self._depends = _depends  
            
            self._polltime = _polltime  
            
class _test:    
    """
    class _test
    ---------------------------------------------------------------
    
    Mount: /OPNsense/monit/_test  
    
    :param (str) _name: Text 
           Required               
    
    :param (str) _type:  
           Required, Default= Custom, Options= ['Existence', 'System Resource', 'Process Resource', 'Process Disk I/O', 'File Checksum', 'Timestamp', 'File Size', 'File Content', 'Filesystem Mount Flags', 'Space Usage', 'Inode Usage', 'Disk I/O', 'Permission', 'UID', 'GID', 'PID', 'PPID', 'Uptime', 'Program Status', 'Network Interface', 'Network Ping', 'Connection', 'Custom']               
    
    :param (str) _condition: Text 
           Required               
    
    :param (str) _action:  
           Required, Options= ['Alert', 'Restart', 'Start', 'Stop', 'Execute', 'Unmonitor']               
    
    :param (str) _path: Text               
    
        """   
    def __init__(self,  _name,  _condition,  _action,  _path, _type='Custom', ):
            if _name is None:
                raise Exception("Required argument _name is missing")
            
            self._name = _name  
            
            if _type is None:
                raise Exception("Required argument _type is missing")
            
            self._type = _type  
            
            if _condition is None:
                raise Exception("Required argument _condition is missing")
            
            self._condition = _condition  
            
            if _action is None:
                raise Exception("Required argument _action is missing")
            
            self._action = _action  
            
            self._path = _path  
            