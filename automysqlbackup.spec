%define name automysqlbackup
%define version 3.0
%define release 4


Summary: provide a dhcp panel in the server-manager for The SME Server
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source: %{name}-%{version}.tar.gz
#Patch0:  smeserver-dhcpmanager-1.5-checkip-scanIP-and-new-panelIP.patch
#Patch1: smeserver-dhcpmanager-1.5-wording-scan_network-remove_all_leases-other_changes.patch
#Patch2: smeserver-dhcpmanager-1.5-add_default_values-change_nmap_options.patch
License: GNU GPL version 2
URL: http://www.contribs.org
Group: SMEserver/addon
BuildRoot: %{_tmppath}/%{name}-buildroot
#Prefix: %{_prefix}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 8.0
AutoReqProv: no

%description
Implementation of some feature arround dhcp clients like : wol, cleaning dhcpd.leases, Scan of your network etc//

%changelog
* Wed Feb 05 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> smeserver-dhcpmanager-1.5-11
- add default db values and change options to nmap in order to see name of computer
 
* Mon Jan 13 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> smeserver-dhcpmanager-1.5-10
- english wording correction [sme:8122]
- change the nmap version to 6.25 (available in smecontribs) [sme:8120]
- add an option to remove all leases
- some subroutines added in the goal to save settings and stay on the same page (main page and connected IP)
- some menu setting box redesigned.

* Sun Jan 05 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> smeserver-dhcpmanager-1.5-5
- Add a checkIP routine against wrong IP [sme:8015]
- Add a new panel to see connected IP [sme:8113]
- Add a counter of host up on the LAN (using nmap) [sme:8111]

* Sun Dec 29 2013 Stephane de Labrusse <stephdl@de-labrusse.fr> smeserver-dhcpmanager-1.5-3
- adaptation for SME Server 8.0
* Thu Dec 23 2004 Thierry Quaak <thierry@quaak.net>
- Last release of e-smith-dhcpmanager-1.5-1, thanks a lot for his work



%prep
%setup
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
%build
#perl createlinks


%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist

%pre
%preun

%post
#/etc/e-smith/events/actions/navigation-conf




%postun
#rm /etc/e-smith/templates-custom/etc/dhcpd.conf/25NetbiosNameServers

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)


