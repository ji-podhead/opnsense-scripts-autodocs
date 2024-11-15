#!/usr/local/bin/php
<?php
/**
 * password.php
 * ----------
 *
 * A script to reset the root user account.
 *
 * *Arguments*
 * 
 * - None
 * 
 * *Parameters*
 * 
 * - $argv[2] and $argv[3]: Options for the script
 *     - -h 0: Mocking "pw usermod root -h 0"
 *     - -x 0: Creates a new root user if none exists
 * 
 * *Functions*
 * 
 * - getUserEntryByUID(int $uid): Returns the user entry for the given UID
 * - local_user_set_password(array $user, string $password): Sets the password for the given user
 * - local_user_set(array $user): Saves the user entry
 * - write_config(string $message): Writes a message to the configuration
 * 
 * *Flow*
 * 
 * 1. Checks if the options -h 0 or -x 0 were provided
 * 2. If -h 0, sets the password for the root user
 * 3. If -x 0, creates a new root user if none exists and sets the password
 * 4. If no options were provided, asks if the user wants to restore the default authentication mode
 * 5. If the user wants to restore the default authentication mode, sets the password for the root user
 * 
 * *Outputs*
 * 
 * - Messages for resetting the root user account
 * - Error messages if the password is empty or does not match
 */