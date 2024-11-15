#!/bin/sh

# script hostnames.sh
# ---------------
#
# Retrieves the hosts of the repositories configured on the system.
#
# *Params*
#
#- None
#
# *Arguments*
#
#- None
#
# *Returns*
#
#- A list of unique hosts of the repositories.
#
# Description:
# This script retrieves the hosts of the repositories configured on the system.
# It uses the `opnsense-verify` command to get the list of repositories,
# and then parses the repository configuration files to extract the URLs.
# It filters out non-HTTPS URLs and extracts the host from the remaining URLs.
# The unique hosts are then printed to the console.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the repository configuration files are in the
#    `/etc/pkg` and `/usr/local/etc/pkg/repos` directories.
#  - This script only considers HTTPS URLs.