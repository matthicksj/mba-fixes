# (un)define the next line to either build for the newest or all current kernels
%define buildforkernels newest
#define buildforkernels current
#define buildforkernels akmod

# name should have a -kmod suffix
Name: mba6x_bl-kmod

Version:        0.4
Release:        1%{?dist}.1
Summary:        Kernel module(s)

Group:          System Environment/Kernel

License:	GPLv2        
URL:		https://github.com/patjak/mba6x_bl
Source0:	%{name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{_bindir}/kmodtool
Provides:   	%{name}-kmod-common = %{version}


# needed for plague to make sure it builds for i586 and i686
ExclusiveArch:  i686 x86_64

# get the proper build-sysbuild package from the repo, which
# tracks in all the kernel-devel packages
BuildRequires:  %{_bindir}/kmodtool

%{!?kernels:BuildRequires: buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }


%description
This is a replacement backlight kernel module implementation for the Macbook Air Model 6,2

%package common
Summary: The common dependencies

%description common
These are the common dependencies needed by the kmod kernel modules

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -n %{name}-%{version}
unzip mba6x_bl.zip

for kernel_version in %{?kernel_versions} ; do
   cp -a mba6x_bl-master _kmod_build_${kernel_version%%___*}
done


%build
for kernel_version in %{?kernel_versions}; do
    make %{?_smp_mflags} -C "${kernel_version##*___}" SUBDIRS=${PWD}/_kmod_build_${kernel_version%%___*} modules
done


%install
rm -rf ${RPM_BUILD_ROOT}

for kernel_version in %{?kernel_versions}; do
    install -D -m 755 _kmod_build_${kernel_version%%___*}/mba6x_bl.ko ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/mba6x_bl.ko
done
%{?akmod_install}

# Copy the xorg file
install    -m 0755 -d         ${RPM_BUILD_ROOT}%{_sysconfdir}/X11/xorg.conf.d/
install -p -m 0644 01-mba-backlight.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/X11/xorg.conf.d/


%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/01-mba-backlight.conf

%changelog
* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.4-1.1
- Updating (mhicks@redhat.com)

* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.3-1.1
- Adding mba6x_bl sources (mhicks@redhat.com)

* Wed Feb 05 2014 Matt Hicks <mhicks@redhat.com> 0.2-1.1
- New package built with tito

* Tue Feb 4 2014 Matt Hicks <matthicksj@gmail.com>
- Initial Build
