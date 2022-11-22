#!/bin/bash 

set -eu 


echo -e "Publish ..."

npm publish

git push
git push --tags

echo -e "Done.\n"