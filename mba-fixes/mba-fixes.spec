Name:		mba-fixes	
Version:	0.4
Release:	1%{?dist}
Summary:	Various configuration fixes for running Fedora on a Macbook Air 6,2
Group:		System Environment/Base
License:	GPLv2
URL:		http://github.com/matthicksj/mba-fixes
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package provides various configuration fixes for things like the keyboard mapping
and SSD hangs when running Fedora on a Macbook Air 6,2 model.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d
cp wakeup_fix.service %{buildroot}%{_sysconfdir}/systemd/system
cp mapping_fix.service %{buildroot}%{_sysconfdir}/systemd/system
cp 59-ssd_depth_fix.rules %{buildroot}%{_sysconfdir}/udev/rules.d

%post
systemctl daemon-reload
systemctl enable wakeup_fix
systemctl start wakeup_fix
systemctl enable mapping_fix
systemctl start mapping_fix

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_sysconfdir}/systemd/system/wakeup_fix.service
%{_sysconfdir}/systemd/system/mapping_fix.service
%{_sysconfdir}/udev/rules.d/59-ssd_depth_fix.rules

%changelog
* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.4-1
- Switching to udev rule instead of systemd script (mhicks@redhat.com)

* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.3-1
- new package built with tito

