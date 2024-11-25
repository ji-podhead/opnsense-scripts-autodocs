from opnsense_helper.config_manager.TrafficShaper.TrafficShaper import pipes.pipe
from opnsense_helper.config_manager.TrafficShaper.TrafficShaper import pipes.pipe

"""
script TrafficShaper 
---------------------------------------------------------------

* OPNsense traffic shaper
* Classes: ['_pipes', '_pipe', '_queues', '_queue', '_rules', '_rule']
"""

class _pipes:    
    """
    class _pipes
    ---------------------------------------------------------------
    
    Mount: /OPNsense/TrafficShaper/_pipes  
     
    :param (list[_pipe]) _pipe: A list of _pipe instances.                    
    
        """   
    def __init__(self,  _pipe, ):
            self._pipe = _pipe  
            
class _pipe:    
    """
    class _pipe
    ---------------------------------------------------------------
    
    Mount: /OPNsense/TrafficShaper/_pipe  
    
    :param (int) _number:  
           Required, Min= 1, Max= 65535               
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (int) _bandwidth:  
           Required, Min= 1, Max= None               
    
    :param (str) _bandwidthMetric:  
           Required, Default= Kbit, Options= ['bit/s', 'kbit/s', 'Mbit/s', 'Gbit/s']               
    
    :param (int) _queue:  
           Min= 2, Max= 100               
    
    :param (str) _mask:  
           Required, Default= none, Options= ['(none)', 'source', 'destination']               
    
    :param (int) _buckets:  
           Min= 1, Max= 65535               
    
    :param (str) _scheduler:  
           Options= ['FIFO', 'Deficit Round Robin', 'QFQ', 'FlowQueue-CoDel', 'FlowQueue-PIE']               
    
    :param (bool) _codel_enable:  
           Required, Default= 0               
    
    :param (int) _codel_target:  
           Min= 1, Max= 10000               
    
    :param (int) _codel_interval:  
           Min= 1, Max= 10000               
    
    :param (bool) _codel_ecn_enable:  
           Required, Default= 0               
    
    :param (bool) _pie_enable:  
           Required, Default= 0               
    
    :param (int) _fqcodel_quantum:  
           Min= 1, Max= 65535               
    
    :param (int) _fqcodel_limit:  
           Min= 1, Max= 65535               
    
    :param (int) _fqcodel_flows:  
           Min= 1, Max= 65535               
    
    :param (str) _origin: Text               
    
    :param (int) _delay:  
           Min= 1, Max= 3000               
    
    :param (str) _description: Description 
           Required               
    
        """   
    def __init__(self,  _number,  _bandwidth,  _queue,  _buckets,  _scheduler,  _codel_target,  _codel_interval,  _fqcodel_quantum,  _fqcodel_limit,  _fqcodel_flows,  _origin,  _delay,  _description, _enabled='1', _bandwidthMetric='Kbit', _mask='none', _codel_enable='0', _codel_ecn_enable='0', _pie_enable='0', ):
            if _number is None:
                raise Exception("Required argument _number is missing")
            
            self._number = _number  
            
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _bandwidth is None:
                raise Exception("Required argument _bandwidth is missing")
            
            self._bandwidth = _bandwidth  
            
            if _bandwidthMetric is None:
                raise Exception("Required argument _bandwidthMetric is missing")
            
            self._bandwidthMetric = _bandwidthMetric  
            
            self._queue = _queue  
            
            if _mask is None:
                raise Exception("Required argument _mask is missing")
            
            self._mask = _mask  
            
            self._buckets = _buckets  
            
            self._scheduler = _scheduler  
            
            if _codel_enable is None:
                raise Exception("Required argument _codel_enable is missing")
            
            self._codel_enable = _codel_enable  
            
            self._codel_target = _codel_target  
            
            self._codel_interval = _codel_interval  
            
            if _codel_ecn_enable is None:
                raise Exception("Required argument _codel_ecn_enable is missing")
            
            self._codel_ecn_enable = _codel_ecn_enable  
            
            if _pie_enable is None:
                raise Exception("Required argument _pie_enable is missing")
            
            self._pie_enable = _pie_enable  
            
            self._fqcodel_quantum = _fqcodel_quantum  
            
            self._fqcodel_limit = _fqcodel_limit  
            
            self._fqcodel_flows = _fqcodel_flows  
            
            self._origin = _origin  
            
            self._delay = _delay  
            
            if _description is None:
                raise Exception("Required argument _description is missing")
            
            self._description = _description  
            
class _queues:    
    """
    class _queues
    ---------------------------------------------------------------
    
    Mount: /OPNsense/TrafficShaper/_queues  
     
    :param (list[_queue]) _queue: A list of _queue instances.                    
    
        """   
    def __init__(self,  _queue, ):
            self._queue = _queue  
            
class _queue:    
    """
    class _queue
    ---------------------------------------------------------------
    
    Mount: /OPNsense/TrafficShaper/_queue  
    
    :param (int) _number:  
           Required, Min= 1, Max= 65535               
    
    :param (bool) _enabled:  
           Required, Default= 1               
     
    :param (TrafficShaper) _pipe: An instance of the TrafficShaper class. 
           Required                
    
    :param (int) _weight:  
           Required, Default= 100, Min= 1, Max= 100               
    
    :param (str) _mask:  
           Required, Default= none, Options= ['(none)', 'source', 'destination']               
    
    :param (int) _buckets:  
           Min= 1, Max= 65535               
    
    :param (bool) _codel_enable:  
           Required, Default= 0               
    
    :param (int) _codel_target:  
           Min= 1, Max= 10000               
    
    :param (int) _codel_interval:  
           Min= 1, Max= 10000               
    
    :param (bool) _codel_ecn_enable:  
           Required, Default= 0               
    
    :param (bool) _pie_enable:  
           Required, Default= 0               
    
    :param (str) _description: Description 
           Required               
    
    :param (str) _origin: Text               
    
        """   
    def __init__(self,  _number,  _pipe,  _buckets,  _codel_target,  _codel_interval,  _description,  _origin, _enabled='1', _weight='100', _mask='none', _codel_enable='0', _codel_ecn_enable='0', _pie_enable='0', ):
            if _number is None:
                raise Exception("Required argument _number is missing")
            
            self._number = _number  
            
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _pipe is None:
                raise Exception("Required argument _pipe is missing")
            
            self._pipe = _pipe  
            
            if _weight is None:
                raise Exception("Required argument _weight is missing")
            
            self._weight = _weight  
            
            if _mask is None:
                raise Exception("Required argument _mask is missing")
            
            self._mask = _mask  
            
            self._buckets = _buckets  
            
            if _codel_enable is None:
                raise Exception("Required argument _codel_enable is missing")
            
            self._codel_enable = _codel_enable  
            
            self._codel_target = _codel_target  
            
            self._codel_interval = _codel_interval  
            
            if _codel_ecn_enable is None:
                raise Exception("Required argument _codel_ecn_enable is missing")
            
            self._codel_ecn_enable = _codel_ecn_enable  
            
            if _pie_enable is None:
                raise Exception("Required argument _pie_enable is missing")
            
            self._pie_enable = _pie_enable  
            
            if _description is None:
                raise Exception("Required argument _description is missing")
            
            self._description = _description  
            
            self._origin = _origin  
            
class _rules:    
    """
    class _rules
    ---------------------------------------------------------------
    
    Mount: /OPNsense/TrafficShaper/_rules  
     
    :param (list[_rule]) _rule: A list of _rule instances.                    
    
        """   
    def __init__(self,  _rule, ):
            self._rule = _rule  
            
class _rule:    
    """
    class _rule
    ---------------------------------------------------------------
    
    Mount: /OPNsense/TrafficShaper/_rule  
    
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
            