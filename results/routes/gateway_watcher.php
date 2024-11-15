#!/usr/local/bin/php
<?php
/**
 * script gateway_watcher.php
 * -------------------------
 * 
 * Dieses Script überwacht die Gateways und generiert Alarme, wenn ein Gateway nicht erreichbar ist.
 * 
 * *Params*
 * 
 * - $argv[1] : string
 *     Der Name der Aktion, die ausgeführt werden soll, wenn ein Alarm generiert wird.
 * 
 * *Returns*
 * 
 * - None
 * 
 * *Functions*
 * 
 * - signalhandler($signal) : Funktion, die aufgerufen wird, wenn ein Signal empfangen wird.
 * - dpinger_status() : Funktion, die den Status der Gateways zurückgibt.
 * - config_read_array($section, $key) : Funktion, die ein Array aus der Konfiguration zurückgibt.
 * - shell_safe($command, $args) : Funktion, die einen Befehl sicher ausführt.
 * - syslog($priority, $message) : Funktion, die eine Meldung in das Systemlog schreibt.
 * 
 * *Variables*
 * 
 * - $config : array
 *     Die Konfiguration des Systems.
 * - $mode : array
 *     Ein Array, das den Status der Gateways speichert.
 * - $poll : int
 *     Der Poll-Intervall in Sekunden.
 * - $wait : int
 *     Der Warte-Intervall in Sekunden.
 * - $alarm : bool
 *     Ein Flag, das anzeigt, ob ein Alarm generiert wurde.
 * 
 */