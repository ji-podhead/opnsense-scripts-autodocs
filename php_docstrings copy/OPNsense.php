#!/usr/local/bin/php
<?php
/**
 * script OPNsense.php
 * ---------------
 *
 * Updates the OPNsense configuration based on the system settings.
 *
 * *Params*
 * 
 * - None
 * 
 * *Arguments*
 * 
 * - None
 * 
 * *Returns*
 * 
 * - None
 * 
 * *Description*
 * 
 * This script updates the OPNsense configuration by executing the opnsense-update command with the following options:
 * 
 * - -A: specifies the ABI (Architecture-Based Interface) to use
 * - -m: specifies the mirror URL to use
 * - -n: specifies the flavour to use
 * 
 * The script also checks for a subscription key and appends the URL suffix if present.
 * If no subscription key is set, the license file is deleted.
 */