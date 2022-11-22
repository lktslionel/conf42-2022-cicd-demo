#!/bin/bash 


echo -e "Preparing ..."

: "${PACKAGE_REGISTRY_TOKEN:Env var[PACKAGE_REGISTRY_TOKEN] is required.}"

echo '//npm.pkg.github.com/:_authToken=${PACKAGE_REGISTRY_TOKEN}' >> ~/.npmrc

echo "Config Git and NPM"

git config user.name github-actions
git config user.email github-actions@github.com

npm config set user github-actions
npm config set email github-actions@github.com

echo -e "Done.\n"