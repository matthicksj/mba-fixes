Name:		mba-fixes	
Version:	0.2
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
cp mapping_fix.service %{buildroot}%{_sysconfdir}/systemd/system
cp ssd_fix.service %{buildroot}%{_sysconfdir}/systemd/system

%post
systemctl daemon-reload
systemctl enable mapping_fix
systemctl enable ssd_fix
systemctl start mapping_fix
systemctl start ssd_fix

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_sysconfdir}/systemd/system/mapping_fix.service
%{_sysconfdir}/systemd/system/ssd_fix.service

%changelog
