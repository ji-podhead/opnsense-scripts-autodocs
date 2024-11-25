from opnsense_helper.config_manager.IPsec.Swanctl import Connections.Connection
from opnsense_helper.config_manager.IPsec.IPsec import keyPairs.keyPair
from opnsense_helper.config_manager.IPsec.Swanctl import Connections.Connection
from opnsense_helper.config_manager.IPsec.IPsec import keyPairs.keyPair
from opnsense_helper.config_manager.IPsec.Swanctl import Connections.Connection

"""
script Swanctl 
---------------------------------------------------------------

* OPNsense IPsec Connections
* Classes: ['_Connections', '_locals', '_local', '_remotes', '_remote', '_children', '_child', '_Pools', '_Pool', '_VTIs', '_SPDs']
"""

class _Connections:    
    """
    class _Connections
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Swanctl/_Connections  
    
    :param (str) _Connection: Connnection               
    
        """   
    def __init__(self,  _Connection, ):
            self._Connection = _Connection  
            
class _locals:    
    """
    class _locals
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Swanctl/_locals  
     
    :param (list[_local]) _local: A list of _local instances.                    
    
        """   
    def __init__(self,  _local, ):
            self._local = _local  
            
class _local:    
    """
    class _local
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Swanctl/_local  
    
    :param (bool) _enabled:  
           Required, Default= 1               
     
    :param (Swanctl) _connection: An instance of the Swanctl class. 
           Required                
    
    :param (int) _round:  
           Required, Default= 0, Min= 0, Max= 10               
    
    :param (str) _auth:  
           Required, Default= psk, Options= ['Pre-Shared Key', 'Public Key', 'eap-tls', 'eap-mschapv2', 'xauth-pam', 'eap-radius']               
    
    :param (str) _id: Text               
    
    :param (str) _eap_id: Text               
    
    :param (list[str]) _certs: Certificate               
     
    :param (IPsec) _pubkeys: An instance of the IPsec class.                
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _connection,  _id,  _eap_id,  _certs,  _pubkeys,  _description, _enabled='1', _round='0', _auth='psk', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _connection is None:
                raise Exception("Required argument _connection is missing")
            
            self._connection = _connection  
            
            if _round is None:
                raise Exception("Required argument _round is missing")
            
            self._round = _round  
            
            if _auth is None:
                raise Exception("Required argument _auth is missing")
            
            self._auth = _auth  
            
            self._id = _id  
            
            self._eap_id = _eap_id  
            
            self._certs = _certs  
            
            self._pubkeys = _pubkeys  
            
            self._description = _description  
            
class _remotes:    
    """
    class _remotes
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Swanctl/_remotes  
     
    :param (list[_remote]) _remote: A list of _remote instances.                    
    
        """   
    def __init__(self,  _remote, ):
            self._remote = _remote  
            
class _remote:    
    """
    class _remote
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Swanctl/_remote  
    
    :param (bool) _enabled:  
           Required, Default= 1               
     
    :param (Swanctl) _connection: An instance of the Swanctl class. 
           Required                
    
    :param (int) _round:  
           Required, Default= 0, Min= 0, Max= 10               
    
    :param (str) _auth:  
           Required, Default= psk, Options= ['Pre-Shared Key', 'Public Key', 'eap-tls', 'eap-mschapv2', 'xauth-pam', 'eap-radius']               
    
    :param (str) _id: Text               
    
    :param (str) _eap_id: Text               
    
    :param (list[str]) _groups: AuthGroup               
    
    :param (list[str]) _certs: Certificate               
     
    :param (IPsec) _pubkeys: An instance of the IPsec class.                
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _connection,  _id,  _eap_id,  _groups,  _certs,  _pubkeys,  _description, _enabled='1', _round='0', _auth='psk', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _connection is None:
                raise Exception("Required argument _connection is missing")
            
            self._connection = _connection  
            
            if _round is None:
                raise Exception("Required argument _round is missing")
            
            self._round = _round  
            
            if _auth is None:
                raise Exception("Required argument _auth is missing")
            
            self._auth = _auth  
            
            self._id = _id  
            
            self._eap_id = _eap_id  
            
            self._groups = _groups  
            
            self._certs = _certs  
            
            self._pubkeys = _pubkeys  
            
            self._description = _description  
            
class _children:    
    """
    class _children
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Swanctl/_children  
     
    :param (list[_child]) _child: A list of _child instances.                    
    
        """   
    def __init__(self,  _child, ):
            self._child = _child  
            
class _child:    
    """
    class _child
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Swanctl/_child  
    
    :param (bool) _enabled:  
           Required, Default= 1               
     
    :param (Swanctl) _connection: An instance of the Swanctl class. 
           Required                
    
    :param (int) _reqid:  
           Min= 1, Max= 65535               
    
    :param (list[str]) _esp_proposals: IPsecProposal 
           Required, Default= default               
    
    :param (bool) _sha256_96:  
           Required, Default= 0               
    
    :param (str) _start_action:  
           Required, Default= start, Options= ['None', 'trap|start', 'Route', 'Start', 'Trap']               
    
    :param (str) _close_action:  
           Required, Default= none, Options= ['None', 'Trap', 'Start']               
    
    :param (str) _dpd_action:  
           Required, Default= clear, Options= ['Clear', 'Trap', 'Start']               
    
    :param (str) _mode:  
           Required, Default= tunnel, Options= ['Tunnel', 'Transport', 'Pass', 'Drop']               
    
    :param (bool) _policies:  
           Required, Default= 1               
    
    :param (str) _local_ts: Network               
    
    :param (str) _remote_ts: Network               
    
    :param (int) _rekey_time:  
           Required, Default= 3600, Min= 0, Max= 500000               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _connection,  _reqid,  _local_ts,  _remote_ts,  _description, _enabled='1', _esp_proposals='default', _sha256_96='0', _start_action='start', _close_action='none', _dpd_action='clear', _mode='tunnel', _policies='1', _rekey_time='3600', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _connection is None:
                raise Exception("Required argument _connection is missing")
            
            self._connection = _connection  
            
            self._reqid = _reqid  
            
            if _esp_proposals is None:
                raise Exception("Required argument _esp_proposals is missing")
            
            self._esp_proposals = _esp_proposals  
            
            if _sha256_96 is None:
                raise Exception("Required argument _sha256_96 is missing")
            
            self._sha256_96 = _sha256_96  
            
            if _start_action is None:
                raise Exception("Required argument _start_action is missing")
            
            self._start_action = _start_action  
            
            if _close_action is None:
                raise Exception("Required argument _close_action is missing")
            
            self._close_action = _close_action  
            
            if _dpd_action is None:
                raise Exception("Required argument _dpd_action is missing")
            
            self._dpd_action = _dpd_action  
            
            if _mode is None:
                raise Exception("Required argument _mode is missing")
            
            self._mode = _mode  
            
            if _policies is None:
                raise Exception("Required argument _policies is missing")
            
            self._policies = _policies  
            
            self._local_ts = _local_ts  
            
            self._remote_ts = _remote_ts  
            
            if _rekey_time is None:
                raise Exception("Required argument _rekey_time is missing")
            
            self._rekey_time = _rekey_time  
            
            self._description = _description  
            
class _Pools:    
    """
    class _Pools
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Swanctl/_Pools  
     
    :param (list[_Pool]) _Pool: A list of _Pool instances.                    
    
        """   
    def __init__(self,  _Pool, ):
            self._Pool = _Pool  
            
class _Pool:    
    """
    class _Pool
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Swanctl/_Pool  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (str) _name: Text 
           Required               
    
    :param (str) _addrs: Network 
           Required               
    
    :param (str) _dns: Network               
    
        """   
    def __init__(self,  _name,  _addrs,  _dns, _enabled='1', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _name is None:
                raise Exception("Required argument _name is missing")
            
            self._name = _name  
            
            if _addrs is None:
                raise Exception("Required argument _addrs is missing")
            
            self._addrs = _addrs  
            
            self._dns = _dns  
            
class _VTIs:    
    """
    class _VTIs
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Swanctl/_VTIs  
    
    :param (str) _VTI: VTI               
    
        """   
    def __init__(self,  _VTI, ):
            self._VTI = _VTI  
            
class _SPDs:    
    """
    class _SPDs
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Swanctl/_SPDs  
    
    :param (str) _SPD: SPD               
    
        """   
    def __init__(self,  _SPD, ):
            self._SPD = _SPD  
            