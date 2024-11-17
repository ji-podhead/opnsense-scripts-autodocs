#!/bin/sh
# script suricata_setup.sh
# ------------------------
#
# Sets up the Suricata directories and configuration files.
#
# It creates the necessary directories, sets the ownership and permissions, and creates a placeholder file if necessary.
#
# *Notes*
#  - This script assumes that the necessary commands (`mkdir`, `chown`, `chmod`, `touch`) are available.
#  - The script uses the `/var/log/suricata` directory for Suricata logs.
#  - The script creates the `/usr/local/etc/suricata/installed_rules.yaml` file if it does not exist.