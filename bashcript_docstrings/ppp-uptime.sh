#!/bin/sh

# script ppp-uptime.sh
# ------------------------
#
# Calculates the uptime of a PPP connection.
#
# *Params*
#
#  1. IF: str
#    The name of the PPP interface.
#
# *Arguments*
#
#- None
#
# *Returns*
#
#- int
#    The uptime of the PPP connection in seconds.
#
# Description:
# This script calculates the uptime of a PPP connection.
# It checks if the `/tmp/${IF}_uptime` file exists.
# If the file exists, it calculates the uptime by subtracting the modification time of the file from the current time.
# The uptime is returned in seconds.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the necessary commands (`date`, `stat`) are available.
#  - The script uses the `/tmp/${IF}_uptime` file to store the uptime of the PPP connection.