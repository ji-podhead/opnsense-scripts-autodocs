#!/usr/local/bin/php
<?php

/**
 * reconfigure_gres.php
 * -------------------
 *
 * A script to reconfigure GRE interfaces.
 *
 * *Arguments*
 * 
 * - None
 * 
 * *Parameters*
 * 
 * - $gres_todo: An array to store the GRE interfaces to reconfigure
 * - $vfilename: The path to the file containing the GRE interfaces to reconfigure
 * - $gre_configure: An array to store the GRE interfaces to reconfigure
 * - $ifdetails: An array to store the interface details
 * 
 * *Functions*
 * 
 * - file_exists(string $filename): Checks if a file exists
 * - filesize(string $filename): Returns the size of a file
 * - fopen(string $filename, string $mode): Opens a file pointer
 * - flock(resource $handle, int $operation): Locks or unlocks a file
 * - fread(resource $handle, int $length): Reads from a file pointer
 * - fwrite(resource $handle, string $string): Writes to a file pointer
 * - ftruncate(resource $handle, int $size): Truncates a file to a specified size
 * - explode(string $delimiter, string $string): Splits a string into an array using a delimiter
 * - trim(string $string): Removes whitespace from a string
 * - OPNsense\Interfaces\Gre()->gre->iterateItems(): Iterates over the GRE interfaces
 * - legacy_interface_destroy(string $interface): Destroys a legacy interface
 * - legacy_interfaces_details(): Returns the interface details
 * - interfaces_addresses_flush(string $interface, int $family, array $ifdetails): Flushes addresses from an interface
 * - _interfaces_gre_configure(array $gre): Configures a GRE interface
 * - interfaces_restart_by_device(bool $force, array $interfaces): Restarts interfaces
 * 
 * *Flow*
 * 
 * 1. Reads the file containing the GRE interfaces to reconfigure
 * 2. Collects the GRE interfaces to reconfigure
 * 3. Removes non-existing interfaces
 * 4. Reconfigures the still existing GRE interfaces
 * 5. Removes addresses from the interfaces (if necessary)
 * 6. Configures the GRE interfaces
 * 7. Re-applies additional addresses and hooks routing (if necessary)
 * 
 * *Outputs*
 * 
 * - None
 * 
 * *Notes*
 * 
 * - This script uses the `file_exists`, `filesize`, `fopen`, `flock`, `fread`, `fwrite`, `ftruncate`, `explode`, `trim`, and other functions to interact with the file system and configure the GRE interfaces
 * - The script assumes that the GRE interfaces are configured correctly and that the necessary dependencies are available
 * - This script is similar to reconfigure_gifs.php, but it is used for GRE interfaces instead of GIF interfaces
 */