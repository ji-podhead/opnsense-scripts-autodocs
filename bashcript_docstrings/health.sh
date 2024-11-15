#!/bin/sh
# script health.sh
# ---------------
#
# Performs a health audit on the system.
#
# *Params*
#
#- None
#
# *Arguments*
#
#- CMD: str
#    Optional command to specify which audit to perform.
#    Possible values: kernel, base, repos, plugins, locked, packages, core
#
# *Returns*
#
#- None
#
# Description:
# This script performs a health audit on the system.
# It checks the root file system, kernel, base system, repositories, plugins,
# locked packages, and package dependencies.
# It also checks for missing or altered package files.
# The audit results are logged to a file.
#
# Functions:
#  - set_check: Checks the version and consistency of a package.
#  - core_check: Checks the consistency of the core packages.