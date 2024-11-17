<?php

/**
 * script Temperature.php
 * ---------------
 * 
 * This script defines the Temperature class, which extends the Base class and is used to manage RRD data for CPU temperature.
 * 
 * *Returns* 
 *   -   object
 *     - An instance of the Temperature class.
 * 
 * *Arguments:*
 * 
 *  - ds_heartbeat: The heartbeat interval for the RRD data source (120 seconds).
 *  - ds_min: The minimum value for the RRD data source (-273).
 *  - ds_max: The maximum value for the RRD data source (5000).
 *  - stdfilename: The standard filename for the RRD file ('system-cputemp.rrd').
 * 
 */