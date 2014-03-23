# Note, you can get the current kernel version using 'uname -r'

%define kversion 3.13.6-200.fc20.x86_64
%define module_dir /lib/modules/%kversion/extra

Name:		mba6x_bl-kmod
Version:	0.9
Release:	1%{?dist}
Summary:	MacBook Air 6x backlight kernel module
Group:		System Environment/Base
License:	GPLv2
URL:		http://github.com/matthicksj/mba-fixes
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This provides a new kernel module for the Macbook Air 6x models that controls the backlight.
This also provides a new xorg configuration to change the Intel video configuration to use
this module.

%prep
%setup -q -n %{name}-%{version}
unzip mba6x_bl.zip
patch -p1 < make.patch

%build
install -m 755 -d %{buildroot}/%{module_dir}/build

cd mba6x_bl-master

# Create environment files for Makefile
export MODLIB=%{buildroot}/%{module_dir}
export KVERSION=%{kversion}
export KDIR=%{buildroot}/%{module_dir}/build
export PWD=$(shell pwd)

make

%install
pushd mba6x_bl-master

rm -rf %{buildroot}
install -m 755 -d %{buildroot}/%{module_dir}

# Install the module
export MODLIB=%{buildroot}/%{module_dir}
make install

popd

# Add the xorg configuration
install -m 755 -d %{buildroot}/%{_sysconfdir}/X11/xorg.conf.d
install -m 644 01-mba-backlight.conf %{buildroot}/%{_sysconfdir}/X11/xorg.conf.d

%post
depmod -a
modprobe mba6x_bl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{module_dir}/mba6x_bl.ko
%config %{_sysconfdir}/X11/xorg.conf.d/01-mba-backlight.conf

%changelog
* Mon Mar 10 2014 Matt Hicks <mhicks@redhat.com> 0.9-1
- Updating kernel (mhicks@redhat.com)

* Fri Mar 07 2014 Matt Hicks <mhicks@redhat.com> 0.8-1
- Updating kernel (mhicks@redhat.com)

* Sat Mar 01 2014 Matt Hicks <mhicks@redhat.com> 0.7-1
- Updating kernel version (mhicks@redhat.com)

* Wed Feb 19 2014 Matt Hicks <mhicks@redhat.com> 0.6-1
- Updating kernel version (mhicks@redhat.com)
- Fixing module loading and location (mhicks@redhat.com)

* Tue Feb 18 2014 Matt Hicks <mhicks@redhat.com> 0.5-1
- Updating doc (mhicks@redhat.com)
- Updating kernel version (mhicks@redhat.com)

* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.4-1
- Fixing source locations (mhicks@redhat.com)

* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.3-1
- new package built with tito

