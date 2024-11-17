<?php
/**
 * script Factory.php
 * --------------
 * 
 * RRD Factory class, offers access to RRD types and statistics.
 * 
 * This class provides a factory for creating RRD types and statistics, and offers methods for collecting and updating RRD data.
 * 
 * *Properties*
 * 
 *   -   stats : array
 *     - An array of gathered statistics.
 * 
 * *Methods*
 * 
 *   -   get(string $type, string $target) : \OPNsense\RRD\Types\Base
 *     - Returns an instance of the specified RRD type.
 *   -   collect() : $this
 *     - Collects statistics to feed to RRD.
 *   -   getData(string $name) : array
 *     - Returns the gathered statistics for a specific collector.
 *   -   getRawStats() : array
 *     - Returns the collected statistics.
 *   -   updateAll($debug = false) : $this
 *     - Updates all registered RRD graphs.
 * 
 * *Exceptions*
 * 
 *   -   TypeNotFound : Thrown if the class is not found or has an improper type.
 * 
 */