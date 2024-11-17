#!/usr/local/bin/php
<?php

/**
 * script generate_certs.php
 * -------------------------
 * 
 * Generates certificate files for captive portal zones.
 *
 * This script generates certificate files for captive portal zones based on the configuration.
 *
 *
*
 * *Functions*
 *   -   require_once(string $filename) : void
 *     - Includes the specified file.
 *   -   Config::getInstance() : \OPNsense\Core\Config
 *     - Returns an instance of the Config class.
 *   -   OPNsense\Core\Config::getInstance() : \OPNsense\Core\Config
 *     - Returns an instance of the Config class.
 *   -   Config::getInstance()->object() : object
 *     - Returns the configuration object.
 *   -   OPNsense\Trust\Store::getCertificate(string $certificate) : array
 *     - Retrieves the certificate with the specified identifier.
 *   -   touch(string $filename) : bool
 *     - Creates a new file or updates the access and modification times of an existing file.
 *   -   chmod(string $filename, int $mode) : bool
 *     - Sets the permissions of a file.
 *   -   file_put_contents(string $filename, string $data) : int
 *     - Writes data to a file.
 *
 * *Arguments*
 *   -   store : \OPNsense\Trust\Store
 *     - An instance of the Store class.
 *   -   configObj : object
 *     - The configuration object.
 *   -   zone : object
 *     - The current zone.
 *   -   cert : array
 *     - The certificate.
 *   -   output_pem_filename : string
 *     - The output filename.
 *
 * *Classes*
 *
 *   -   \OPNsense\Core\Config
 *     - The Config class.
 *   -   \OPNsense\Trust\Store
 *     - The Store class.
 *
 */