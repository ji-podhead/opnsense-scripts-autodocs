#!/bin/sh
# script restore.sh
# -------------------------
#
# Restores a backup of the OPNsense configuration.
#
# It lists all available backups, allows the user to select one, and then restores it.
# The script also offers the option to reboot the system to apply the backup cleanly.
#
# *Notes*
#  - This script assumes that the necessary commands (`cd`, `find`, `date`, `sort`, `head`, `echo`, `read`, `cp`, `rc.reboot`, `rc.reload_all`) are available.
#  - The script uses the `/conf/backup` directory to store the backups.