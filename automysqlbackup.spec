%define name automysqlbackup
%define version 3.0.RC6
%define release 12
%define rpmver   3.0.RC6


Summary:            automysqlbackup is a script to backup your msql database on sme8
Name:               %{name}
Version:            %{version}
Release:            %{release}%{?dist}
License:            GPL
Group:              /Web/Application
Source:             %{name}-%{version}.tar.gz
URL:                http://sourceforge.net/projects/automysqlbackup/
# BuildRoot:          /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires:           nethserver-mysql
BuildRequires:      nethserver-devtools

%description
This RPM is an unofficial addon for the NethServer
The target audience is the  administrator 
who wants to backup their mysql databases with an automatic way.
This script is based on automysqlbackup V3.0

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ;/usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
/bin/rm -f %{name}-%{version}-filelist
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-filelist


%files -f %{name}-%{version}-filelist

%defattr(-,root,root)

%clean 
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%changelog
* Sun NOv 29 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 3.0.RC6-12.ns7
- Dynamic path to the mysqldump binary (default is /usr/bin/mysqldump)
- add in the config CONFIG_mysql_dump_binary='/usr/bin/mysqldump103'

* Sat Nov 05 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> 3.0.RC6-6.ns7
- new rebuild for NS7

* Thu May 21 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> 3.0.RC6-5
- first version to Neth, added good require & build require

* Sun Aug 17 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> 3.0.RC6-4
- added my own patch against the --events warning
--Warning: Skipping the data of table mysql.event. Specify the --events option explicitly.

* Sun May 18 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> 3.0.RC6.3
- first release for sme9

* Sun Oct 27 2013 Stephane de Labrusse <stephdl@de-labrusse.fr> 3.0.RC6.3
- split the contrib in two versions smeserver-automysqlbackup and automysqlbackup

* Mon Apr 22 2013 Stephane de Labrusse <stephdl@de-labrusse.fr>
- [3.0.RC6] version Based on automysqlbackup V3.0 RC6
* Mon Apr 08 2013 Stephane de Labrusse <stephdl@de-labrusse.fr>
- [0.01] Initial version Based on automysqlbackup V3.0 RC6
