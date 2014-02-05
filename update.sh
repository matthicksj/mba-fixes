#!/bin/sh

pushd `dirname $0` > /dev/null
echo "Downloading latest sources from patjak/mba6x_bl on GitHub"
wget -O mba6x_bl/mba6x_bl.zip https://github.com/patjak/mba6x_bl/archive/master.zip
git commit -a -m 'Updating mba6x_bl sources'
cd mba6x_bl
tito tag
git push
git push --tags
popd > /dev/null