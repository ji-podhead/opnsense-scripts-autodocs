#!/bin/sh
# script ppp-rename.sh
# ------------------------
#
# Handles the link up event for a PPP interface.
#
# *Params*
#
#  1. INTERFACE: str
#    The name of the PPP interface.
#  2. NG_DEVICE: str
#    The name of the ng device.
#  3. NG_TYPE: str
#    The type of the ng device.
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
# This script handles the link up event for a PPP interface.
# It sets the interface name, ng device name, and ng device type.
# It then iterates over the ngctl list and checks if the ng device is found.
# If the ng device is found, it sets the ng device name.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the necessary commands (`ngctl`) are available.
#  - The script uses the `ngctl list` command to list the ng devices.
#  - The script uses the `ngctl info` command to get the ng device information.
#  - The script uses the `ngctl name` command to set the ng device name.