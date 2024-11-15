<?php
/**
 * script States.php
 * ---------------
 * 
 * This script defines the States class, which extends the Base class and is used to manage RRD data for system states.
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
 *     An instance of the States class.
 * 
 * Notes:
 * This script defines the following properties:
 * - ds_heartbeat: The heartbeat interval for the RRD data source (120 seconds).
 * - ds_min: The minimum value for the RRD data source (0).
 * - ds_max: The maximum value for the RRD data source (10000000).
 * - stdfilename: The standard filename for the RRD file ('system-states.rrd').
 * 
 * The script also defines a constructor method that initializes the object with the given filename and adds datasets for pfrate, pfstates, pfnat, srcip, and dstip.
 */