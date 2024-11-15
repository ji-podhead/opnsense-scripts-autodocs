#!/usr/local/bin/php
<?php
/**
 * Manages CARP (Common Address Redundancy Protocol) configuration and state.
 * 
 * This script performs actions on the CARP configuration, such as entering or leaving maintenance mode, disabling or enabling CARP, and configuring interfaces.
 * 
 * *Params*
 * 
 * - action : string
 *     The action to perform (maintenance, disable, enable).
 * 
 * *Arguments*
 * 
 * - a_vip : array
 *     An array of virtual IP addresses.
 * - config : array
 *     The system configuration array.
 * 
 * *Returns*
 * 
 * - A JSON-encoded array with the result of the action.
 * 
 */