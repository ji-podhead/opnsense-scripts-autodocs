#!/usr/local/bin/php
<?php
/**
 * rollback_timer.php
 * -----------------
 *
 * A script to manage the rollback timer for firewall filter changes.
 *
 * *Arguments*
 * 
 * - $revision (optional): The revision number to rollback to
 * 
 * *Functions*
 * 
 * - OPNsense\Firewall\Filter::rollback($revision): Rolls back to the specified revision
 * - OPNsense\Core\Backend::configdRun($command): Runs a command on the backend
 * 
 * *Flow*
 * 
 * 1. Checks the command-line arguments for the revision number
 * 2. Creates a lock file for the revision
 * 3. Waits for 60 seconds for the API to callback
 * 4. If the lock file is deleted, exits with success
 * 5. If the lock file still exists, rolls back to the specified revision
 * 6. Reloads the firewall filter configuration if the rollback is successful
 * 
 * *Outputs*
 * 
 * - None
 * 
 * *Notes*
 * 
 * - This script uses the OPNsense\Firewall\Filter class to manage firewall filter changes
 * - The script assumes that the revision number is a valid integer
 * - This script is used to manage the rollback timer for firewall filter changes
 */