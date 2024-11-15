#!/usr/local/bin/php
<?php
/**
 * ovpn_service_control.php
 * -------------------------
 *
 * Controls the OpenVPN instances on the system.
 *
 * *Arguments*
 * 
 * - -a: all instances
 * - -h: help
 * - stop|start|restart|configure: action
 * - uuid: UUID of the instance
 *
 * *Description*
 * 
 * This script controls the OpenVPN instances on the system. It can be used to start, stop, restart, or configure instances.
 *
 * *Functions*
 * 
 * - setup_interface($instance): Configures the network interface for the OpenVPN instance.
 * - ovpn_start($instance, $fhandle): Starts the OpenVPN instance.
 * - ovpn_stop($instance, $destroy_if = false): Stops the OpenVPN instance.
 * - ovpn_instance_stats($instance, $fhandle): Reads the statistics of the OpenVPN instance.
 * - get_vhid_status(): Reads the status of the CARP instances.
 *
 * *Notes*
 * 
 * - The functions setup_interface, ovpn_start, ovpn_stop, and ovpn_instance_stats are used to control the OpenVPN instances.
 * - The function get_vhid_status is used to read the status of the CARP instances.
 * - The -a option can be used to control all instances.
 * - The -h option can be used to display the help.
 */