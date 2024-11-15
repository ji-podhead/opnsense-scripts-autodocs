#!/usr/local/bin/php
<?php
/**
 * script user_pass_verify
 * ---------------
 * 
 * This script performs authentication for OpenVPN users.
 * 
 * *Params*
 * 
 * - auth_server : string
 *     The ID of the OpenVPN server.
 * - auth_method : string
 *     The authentication method to use (via-env or via-file).
 * - common_name : string
 *     The common name of the certificate.
 * - auth_file : string
 *     The file containing the username and password (when using via-file method).
 * - auth_defer : bool
 *     Whether to defer authentication to another process.
 * - auth_control_file : string
 *     The file to write the authentication result to (when using auth_defer).
 * 
 * *Arguments*
 * 
 * - None
 * 
 * *Returns*
 * 
 * - int
 *     0 on success, non-zero on failure.
 * 
 * Notes:
 * This script uses the OPNsense\Auth\AuthenticationFactory class to perform authentication.
 * It also uses the OPNsense\OpenVPN\OpenVPN class to retrieve OpenVPN server information and create client-specific overrides.
 * The script logs authentication results to the syslog.
 */