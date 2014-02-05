mba-fixes
=========

Fixes for running Fedora on a Macbook Air 6,2

To build these, first follow the setup instructions for building a Fedora package (http://bit.ly/1eoG8jl).  Once you have your rpmbuild environment setup, just copy over the SPEC and SOURCES content and then you can build the RPM's from the SPEC files.

For example, you should be able to run the following:

cd ~/rpmbuild
rpmbuild -ba SPEC/mba-fixes.spec

I would also recommend looking at Mock to help isolate your environment from your builds (http://bit.ly/1g0lNhj).

Enjoy! 
