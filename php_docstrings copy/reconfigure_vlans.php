#!/usr/local/bin/php
<?php
/**
 * reconfigure_vlans.php
 * -------------------
 *
 * A script to reconfigure the VLANs.
 *
 * *Arguments*
 * 
 * - None
 * 
 * *Functions*
 * 
 * - legacy_interfaces_details(): Returns the interface details
 * - legacy_interface_destroy(): Destroys an interface
 * - legacy_vlan_remove_tag(): Removes a VLAN tag from an interface
 * - legacy_vlan_tag(): Adds a VLAN tag to an interface
 * - legacy_vlan_pcp(): Sets the PCP (Priority Code Point) for a VLAN
 * - legacy_vlan_proto(): Sets the protocol for a VLAN
 * - _interfaces_vlan_configure(): Configures a VLAN interface
 * - ifgroup_setup(): Sets up the interface groups
 * 
 * *Flow*
 * 
 * 1. Collects all relevant VLANs (new, updated, and removed) into a single list
 * 2. Merges the configured VLANs with the existing VLANs
 * 3. Handles existing VLANs (removed, changed, or unchanged)
 * 4. Configures new VLANs
 * 5. Sets up the interface groups
 * 
 * *Outputs*
 * 
 * - None
 * 
 */