#!/usr/local/bin/php
<?php

/**
 * script  prefixes.php
 * ----------
 *
 * A script to manage IPv6 prefixes and routes based on DHCPv6 leases.
 *
 * *Arguments* 
 *   -   $leases_file: The path to the DHCPv6 leases file
 *   -   $duid_arr: An array to store DUIDs and their corresponding addresses and prefixes
 *   -   $routes: An array to store the routes to be added or deleted
 * 
 * *Functions* 
 *   -   dhcpd_parse_duid(string $duid): Parses a DUID and returns its components
 *   -   is_linklocal(string $ipaddrv6): Checks if an IPv6 address is link-local
 *   -   get_real_interface(string $interface, string $family): Returns the real interface name for a given interface and family
 *   -   plugins_run(string $hook): Runs a plugin hook and returns the results
 *   -   shell_safe(string $command): Runs a shell command and returns the output
 *   -   mwexecf(string $command, array $args, bool $quiet): Runs a shell command with arguments and returns the output
 * 
 * *Flow*
 *  - Reads the DHCPv6 leases file and extracts the DUIDs, addresses, and prefixes
 *  -  Iterates through the static mapping plugin results and updates the DUID array with static mappings
 *  -  Collects expired leases from the DHCPv6 log file
 *  -  Collects active leases from the DUID array
 *  -  Deletes all expired routes
 *  -  Adds active routes
 *
 * *Notes*
 * 
 *   -   This script assumes that the DHCPv6 leases file is in the format expected by the DHCPv6 server
 *   -   The script uses the `plugins_run` function to run the `static_mapping:dhcpd` plugin hook
 *   -   The script uses the `shell_safe` function to run shell commands and capture the output
 */