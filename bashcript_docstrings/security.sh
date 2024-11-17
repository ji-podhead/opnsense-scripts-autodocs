#!/bin/sh

# script security.sh
# ------------------------
#
# Performs a security audit on the OPNsense system.
#
# It uses the `pkg` command to run the audit and logs its actions to the `${LOCKFILE}` file.
#
# *Notes*
#  - This script assumes that the necessary commands (`pkg`, `opnsense-version`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
#  - The script clears the `${LOCKFILE}` file before starting the audit.