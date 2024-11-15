<?php

/**
 * script Temperature.php
 * ---------------
 * 
 * This script defines the Temperature class, which extends the Base class and is used to manage RRD data for CPU temperature.
 * 
 * *Params*
 * 
 * - None
 * 
 * *Arguments*
 * 
 * - filename : string
 *     index: 1
 *     The filename of the RRD file to be used.
 * 
 * *Returns*
 * 
 * - object
 *     An instance of the Temperature class.
 * 
 * Notes:
 * This script defines the following properties:
 * - ds_heartbeat: The heartbeat interval for the RRD data source (120 seconds).
 * - ds_min: The minimum value for the RRD data source (-273).
 * - ds_max: The maximum value for the RRD data source (5000).
 * - stdfilename: The standard filename for the RRD file ('system-cputemp.rrd').
 * 
 * The script also defines a constructor method that initializes the object with the given filename and adds a dataset for cpu0temp.
 * It also sets RRA (Round Robin Archive) for the RRD data source.
 */