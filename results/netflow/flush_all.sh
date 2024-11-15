#!/bin/sh

# script flush_all.sh
# ---------------
#
# Flushes local netflow data.
#
# *Params*
#
#- None
#
# *Arguments*
#
#- all: str
#    If provided, all local netflow data will be flushed.
#
# *Returns*
#
#- None
#
# Description:
# This script flushes local netflow data.
# If the "all" argument is provided, it stops the flowd and flowd_aggregate services,
# removes all netflow data files and log files, and then starts the services again.
# If the "all" argument is not provided, it prints a message indicating that local netflow data will not be flushed.