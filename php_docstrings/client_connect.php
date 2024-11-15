#!/usr/local/bin/php
<?php
/**
 * script client_connect.php
 * -------------------------
 * 
 * Authenticates an OpenVPN user and generates a client configuration file.
 * 
 * This script authenticates an OpenVPN user based on the provided common name and server ID, and generates a client configuration file if required.
 * 
 * *Params*
 * 
 * - None
 * 
 * *Arguments*
 * 
 * - common_name : string
 *     The common name of the user.
 * - vpnid : string
 *     The ID of the OpenVPN server.
 * - config_file : string
 *     The path to the client configuration file.
 * - server : OPNsense\OpenVPN\OpenVPN
 *     The OpenVPN server instance.
 * - cso : OPNsense\OpenVPN\OpenVPN
 *     The client-specific override configuration.
 * 
 * *Returns*
 * 
 * - None
 * 
 * *Environment Variables*
 * 
 * - common_name : The common name of the user.
 * - auth_server : The ID of the OpenVPN server.
 * - config_file : The path to the client configuration file.
 * 
 */