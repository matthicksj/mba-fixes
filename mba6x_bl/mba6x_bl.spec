# Note the kversion must be passed in at the rpmbuild time as an argument
# For example:
#     rpmbuild -ba --define "kversion `uname -r`"
# or if using tito:
#     tito build --rpmbuild-options="--define 'kversion `uname -r`'"

%define module_dir /lib/modules/%kversion/extra/mba6x_bl

Name:		mba6x_bl-kmod
Version:	0.6
Release:	1%{?dist}
Summary:	MacBook Air 6x backlight kernel module
Group:		System Environment/Base
License:	GPLv2
URL:		http://github.com/matthicksj/mba-fixes
Source0:	%{name}-%{version}
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
cd mba6x_bl-master
install -m 755 -d %{buildroot}/%{module_dir}
install -m 644 mba6x_bl.ko %{buildroot}/%{module_dir}

# Add the xorg configuration
install -m 755 -d %{buildroot}/%{_sysconfdir}/X11/xorg.conf.d
install -m 644 01-mba-backlight.conf %{buildroot}/%{_sysconfdir}/X11/xorg.conf.d

%post
modprobe mba6x_bl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{module_dir}/mba6x_bl.ko
%config %{_sysconfdir}/X11/xorg.conf.d/01-mba-backlight.conf

%changelog
* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.6-1
- More manual build approach by just passing in the kernel version
  (mhicks@redhat.com)

* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.5-1
- Updating spec to a simpler format (mhicks@redhat.com)
- Updating (mhicks@redhat.com)

* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.2-1
- New package built with tito

* Tue Feb 04 2014 Matt Hicks <matthicksj@gmail.com> - 0.1-1
- Initial build
