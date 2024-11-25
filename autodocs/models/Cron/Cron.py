
"""
script Cron 
---------------------------------------------------------------

* Cron settings
* Classes: ['_jobs', '_job']
"""

class _jobs:    
    """
    class _jobs
    ---------------------------------------------------------------
    
    Mount: /OPNsense/cron/_jobs  
     
    :param (list[_job]) _job: A list of _job instances.                    
    
        """   
    def __init__(self,  _job, ):
            self._job = _job  
            
class _job:    
    """
    class _job
    ---------------------------------------------------------------
    
    Mount: /OPNsense/cron/_job  
    
    :param (str) _origin: Text 
           Required, Default= cron               
    
    :param (bool) _enabled:  
           Required, Default= 1               
    
    :param (str) _minutes: Text 
           Required, Default= 0               
    
    :param (str) _hours: Text 
           Required, Default= 0               
    
    :param (str) _days: Text 
           Required, Default= *               
    
    :param (str) _months: Text 
           Required, Default= *               
    
    :param (str) _weekdays: Text 
           Required, Default= *               
    
    :param (str) _who: Text 
           Required, Default= root               
    
    :param (str) _command: ConfigdActions 
           Required               
    
    :param (str) _parameters: Text               
    
    :param (str) _description: Description 
           Required               
    
        """   
    def __init__(self,  _command,  _parameters,  _description, _origin='cron', _enabled='1', _minutes='0', _hours='0', _days='*', _months='*', _weekdays='*', _who='root', ):
            if _origin is None:
                raise Exception("Required argument _origin is missing")
            
            self._origin = _origin  
            
            if _enabled is None:
                raise Exception("Required argument _enabled is missing")
            
            self._enabled = _enabled  
            
            if _minutes is None:
                raise Exception("Required argument _minutes is missing")
            
            self._minutes = _minutes  
            
            if _hours is None:
                raise Exception("Required argument _hours is missing")
            
            self._hours = _hours  
            
            if _days is None:
                raise Exception("Required argument _days is missing")
            
            self._days = _days  
            
            if _months is None:
                raise Exception("Required argument _months is missing")
            
            self._months = _months  
            
            if _weekdays is None:
                raise Exception("Required argument _weekdays is missing")
            
            self._weekdays = _weekdays  
            
            if _who is None:
                raise Exception("Required argument _who is missing")
            
            self._who = _who  
            
            if _command is None:
                raise Exception("Required argument _command is missing")
            
            self._command = _command  
            
            self._parameters = _parameters  
            
            if _description is None:
                raise Exception("Required argument _description is missing")
            
            self._description = _description  
            