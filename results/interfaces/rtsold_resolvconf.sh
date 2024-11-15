#!/bin/sh
# script rtsold_resolvconf.sh
# ----------------
#
# Processes Router Advertisements (RA) with RDNSS and DNSSL options.
#
# *Params*
#
#  1. Action: str
#    "-a" to add DNS information
#    "-d" to delete DNS information
#  2. Interface information: str
#    "ifname:slaac:[RA source address]"
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
# This script is invoked by rtsold when a Router Advertisement with RDNSS
# and DNSSL options is received. It extracts the interface, router, and DNS
# information from the arguments and STDIN.
#
# Functions:
#  - None
#
# Notes:
#  - This script uses the ifctl(8) and configctl(8) commands to modify
#    the interface configuration.
#  - It uses the /var/etc/radvd.conf file to recognize its own configuration.