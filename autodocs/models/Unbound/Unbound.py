from opnsense_helper.config_manager.Unbound.Unbound import hosts.host

"""
script Unbound 
---------------------------------------------------------------

* Unbound configuration
* Classes: ['_general', '_advanced', '_acls', '_acl', '_dnsbl', '_forwarding', '_dots', '_dot', '_hosts', '_host', '_aliases', '_alias']
"""

class _general:    
    """
    class _general
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_general  
    
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
            
class _advanced:    
    """
    class _advanced
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_advanced  
    
    :param (bool) _hideidentity:                
    
    :param (bool) _hideversion:                
    
    :param (bool) _prefetch:                
    
    :param (bool) _prefetchkey:                
    
    :param (bool) _dnssecstripped:                
    
    :param (bool) _aggressivensec:  
           Required, Default= 1               
    
    :param (bool) _serveexpired:                
    
    :param (str) _serveexpiredreplyttl: Numeric               
    
    :param (str) _serveexpiredttl: Numeric               
    
    :param (bool) _serveexpiredttlreset:                
    
    :param (str) _serveexpiredclienttimeout: Numeric               
    
    :param (bool) _qnameminstrict:                
    
    :param (bool) _extendedstatistics:                
    
    :param (bool) _logqueries:                
    
    :param (bool) _logreplies:                
    
    :param (bool) _logtagqueryreply:                
    
    :param (bool) _logservfail:                
    
    :param (bool) _loglocalactions:                
    
    :param (str) _logverbosity:  
           Required, Default= 1, Options= ['0', '1', '2', '3', '4', '5']               
    
    :param (str) _valloglevel:  
           Required, Default= 0, Options= ['0', '1', '2']               
    
    :param (str) _privatedomain: CSVList               
    
    :param (str) _privateaddress: Network 
           Required, Default= 0.0.0.0/8,10.0.0.0/8,100.64.0.0/10,169.254.0.0/16,172.16.0.0/12,192.0.2.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,233.252.0.0/24,::1/128,2001:db8::/32,fc00::/8,fd00::/8,fe80::/10               
    
    :param (str) _insecuredomain: CSVList               
    
    :param (str) _msgcachesize: Text               
    
    :param (str) _rrsetcachesize: Text               
    
    :param (str) _outgoingnumtcp: Numeric               
    
    :param (str) _incomingnumtcp: Numeric               
    
    :param (str) _numqueriesperthread: Numeric               
    
    :param (str) _outgoingrange: Numeric               
    
    :param (str) _jostletimeout: Numeric               
    
    :param (str) _discardtimeout: Numeric               
    
    :param (str) _cachemaxttl: Numeric               
    
    :param (str) _cachemaxnegativettl: Numeric               
    
    :param (str) _cacheminttl: Numeric               
    
    :param (str) _infrahostttl: Numeric               
    
    :param (bool) _infrakeepprobing:                
    
    :param (str) _infracachenumhosts: Numeric               
    
    :param (str) _unwantedreplythreshold: Numeric               
    
        """   
    def __init__(self,  _hideidentity,  _hideversion,  _prefetch,  _prefetchkey,  _dnssecstripped,  _serveexpired,  _serveexpiredreplyttl,  _serveexpiredttl,  _serveexpiredttlreset,  _serveexpiredclienttimeout,  _qnameminstrict,  _extendedstatistics,  _logqueries,  _logreplies,  _logtagqueryreply,  _logservfail,  _loglocalactions,  _privatedomain,  _insecuredomain,  _msgcachesize,  _rrsetcachesize,  _outgoingnumtcp,  _incomingnumtcp,  _numqueriesperthread,  _outgoingrange,  _jostletimeout,  _discardtimeout,  _cachemaxttl,  _cachemaxnegativettl,  _cacheminttl,  _infrahostttl,  _infrakeepprobing,  _infracachenumhosts,  _unwantedreplythreshold, _aggressivensec='1', _logverbosity='1', _valloglevel='0', _privateaddress='0.0.0.0/8,10.0.0.0/8,100.64.0.0/10,169.254.0.0/16,172.16.0.0/12,192.0.2.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,233.252.0.0/24,::1/128,2001:db8::/32,fc00::/8,fd00::/8,fe80::/10', ):
            self._hideidentity = _hideidentity  
            
            self._hideversion = _hideversion  
            
            self._prefetch = _prefetch  
            
            self._prefetchkey = _prefetchkey  
            
            self._dnssecstripped = _dnssecstripped  
            
            if _aggressivensec is None:
                raise Exception("Required argument _aggressivensec is missing")
            
            self._aggressivensec = _aggressivensec  
            
            self._serveexpired = _serveexpired  
            
            self._serveexpiredreplyttl = _serveexpiredreplyttl  
            
            self._serveexpiredttl = _serveexpiredttl  
            
            self._serveexpiredttlreset = _serveexpiredttlreset  
            
            self._serveexpiredclienttimeout = _serveexpiredclienttimeout  
            
            self._qnameminstrict = _qnameminstrict  
            
            self._extendedstatistics = _extendedstatistics  
            
            self._logqueries = _logqueries  
            
            self._logreplies = _logreplies  
            
            self._logtagqueryreply = _logtagqueryreply  
            
            self._logservfail = _logservfail  
            
            self._loglocalactions = _loglocalactions  
            
            if _logverbosity is None:
                raise Exception("Required argument _logverbosity is missing")
            
            self._logverbosity = _logverbosity  
            
            if _valloglevel is None:
                raise Exception("Required argument _valloglevel is missing")
            
            self._valloglevel = _valloglevel  
            
            self._privatedomain = _privatedomain  
            
            if _privateaddress is None:
                raise Exception("Required argument _privateaddress is missing")
            
            self._privateaddress = _privateaddress  
            
            self._insecuredomain = _insecuredomain  
            
            self._msgcachesize = _msgcachesize  
            
            self._rrsetcachesize = _rrsetcachesize  
            
            self._outgoingnumtcp = _outgoingnumtcp  
            
            self._incomingnumtcp = _incomingnumtcp  
            
            self._numqueriesperthread = _numqueriesperthread  
            
            self._outgoingrange = _outgoingrange  
            
            self._jostletimeout = _jostletimeout  
            
            self._discardtimeout = _discardtimeout  
            
            self._cachemaxttl = _cachemaxttl  
            
            self._cachemaxnegativettl = _cachemaxnegativettl  
            
            self._cacheminttl = _cacheminttl  
            
            self._infrahostttl = _infrahostttl  
            
            self._infrakeepprobing = _infrakeepprobing  
            
            self._infracachenumhosts = _infracachenumhosts  
            
            self._unwantedreplythreshold = _unwantedreplythreshold  
            
class _acls:    
    """
    class _acls
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_acls  
    
    :param (str) _default_action:  
           Required, Default= allow, Options= ['allow', 'deny', 'refuse']               
     
    :param (list[_acl]) _acl: A list of _acl instances.                    
    
        """   
    def __init__(self,  _acl, _default_action='allow', ):
            if _default_action is None:
                raise Exception("Required argument _default_action is missing")
            
            self._default_action = _default_action  
            
            self._acl = _acl  
            
class _acl:    
    """
    class _acl
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_acl  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (str) _name: Text 
           Required               
    
    :param (str) _action:  
           Required, Default= allow, Options= ['allow', 'deny', 'refuse', 'allow_snoop', 'deny_non_local', 'refuse_non_local']               
    
    :param (list[str]) _networks: Network 
           Required               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _name,  _networks,  _description, _enabled='1', _action='allow', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _name is None:
                raise Exception("Required argument _name is missing")
            
            self._name = _name  
            
            if _action is None:
                raise Exception("Required argument _action is missing")
            
            self._action = _action  
            
            if _networks is None:
                raise Exception("Required argument _networks is missing")
            
            self._networks = _networks  
            
            self._description = _description  
            
class _dnsbl:    
    """
    class _dnsbl
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_dnsbl  
    
    :param (bool) _enabled:  
           Required, Default= 0               
    
    :param (bool) _safesearch:                
    
    :param (str) _type:  
           Options= ['Abuse.ch - ThreatFox IOC database', 'OISD - Domain Blocklist Ads', 'OISD - Domain Blocklist Big', 'OISD - Domain Blocklist NSFW', 'AdAway List', 'AdGuard List', 'Blocklist.site Abuse', 'Blocklist.site Ads', 'Blocklist.site Crypto', 'Blocklist.site Drugs', 'Blocklist.site Fraud', 'Blocklist.site Facebook', 'Blocklist.site Gambling', 'Blocklist.site Malware', 'Blocklist.site Phishing', 'Blocklist.site Piracy', 'Blocklist.site Porn', 'Blocklist.site Ransomware', 'Blocklist.site Redirect', 'Blocklist.site Scam', 'Blocklist.site Tiktok', 'Blocklist.site Torrent', 'Blocklist.site Tracking', 'Blocklist.site Youtube', 'EasyList', 'EasyPrivacy', 'NoCoin List', 'All Porn List', 'PornTop1M List', 'Simple Ad List', 'Simple Tracker List', 'Steven Black List', 'WindowsSpyBlocker (spy)', 'WindowsSpyBlocker (update)', 'WindowsSpyBlocker (extra)', 'YoYo List']               
    
    :param (str) _lists: CSVList               
    
    :param (str) _whitelists: CSVList               
    
    :param (str) _blocklists: CSVList               
    
    :param (str) _wildcards: CSVList               
    
    :param (str) _address: Network               
    
    :param (bool) _nxdomain:                
    
        """   
    def __init__(self,  _safesearch,  _type,  _lists,  _whitelists,  _blocklists,  _wildcards,  _address,  _nxdomain, _enabled='0', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            self._safesearch = _safesearch  
            
            self._type = _type  
            
            self._lists = _lists  
            
            self._whitelists = _whitelists  
            
            self._blocklists = _blocklists  
            
            self._wildcards = _wildcards  
            
            self._address = _address  
            
            self._nxdomain = _nxdomain  
            
class _forwarding:    
    """
    class _forwarding
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_forwarding  
    
    :param (bool) _enabled:                
    
        """   
    def __init__(self,  _enabled, ):
            self._enabled = _enabled  
            
class _dots:    
    """
    class _dots
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_dots  
     
    :param (list[_dot]) _dot: A list of _dot instances.                    
    
        """   
    def __init__(self,  _dot, ):
            self._dot = _dot  
            
class _dot:    
    """
    class _dot
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_dot  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (str) _type:  
           Required, Default= dot, Options= ['DNS over TLS', 'Forward']               
    
    :param (str) _domain: Hostname               
    
    :param (str) _server: Network 
           Required               
    
    :param (str) _port: Port               
    
    :param (str) _verify: Hostname               
    
    :param (bool) _forward_tcp_upstream:  
           Required, Default= 0               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _domain,  _server,  _port,  _verify,  _description, _enabled='1', _type='dot', _forward_tcp_upstream='0', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _type is None:
                raise Exception("Required argument _type is missing")
            
            self._type = _type  
            
            self._domain = _domain  
            
            if _server is None:
                raise Exception("Required argument _server is missing")
            
            self._server = _server  
            
            self._port = _port  
            
            self._verify = _verify  
            
            if _forward_tcp_upstream is None:
                raise Exception("Required argument _forward_tcp_upstream is missing")
            
            self._forward_tcp_upstream = _forward_tcp_upstream  
            
            self._description = _description  
            
class _hosts:    
    """
    class _hosts
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_hosts  
     
    :param (list[_host]) _host: A list of _host instances.                    
    
        """   
    def __init__(self,  _host, ):
            self._host = _host  
            
class _host:    
    """
    class _host
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_host  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (str) _hostname: Hostname               
    
    :param (str) _domain: Text 
           Required               
    
    :param (str) _rr:  
           Required, Default= A, Options= ['A (IPv4 address)', 'AAAA (IPv6 address)', 'MX (Mail server)']               
    
    :param (int) _mxprio:  
           Min= None, Max= None               
    
    :param (str) _mx: Hostname               
    
    :param (str) _server: Network               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _hostname,  _domain,  _mxprio,  _mx,  _server,  _description, _enabled='1', _rr='A', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            self._hostname = _hostname  
            
            if _domain is None:
                raise Exception("Required argument _domain is missing")
            
            self._domain = _domain  
            
            if _rr is None:
                raise Exception("Required argument _rr is missing")
            
            self._rr = _rr  
            
            self._mxprio = _mxprio  
            
            self._mx = _mx  
            
            self._server = _server  
            
            self._description = _description  
            
class _aliases:    
    """
    class _aliases
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_aliases  
     
    :param (list[_alias]) _alias: A list of _alias instances.                    
    
        """   
    def __init__(self,  _alias, ):
            self._alias = _alias  
            
class _alias:    
    """
    class _alias
    ---------------------------------------------------------------
    
    Mount: /OPNsense/unboundplus/_alias  
    
    :param (bool) _enabled:  
           Required, Default= 1               
     
    :param (Unbound) _host: An instance of the Unbound class. 
           Required                
    
    :param (str) _hostname: Hostname               
    
    :param (str) _domain: Text               
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _host,  _hostname,  _domain,  _description, _enabled='1', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _host is None:
                raise Exception("Required argument _host is missing")
            
            self._host = _host  
            
            self._hostname = _hostname  
            
            self._domain = _domain  
            
            self._description = _description  
            