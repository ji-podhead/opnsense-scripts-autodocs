
"""
script OpenVPN 
---------------------------------------------------------------

* OpenVPN
* Classes: ['_Overwrites', '_Overwrite', '_Instances', '_StaticKeys', '_StaticKey']
"""

class _Overwrites:    
    """
    class _Overwrites
    ---------------------------------------------------------------
    
    Mount: /OPNsense/OpenVPN/_Overwrites  
     
    :param (list[_Overwrite]) _Overwrite: A list of _Overwrite instances.                    
    
        """   
    def __init__(self,  _Overwrite, ):
            self._Overwrite = _Overwrite  
            
class _Overwrite:    
    """
    class _Overwrite
    ---------------------------------------------------------------
    
    Mount: /OPNsense/OpenVPN/_Overwrite  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (list[str]) _servers: OpenVPNServer               
    
    :param (str) _common_name: Text 
           Required               
    
    :param (bool) _block:  
           Required, Default= 0               
    
    :param (bool) _push_reset:  
           Required, Default= 0               
    
    :param (str) _tunnel_network: Network               
    
    :param (str) _tunnel_networkv6: Network               
    
    :param (str) _local_networks: Network               
    
    :param (str) _remote_networks: Network               
    
    :param (str) _route_gateway: Network               
    
    :param (str) _redirect_gateway:  
           Options= ['local', 'autolocal', 'default', 'bypass-dhcp', 'bypass-dns', 'block-local', 'ipv6', '!ipv4']               
    
    :param (bool) _register_dns:  
           Required, Default= 0               
    
    :param (str) _dns_domain: Hostname               
    
    :param (str) _dns_domain_search: Hostname               
    
    :param (str) _dns_servers: Network               
    
    :param (str) _ntp_servers: Network               
    
    :param (str) _wins_servers: Network               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _servers,  _common_name,  _tunnel_network,  _tunnel_networkv6,  _local_networks,  _remote_networks,  _route_gateway,  _redirect_gateway,  _dns_domain,  _dns_domain_search,  _dns_servers,  _ntp_servers,  _wins_servers,  _description, _enabled='1', _block='0', _push_reset='0', _register_dns='0', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            self._servers = _servers  
            
            if _common_name is None:
                raise Exception("Required argument _common_name is missing")
            
            self._common_name = _common_name  
            
            if _block is None:
                raise Exception("Required argument _block is missing")
            
            self._block = _block  
            
            if _push_reset is None:
                raise Exception("Required argument _push_reset is missing")
            
            self._push_reset = _push_reset  
            
            self._tunnel_network = _tunnel_network  
            
            self._tunnel_networkv6 = _tunnel_networkv6  
            
            self._local_networks = _local_networks  
            
            self._remote_networks = _remote_networks  
            
            self._route_gateway = _route_gateway  
            
            self._redirect_gateway = _redirect_gateway  
            
            if _register_dns is None:
                raise Exception("Required argument _register_dns is missing")
            
            self._register_dns = _register_dns  
            
            self._dns_domain = _dns_domain  
            
            self._dns_domain_search = _dns_domain_search  
            
            self._dns_servers = _dns_servers  
            
            self._ntp_servers = _ntp_servers  
            
            self._wins_servers = _wins_servers  
            
            self._description = _description  
            
class _Instances:    
    """
    class _Instances
    ---------------------------------------------------------------
    
    Mount: /OPNsense/OpenVPN/_Instances  
    
    :param (str) _Instance: Instance               
    
        """   
    def __init__(self,  _Instance, ):
            self._Instance = _Instance  
            
class _StaticKeys:    
    """
    class _StaticKeys
    ---------------------------------------------------------------
    
    Mount: /OPNsense/OpenVPN/_StaticKeys  
     
    :param (list[_StaticKey]) _StaticKey: A list of _StaticKey instances.                    
    
        """   
    def __init__(self,  _StaticKey, ):
            self._StaticKey = _StaticKey  
            
class _StaticKey:    
    """
    class _StaticKey
    ---------------------------------------------------------------
    
    Mount: /OPNsense/OpenVPN/_StaticKey  
    
    :param (str) _mode:  
           Required, Default= crypt, Options= ['auth (Authenticate control channel packets)', 'crypt (Encrypt and authenticate all control channel packets)']               
    
    :param (str) _key: Text 
           Required               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _key,  _description, _mode='crypt', ):
            if _mode is None:
                raise Exception("Required argument _mode is missing")
            
            self._mode = _mode  
            
            if _key is None:
                raise Exception("Required argument _key is missing")
            
            self._key = _key  
            
            self._description = _description  
            