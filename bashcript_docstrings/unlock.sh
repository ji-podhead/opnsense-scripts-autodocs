#!/bin/sh
# script unlock.sh
# ------------------------
#
# Unlocks a package or set on the OPNsense system.
#
# *Params*
#
#  1. PACKAGE: str
#    The name of the package or set to unlock.
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
# This script unlocks a package or set on the OPNsense system.
# It uses the `opnsense-update` command to unlock the base or kernel sets, and the `pkg` command to unlock other packages.
# The script logs its actions to the `${LOCKFILE}` file.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the necessary commands (`opnsense-update`, `pkg`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.