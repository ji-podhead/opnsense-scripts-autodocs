#!/usr/local/bin/php
<?php
/**
 * script process_accounting_messages.php
 * -----------------------------
 *
 * A script to process accounting messages for captive portal sessions.
 *
 * The script uses the `OPNsense\Auth\AuthenticationFactory` class to get the authenticator object for the session.
 * The script uses the `method_exists` function to check if the authenticator object has the required methods.
 * 
 * *Arguments* 
 *   -   $database_filename: The path to the captive portal database file
 *   -   $db: The SQLite database object
 *   -   $result: The result of the database query
 *   -   $authFactory: The authentication factory object
 *   -   $authenticator: The authenticator object for the session
 *   -   $row: The current row of the database query result
 * 
 * *Functions* 
 *   -   OPNsense\Auth\AuthenticationFactory::get(string $authenticated_via): Returns the authenticator object for the given authentication method
 *   -   $authenticator->startAccounting(string $username, string $sessionid): Sends a start accounting event to the authenticator (if applicable)
 *   -   $authenticator->stopAccounting(string $username, string $sessionid, int $time_spend, int $bytes_in, int $bytes_out, string $ip_address): Sends a stop accounting event to the authenticator (if applicable)
 *   -   $authenticator->updateAccounting(string $username, string $sessionid, int $time_spend, int $bytes_in, int $bytes_out, string $ip_address): Sends an interim update event to the authenticator (if applicable)
 * 
 * *Flow*
 *  - Opens the captive portal database file
 *  -  Queries the database for all sessions with client restrictions
 *  -  Processes each session in the query result
 *  -  For each session, checks the authentication method and gets the corresponding authenticator object
 *  -  If the session has a new accounting state, sends a start accounting event to the authenticator (if applicable)
 *  -  If the session is deleted and the accounting state is not stopped, sends a stop accounting event to the authenticator (if applicable)
 *  -  If the session is not stopped, sends an interim update event to the authenticator (if applicable)
 *  -  Closes the database connection
 *
 * *Notes*
 * 
 *   -   
 *   -   
 *   -   
 */