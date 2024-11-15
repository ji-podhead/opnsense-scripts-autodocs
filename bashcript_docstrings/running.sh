#!/bin/sh
# script running.sh
# ------------------------
#
# Checks if the OPNsense system is currently locked for updates.
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
#- "ready" if the system is not locked
#- "busy" if the system is locked
#
# Description:
# This script checks if the OPNsense system is currently locked for updates.
# It uses the `flock` command to check if the lock file is available.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the necessary commands (`flock`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
#  - The script uses the `${LOCKFILE}` file to store the lock information.