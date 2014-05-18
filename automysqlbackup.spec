%define name automysqlbackup
%define version 3.0.RC6
%define release 3
%define rpmver   3.0.RC6


Summary:            automysqlbackup is a script to backup your msql database on sme8
Name:               %{name}
Version:            %{version}
Release:            %{release}%{?dist}
License:            GPL
Group:              /Web/Application
Source:             %{name}-%{version}.tar.gz
URL:                http://sourceforge.net/projects/automysqlbackup/
BuildRoot:          /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires:           e-smith-base, e-smith-release >= 9
BuildRequires:      e-smith-devtools

%description
This RPM is an unofficial addon for the SME Server 9.x.  
The target audience is the Linux/E-smith administrator 
who wants to backup their mysql databases with an automatic way.
This script is based on automysqlbackup V3.0



%changelog
* Sun May 18 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> 3.0.RC6.3
- first release for sme9

* Sun Oct 27 2013 Stephane de Labrusse <stephdl@de-labrusse.fr> 3.0.RC6.3
- split the contrib in two versions smeserver-automysqlbackup and automysqlbackup

* Mon Apr 22 2013 Stephane de Labrusse <stephdl@de-labrusse.fr>
- [3.0.RC6] version Based on automysqlbackup V3.0 RC6
* Mon Apr 08 2013 Stephane de Labrusse <stephdl@de-labrusse.fr>
- [0.01] Initial version Based on automysqlbackup V3.0 RC6

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ;/usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
/bin/rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist


%files -f %{name}-%{version}-filelist

%defattr(-,root,root)

%clean 
rm -rf $RPM_BUILD_ROOT

%pre

%post

			     
%preun
%postun

