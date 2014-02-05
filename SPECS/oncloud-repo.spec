Name:		oncloud-repo
Version:	0.1
Release:	1%{?dist}
Summary:	Matt-OnCloud repository for running Fedora on a Macbook Air
Group:		System Environment/Base
License:	GPLv2
URL:		http://github.com/matthicksj/mba-fixes
Source0:	oncloud.repo
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package provides the yum repository configuration for the Matt-OnCloud repository.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d/
cp %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/oncloud.repo

%changelog
* Tue Feb 04 2014 Matt Hicks <matthicksj@gmail.com> - 0.1-1
- Initial build
