
"""
script Export 
---------------------------------------------------------------

* OpenVPN export presets
* Classes: ['_servers', '_server']
"""

class _servers:    
    """
    class _servers
    ---------------------------------------------------------------
    
    Mount: /OPNsense/OpenVPNExport/_servers  
    
    :param (str) _server: Server               
    
        """   
    def __init__(self,  _server, ):
            self._server = _server  
            
class _server:    
    """
    class _server
    ---------------------------------------------------------------
    
    Mount: /OPNsense/OpenVPNExport/_server  
    
    :param (str) _vpnid: Text 
           Required               
    
    :param (str) _hostname: Hostname 
           Required               
    
    :param (str) _template: Text               
    
    :param (int) _local_port:  
           Min= 1, Max= 65535               
    
    :param (bool) _random_local_port:  
           Required, Default= 1               
    
    :param (bool) _validate_server_cn:  
           Required, Default= 1               
    
    :param (bool) _cryptoapi:                
    
    :param (bool) _auth_nocache:                
    
    :param (str) _plain_config: Text               
    
        """   
    def __init__(self,  _vpnid,  _hostname,  _template,  _local_port,  _cryptoapi,  _auth_nocache,  _plain_config, _random_local_port='1', _validate_server_cn='1', ):
            if _vpnid is None:
                raise Exception("Required argument _vpnid is missing")
            
            self._vpnid = _vpnid  
            
            if _hostname is None:
                raise Exception("Required argument _hostname is missing")
            
            self._hostname = _hostname  
            
            self._template = _template  
            
            self._local_port = _local_port  
            
            if _random_local_port is None:
                raise Exception("Required argument _random_local_port is missing")
            
            self._random_local_port = _random_local_port  
            
            if _validate_server_cn is None:
                raise Exception("Required argument _validate_server_cn is missing")
            
            self._validate_server_cn = _validate_server_cn  
            
            self._cryptoapi = _cryptoapi  
            
            self._auth_nocache = _auth_nocache  
            
            self._plain_config = _plain_config  
            