from opnsense_helper.config_manager.Firewall.Category import categories.category
from opnsense_helper.config_manager.Firewall.Category import categories.category
from opnsense_helper.config_manager.Firewall.Category import categories.category
from opnsense_helper.config_manager.Firewall.Category import categories.category

"""
script Filter 
---------------------------------------------------------------

* OPNsense firewall filter rules
* Classes: ['_rules', '_rule', '_interface', '_Filters', '_source_port', '_destination_port', '_gateway', '_snatrules', '_rule', '_source_port', '_destination_port', '_target_port', '_npt', '_rule', '_destination_net', '_onetoone', '_rule']
"""

class _rules:    
    """
    class _rules
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_rules  
     
    :param (list[_rule]) _rule: A list of _rule instances.                    
    
        """   
    def __init__(self,  _rule, ):
            self._rule = _rule  
            
class _rule:    
    """
    class _rule
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_rule  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (bool) _log:  
           Required, Default= 0               
    
    :param (int) _sequence:  
           Required, Default= 1, Min= 1, Max= 99999               
    
    :param (str) _interface: Interface 
           Required, Default= wan               
    
    :param (str) _type:  
           Required, Default= binat, Options= ['BINAT', 'NAT']               
    
    :param (str) _source_net: NetworkAlias 
           Required               
    
    :param (bool) _source_not:  
           Required, Default= 0               
    
    :param (str) _destination_net: NetworkAlias 
           Required, Default= any               
    
    :param (bool) _destination_not:  
           Required, Default= 0               
    
    :param (str) _external: Network 
           Required               
    
    :param (str) _natreflection:  
           Options= ['', 'Enable', 'Disable']               
     
    :param (Category) _categories: An instance of the Category class.                
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _source_net,  _external,  _natreflection,  _categories,  _description, _enabled='1', _log='0', _sequence='1', _interface='wan', _type='binat', _source_not='0', _destination_net='any', _destination_not='0', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _log is None:
                raise Exception("Required argument _log is missing")
            
            self._log = _log  
            
            if _sequence is None:
                raise Exception("Required argument _sequence is missing")
            
            self._sequence = _sequence  
            
            if _interface is None:
                raise Exception("Required argument _interface is missing")
            
            self._interface = _interface  
            
            if _type is None:
                raise Exception("Required argument _type is missing")
            
            self._type = _type  
            
            if _source_net is None:
                raise Exception("Required argument _source_net is missing")
            
            self._source_net = _source_net  
            
            if _source_not is None:
                raise Exception("Required argument _source_not is missing")
            
            self._source_not = _source_not  
            
            if _destination_net is None:
                raise Exception("Required argument _destination_net is missing")
            
            self._destination_net = _destination_net  
            
            if _destination_not is None:
                raise Exception("Required argument _destination_not is missing")
            
            self._destination_not = _destination_not  
            
            if _external is None:
                raise Exception("Required argument _external is missing")
            
            self._external = _external  
            
            self._natreflection = _natreflection  
            
            self._categories = _categories  
            
            self._description = _description  
            
class _interface:    
    """
    class _interface
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_interface  
    
    :param (str) _Multiple:                
     
    :param (list[_Filters]) _Filters: A list of _Filters instances.                    
    
    :param (str) _AllowDynamic:                
    
        """   
    def __init__(self,  _Multiple,  _Filters,  _AllowDynamic, ):
            self._Multiple = _Multiple  
            
            self._Filters = _Filters  
            
            self._AllowDynamic = _AllowDynamic  
            
class _Filters:    
    """
    class _Filters
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_Filters  
    
    :param (str) _if:                
    
        """   
    def __init__(self,  _if, ):
            self._if = _if  
            
class _source_port:    
    """
    class _source_port
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_source_port  
    
    :param (str) _EnableWellKnown:                
    
    :param (str) _EnableRanges:                
    
    :param (str) _EnableAlias:                
    
    :param (str) _ValidationMessage:                
    
        """   
    def __init__(self,  _EnableWellKnown,  _EnableRanges,  _EnableAlias,  _ValidationMessage, ):
            self._EnableWellKnown = _EnableWellKnown  
            
            self._EnableRanges = _EnableRanges  
            
            self._EnableAlias = _EnableAlias  
            
            self._ValidationMessage = _ValidationMessage  
            
class _destination_port:    
    """
    class _destination_port
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_destination_port  
    
    :param (str) _EnableWellKnown:                
    
    :param (str) _EnableRanges:                
    
    :param (str) _EnableAlias:                
    
    :param (str) _ValidationMessage:                
    
        """   
    def __init__(self,  _EnableWellKnown,  _EnableRanges,  _EnableAlias,  _ValidationMessage, ):
            self._EnableWellKnown = _EnableWellKnown  
            
            self._EnableRanges = _EnableRanges  
            
            self._EnableAlias = _EnableAlias  
            
            self._ValidationMessage = _ValidationMessage  
            
class _gateway:    
    """
    class _gateway
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_gateway  
    
    :param (str) _ConfigdPopulateAct:                
    
    :param (str) _ValidationMessage:                
    
        """   
    def __init__(self,  _ConfigdPopulateAct,  _ValidationMessage, ):
            self._ConfigdPopulateAct = _ConfigdPopulateAct  
            
            self._ValidationMessage = _ValidationMessage  
            
class _snatrules:    
    """
    class _snatrules
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_snatrules  
     
    :param (list[_rule]) _rule: A list of _rule instances.                    
    
        """   
    def __init__(self,  _rule, ):
            self._rule = _rule  
            
class _rule:    
    """
    class _rule
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_rule  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (bool) _log:  
           Required, Default= 0               
    
    :param (int) _sequence:  
           Required, Default= 1, Min= 1, Max= 99999               
    
    :param (str) _interface: Interface 
           Required, Default= wan               
    
    :param (str) _type:  
           Required, Default= binat, Options= ['BINAT', 'NAT']               
    
    :param (str) _source_net: NetworkAlias 
           Required               
    
    :param (bool) _source_not:  
           Required, Default= 0               
    
    :param (str) _destination_net: NetworkAlias 
           Required, Default= any               
    
    :param (bool) _destination_not:  
           Required, Default= 0               
    
    :param (str) _external: Network 
           Required               
    
    :param (str) _natreflection:  
           Options= ['', 'Enable', 'Disable']               
     
    :param (Category) _categories: An instance of the Category class.                
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _source_net,  _external,  _natreflection,  _categories,  _description, _enabled='1', _log='0', _sequence='1', _interface='wan', _type='binat', _source_not='0', _destination_net='any', _destination_not='0', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _log is None:
                raise Exception("Required argument _log is missing")
            
            self._log = _log  
            
            if _sequence is None:
                raise Exception("Required argument _sequence is missing")
            
            self._sequence = _sequence  
            
            if _interface is None:
                raise Exception("Required argument _interface is missing")
            
            self._interface = _interface  
            
            if _type is None:
                raise Exception("Required argument _type is missing")
            
            self._type = _type  
            
            if _source_net is None:
                raise Exception("Required argument _source_net is missing")
            
            self._source_net = _source_net  
            
            if _source_not is None:
                raise Exception("Required argument _source_not is missing")
            
            self._source_not = _source_not  
            
            if _destination_net is None:
                raise Exception("Required argument _destination_net is missing")
            
            self._destination_net = _destination_net  
            
            if _destination_not is None:
                raise Exception("Required argument _destination_not is missing")
            
            self._destination_not = _destination_not  
            
            if _external is None:
                raise Exception("Required argument _external is missing")
            
            self._external = _external  
            
            self._natreflection = _natreflection  
            
            self._categories = _categories  
            
            self._description = _description  
            
class _source_port:    
    """
    class _source_port
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_source_port  
    
    :param (str) _EnableWellKnown:                
    
    :param (str) _EnableRanges:                
    
    :param (str) _EnableAlias:                
    
    :param (str) _ValidationMessage:                
    
        """   
    def __init__(self,  _EnableWellKnown,  _EnableRanges,  _EnableAlias,  _ValidationMessage, ):
            self._EnableWellKnown = _EnableWellKnown  
            
            self._EnableRanges = _EnableRanges  
            
            self._EnableAlias = _EnableAlias  
            
            self._ValidationMessage = _ValidationMessage  
            
class _destination_port:    
    """
    class _destination_port
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_destination_port  
    
    :param (str) _EnableWellKnown:                
    
    :param (str) _EnableRanges:                
    
    :param (str) _EnableAlias:                
    
    :param (str) _ValidationMessage:                
    
        """   
    def __init__(self,  _EnableWellKnown,  _EnableRanges,  _EnableAlias,  _ValidationMessage, ):
            self._EnableWellKnown = _EnableWellKnown  
            
            self._EnableRanges = _EnableRanges  
            
            self._EnableAlias = _EnableAlias  
            
            self._ValidationMessage = _ValidationMessage  
            
class _target_port:    
    """
    class _target_port
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_target_port  
    
    :param (str) _EnableWellKnown:                
    
    :param (str) _EnableRanges:                
    
        """   
    def __init__(self,  _EnableWellKnown,  _EnableRanges, ):
            self._EnableWellKnown = _EnableWellKnown  
            
            self._EnableRanges = _EnableRanges  
            
class _npt:    
    """
    class _npt
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_npt  
     
    :param (list[_rule]) _rule: A list of _rule instances.                    
    
        """   
    def __init__(self,  _rule, ):
            self._rule = _rule  
            
class _rule:    
    """
    class _rule
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_rule  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (bool) _log:  
           Required, Default= 0               
    
    :param (int) _sequence:  
           Required, Default= 1, Min= 1, Max= 99999               
    
    :param (str) _interface: Interface 
           Required, Default= wan               
    
    :param (str) _type:  
           Required, Default= binat, Options= ['BINAT', 'NAT']               
    
    :param (str) _source_net: NetworkAlias 
           Required               
    
    :param (bool) _source_not:  
           Required, Default= 0               
    
    :param (str) _destination_net: NetworkAlias 
           Required, Default= any               
    
    :param (bool) _destination_not:  
           Required, Default= 0               
    
    :param (str) _external: Network 
           Required               
    
    :param (str) _natreflection:  
           Options= ['', 'Enable', 'Disable']               
     
    :param (Category) _categories: An instance of the Category class.                
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _source_net,  _external,  _natreflection,  _categories,  _description, _enabled='1', _log='0', _sequence='1', _interface='wan', _type='binat', _source_not='0', _destination_net='any', _destination_not='0', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _log is None:
                raise Exception("Required argument _log is missing")
            
            self._log = _log  
            
            if _sequence is None:
                raise Exception("Required argument _sequence is missing")
            
            self._sequence = _sequence  
            
            if _interface is None:
                raise Exception("Required argument _interface is missing")
            
            self._interface = _interface  
            
            if _type is None:
                raise Exception("Required argument _type is missing")
            
            self._type = _type  
            
            if _source_net is None:
                raise Exception("Required argument _source_net is missing")
            
            self._source_net = _source_net  
            
            if _source_not is None:
                raise Exception("Required argument _source_not is missing")
            
            self._source_not = _source_not  
            
            if _destination_net is None:
                raise Exception("Required argument _destination_net is missing")
            
            self._destination_net = _destination_net  
            
            if _destination_not is None:
                raise Exception("Required argument _destination_not is missing")
            
            self._destination_not = _destination_not  
            
            if _external is None:
                raise Exception("Required argument _external is missing")
            
            self._external = _external  
            
            self._natreflection = _natreflection  
            
            self._categories = _categories  
            
            self._description = _description  
            
class _destination_net:    
    """
    class _destination_net
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_destination_net  
    
    :param (str) _AddressFamily:                
    
    :param (str) _NetMaskRequired:                
    
    :param (str) _WildcardEnabled:                
    
        """   
    def __init__(self,  _AddressFamily,  _NetMaskRequired,  _WildcardEnabled, ):
            self._AddressFamily = _AddressFamily  
            
            self._NetMaskRequired = _NetMaskRequired  
            
            self._WildcardEnabled = _WildcardEnabled  
            
class _onetoone:    
    """
    class _onetoone
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_onetoone  
     
    :param (list[_rule]) _rule: A list of _rule instances.                    
    
        """   
    def __init__(self,  _rule, ):
            self._rule = _rule  
            
class _rule:    
    """
    class _rule
    ---------------------------------------------------------------
    
    Mount: /OPNsense/Firewall/Filter/_rule  
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (bool) _log:  
           Required, Default= 0               
    
    :param (int) _sequence:  
           Required, Default= 1, Min= 1, Max= 99999               
    
    :param (str) _interface: Interface 
           Required, Default= wan               
    
    :param (str) _type:  
           Required, Default= binat, Options= ['BINAT', 'NAT']               
    
    :param (str) _source_net: NetworkAlias 
           Required               
    
    :param (bool) _source_not:  
           Required, Default= 0               
    
    :param (str) _destination_net: NetworkAlias 
           Required, Default= any               
    
    :param (bool) _destination_not:  
           Required, Default= 0               
    
    :param (str) _external: Network 
           Required               
    
    :param (str) _natreflection:  
           Options= ['', 'Enable', 'Disable']               
     
    :param (Category) _categories: An instance of the Category class.                
    
    :param (str) _description: Description               
    
        """   
    def __init__(self,  _source_net,  _external,  _natreflection,  _categories,  _description, _enabled='1', _log='0', _sequence='1', _interface='wan', _type='binat', _source_not='0', _destination_net='any', _destination_not='0', ):
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _log is None:
                raise Exception("Required argument _log is missing")
            
            self._log = _log  
            
            if _sequence is None:
                raise Exception("Required argument _sequence is missing")
            
            self._sequence = _sequence  
            
            if _interface is None:
                raise Exception("Required argument _interface is missing")
            
            self._interface = _interface  
            
            if _type is None:
                raise Exception("Required argument _type is missing")
            
            self._type = _type  
            
            if _source_net is None:
                raise Exception("Required argument _source_net is missing")
            
            self._source_net = _source_net  
            
            if _source_not is None:
                raise Exception("Required argument _source_not is missing")
            
            self._source_not = _source_not  
            
            if _destination_net is None:
                raise Exception("Required argument _destination_net is missing")
            
            self._destination_net = _destination_net  
            
            if _destination_not is None:
                raise Exception("Required argument _destination_not is missing")
            
            self._destination_not = _destination_not  
            
            if _external is None:
                raise Exception("Required argument _external is missing")
            
            self._external = _external  
            
            self._natreflection = _natreflection  
            
            self._categories = _categories  
            
            self._description = _description  
            