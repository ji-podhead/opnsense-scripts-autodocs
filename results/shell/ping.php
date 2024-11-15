#!/usr/local/bin/php
<?php

/**
 * ping.php
 * ----------
 *
 * A script to ping a host name or IP address.
 *
 * *Arguments*
 * 
 * - None
 * 
 * *Parameters*
 * 
 * - $fp: The file pointer for standard input
 * - $pinghost: The host name or IP address to ping
 * 
 * *Functions*
 * 
 * - fopen(string $filename, string $mode): Opens a file pointer
 * - fgets(resource $fp): Reads a line from the file pointer
 * - escapeshellarg(string $arg): Escapes a shell argument
 * - passthru(string $command): Executes a shell command and displays the output
 * - fclose(resource $fp): Closes a file pointer
 * 
 * *Flow*
 * 
 * 1. Opens the standard input file pointer
 * 2. Prompts the user to enter a host name or IP address
 * 3. Reads the user input and stores it in the $pinghost variable
 * 4. Pings the host name or IP address using the [/sbin/ping](cci:7://file:///sbin/ping:0:0-0:0) command with the `-c 3` and `-n` options
 * 5. Displays the output of the ping command
 * 6. Prompts the user to press ENTER to continue
 * 7. Reads the user input and closes the standard input file pointer
 * 
 * *Outputs*
 * 
 * - The output of the ping command
 * 
 * *Notes*
 * 
 * - This script uses the `fopen`, `fgets`, `escapeshellarg`, `passthru`, and `fclose` functions to interact with the user and execute the ping command
 * - The script assumes that the [/sbin/ping](cci:7://file:///sbin/ping:0:0-0:0) command is available on the system
 */