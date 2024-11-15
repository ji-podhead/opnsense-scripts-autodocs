#!/bin/sh
# script update.sh
# -------------------------
#
# Updates the OPNsense system to the latest version.
#
# *Params*
#
#  1. CMD: str
#    The command to execute (e.g. "sync").
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
# This script updates the OPNsense system to the latest version.
# It uses the `opnsense-update` command to perform the update and the `rc.restart_webgui` command to restart the web server.
# The script also uses the `tee` command to log the output to the `${LOCKFILE}` file.
# If the update is successful, the script initiates a reboot after a short delay if necessary.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the necessary commands (`opnsense-update`, `rc.restart_webgui`, `tee`, `rc.reboot`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.