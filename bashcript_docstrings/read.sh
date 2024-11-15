#!/bin/sh
# script read.sh
# ------------------------
#
# Retrieves the lock file for a package.
#
# *Params*
#
#  1. None
#
# *Arguments*
#
#- None
#
# *Returns*
#
#- str
#    The lock file content.
#
# Description:
# This script retrieves the lock file for a package.
# It checks if the lock file exists and prints its content.
# The lock file is assumed to be located at the `${LOCKFILE}` directory.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the necessary commands (`cat`, `sed`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
