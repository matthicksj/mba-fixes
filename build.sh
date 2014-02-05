#!/bin/sh

pushd `dirname $0` > /dev/null
echo "Building RPMs with tito"
rm -rf /tmp/mba-repo
mkdir -p /tmp/mba-repo

cd mba-fixes
tito build --output=/tmp/mba-repo

cd ../mba6x_bl
tito build --output=/tmp/mba-repo

cd ../oncloud-repo
tito build --output=/tmp/mba-repo

popd > /dev/null
