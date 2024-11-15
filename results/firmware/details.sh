#!/bin/sh

# script details.sh
# ---------------
#
# Queries package information.
#
# *Params*
#
#- PACKAGE: str
#    index: 1
#    The package to query.
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
# This script queries information about a package.
# It takes a package name as an argument and uses the `pkg rquery` command to retrieve information about the package.
# The script outputs the package name, version, and maintainer.