#!/usr/local/bin/php
<?php
/**
 * reconfigure_laggs.php
 * -------------------
 *
 * A script to reconfigure LAGG interfaces.
 *
 * *Arguments*
 * 
 * - None
 * 
 * *Parameters*
 * 
 * - $laggs_todo: An array to store the LAGG interfaces to reconfigure
 * - $vfilename: The path to the file containing the LAGG interfaces to reconfigure
 * - $lagg_configure: An array to store the LAGG interfaces to reconfigure
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
 * - OPNsense\Interfaces\Lagg()->lagg->iterateItems(): Iterates over the LAGG interfaces
 * - legacy_interface_destroy(string $interface): Destroys a legacy interface
 * - _interfaces_lagg_configure(array $lagg): Configures a LAGG interface
 * 
 * *Flow*
 * 
 * 1. Reads the file containing the LAGG interfaces to reconfigure
 * 2. Collects the LAGG interfaces to reconfigure
 * 3. Removes non-existing interfaces
 * 4. Reconfigures the still existing LAGG interfaces
 * 
 * *Outputs*
 * 
 * - None
 * 
 * *Notes*
 * 
 * - This script uses the `file_exists`, `filesize`, `fopen`, `flock`, `fread`, `fwrite`, `ftruncate`, `explode`, `trim`, and other functions to interact with the file system and configure the LAGG interfaces
 * - The script assumes that the LAGG interfaces are configured correctly and that the necessary dependencies are available
 * - This script is similar to reconfigure_gifs.php and reconfigure_gres.php, but it is used for LAGG interfaces instead
 * - Unlike the other reconfigure scripts, this script does not remove addresses from the interfaces or re-apply additional addresses and hook routing
 */