<?php

/**
 * script Processor.php
 * ----------
 *
 * A class representing a processor RRD type.
 *
 * *Namespace*
 * 
 *   -   OPNsense\RRD\Types
 * 
 * *Class*
 * 
 *   -   Processor
 * 
 * *Inheritance*
 * 
 *   -   Extends Base
 * 
 * *Properties*
 * 
 *   -   $ds_heartbeat: The heartbeat interval for the RRD data source (default: 120)
 *   -   $ds_min: The minimum value for the RRD data source (default: 0)
 *   -   $ds_max: The maximum value for the RRD data source (default: 10000000)
 *   -   $stdfilename: The standard filename for the RRD file (default: 'system-processor.rrd')
 * 
 * *Methods*
 * 
 *   -   __construct(string $filename): Initializes the processor RRD type with the given filename
 *   -   addDatasets(array $datasets, string $type): Adds the given datasets to the RRD type
 * 
 * *Flow*
 *  - Initializes the processor RRD type with the given filename
 *  -  Adds the 'user', 'nice', 'system', 'interrupt', and 'processes' datasets to the RRD type with a GAUGE type
 *
 * *Notes*
 * 
 *   -   This class extends the Base class and provides a specific implementation for processor RRD types
 *   -   The $ds_heartbeat, $ds_min, and $ds_max properties are used to configure the RRD data source
 *   -   The $stdfilename property provides a default filename for the RRD file
 */