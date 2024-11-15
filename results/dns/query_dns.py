"""
script query_dns.py
------------------------------------------

*Parameters*
                        
* domain : str
    * Description: domain name to query 
    * options : [] 
    * const : None 
    * default : None 
    * choices : None 
    * required : True
* types : str
    * Description: list of types to query (when querying hostnames) 
    * options : ['--types'] 
    * const : None 
    * default : A,AAAA,MX,TXT 
    * choices : None 
    * required : False
* server : str
    * Description: server to query 
    * options : ['--server'] 
    * const : None 
    * default : None 
    * choices : None 
    * required : False"""