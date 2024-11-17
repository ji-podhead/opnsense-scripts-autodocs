<?php
/**
 * script Memory.php
 * ---------------
 *
 * Represents a Memory RRD (Round-Robin Database) type.
 *
 * 
 * 
 * *Arguments* 
 *   -   filename : string
 *     - Path to the RRD file (required)
 *
 * *Properties*
 * 
 *   -   ds_heartbeat : int
 *     - Heartbeat interval for the RRD (default: 120)
 *   -   ds_min : int
 *     - Minimum value for the RRD (default: 0)
 *   -   ds_max : int
 *     - Maximum value for the RRD (default: 10000000)
 *   -   stdfilename : string
 *     - Standard filename for the RRD (default: 'system-memory.rrd')
 * 
 * *Datasets*
 * 
 *   -   active : GAUGE
 *     - Active memory usage
 *   -   inactive : GAUGE
 *     - Inactive memory usage
 *   -   free : GAUGE
 *     - Free memory
 *   -   cache : GAUGE
 *     - Cache memory usage
 *   -   wire : GAUGE
 *     - Wired memory usage
 */