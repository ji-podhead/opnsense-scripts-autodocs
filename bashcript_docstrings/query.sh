#!/bin/sh
# script query.sh
# -------------------------
#
# Retrieves version information for OPNsense.
#
# *Params*
#
#  1. MODE: str
#    The mode to retrieve version information (local, remote, tiers).
#
# *Arguments*
#
#- None
#
# *Returns*
#
#- str
#    The version information in a formatted string.
#
# Description:
# This script retrieves version information for OPNsense.
# It uses the `opnsense-version` command to retrieve version information for the base and kernel sets.
# It also uses the `pkg` command to retrieve package information.
# The script supports three modes:
#  - local: Retrieves version information for the local OPNsense installation.
#  - remote: Retrieves version information from a remote repository.
#  - tiers: Retrieves product tier annotations from a remote repository.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the necessary commands (`opnsense-version`, `pkg`) are available.
#  - The script uses the `/usr/local/opnsense/scripts/firmware/config.sh` file to configure the OPNsense environment.