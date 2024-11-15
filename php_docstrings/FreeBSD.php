#!/usr/local/bin/php
<?php
/**
 * Disables the FreeBSD repository to avoid breakage.
 * 
 * This script ensures that the FreeBSD repository is disabled by copying the sample configuration file over the active configuration file.
 * 
 * *Variables*
 * 
 * - conf : string
 *     The path to the FreeBSD repository configuration file.
 * 
 * *Actions*
 * 
 * - Copies the sample configuration file ($conf . '.sample') over the active configuration file ($conf).
 * 
 */