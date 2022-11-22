#!/bin/bash 

set -eu 


echo -e "Publish ..."

npm publish

git push ${GIT_BRANCH}
git push --tags

echo -e "Done.\n"