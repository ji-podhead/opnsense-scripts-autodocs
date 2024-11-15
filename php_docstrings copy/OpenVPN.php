<?php
/**
 * class OpenVPN.php
 * ---------------
 *
 * Represents an OpenVPN RRD (Round-Robin Database) type.
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
 *     Maximum value for the RRD (default: 10000)
 * - stdfilename : string
 *     Standard filename for the RRD (default: '%s-vpnusers.rrd')
 * 
 * *Datasets*
 * 
 * - users : GAUGE
 *     Number of VPN users
 * 
 * *Methods*
 * 
 * - payloadSplitter(array $payload) : iterable
 *     Splits the payload into separate RRD files based on the interface name.
 *     - Parameters:
 *         - payload : array
 *             An array containing interface names as keys and data as values.
 *     - Returns:
 *         - iterable
 *             An iterable containing RRD filenames as keys and data as values.
 */