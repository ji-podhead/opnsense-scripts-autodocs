#!/bin/sh
# script start.sh
# ------------------------
#
# Starts the Unbound DNS resolver and configures it for use with OPNsense.
#
# *Params*
#
#  1. DOMAIN: str
#    The domain name to use for DHCP and DNS configuration.
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
# This script starts the Unbound DNS resolver and configures it for use with OPNsense.
# It removes any existing configuration files, checks for the presence of the root.key file, and runs unbound-anchor if necessary.
# The script then copies configuration files from /usr/local/etc/unbound.opnsense.d to /var/unbound/etc and sets the ownership of the files to the unbound user.
# Finally, the script starts the Unbound service and loads the DNS cache.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the necessary commands (`unbound`, `unbound-anchor`, `unbound-control-setup`, `chown`, `daemon`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/unbound` directory for Unbound-related scripts and configuration files.