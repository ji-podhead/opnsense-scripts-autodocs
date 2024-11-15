"""
script logger.py
------------------------------------------

*Parameters*
                        
* pipe : str
    * Description: named pipe file location 
    * options : ['--pipe'] 
    * const : None 
    * default : /var/unbound/data/dns_logger 
    * choices : None 
    * required : False
* targetdb : str
    * Description: duckdb filename 
    * options : ['--targetdb'] 
    * const : None 
    * default : /var/unbound/data/unbound.duckdb 
    * choices : None 
    * required : False
* backup_dir : str
    * Description: backup directory 
    * options : ['--backup_dir'] 
    * const : None 
    * default : /var/cache/unbound.duckdb 
    * choices : None 
    * required : False
* flush_interval : str
    * Description: interval to flush to db 
    * options : ['--flush_interval'] 
    * const : None 
    * default : 10 
    * choices : None 
    * required : False"""