#!/bin/sh

# script firmware_runner.sh
# ------------------------
#
# Runs a firmware script.
#
# *Params*
#
#- r: int
#    Optional: Sets a random delay before running the script.
#- s: str
#    Optional: Specifies the script to run.
#- u: bool
#    Optional: Runs the script without a lock file.
#- V: bool
#    Optional: Enables verbose mode.
#
# *Arguments*
#
#- None
#
# *Returns*
#
#- int
#    The return value of the run script.
#
# Description:
# This script runs a firmware script.
# It supports various options, such as specifying a script, setting a random delay, and enabling verbose mode.
# The script uses a lock file to ensure that only one script is run at a time.
#
# Functions:
#  - None
#
# Notes:
#  - This script uses the `flock` function to manage the lock file.
#  - The script uses the `jot` function to generate a random delay.