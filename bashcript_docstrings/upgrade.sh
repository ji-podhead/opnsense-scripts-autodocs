#!/bin/sh

# script upgrade.sh
# -------------------------
#
# Upgrades the OPNsense system to the latest version.
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
#- None
#
# Description:
# This script upgrades the OPNsense system to the latest version.
# It uses the `opnsense-update` command to perform the upgrade and the `rc.syshook` command to execute system hooks.
# The script also uses the `tee` command to log the output to the `${LOCKFILE}` file.
# If the upgrade is successful, the script initiates a reboot after a short delay.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the necessary commands (`opnsense-update`, `rc.syshook`, `tee`, `rc.reboot`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.