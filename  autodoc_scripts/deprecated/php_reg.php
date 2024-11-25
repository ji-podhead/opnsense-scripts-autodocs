<?php
namespace OPNsense\Autoload;

class Loader
{
    private $probe_dirs = [];
    private $is_registered = false;
    private $classes_loaded = [];
    public function __construct($dirs = null)
    {
        $this->probe_dirs = $dirs;
    }
    public function register()
    {
        if (!$this->is_registered) {
            spl_autoload_register([$this, "autoload"], true);
            $this->is_registered = true;
        }
    }
    public function autoload($className)
    {   print_r("\n ----------------- \n autoloading:    ");
        if (!in_array($className, $this->classes_loaded)) {
            $parts = explode('\\', $className);
            $lastParts = array_slice($parts, -3);
            $class_path = end($lastParts) . '.php';
            print_r($class_path);

            foreach ($this->probe_dirs as $dirname) {
                $path =  $dirname;
                $file = $path . "/" . $class_path;
                if (is_file($file)) {
                    print_r("\n file found in " . $file);
                    require($file);
                    $this->classes_loaded[] = $className;
                    break;
                }
            }
        }
    }
}
$loader = new Loader( [    
    __DIR__ . 'usr/local/opnsense/mvc/app/models/OPNsense/Base',
    __DIR__ . 'usr/local/opnsense/mvc/app/models/OPNsense/Firewall',
    __DIR__ . 'usr/local/opnsense/mvc/app/controllers/OPNsense/Base',
    __DIR__ . 'usr/local/opnsense/mvc/app/controllers/OPNsense/Firewall',
    __DIR__ . 'usr/local/opnsense/mvc/app/library/OPNsense/Core',
    __DIR__ . 'usr/local/opnsense/mvc/app/library/OPNsense/Autoload',
    __DIR__ . 'usr/local/opnsense/scripts/system/',

    

]);
//require('usr/local/www/guiconfig.inc');
require('usr/local/etc/inc/config.inc');
// file needs to get placed in /usr/local/opnsense
// sudo scp ~/Dokumente/ji-podhead/opnsense-scripts-autodoc/php_reg.php root@opnsense:/usr/local/opnsense/php1.php
$loader->register();
use OPNsense\Firewall\Filter;
use OPNsense\Base;

$filter = new Filter();
//$filter-> {"id"} = "";
$filter-> {"after"} = "";
$filter-> {"floating"} = "";
$filter-> {"type"} = "pass";
$filter-> {"quick"} = "yes";
$filter-> {"interface"} = "lan";
$filter-> {"direction"} = "in";
$filter-> {"ipprotocol"} = "inet";
$filter-> {"protocol"} = "any";
$filter-> {"icmptype"} = "";
$filter-> {"icmp6-type"} = "";
$filter-> {"src"} = "any";
$filter-> {"dst"} = "any";
$filter-> {"category[]"} = "testCat";
$filter-> {"descr"} = "sssssssssssssssssss";
$filter-> {"sched"} = "";
$filter-> {"gateway"} = "";
$filter-> {"reply-to"} = "";
$filter-> {"set-prio"} = "";
$filter-> {"set-prio-low"} = "";
$filter-> {"prio"} = "";
$filter-> {"tos"} = "";
$filter-> {"tag"} = "";
$filter-> {"tagged"} = "";
$filter-> {"max"} = "";
$filter-> {"max-src-nodes"} = "";
$filter-> {"max-src-conn"} = "";
$filter-> {"max-src-states"} = "";
$filter-> {"max-src-conn-rate"} = "";
$filter-> {"max-src-conn-rates"} = "";
$filter-> {"overload"} = "virusprot";
$filter-> {"statetimeout"} = "";
$filter-> {"adaptivestart"} = "";
$filter-> {"adaptiveend"} = "";
$filter-> {"os"} = "";
$filter-> {"statetype"} = "keep+state";
$filter-> {"Submit"} = "Save";

$filter->performValidation();