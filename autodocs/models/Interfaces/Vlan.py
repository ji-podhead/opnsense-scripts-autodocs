
"""
script Vlan 
---------------------------------------------------------------

* VLAN configuration
* Classes: ['_vlan']
"""

class _vlan:    
    """
    class _vlan
    ---------------------------------------------------------------
    
    Mount: vlans/_vlan  
    
    :param (str) _if: VlanInterface 
           Required               
    
    :param (int) _tag:  
           Required, Min= 1, Max= 4094               
    
    :param (str) _pcp:  
           Required, Default= 0, Options= ['1', '0', '2', '3', '4', '5', '6', '7']               
    
    :param (str) _proto:  
           Options= ['802.1q', '802.1ad']               
    
    :param (str) _descr: Description               
    
    :param (str) _vlanif: Text 
           Required               
    
        """   
    def __init__(self,  _if,  _tag,  _proto,  _descr,  _vlanif, _pcp='0', ):
            if _if is None:
                raise Exception("Required argument _if is missing")
            
            self._if = _if  
            
            if _tag is None:
                raise Exception("Required argument _tag is missing")
            
            self._tag = _tag  
            
            if _pcp is None:
                raise Exception("Required argument _pcp is missing")
            
            self._pcp = _pcp  
            
            self._proto = _proto  
            
            self._descr = _descr  
            
            if _vlanif is None:
                raise Exception("Required argument _vlanif is missing")
            
            self._vlanif = _vlanif  
            