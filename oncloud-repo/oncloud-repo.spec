Name:		oncloud-repo
Version:	0.3
Release:	1%{?dist}
Summary:	Matt-OnCloud repository for running Fedora on a Macbook Air
Group:		System Environment/Base
License:	GPLv2
URL:		http://github.com/matthicksj/mba-fixes
Source0:	%{name}-%{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package provides the yum repository configuration for the Matt-OnCloud repository.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d/
install -m 644 oncloud.repo %{buildroot}%{_sysconfdir}/yum.repos.d/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/oncloud.repo

%changelog
* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.3-1
- new package built with tito

