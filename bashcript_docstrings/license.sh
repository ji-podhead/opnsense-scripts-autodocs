#!/bin/sh
# script license.sh
# ------------------------
#
# Displays the license information for a package.
#
# It uses the `pkg` command to query the package database and retrieve the license information.
# The script then displays the license text for each license found.
#
# *Params*
#   - ${1} : str
#       - The name of the package to display the license information for.
#
# *Notes*
#  - This script assumes that the license files are stored in the `${LICENSEDIR}` directory.
#  - The script uses the `${PKG}` command to query the package database.