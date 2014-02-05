Name:		mba6x_bl-kmod
Version:	0.5
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
unzip mba6x_bl-master

%build
cd mba6x_bl-master
make

%install
rm -rf %{buildroot}
cd mba6x_bl-master
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/modules/`uname -r`/extra/mba6x_bl/mba6x_bl.ko

%changelog
* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.5-1
- Updating spec to a simpler format (mhicks@redhat.com)
- Updating (mhicks@redhat.com)

* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.2-1
- New package built with tito

* Tue Feb 04 2014 Matt Hicks <matthicksj@gmail.com> - 0.1-1
- Initial build
