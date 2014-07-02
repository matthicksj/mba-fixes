mba-fixes
=========

## Intro
Fixes for running Fedora on a Macbook Air 6,2.  These are basically helper RPM's for setting up my Fedora installation as described here - http://mattoncloud.org/2014/02/05/fedora-20-on-a-macbook-air/.

## Requirements

- **Tito** You can get tito from https://github.com/dgoodwin/tito and install it using the instructions supplied.
- **RPM build environment** You can install this on Fedora using:

        # yum install @development-tools
        # yum install fedora-packager


    To build mba6x_bl you will also need:
        
         # yum install kernel-devel

## Build
To build, go into one of the src directories (e.g. mba-fixes) and run:

        # tito build --rpm --output=<directory>

I host the results as a yum repository on OpenShift and you can see the
build.sh script as to how I automate that.

build.sh
-----------

For any updates, you need to commit the work, push it and 'tito tag' it
before running the overall build.  For example, you would do:

    git commit -a -m "My changes"
    tito tag
    git push
    git push --tags

Then you should be safe to run 'build.sh' to upload the results to
OpenShift.

Enjoy! 
