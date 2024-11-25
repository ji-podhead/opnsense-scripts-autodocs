
"""
script Group 
---------------------------------------------------------------

* Firewall interface groups
* Classes: ['_ifgroupentry']
"""

class _ifgroupentry:    
    """
    class _ifgroupentry
    ---------------------------------------------------------------
    
    Mount: ifgroups/_ifgroupentry  
    
    :param (str) _ifname: GroupName 
           Required               
    
    :param (list[str]) _members: Interface 
           Required               
    
    :param (bool) _nogroup:                
    
    :param (int) _sequence:  
           Required, Default= 0, Min= 0, Max= 9999               
    
    :param (str) _descr: Description               
    
        """   
    def __init__(self,  _ifname,  _members,  _nogroup,  _descr, _sequence='0', ):
            if _ifname is None:
                raise Exception("Required argument _ifname is missing")
            
            self._ifname = _ifname  
            
            if _members is None:
                raise Exception("Required argument _members is missing")
            
            self._members = _members  
            
            self._nogroup = _nogroup  
            
            if _sequence is None:
                raise Exception("Required argument _sequence is missing")
            
            self._sequence = _sequence  
            
            self._descr = _descr  
            