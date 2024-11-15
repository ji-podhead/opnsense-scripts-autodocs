<?php
/**
 * class Packets.php
 * ---------------
 *
 * Represents a Packets RRD (Round-Robin Database) type.
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
 *     Maximum value for the RRD (default: 2500000000)
 * - stdfilename : string
 *     Standard filename for the RRD (default: '%s-packets.rrd')
 * 
 * *Datasets*
 * 
 * - inpass : COUNTER
 *     Number of incoming packets that were passed
 * - outpass : COUNTER
 *     Number of outgoing packets that were passed
 * - inblock : COUNTER
 *     Number of incoming packets that were blocked
 * - outblock : COUNTER
 *     Number of outgoing packets that were blocked
 * - inpass6 : COUNTER
 *     Number of incoming IPv6 packets that were passed
 * - outpass6 : COUNTER
 *     Number of outgoing IPv6 packets that were passed
 * - inblock6 : COUNTER
 *     Number of incoming IPv6 packets that were blocked
 * - outblock6 : COUNTER
 *     Number of outgoing IPv6 packets that were blocked
 * 
 * *Methods*
 * 
 * - wantsStats() : string
 *     Returns the name of the subcollection (Interfaces)
 * - payloadSplitter(array $payload) : iterable
 *     Splits the payload into separate RRD files based on the interface name.
 *     - Parameters:
 *         - payload : array
 *             An array containing interface names as keys and data as values.
 *     - Returns:
 *         - iterable
 *             An iterable containing RRD filenames as keys and data as values.
 */