#!/bin/sh
# script resync.sh
# ------------------------
#
# Resynchronizes the OPNsense system with the latest configuration.
#
# It uses the `register.php` script to perform the resynchronization and logs its actions to the `${LOCKFILE}` file.
#
# *Notes*
#  - This script assumes that the necessary commands (`opnsense-version`, `register.php`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.
#  - The script clears the `${LOCKFILE}` file before starting the resynchronization.