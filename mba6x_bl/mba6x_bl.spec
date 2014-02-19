# Note, you can get the current kernel version using 'uname -r'

%define kversion 3.13.3-201.fc20.x86_64
%define module_dir /lib/modules/%kversion/extra

Name:		mba6x_bl-kmod
Version:	0.5
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

%build
cd mba6x_bl-master
make

%install
rm -rf %{buildroot}
pushd mba6x_bl-master
install -m 755 -d %{buildroot}/%{module_dir}
install -m 644 mba6x_bl.ko %{buildroot}/%{module_dir}
popd

# Add the xorg configuration
install -m 755 -d %{buildroot}/%{_sysconfdir}/X11/xorg.conf.d
install -m 644 01-mba-backlight.conf %{buildroot}/%{_sysconfdir}/X11/xorg.conf.d

%post
depmod -a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{module_dir}/mba6x_bl.ko
%config %{_sysconfdir}/X11/xorg.conf.d/01-mba-backlight.conf

%changelog
* Tue Feb 18 2014 Matt Hicks <mhicks@redhat.com> 0.5-1
- Updating doc (mhicks@redhat.com)
- Updating kernel version (mhicks@redhat.com)

* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.4-1
- Fixing source locations (mhicks@redhat.com)

* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.3-1
- new package built with tito

