<?php
/**
 * script States.php
 * ---------------
 * 
 * This script defines the States class, which extends the Base class and is used to manage RRD data for system states.
 * 
 * *Params*
 *
 *  - argsv[0] :  str
 *     -  - The filename of the RRD file to be used.
 * 
 * *Returns* 
 *   -   object
 *     - An instance of the States class.
 * 
 * *Arguments* 
 *   -   ds_heartbeat: The heartbeat interval for the RRD data source (120 seconds).
 *   -   ds_min: The minimum value for the RRD data source (0).
 *   -   ds_max: The maximum value for the RRD data source (10000000).
 *   -   stdfilename: The standard filename for the RRD file ('system-states.rrd').
 */