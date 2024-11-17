<?php

/**
 * script Traffic.php
 * ---------------
 * 
 * This script defines the Traffic class, which extends the Base class and is used to manage RRD data for network traffic.
 * 
 * *Params*
 * 
 *   -   $argv[0] : str
 *     - The filename of the RRD file to be used.
 * 
 * *Returns* 
 *   -   object
 *     - An instance of the Traffic class.
 * 
 * *Arguments:*
 *  - ds_heartbeat: The heartbeat interval for the RRD data source (120 seconds).
 *  - ds_min: The minimum value for the RRD data source (0).
 *  - ds_max: The maximum value for the RRD data source (2500000000).
 *  - stdfilename: The standard filename for the RRD file ('%s-traffic.rrd').
 * 
 */