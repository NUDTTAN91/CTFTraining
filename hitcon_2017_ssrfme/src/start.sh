#!/usr/bin/env bash

echo $FLAG > /flag
chmod u+s /readflag
chown root:root -R /var/www/html/
chmod 400 /flag

export FLAG=not_flag
FLAG=not_flag

apache2-foreground
