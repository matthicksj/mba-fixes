#!/bin/sh

pushd `dirname $0` > /dev/null

echo "Building RPMs with tito"
rm -rf /tmp/mba-repo
mkdir -p /tmp/mba-repo

cd mba-fixes
tito build --rpm --output=/tmp/mba-repo

cd ../mba6x_bl
tito build --rpm --output=/tmp/mba-repo

cd ../oncloud-repo
tito build --rpm --output=/tmp/mba-repo

cd /tmp/mba-repo
mkdir SRPMS
mv *.src.rpm SRPMS
mkdir RPMS
mv x86_64 RPMS
rm *.tar.gz
createrepo .

# Now merge with the OpenShift application
rm -rf /tmp/working
mkdir /tmp/working
cd /tmp/working

# Make sure the files application is setup for binary deployment
rhc configure-app --deployment-type binary -a files

# Now download and update the OpenShift application
rhc save-snapshot files --deployment
tar -zxf files.tar.gz
rm files.tar.gz

# Now merge the yum repository with the content
mkdir repo/php/yum
cp -r /tmp/mba-repo/* repo/php/yum

tar -cvf /tmp/mba-repo/files.tar *
gzip /tmp/mba-repo/files.tar

rhc deploy /tmp/mba-repo/files.tar.gz -a files

popd > /dev/null
