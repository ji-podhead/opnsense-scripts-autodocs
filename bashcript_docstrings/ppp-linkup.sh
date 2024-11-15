#!/bin/sh
# script ppp-linkup.sh
# ------------------------
#
# Handles the link up event for a PPP interface.
#
# *Params*
#
#  1. IF: str
#    The name of the PPP interface.
#  2. AF: str
#    The address family (inet or inet6).
#  3. (unused)
#  4. ROUTER: str
#    The IP address of the router (optional).
#  5. (unused)
#  6. DNS1: str
#    The first DNS server IP address (optional).
#  7. DNS2: str
#    The second DNS server IP address (optional).
#
# *Arguments*
#
#- None
#
# *Returns*
#
#- None
#
# Description:
# This script handles the link up event for a PPP interface.
# It configures the interface for the specified address family (inet or inet6).
# It sets the DNS servers and router IP address if provided.
# It also triggers the `configctl` command to update the interface configuration.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the necessary commands (`ifctl`, `configctl`, `ppp-ipv6.php`) are available.
#  - The script uses the `/tmp/${IF}_uptime` file to store the uptime of the PPP connection.