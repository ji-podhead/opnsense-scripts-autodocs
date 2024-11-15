#!/usr/local/bin/php
<?php
/**
 * script latest.php
 * ---------------
 *
 * Retrieves the latest stable version of OPNsense by parsing the changelog file.
 *
 * *Params*
 * 
 * - changelogfile : str
 *     index: 1
 *     Path to the changelog file (default: /usr/local/opnsense/changelog/index.json)
 * 
 * *Arguments*
 * 
 * - None
 * 
 * *Returns*
 * 
 * - string
 *     The latest stable version of OPNsense, or the current version if unknown.
 */