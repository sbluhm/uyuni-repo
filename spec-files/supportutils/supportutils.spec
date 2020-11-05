#
# spec file for package supportutils
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define support_libdir /usr/lib/supportconfig

Name:           supportutils
Version:        3.1.9
Release:        1.2
Summary:        Support Troubleshooting Tools
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://github.com/g23guy/supportutils
Source:         %{name}-%{version}.tar.gz
Requires:       gawk
%if 0%{?rhel}
Requires:       iproute
Requires:       kmod
Requires:       ncurses
Requires:       util-linux
%else
Requires:       iproute2
Requires:       kmod-compat
Requires:       ncurses-utils
Requires:       util-linux-systemd
%endif
Requires:       net-tools
Requires:       sed
Requires:       sysfsutils
Requires:       tar
Requires:       which
Provides:       supportconfig-plugin-icommand
Provides:       supportconfig-plugin-resource
Provides:       supportconfig-plugin-tag
BuildArch:      noarch

%description
A package containing troubleshooting tools. This package contains
the following: supportconfig, chkbin, getappcore, analyzevmcore

%prep
%setup -q

%build
gzip -9f man/*3
gzip -9f man/*5
gzip -9f man/*8

%install
pwd;ls -la
install -d %{buildroot}/sbin
install -d %{buildroot}/etc
install -d %{buildroot}%{_mandir}/man3
install -d %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{support_libdir}/resources
install -d %{buildroot}%{support_libdir}/plugins
install -d %{buildroot}%{_docdir}/%{name}
install -m 544 bin/supportconfig %{buildroot}/sbin
install -m 544 bin/chkbin %{buildroot}/sbin
install -m 544 bin/getappcore %{buildroot}/sbin
install -m 544 bin/analyzevmcore %{buildroot}/sbin
install -m 444 bin/scplugin.rc %{buildroot}%{support_libdir}/resources
install -m 444 bin/supportconfig.rc %{buildroot}%{support_libdir}/resources
install -m 644 man/*.3.gz %{buildroot}%{_mandir}/man3
install -m 644 man/*.5.gz %{buildroot}%{_mandir}/man5
install -m 644 man/*.8.gz %{buildroot}%{_mandir}/man8
install -m 644 man/COPYING.GPLv2 %{buildroot}%{_docdir}/%{name}

%files
%defattr(-,root,root)
/sbin/supportconfig
/sbin/chkbin
/sbin/getappcore
/sbin/analyzevmcore
%dir %{support_libdir}
%dir %{support_libdir}/resources
%dir %{support_libdir}/plugins
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*

%if 0%{?suse_version} < 1500
%doc %{_docdir}/%{name}/COPYING.GPLv2
%else
%license %{_docdir}/%{name}/COPYING.GPLv2
%endif

%{support_libdir}/resources/*
%doc %{_mandir}/man5/*
%doc %{_mandir}/man3/*
%doc %{_mandir}/man8/*

%changelog
* Fri Mar 13 2020 jason.record@suse.com
- Addition to version 3.1.9
  + Changes affecting getappcore
  - Added core file validation (bsc#1166126)
  - Added -j <PID> to extract core from systemd journal
  - Capture coredumptctl info in getappcore.log
  + Changed filename prefixes from nts_ to scc_ (SLE-8702, SLE-6762)
  - The new prefix references SUSE Customer Center
* Tue Mar  3 2020 jason.record@suse.com
- Addition to version 3.1.8
  + Changes affecting getappcore
  - Added -u for HTTPS and -f for FTPES uploads to SUSE FTP servers
  - Replaced Novell with SUSE FTP servers (bsc#1165475)
  - Uses /etc/getappcore.conf if present
  + Changes affecting supportconfig
  - Added missed Power collection per bsc#1162539
  - Added zypper patterns output to updates.txt #66
* Mon Mar  2 2020 jason.record@suse.com
- Addition to version 3.1.7
  + exclude /proc/pagetypeinfo as it can be an expensive operation on some systems (bsc#1162357)
  + Readded LPM/DLPAR data for Power (bsc#1162539)
* Thu Nov 21 2019 jason.record@suse.com
- Addition to version 3.1.6
  + Strip trailing commas from process names #64 (bsc#1156837)
  + Dynamically select compression method (bsc#1145233)
  + Updated detailed unit information fix in systemd.txt (bsc#1023308)
  + Fixed supportconig.conf man page with order placement
  + Include IPv6 routes (bsc#1089877)
* Fri Oct 18 2019 jason.record@suse.com
- Updated to version 3.1.5
  + Removed root .snapshots directory from full file list (bsc#1154482)
* Wed Oct 16 2019 jason.record@suse.com
- Updated to version 3.1.4
  + Removed LPM/DLPAR data for POWER (bsc#1111029)
  + prevent running 'systool -vb memory' by default on systems with 16TB or more #57 (bsc#1127734)
  + Tumbleweed support #50
  + Added zypper orphaned packages check to updates.txt
  + Cpuset listing #52
  + Docker disunite #53
  + Added sed and gawk to spec requirements (bsc#1137336)
  + Added nstat to network
  + Add collection of livepatch information #63
  + Check for missing ldap.conf file
* Thu May  9 2019 jason.record@suse.com
- Updated to version 3.1.3
  + Uses SUSE FTP servers (bsc#1132865)
  + btrfs quota #43
  + supportconfig: open-files: add file flags #44
  + Merged etc_info: Add support for .cfg files in /etc dir #46
  + Silence warning in rpm backup db collection path #47
  + Set files in tarball to 660 instead of 600 #48
  + SUSE separation finalized (bsc#1125623)
  + Default compression through xz, but -z forces bzip2
  + Updated man pages (bsc#1088234)
  + Changed VAR_OPTION_BIN_TIMEOUT_SEC from 300 to 120
  + Avoids some IO delays (bsc#1100529)
  + Corrected supported services help info for -U
  + Collects iSCSI Target information (bsc#1133844)
  + FTPES uses --ssl-reqd instead of depricated --ftp-ssl
  + Defaults to https FTP server uploads (bsc#1134599)
* Mon Mar  4 2019 jason.record@suse.com
- Updated to version 3.1.2
  + Fixed missing sapconf and log (bsc#1081326)
  + Added timed_log_cmd to hwinfo and showmount commands (bsc#1120967)
* Fri Mar  1 2019 jason.record@suse.com
- Updated to version 3.1.1
  + Fixed X missing /prob/fb error (bsc#1127069)
  + Fixed dasdview -f (bsc#1109664)
  + Clarified -t help description (bsc#1121043)
  + Fixed grep error in NTP when /etc/cron.d is empty (bsc#1127063)
  + Collects systemd journal with minimum install (bsc#1094225)
  + Supportconfig fails on bzip archives (bsc#1120049)
  + Get few drbd output & configuration #42
* Mon Feb 18 2019 jason.record@suse.com
- Corrected missed SUSE separation lines
- Fixed invalid exit code commands (bsc#1125666)
- CVE-2018-19640: supportutils: Users can kill arbitrary processes
  (CVE-2018-19640 bsc#1118463)
- User can overwrite arbitrary log files in support tar
  (CVE-2018-19638 bsc#1118460)
- Code execution if run with -v
  (CVE-2018-19639 bsc#1118462)
- Static temporary filename allows overwriting of files
  (CVE-2018-19637 bsc#1117776)
* Fri Feb 15 2019 jason.record@suse.com
- Included additional SUSE separation (bsc#1125609)
- Merged added listing of locked packes by zypper #41
* Wed Jan 30 2019 jason.record@suse.com
- Corrected spec file errors
* Mon Jan 28 2019 jason.record@suse.com
- Added firewall-cmd info
- btrfs filesystem usage
- Add ls -lA --time-style=long-iso /etc/products.d/
- Dump lsof errors
- Added corosync status to ha_info
* Fri Dec 28 2018 jason.record@suse.com
- Clarified -x functionality in supportconfig(8) (bsc#1115245)
- Dump find errors in ib_info
* Fri Oct 26 2018 jason.record@suse.com
- Exclude pam.txt per GDPR by default (bsc#1112461)
* Thu Oct 11 2018 jason.record@suse.com
- udev service and journal content (bsc#1051797)
- supportconfig collects tuned profile settings (bsc#1071545)
- sfdisk -d no disk device specified (bsc#1043311)
* Thu Aug 23 2018 jason.record@suse.com
- Added vulnerabilites check in basic-health.txt (bsc#1105849)
* Thu Jul 12 2018 jason.record@suse.com
- Added backup rpm database directory
- Updated URLs in documentation
* Tue Jul 10 2018 jason.record@suse.com
- Added only sched_domain from cpu0
* Fri Jun 15 2018 jason.record@suse.com
- Blacklist sched_domain from proc.txt (bsc#1046681)
* Mon Mar 26 2018 kukuk@suse.de
- Use %%license instead of %%doc [bsc#1082318]
* Fri Feb  2 2018 jason.record@suse.com
- Accounts for firewalld now (bsc#1079137)
- Added dmesg taint seach
- Removed mii-tool from networking
- Updated HA to use chrony
- Added kdumptool calibrate to crash.txt
- Removed SLES_VER case for sles8,9 and 10
* Thu Feb  1 2018 jason.record@suse.com
- Added tuned feature OPTION_TUNED tuned.txt (bsc#1071545)
- Fixed udev service
- Fixed no disk device with sfdisk (bsc#1078638)
* Tue Jan 30 2018 jason.record@suse.com
- Removed OPTION_SAM from man pages and resource file
- Validated missing commands
- Updated apparmor with systemctl service
- Replaced deprecated networking commands (bsc#1078318)
* Mon Jan 29 2018 jason.record@suse.com
- Removed sam_info since suse_sam is no longer available
- Assigned SLE15 to SLES_VER selections (bsc#1078168)
* Mon Jan 29 2018 jason.record@suse.com
- Includes X without display issue (bsc#1077813)
- Fixes for Infiniband (bsc#1071294)
- Using chrony for NTP (bsc#1077818)
* Fri Jan 26 2018 jason.record@suse.com
- Added os-release processing (bsc#1077758)
- Removed invalid string tty string (bsc#1077681)
- Added SLE15 taint values (bsc#1077683)
* Tue Jan 23 2018 jason.record@suse.com
- Added transactional update with OPTION_TRANSACTIONAL=1
- Updated supportconfig.conf.5 with OPTION_TRANSACTIONAL
* Fri Jan 19 2018 jason.record@suse.com
- Fixed docker package detection (bsc#1069457)
* Fri Jan  5 2018 jason.record@suse.com
- Replaced route with ip route (bsc#1070379)
- Added systemd-delta to systemd.txt (bsc#1071924)
- Changed repos -u to repos -d (bsc#1071926)
- Added rdma-core for infiniband (bsc#1071294)
* Tue Dec 19 2017 jason.record@suse.com
- Branding updates fate#324067
- Fixed piped spelling error
* Fri Oct 27 2017 jason.record@suse.com
- Separated core supportconfig function into resources/supportconfig.rc
- Removed virtualization functions
- Removed OES functions
- Removed eDirectory functions
* Thu Oct 26 2017 jason.record@suse.com
- Initial commit
