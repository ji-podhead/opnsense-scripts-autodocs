
"""
script IPsec 
---------------------------------------------------------------

* OPNsense IPsec
* Classes: ['_general', '_charon', '_syslog', '_daemon', '_keyPairs', '_keyPair', '_preSharedKeys', '_preSharedKey']
"""

class _general:    
    """
    class _general
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IPsec/_general  
    
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
            
class _charon:    
    """
    class _charon
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IPsec/_charon  
    
    :param (int) _max_ikev1_exchanges:  
           Min= 0, Max= 65536               
    
    :param (int) _threads:  
           Required, Default= 16, Min= 1, Max= 65536               
    
    :param (int) _ikesa_table_size:  
           Required, Default= 32, Min= 1, Max= 65536               
    
    :param (int) _ikesa_table_segments:  
           Required, Default= 4, Min= 1, Max= 65536               
    
    :param (int) _init_limit_half_open:  
           Required, Default= 1000, Min= 1, Max= 65536               
    
    :param (bool) _ignore_acquire_ts:  
           Required, Default= 1               
    
    :param (bool) _make_before_break:                
    
    :param (int) _retransmit_tries:  
           Min= None, Max= None               
    
    :param (str) _retransmit_timeout: Numeric               
    
    :param (str) _retransmit_base: Numeric               
    
    :param (int) _retransmit_jitter:  
           Min= None, Max= None               
    
    :param (int) _retransmit_limit:  
           Min= None, Max= None               
     
    :param (list[_syslog]) _syslog: A list of _syslog instances.                    
    
        """   
    def __init__(self,  _max_ikev1_exchanges,  _make_before_break,  _retransmit_tries,  _retransmit_timeout,  _retransmit_base,  _retransmit_jitter,  _retransmit_limit,  _syslog, _threads='16', _ikesa_table_size='32', _ikesa_table_segments='4', _init_limit_half_open='1000', _ignore_acquire_ts='1', ):
            self._max_ikev1_exchanges = _max_ikev1_exchanges  
            
            if _threads is None:
                raise Exception("Required argument _threads is missing")
            
            self._threads = _threads  
            
            if _ikesa_table_size is None:
                raise Exception("Required argument _ikesa_table_size is missing")
            
            self._ikesa_table_size = _ikesa_table_size  
            
            if _ikesa_table_segments is None:
                raise Exception("Required argument _ikesa_table_segments is missing")
            
            self._ikesa_table_segments = _ikesa_table_segments  
            
            if _init_limit_half_open is None:
                raise Exception("Required argument _init_limit_half_open is missing")
            
            self._init_limit_half_open = _init_limit_half_open  
            
            if _ignore_acquire_ts is None:
                raise Exception("Required argument _ignore_acquire_ts is missing")
            
            self._ignore_acquire_ts = _ignore_acquire_ts  
            
            self._make_before_break = _make_before_break  
            
            self._retransmit_tries = _retransmit_tries  
            
            self._retransmit_timeout = _retransmit_timeout  
            
            self._retransmit_base = _retransmit_base  
            
            self._retransmit_jitter = _retransmit_jitter  
            
            self._retransmit_limit = _retransmit_limit  
            
            self._syslog = _syslog  
            
class _syslog:    
    """
    class _syslog
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IPsec/_syslog  
     
    :param (list[_daemon]) _daemon: A list of _daemon instances.                    
    
        """   
    def __init__(self,  _daemon, ):
            self._daemon = _daemon  
            
class _daemon:    
    """
    class _daemon
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IPsec/_daemon  
    
    :param (bool) _ike_name:  
           Required, Default= 1               
    
    :param (bool) _log_level:  
           Required, Default= 0               
    
    :param (str) _app: CharonLogLevel               
    
    :param (str) _asn: CharonLogLevel               
    
    :param (str) _cfg: CharonLogLevel               
    
    :param (str) _chd: CharonLogLevel               
    
    :param (str) _dmn: CharonLogLevel               
    
    :param (str) _enc: CharonLogLevel               
    
    :param (str) _esp: CharonLogLevel               
    
    :param (str) _ike: CharonLogLevel               
    
    :param (str) _imc: CharonLogLevel               
    
    :param (str) _imv: CharonLogLevel               
    
    :param (str) _imv: CharonLogLevel               
    
    :param (str) _job: CharonLogLevel               
    
    :param (str) _knl: CharonLogLevel               
    
    :param (str) _lib: CharonLogLevel               
    
    :param (str) _mgr: CharonLogLevel               
    
    :param (str) _net: CharonLogLevel               
    
    :param (str) _pts: CharonLogLevel               
    
    :param (str) _tls: CharonLogLevel               
    
    :param (str) _tnc: CharonLogLevel               
    
        """   
    def __init__(self,  _app,  _asn,  _cfg,  _chd,  _dmn,  _enc,  _esp,  _ike,  _imc,  _imv,  _imv,  _job,  _knl,  _lib,  _mgr,  _net,  _pts,  _tls,  _tnc, _ike_name='1', _log_level='0', ):
            if _ike_name is None:
                raise Exception("Required argument _ike_name is missing")
            
            self._ike_name = _ike_name  
            
            if _log_level is None:
                raise Exception("Required argument _log_level is missing")
            
            self._log_level = _log_level  
            
            self._app = _app  
            
            self._asn = _asn  
            
            self._cfg = _cfg  
            
            self._chd = _chd  
            
            self._dmn = _dmn  
            
            self._enc = _enc  
            
            self._esp = _esp  
            
            self._ike = _ike  
            
            self._imc = _imc  
            
            self._imv = _imv  
            
            self._imv = _imv  
            
            self._job = _job  
            
            self._knl = _knl  
            
            self._lib = _lib  
            
            self._mgr = _mgr  
            
            self._net = _net  
            
            self._pts = _pts  
            
            self._tls = _tls  
            
            self._tnc = _tnc  
            
class _keyPairs:    
    """
    class _keyPairs
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IPsec/_keyPairs  
     
    :param (list[_keyPair]) _keyPair: A list of _keyPair instances.                    
    
        """   
    def __init__(self,  _keyPair, ):
            self._keyPair = _keyPair  
            
class _keyPair:    
    """
    class _keyPair
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IPsec/_keyPair  
    
    :param (str) _name: Text 
           Required               
    
    :param (str) _keyType:  
           Required, Default= rsa, Options= ['RSA', 'ECDSA']               
    
    :param (str) _publicKey: Text 
           Required               
    
    :param (str) _privateKey: Text               
    
    :param (int) _keySize:  
           Min= None, Max= None               
    
    :param (str) _keyFingerprint: Text               
    
        """   
    def __init__(self,  _name,  _publicKey,  _privateKey,  _keySize,  _keyFingerprint, _keyType='rsa', ):
            if _name is None:
                raise Exception("Required argument _name is missing")
            
            self._name = _name  
            
            if _keyType is None:
                raise Exception("Required argument _keyType is missing")
            
            self._keyType = _keyType  
            
            if _publicKey is None:
                raise Exception("Required argument _publicKey is missing")
            
            self._publicKey = _publicKey  
            
            self._privateKey = _privateKey  
            
            self._keySize = _keySize  
            
            self._keyFingerprint = _keyFingerprint  
            
class _preSharedKeys:    
    """
    class _preSharedKeys
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IPsec/_preSharedKeys  
     
    :param (list[_preSharedKey]) _preSharedKey: A list of _preSharedKey instances.                    
    
        """   
    def __init__(self,  _preSharedKey, ):
            self._preSharedKey = _preSharedKey  
            
class _preSharedKey:    
    """
    class _preSharedKey
    ---------------------------------------------------------------
    
    Mount: /OPNsense/IPsec/_preSharedKey  
    
    :param (str) _ident: Text 
           Required               
    
    :param (str) _remote_ident: Text               
    
    :param (str) _keyType:  
           Required, Default= PSK, Options= ['PSK', 'EAP']               
    
    :param (str) _Key: Text               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _ident,  _remote_ident,  _Key,  _description, _keyType='PSK', ):
            if _ident is None:
                raise Exception("Required argument _ident is missing")
            
            self._ident = _ident  
            
            self._remote_ident = _remote_ident  
            
            if _keyType is None:
                raise Exception("Required argument _keyType is missing")
            
            self._keyType = _keyType  
            
            self._Key = _Key  
            
            self._description = _description  
            