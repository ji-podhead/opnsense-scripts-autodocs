#!/usr/local/bin/php
<?php

/**
 * script traffic_stats.php
 * ---------------
 * 
 * This script collects and displays traffic statistics for network interfaces.
 * 
 * *Params*
 * 
 * - interval : int
 *     index: 1
 *     The interval in seconds to collect traffic statistics.
 * 
 * *Arguments*
 * 
 * - None
 * 
 * *Returns*
 * 
 * - string
 *     The traffic statistics in JSON format.
 * 
 * Notes:
 * This script uses the `legacy_config_get_interfaces` and `legacy_interface_stats` functions to collect interface information and statistics.
 * It also uses the `map_ifs` function to map interface data to a standardized format.
 * If an interval is specified, the script will collect statistics at that interval and output the results in a streaming format.
 * If no interval is specified, the script will collect statistics once and output the results in a single JSON object.
 */