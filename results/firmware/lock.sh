#!/bin/sh

# script lock.sh
# ------------------------
#
# Locks a package to prevent updates.
#
# *Params*
#
#  1. PACKAGE: str
#    The name of the package to lock.
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
# This script locks a package to prevent updates.
# It uses the `opnsense-update` command to lock the base or kernel set, or the `pkg` command to lock a specific package.
# The script logs its actions to a lock file.
#
# Functions:
#  - None
#
# Notes:
#  - This script assumes that the lock file is stored in the `${LOCKFILE}` directory.
#  - The script uses the `opnsense-version` command to retrieve the current version of the system.