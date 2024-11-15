#!/bin/sh
# script sync.sh
# ------------------------
#
# Synchronizes the OPNsense system with the latest configuration.
#
# *Params*
#
#  None
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
# This script synchronizes the OPNsense system with the latest configuration.
# It uses the `sync.subr.sh` script to perform the synchronization and logs its actions to the `${LOCKFILE}` file.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the necessary commands (`opnsense-version`, `sync.subr.sh`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.