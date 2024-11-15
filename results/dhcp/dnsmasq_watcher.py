"""
script dnsmasq_watcher.py
------------------------------------------

*Parameters*
                        
* domain : str
    * Description: default domain to use 
    * options : ['--domain'] 
    * const : None 
    * default : local 
    * choices : None 
    * required : False
* pid : str
    * Description: pid file location 
    * options : ['--pid'] 
    * const : None 
    * default : /var/run/dnsmasq_dhcpd.pid 
    * choices : None 
    * required : False
* servicepid : str
    * Description: dnsmasq pid file location 
    * options : ['--servicepid'] 
    * const : None 
    * default : /var/run/dnsmasq.pid 
    * choices : None 
    * required : False
* source : str
    * Description: source leases file 
    * options : ['--source'] 
    * const : None 
    * default : /var/dhcpd/var/db/dhcpd.leases 
    * choices : None 
    * required : False
* target : str
    * Description: target config file 
    * options : ['--target'] 
    * const : None 
    * default : /var/etc/dnsmasq-leases 
    * choices : None 
    * required : False"""