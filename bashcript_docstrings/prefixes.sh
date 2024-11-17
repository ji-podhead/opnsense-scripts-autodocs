#!/bin/sh

# script prefixes.sh
# --------------------------------
#
# Watches for changes in the DHCPv6 leases file and updates the configuration.
#
# It uses the `md5` command to calculate the checksum of the leases file.
# If the checksum changes, it updates the DHCPv6 configuration using the `configctl` command.
# The script runs indefinitely and checks for changes at the specified interval.
#
# *Params*
#  - ${1} : int
#     - INTERVAL: The interval in seconds to check for changes (default: 20).
#
# *Notes*
#  - This script assumes that the necessary commands (`md5`, `configctl`) are available.
#  - The script uses the `/var/dhcpd/var/db/dhcpd6.leases` file to store the DHCPv6 leases.