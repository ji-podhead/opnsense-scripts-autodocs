from opnsense_helper.config_manager.Captiveportal.Captiveportal import templates.template

"""
script CaptivePortal 
---------------------------------------------------------------

* Captive portal application model
* Classes: ['_zones', '_zone', '_templates', '_template']
"""

class _zones:    
    """
    class _zones
    ---------------------------------------------------------------
    
    Mount: /OPNsense/captiveportal/_zones  
     
    :param (list[_zone]) _zone: A list of _zone instances.                    
    
        """   
    def __init__(self,  _zone, ):
            self._zone = _zone  
            
class _zone:    
    """
    class _zone
    ---------------------------------------------------------------
    
    Mount: /OPNsense/captiveportal/_zone  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (str) _zoneid: AutoNumber 
           Required               
    
    :param (list[str]) _interfaces: Interface 
           Required, Default= lan               
    
    :param (list[str]) _interfaces_inbound: Interface               
    
    :param (list[str]) _authservers: AuthenticationServer               
    
    :param (bool) _alwaysSendAccountingReqs:  
           Required, Default= 0               
    
    :param (str) _authEnforceGroup: AuthGroup               
    
    :param (int) _idletimeout:  
           Required, Default= 0, Min= 0, Max= 10080               
    
    :param (int) _hardtimeout:  
           Required, Default= 0, Min= 0, Max= 10080               
    
    :param (bool) _concurrentlogins:  
           Required, Default= 1               
    
    :param (str) _certificate: Certificate               
    
    :param (str) _servername: Text               
    
    :param (str) _allowedAddresses: Network               
    
    :param (str) _allowedMACAddresses: MacAddress               
    
    :param (bool) _extendedPreAuthData:  
           Required, Default= 0               
     
    :param (Captiveportal) _template: An instance of the Captiveportal class.                
    
    :param (str) _description: Description 
           Required               
    
        """   
    def __init__(self,  _zoneid,  _interfaces_inbound,  _authservers,  _authEnforceGroup,  _certificate,  _servername,  _allowedAddresses,  _allowedMACAddresses,  _template,  _description, _enabled='1', _interfaces='lan', _alwaysSendAccountingReqs='0', _idletimeout='0', _hardtimeout='0', _concurrentlogins='1', _extendedPreAuthData='0', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _zoneid is None:
                raise Exception("Required argument _zoneid is missing")
            
            self._zoneid = _zoneid  
            
            if _interfaces is None:
                raise Exception("Required argument _interfaces is missing")
            
            self._interfaces = _interfaces  
            
            self._interfaces_inbound = _interfaces_inbound  
            
            self._authservers = _authservers  
            
            if _alwaysSendAccountingReqs is None:
                raise Exception("Required argument _alwaysSendAccountingReqs is missing")
            
            self._alwaysSendAccountingReqs = _alwaysSendAccountingReqs  
            
            self._authEnforceGroup = _authEnforceGroup  
            
            if _idletimeout is None:
                raise Exception("Required argument _idletimeout is missing")
            
            self._idletimeout = _idletimeout  
            
            if _hardtimeout is None:
                raise Exception("Required argument _hardtimeout is missing")
            
            self._hardtimeout = _hardtimeout  
            
            if _concurrentlogins is None:
                raise Exception("Required argument _concurrentlogins is missing")
            
            self._concurrentlogins = _concurrentlogins  
            
            self._certificate = _certificate  
            
            self._servername = _servername  
            
            self._allowedAddresses = _allowedAddresses  
            
            self._allowedMACAddresses = _allowedMACAddresses  
            
            if _extendedPreAuthData is None:
                raise Exception("Required argument _extendedPreAuthData is missing")
            
            self._extendedPreAuthData = _extendedPreAuthData  
            
            self._template = _template  
            
            if _description is None:
                raise Exception("Required argument _description is missing")
            
            self._description = _description  
            
class _templates:    
    """
    class _templates
    ---------------------------------------------------------------
    
    Mount: /OPNsense/captiveportal/_templates  
     
    :param (list[_template]) _template: A list of _template instances.                    
    
        """   
    def __init__(self,  _template, ):
            self._template = _template  
            
class _template:    
    """
    class _template
    ---------------------------------------------------------------
    
    Mount: /OPNsense/captiveportal/_template  
    
    :param (str) _name: Text 
           Required               
    
    :param (bool) _or:  
           Required, Default= 0               
    
    :param (str) _filters: CSVList 
           Required               
    
        """   
    def __init__(self,  _name,  _filters, _or='0', ):
            if _name is None:
                raise Exception("Required argument _name is missing")
            
            self._name = _name  
            
            if _or is None:
                raise Exception("Required argument _or is missing")
            
            self._or = _or  
            
            if _filters is None:
                raise Exception("Required argument _filters is missing")
            
            self._filters = _filters  
            