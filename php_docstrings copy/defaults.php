#!/usr/local/bin/php
<?php
/**
 * script defaults.php
 * ------------------
 * 
 * Resets the firewall to factory defaults.
 * 
 * This script prompts the user to confirm whether they want to reset the firewall to factory defaults, and then calls the reset_factory_defaults() function if the user confirms.
 * 
 * *Params*
 * 
 * - None
 * 
 * *Arguments*
 * 
 * - fp : resource
 *     A file pointer to the standard input stream.
 * - yes_no_prompt : string
 *     The prompt to display to the user.
 * 
 * *Returns*
 * 
 * - None
 * 
 * *Functions*
 * 
 * - reset_factory_defaults() : Resets the firewall to factory defaults.
 * 
 */