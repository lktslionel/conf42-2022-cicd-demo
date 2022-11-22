#!/bin/bash 

set -eu 


echo -e "Testing ..."

sleep $((1 + $RANDOM % 3))

echo -e "Done.\n"