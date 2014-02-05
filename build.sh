#!/bin/sh

pushd `dirname $0` > /dev/null
echo "Downloading latest sources from patjak/mba6x_bl on GitHub"
wget -O mba6x_bl/mba6x_bl.zip https://github.com/patjak/mba6x_bl/archive/master.zip

echo "Building RPMs with tito"
tito build --rpm
popd > /dev/null