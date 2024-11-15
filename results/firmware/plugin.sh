#!/bin/sh
# script plugin.sh
# ------------------------
#
# Checks if a plugin is installed.
#
# *Params*
#
#  1. PLUGIN: str
#    The name of the plugin to check.
#
# *Arguments*
#
#- None
#
# *Returns*
#
#- int
#    0 if the plugin is not installed, 1 if it is installed.
#
# Description:
# This script checks if a plugin is installed.
# It uses the `opnsense-version` command to check if the plugin is installed, either in stable or development version.
# The script returns 0 if the plugin is not installed, and 1 if it is installed.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the `opnsense-version` command is available.