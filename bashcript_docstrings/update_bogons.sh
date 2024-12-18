#!/bin/sh
# script update_bogons.sh
# ------------------------
#
# Updates the bogons files for IPv4 and IPv6.
#
# It downloads the latest bogons files from the OPNsense repository, verifies their integrity, and extracts them to a temporary directory.
# The script then updates the bogons tables in the pf firewall configuration.
# If the update is successful, the script logs a success message.
#
# *Params*
#    - ${1} : str
#        - COMMAND: The command to execute (e.g. "cron").
#
# *Notes*
#  - This script assumes that the necessary commands (`opnsense-update`, `fetch`, `tar`, `pfctl`, `logger`) are available.
#  - The script uses the `/usr/local/etc` directory to store the bogons files.