#!/bin/sh
# script update.sh
# -------------------------
#
# Updates the OPNsense system to the latest version.
#
# It uses the `opnsense-update` command to perform the update and the `rc.restart_webgui` command to restart the web server.
# The script also uses the `tee` command to log the output to the `${LOCKFILE}` file.
# If the update is successful, the script initiates a reboot after a short delay if necessary.
#
# *Params*
#  - {1} : str
#      - CMD: The command to execute (e.g. "sync").
#
# *Notes*
#  - This script assumes that the necessary commands (`opnsense-update`, `rc.restart_webgui`, `tee`, `rc.reboot`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.