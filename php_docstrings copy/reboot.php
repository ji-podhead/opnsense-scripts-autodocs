#!/usr/local/bin/php
<?php
/**
 * netboot.php
 * ----------
 *
 * A script to reboot the system after confirmation.
 *
 * *Arguments*
 * 
 * - None
 * 
 * *Parameters*
 * 
 * - $fp: The file pointer for standard input
 * 
 * *Functions*
 * 
 * - fopen(string $filename, string $mode): Opens a file pointer
 * - fgets(resource $fp): Reads a line from the file pointer
 * - chop(string $string): Removes trailing whitespace from a string
 * - strcasecmp(string $str1, string $str2): Compares two strings in a case-insensitive manner
 * - passthru(string $command): Executes a shell command and displays the output
 * - fclose(resource $fp): Closes a file pointer
 * 
 * *Flow*
 * 
 * 1. Opens the standard input file pointer
 * 2. Prompts the user to confirm the reboot
 * 3. Reads the user input and checks if it matches 'y' (case-insensitive)
 * 4. If confirmed, executes the `/usr/local/etc/rc.reboot` command to reboot the system
 * 5. Closes the standard input file pointer
 * 
 * *Outputs*
 * 
 * - The output of the reboot command (if executed)
 * 
 * *Notes*
 * 
 * - This script uses the `fopen`, `fgets`, `chop`, `strcasecmp`, `passthru`, and `fclose` functions to interact with the user and execute the reboot command
 * - The script assumes that the `/usr/local/etc/rc.reboot` command is available on the system and will reboot the system
 */