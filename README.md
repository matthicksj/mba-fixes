mba-fixes
=========

Fixes for running Fedora on a Macbook Air 6,2.  These are basically helper RPM's for setting up my Fedora installation as described here - http://mattoncloud.org/2014/02/05/fedora-20-on-a-macbook-air/.

These packages are build using tito (https://github.com/dgoodwin/tito).
You must install that first and need a valid RPM build environment as
well.

To build, go into one of the src directories (e.g. mba-fixes) and run:
    tito build

I host the results as a yum repository on OpenShift and you can see the
build.sh script as to how I automate that.

Enjoy! 
