
"""
script Lagg 
---------------------------------------------------------------

* Lagg interfaces
* Classes: ['_lagg']
"""

class _lagg:    
    """
    class _lagg
    ---------------------------------------------------------------
    
    Mount: laggs/_lagg  
    
    :param (str) _laggif: Text 
           Required               
    
    :param (list[str]) _members: LaggInterface 
           Required               
    
    :param (str) _primary_member: LaggInterface               
    
    :param (str) _proto:  
           Required, Default= lacp, Options= ['None', 'lacp', 'failover', 'fec', 'loadbalance', 'roundrobin']               
    
    :param (bool) _lacp_fast_timeout:  
           Required, Default= 0               
    
    :param (str) _use_flowid:  
           Options= ['', '1', '0']               
    
    :param (str) _lagghash:  
           Options= ['L2: src/dst MAC address and optional VLAN number.', 'L3: src/dst address for IPv4 or IPv6.', 'L4: src/dst port for TCP/UDP/SCTP.']               
    
    :param (str) _lacp_strict:  
           Options= ['', '1', '0']               
    
    :param (int) _mtu:  
           Min= 576, Max= 65535               
    
    :param (str) _descr: Description               
    
        """   
    def __init__(self,  _laggif,  _members,  _primary_member,  _use_flowid,  _lagghash,  _lacp_strict,  _mtu,  _descr, _proto='lacp', _lacp_fast_timeout='0', ):
            if _laggif is None:
                raise Exception("Required argument _laggif is missing")
            
            self._laggif = _laggif  
            
            if _members is None:
                raise Exception("Required argument _members is missing")
            
            self._members = _members  
            
            self._primary_member = _primary_member  
            
            if _proto is None:
                raise Exception("Required argument _proto is missing")
            
            self._proto = _proto  
            
            if _lacp_fast_timeout is None:
                raise Exception("Required argument _lacp_fast_timeout is missing")
            
            self._lacp_fast_timeout = _lacp_fast_timeout  
            
            self._use_flowid = _use_flowid  
            
            self._lagghash = _lagghash  
            
            self._lacp_strict = _lacp_strict  
            
            self._mtu = _mtu  
            
            self._descr = _descr  
            