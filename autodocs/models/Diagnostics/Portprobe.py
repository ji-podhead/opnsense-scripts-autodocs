
"""
script Portprobe 
---------------------------------------------------------------

* OPNsense Port probe
* Classes: ['_settings']
"""

class _settings:    
    """
    class _settings
    ---------------------------------------------------------------
    
    Mount: memory:/_settings  
    
    :param (str) _hostname: Hostname 
           Required               
    
    :param (str) _ipproto:  
           Required, Default= inet, Options= ['IPv4', 'IPv6']               
    
    :param (str) _protocol:  
           Required, Default= udp, Options= ['UDP', 'ICMP']               
    
    :param (str) _source_address: Network               
    
        """   
    def __init__(self,  _hostname,  _source_address, _ipproto='inet', _protocol='udp', ):
            if _hostname is None:
                raise Exception("Required argument _hostname is missing")
            
            self._hostname = _hostname  
            
            if _ipproto is None:
                raise Exception("Required argument _ipproto is missing")
            
            self._ipproto = _ipproto  
            
            if _protocol is None:
                raise Exception("Required argument _protocol is missing")
            
            self._protocol = _protocol  
            
            self._source_address = _source_address  
            