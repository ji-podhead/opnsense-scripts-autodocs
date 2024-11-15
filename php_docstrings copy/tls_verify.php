#!/usr/local/bin/php
<?php

/**
 * script tls_verify.php
 * ---------------
 * 
 * This script verifies the certificate depth for OpenVPN authentication.
 * 
 * *Params*
 * 
 * - auth_server : string
 *     index: 1
 *     The server identifier for authentication.
 * 
 * *Arguments*
 * 
 * - None
 * 
 * *Returns*
 * 
 * - int
 *     0 on success, 1 on failure.
 * 
 * Notes:
 * This script uses the OPNsense\OpenVPN\OpenVPN class to retrieve the server instance by ID.
 * It also uses the OPNsense\Trust\Store class to validate the OCSP response.
 * The script checks the certificate depth and OCSP validation for the given server ID.
 * If the verification fails, it logs a warning message and exits with a non-zero status code.
 */