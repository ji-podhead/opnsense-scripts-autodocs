
"""
script Gre 
---------------------------------------------------------------

* GRE interfaces
* Classes: ['_gre']
"""

class _gre:    
    """
    class _gre
    ---------------------------------------------------------------
    
    Mount: gres/_gre  
    
    :param (str) _local-addr: LinkAddress 
           Required, Default= wan               
    
    :param (str) _if: Text               
    
    :param (str) _ipaddr: Text               
    
    :param (str) _greif: Text 
           Required               
    
    :param (str) _remote-addr: Network               
    
    :param (str) _tunnel-local-addr: Network               
    
    :param (str) _tunnel-remote-addr: Network               
    
    :param (int) _tunnel-remote-net:  
           Required, Default= 32, Min= 1, Max= 128               
    
    :param (str) _descr: Description               
    
        """   
    def __init__(self,  _if,  _ipaddr,  _greif,  _remote-addr,  _tunnel-local-addr,  _tunnel-remote-addr,  _descr, _local-addr='wan', _tunnel-remote-net='32', ):
            if _local-addr is None:
                raise Exception("Required argument _local-addr is missing")
            
            self._local-addr = _local-addr  
            
            self._if = _if  
            
            self._ipaddr = _ipaddr  
            
            if _greif is None:
                raise Exception("Required argument _greif is missing")
            
            self._greif = _greif  
            
            self._remote-addr = _remote-addr  
            
            self._tunnel-local-addr = _tunnel-local-addr  
            
            self._tunnel-remote-addr = _tunnel-remote-addr  
            
            if _tunnel-remote-net is None:
                raise Exception("Required argument _tunnel-remote-net is missing")
            
            self._tunnel-remote-net = _tunnel-remote-net  
            
            self._descr = _descr  
            