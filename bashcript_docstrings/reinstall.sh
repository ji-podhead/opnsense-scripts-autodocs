#!/bin/sh

# script reinstall.sh
# ---------------------------
#
# Reinstalls a package on the OPNsense system.
#
# It checks if the package is the base or kernel package and performs the necessary actions.
# If the package is a plugin, it reverts the plugin to its original state and reinstalls it.
# The script uses the `opnsense-update` command to update the package and the `opnsense-revert` command to revert the plugin.
# If a reboot is necessary, the script initiates a reboot after a short delay.
#
# *Params*
#  - ${1} : str
#     - PACKAGE: The name of the package to reinstall (base, kernel, or a plugin name).
#
# *Notes*
#  - This script assumes that the necessary commands (`opnsense-update`, `opnsense-revert`, `pkg`, `rc.reboot`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.