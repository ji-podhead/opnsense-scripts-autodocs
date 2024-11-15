<?php

/**
 * class Mbuf.php
 * ---------------
 *
 * Represents a Mbuf (Memory Buffer) RRD (Round-Robin Database) type.
 *
 * *Params*
 * 
 * - None
 * 
 * *Arguments*
 * 
 * - filename : string
 *     Path to the RRD file (required)
 * 
 * *Returns*
 * 
 * - None
 * 
 * *Properties*
 * 
 * - ds_heartbeat : int
 *     Heartbeat interval for the RRD (default: 120)
 * - ds_min : int
 *     Minimum value for the RRD (default: 0)
 * - ds_max : int
 *     Maximum value for the RRD (default: 10000000)
 * - stdfilename : string
 *     Standard filename for the RRD (default: 'system-mbuf.rrd')
 */