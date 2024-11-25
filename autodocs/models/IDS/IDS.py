from opnsense_helper.config_manager.Cron.Cron import jobs.job
from opnsense_helper.config_manager.IDS.IDS import files.file

"""
script IDS 
---------------------------------------------------------------

* OPNsense IDS
* Classes: ['_rules', '_policies', '_policy', '_userDefinedRules', '_rule', '_files', '_file', '_fileTags', '_tag', '_general', '_detect', '_eveLog', '_http', '_tls']
"""

class _rules:    
    """
    class _rules
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_rules  
     
    :param (list[_rule]) _rule: A list of _rule instances.                    
    
        """   
    def __init__(self,  _rule, ):
            self._rule = _rule  
            
class _policies:    
    """
    class _policies
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_policies  
     
    :param (list[_policy]) _policy: A list of _policy instances.                    
    
        """   
    def __init__(self,  _policy, ):
            self._policy = _policy  
            
class _policy:    
    """
    class _policy
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_policy  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (int) _prio:  
           Required, Default= 0, Min= None, Max= None               
    
    :param (str) _action:  
           Options= ['Disabled', 'Alert', 'Drop']               
     
    :param (IDS) _rulesets: An instance of the IDS class.                
    
    :param (list[str]) _content: PolicyContent               
    
    :param (str) _new_action:  
           Required, Default= alert, Options= ['default', 'Alert', 'Drop', 'Disable']               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _action,  _rulesets,  _content,  _description, _enabled='1', _prio='0', _new_action='alert', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _prio is None:
                raise Exception("Required argument _prio is missing")
            
            self._prio = _prio  
            
            self._action = _action  
            
            self._rulesets = _rulesets  
            
            self._content = _content  
            
            if _new_action is None:
                raise Exception("Required argument _new_action is missing")
            
            self._new_action = _new_action  
            
            self._description = _description  
            
class _userDefinedRules:    
    """
    class _userDefinedRules
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_userDefinedRules  
     
    :param (list[_rule]) _rule: A list of _rule instances.                    
    
        """   
    def __init__(self,  _rule, ):
            self._rule = _rule  
            
class _rule:    
    """
    class _rule
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_rule  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (int) _sequence:  
           Required, Default= 1, Min= 1, Max= 1000000               
    
    :param (str) _interface: Interface 
           Required, Default= wan               
    
    :param (str) _interface2: Interface               
    
    :param (str) _proto:  
           Required, Default= ip, Options= ['ip', 'ipv4', 'ipv6', 'udp', 'tcp', 'tcp (ACK packets only)', 'tcp (non-ACK packets)', 'icmp', 'ipv6-icmp', 'igmp', 'esp', 'ah', 'gre']               
    
    :param (int) _iplen:  
           Min= 2, Max= 65535               
    
    :param (str) _source: Network 
           Required, Default= any               
    
    :param (bool) _source_not:  
           Required, Default= 0               
    
    :param (str) _src_port: Port 
           Required, Default= any               
    
    :param (str) _destination: Network 
           Required, Default= any               
    
    :param (bool) _destination_not:  
           Required, Default= 0               
    
    :param (str) _dst_port: Port 
           Required, Default= any               
    
    :param (str) _dscp:  
           Options= ['Best Effort', 'Expedited Forwarding', 'AF11', 'AF12', 'AF13', 'AF21', 'AF22', 'AF23', 'AF31', 'AF32', 'AF33', 'AF41', 'AF42', 'AF43', 'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'CS7']               
    
    :param (str) _direction:  
           Options= ['in', 'out']               
     
    :param (TrafficShaper) _target: An instance of the TrafficShaper class. 
           Required                
    
    :param (str) _description: Description               
    
    :param (str) _origin: Text               
    
        """   
    def __init__(self,  _interface2,  _iplen,  _dscp,  _direction,  _target,  _description,  _origin, _enabled='1', _sequence='1', _interface='wan', _proto='ip', _source='any', _source_not='0', _src_port='any', _destination='any', _destination_not='0', _dst_port='any', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _sequence is None:
                raise Exception("Required argument _sequence is missing")
            
            self._sequence = _sequence  
            
            if _interface is None:
                raise Exception("Required argument _interface is missing")
            
            self._interface = _interface  
            
            self._interface2 = _interface2  
            
            if _proto is None:
                raise Exception("Required argument _proto is missing")
            
            self._proto = _proto  
            
            self._iplen = _iplen  
            
            if _source is None:
                raise Exception("Required argument _source is missing")
            
            self._source = _source  
            
            if _source_not is None:
                raise Exception("Required argument _source_not is missing")
            
            self._source_not = _source_not  
            
            if _src_port is None:
                raise Exception("Required argument _src_port is missing")
            
            self._src_port = _src_port  
            
            if _destination is None:
                raise Exception("Required argument _destination is missing")
            
            self._destination = _destination  
            
            if _destination_not is None:
                raise Exception("Required argument _destination_not is missing")
            
            self._destination_not = _destination_not  
            
            if _dst_port is None:
                raise Exception("Required argument _dst_port is missing")
            
            self._dst_port = _dst_port  
            
            self._dscp = _dscp  
            
            self._direction = _direction  
            
            if _target is None:
                raise Exception("Required argument _target is missing")
            
            self._target = _target  
            
            self._description = _description  
            
            self._origin = _origin  
            
class _files:    
    """
    class _files
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_files  
     
    :param (list[_file]) _file: A list of _file instances.                    
    
        """   
    def __init__(self,  _file, ):
            self._file = _file  
            
class _file:    
    """
    class _file
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_file  
    
    :param (str) _filename: Text 
           Required               
    
    :param (bool) _enabled:  
           Required, Default= 0               
    
        """   
    def __init__(self,  _filename, _enabled='0', ):
            if _filename is None:
                raise Exception("Required argument _filename is missing")
            
            self._filename = _filename  
            
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
class _fileTags:    
    """
    class _fileTags
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_fileTags  
     
    :param (list[_tag]) _tag: A list of _tag instances.                    
    
        """   
    def __init__(self,  _tag, ):
            self._tag = _tag  
            
class _tag:    
    """
    class _tag
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_tag  
    
    :param (str) _property: Text 
           Required               
    
    :param (str) _value: Text               
    
        """   
    def __init__(self,  _property,  _value, ):
            if _property is None:
                raise Exception("Required argument _property is missing")
            
            self._property = _property  
            
            self._value = _value  
            
class _general:    
    """
    class _general
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_general  
    
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
            
class _detect:    
    """
    class _detect
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_detect  
    
    :param (str) _Profile:  
           Options= ['Low', 'Medium', 'High', 'Custom']               
    
    :param (int) _toclient_groups:  
           Min= 0, Max= 65535               
    
    :param (int) _toserver_groups:  
           Min= 0, Max= 65535               
    
        """   
    def __init__(self,  _Profile,  _toclient_groups,  _toserver_groups, ):
            self._Profile = _Profile  
            
            self._toclient_groups = _toclient_groups  
            
            self._toserver_groups = _toserver_groups  
            
class _eveLog:    
    """
    class _eveLog
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_eveLog  
     
    :param (list[_http]) _http: A list of _http instances.                    
     
    :param (list[_tls]) _tls: A list of _tls instances.                    
    
        """   
    def __init__(self,  _http,  _tls, ):
            self._http = _http  
            
            self._tls = _tls  
            
class _http:    
    """
    class _http
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_http  
    
    :param (bool) _enable:  
           Required, Default= 0               
    
    :param (bool) _extended:  
           Required, Default= 0               
    
    :param (str) _dumpAllHeaders:  
           Options= ['Request', 'Response', 'Both']               
    
        """   
    def __init__(self,  _dumpAllHeaders, _enable='0', _extended='0', ):
            if _enable is None:
                raise Exception("Required argument _enable is missing")
            
            self._enable = _enable  
            
            if _extended is None:
                raise Exception("Required argument _extended is missing")
            
            self._extended = _extended  
            
            self._dumpAllHeaders = _dumpAllHeaders  
            
class _tls:    
    """
    class _tls
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IDS/_tls  
    
    :param (bool) _enable:  
           Required, Default= 0               
    
    :param (bool) _extended:  
           Required, Default= 0               
    
    :param (bool) _sessionResumption:  
           Required, Default= 0               
    
    :param (str) _custom:  
           Options= ['subject', 'issuer', 'session_resumed', 'serial', 'fingerprint', 'sni', 'version', 'not_before', 'not_after', 'certificate', 'chain', 'ja3', 'ja3s']               
    
        """   
    def __init__(self,  _custom, _enable='0', _extended='0', _sessionResumption='0', ):
            if _enable is None:
                raise Exception("Required argument _enable is missing")
            
            self._enable = _enable  
            
            if _extended is None:
                raise Exception("Required argument _extended is missing")
            
            self._extended = _extended  
            
            if _sessionResumption is None:
                raise Exception("Required argument _sessionResumption is missing")
            
            self._sessionResumption = _sessionResumption  
            
            self._custom = _custom  
            