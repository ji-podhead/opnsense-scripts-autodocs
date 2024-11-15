<?php
/**
 * class Ntp.php
 * ---------------
 *
 * Represents an NTP (Network Time Protocol) RRD (Round-Robin Database) type.
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
 *     Maximum value for the RRD (default: 1000)
 * - stdfilename : string
 *     Standard filename for the RRD (default: 'ntpd.rrd')
 * 
 * *Datasets*
 * 
 * - offset : GAUGE
 *     NTP offset value
 * - sjit : GAUGE
 *     NTP synchronization jitter
 * - cjit : GAUGE
 *     NTP clock jitter
 * - wander : GAUGE
 *     NTP clock wander
 * - freq : GAUGE
 *     NTP frequency offset
 * - disp : GAUGE
 *     NTP dispersion
 */