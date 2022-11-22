#!/bin/bash 

set -eu 


echo -e "Building package[$PACKAGE_NAME]..."

sleep $((1 + $RANDOM % 3))

echo -e "Done.\n"