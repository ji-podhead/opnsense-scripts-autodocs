#!/usr/local/bin/php
<?php
/**
 * register.php
 * ------------
 *
 * A script to manage plugin registration.
 *
 * *Arguments*
 * 
 * - $action (optional): The action to perform (install, remove, sync, resync)
 * - $name (optional): The name of the plugin to install or remove
 * 
 * *Functions*
 * 
 * - plugins_config_get($config): Returns the current plugin configuration
 * - plugins_config_set($config, $plugins): Sets the plugin configuration
 * - plugins_disk_found($name): Checks if a plugin is found on disk
 * - plugins_disk_get(): Returns a list of plugins found on disk
 * 
 * *Flow*
 * 
 * 1. Checks the command-line arguments for the action and plugin name
 * 2. Initializes the plugin configuration and disk plugins
 * 3. Performs the specified action (install, remove, sync, resync)
 * 4. Updates the plugin configuration if necessary
 * 
 * *Outputs*
 * 
 * - None
 * 
 * *Notes*
 * 
 * - This script uses the Config class to manage the plugin configuration
 * - The script assumes that the plugin metadata is stored in JSON files on disk
 * - This script is used to manage plugin registration and updates
 */