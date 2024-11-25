from opnsense_helper.config_manager.Kea.KeaDhcpv4 import subnets.subnet4

"""
script KeaDhcpv4 
---------------------------------------------------------------

* Kea DHCPv4 configuration
* Classes: ['_general', '_ha', '_subnets', '_subnet4', '_option_data', '_reservations', '_reservation', '_ha_peers', '_peer']
"""

class _general:    
    """
    class _general
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Kea/dhcp4/_general  
    
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
            
class _ha:    
    """
    class _ha
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Kea/dhcp4/_ha  
    
    :param (bool) _enabled:  
           Required, Default= 0               
    
    :param (str) _this_server_name: Text               
    
    :param (int) _max_unacked_clients:  
           Required, Default= 2, Min= 0, Max= 65535               
    
        """   
    def __init__(self,  _this_server_name, _enabled='0', _max_unacked_clients='2', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            self._this_server_name = _this_server_name  
            
            if _max_unacked_clients is None:
                raise Exception("Required argument _max_unacked_clients is missing")
            
            self._max_unacked_clients = _max_unacked_clients  
            
class _subnets:    
    """
    class _subnets
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Kea/dhcp4/_subnets  
     
    :param (list[_subnet4]) _subnet4: A list of _subnet4 instances.                    
    
        """   
    def __init__(self,  _subnet4, ):
            self._subnet4 = _subnet4  
            
class _subnet4:    
    """
    class _subnet4
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Kea/dhcp4/_subnet4  
    
    :param (str) _subnet: Network 
           Required               
    
    :param (str) _next_server: Network               
    
    :param (bool) _option_data_autocollect:  
           Required, Default= 1               
     
    :param (list[_option_data]) _option_data: A list of _option_data instances.                    
    
    :param (str) _pools: KeaPools               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _subnet,  _next_server,  _option_data,  _pools,  _description, _option_data_autocollect='1', ):
            if _subnet is None:
                raise Exception("Required argument _subnet is missing")
            
            self._subnet = _subnet  
            
            self._next_server = _next_server  
            
            if _option_data_autocollect is None:
                raise Exception("Required argument _option_data_autocollect is missing")
            
            self._option_data_autocollect = _option_data_autocollect  
            
            self._option_data = _option_data  
            
            self._pools = _pools  
            
            self._description = _description  
            
class _option_data:    
    """
    class _option_data
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Kea/dhcp4/_option_data  
    
    :param (str) _domain_name_servers: Network               
    
    :param (str) _domain_search: Hostname               
    
    :param (str) _routers: Network               
    
    :param (str) _static_routes: Text               
    
    :param (str) _domain_name: Hostname               
    
    :param (str) _ntp_servers: Network               
    
    :param (str) _time_servers: Network               
    
    :param (str) _tftp_server_name: Text               
    
    :param (str) _boot_file_name: Text               
    
        """   
    def __init__(self,  _domain_name_servers,  _domain_search,  _routers,  _static_routes,  _domain_name,  _ntp_servers,  _time_servers,  _tftp_server_name,  _boot_file_name, ):
            self._domain_name_servers = _domain_name_servers  
            
            self._domain_search = _domain_search  
            
            self._routers = _routers  
            
            self._static_routes = _static_routes  
            
            self._domain_name = _domain_name  
            
            self._ntp_servers = _ntp_servers  
            
            self._time_servers = _time_servers  
            
            self._tftp_server_name = _tftp_server_name  
            
            self._boot_file_name = _boot_file_name  
            
class _reservations:    
    """
    class _reservations
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Kea/dhcp4/_reservations  
     
    :param (list[_reservation]) _reservation: A list of _reservation instances.                    
    
        """   
    def __init__(self,  _reservation, ):
            self._reservation = _reservation  
            
class _reservation:    
    """
    class _reservation
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Kea/dhcp4/_reservation  
     
    :param (KeaDhcpv4) _subnet: An instance of the KeaDhcpv4 class. 
           Required                
    
    :param (str) _ip_address: Network               
    
    :param (str) _hw_address: MacAddress 
           Required               
    
    :param (str) _hostname: Hostname               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _subnet,  _ip_address,  _hw_address,  _hostname,  _description, ):
            if _subnet is None:
                raise Exception("Required argument _subnet is missing")
            
            self._subnet = _subnet  
            
            self._ip_address = _ip_address  
            
            if _hw_address is None:
                raise Exception("Required argument _hw_address is missing")
            
            self._hw_address = _hw_address  
            
            self._hostname = _hostname  
            
            self._description = _description  
            
class _ha_peers:    
    """
    class _ha_peers
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Kea/dhcp4/_ha_peers  
     
    :param (list[_peer]) _peer: A list of _peer instances.                    
    
        """   
    def __init__(self,  _peer, ):
            self._peer = _peer  
            
class _peer:    
    """
    class _peer
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Kea/dhcp4/_peer  
    
    :param (str) _name: Text 
           Required               
    
    :param (str) _role:  
           Required, Default= primary, Options= ['primary', 'standby']               
    
    :param (str) _url: Url 
           Required               
    
        """   
    def __init__(self,  _name,  _url, _role='primary', ):
            if _name is None:
                raise Exception("Required argument _name is missing")
            
            self._name = _name  
            
            if _role is None:
                raise Exception("Required argument _role is missing")
            
            self._role = _role  
            
            if _url is None:
                raise Exception("Required argument _url is missing")
            
            self._url = _url  
            