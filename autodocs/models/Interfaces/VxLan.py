
"""
script VxLan 
---------------------------------------------------------------

* VXLAN configuration
* Classes: ['_vxlan']
"""

class _vxlan:    
    """
    class _vxlan
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Interfaces/vxlans/_vxlan  
    
    :param (str) _deviceId: AutoNumber 
           Required               
    
    :param (int) _vxlanid:  
           Required, Min= 0, Max= 16777215               
    
    :param (str) _vxlanlocal: Network 
           Required               
    
    :param (str) _vxlanlocalport: Port               
    
    :param (str) _vxlanremote: Network               
    
    :param (str) _vxlanremoteport: Port               
    
    :param (str) _vxlangroup: Network               
    
    :param (str) _vxlandev: Interface               
    
        """   
    def __init__(self,  _deviceId,  _vxlanid,  _vxlanlocal,  _vxlanlocalport,  _vxlanremote,  _vxlanremoteport,  _vxlangroup,  _vxlandev, ):
            if _deviceId is None:
                raise Exception("Required argument _deviceId is missing")
            
            self._deviceId = _deviceId  
            
            if _vxlanid is None:
                raise Exception("Required argument _vxlanid is missing")
            
            self._vxlanid = _vxlanid  
            
            if _vxlanlocal is None:
                raise Exception("Required argument _vxlanlocal is missing")
            
            self._vxlanlocal = _vxlanlocal  
            
            self._vxlanlocalport = _vxlanlocalport  
            
            self._vxlanremote = _vxlanremote  
            
            self._vxlanremoteport = _vxlanremoteport  
            
            self._vxlangroup = _vxlangroup  
            
            self._vxlandev = _vxlandev  
            