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
require_once("/usr/local/opnsense/mvc/script/load_phalcon.php");
$loader->register();
use OPNsense\Core\Config;
use stdClass;

$newRule = new stdClass();
$newRule->type = 'pass';
$newRule->interface = 'lan';
$newRule->ipprotocol = 'inet';
$newRule->statetype = 'keep state';
$newRule->descr = 'testRule';
$newRule->gateway = 'LAN_DHCP';
$newRule->direction = 'in';
$newRule->category = 'testCat';
$newRule->allowopts = 1;
$newRule->prio = 0;
$newRule->quick = 1;
$newRule->protocol = 'udp';
$newRule->source = new stdClass();
$newRule->source->any = 1;
$newRule->destination = new stdClass();
$newRule->destination->any = 1;

$cfg = Config::getInstance()->object();

// print_r($cfg->OPNsense);
// $keys = array_keys((array)$cfg);
// print_r($keys);
// function find_element($element,$searchterm) {
//     if ($element->$searchterm) {
//         return $element->snatrules;
//     } else {
//         foreach ($element->children() as $child) {
//             $result = find_element($child, $searchterm);    
//             if ($result !== null) {
//                 return $result;
//             }
//         }
//     }
//     return null;
// }

// $element = $cfg; // dein SimpleXMLElement-Objekt
// $searchterm= "nptd";
// $npt = find_element($element, $searchterm);

// if ($nptd !== null) {
//     print_r($npt);
// } else {
//     echo "\n".$searchterm . " nicht gefunden"."\n";
// }
print_r($cfg->OPNsense->nptd);
// Neue Regel zur rules-Liste hinzufügen
// $cfg->Firewall->Filter->rules[] = $newRule;

// // oder alternativ:
// // $cfg->Firewall->Filter->rules = array_merge($cfg->Firewall->Filter->rules, [$newRule]);

// // Konfiguration speichern
// Config::getInstance()->save(
//     [
//         'username' => 'root',
//         'time' => microtime(true),
//         'description' => 'my custom update'
//     ]
// );