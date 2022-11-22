#!/bin/bash 

set -eu 


echo -e "Publish ..."

npm publish

git push origin main
git push origin --tags

echo -e "Done.\n"