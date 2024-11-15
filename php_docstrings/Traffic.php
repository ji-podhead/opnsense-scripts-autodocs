<?php

/**
 * script Traffic.php
 * ---------------
 * 
 * This script defines the Traffic class, which extends the Base class and is used to manage RRD data for network traffic.
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
 *     An instance of the Traffic class.
 * 
 * Notes:
 * This script defines the following properties:
 * - ds_heartbeat: The heartbeat interval for the RRD data source (120 seconds).
 * - ds_min: The minimum value for the RRD data source (0).
 * - ds_max: The maximum value for the RRD data source (2500000000).
 * - stdfilename: The standard filename for the RRD file ('%s-traffic.rrd').
 * 
 * The script also defines a constructor method that initializes the object with the given filename and adds datasets for traffic statistics.
 * It also defines a payloadSplitter method that splits the payload data into separate RRD files for each interface.
 */