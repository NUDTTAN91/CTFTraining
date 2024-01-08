#!/bin/sh

echo $FLAG > /flag
export FLAG=not_flag
FLAG=not_flag

service --status-all | awk '{print $4}'| xargs  -i service {} start

sleep infinity;
