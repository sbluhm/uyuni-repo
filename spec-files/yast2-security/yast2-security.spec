#
# spec file for package yast2-security
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-security
Version:        4.3.3
Release:        1.2
Summary:        YaST2 - Security Configuration
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-security

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  perl-XML-Writer
BuildRequires:  pkgconf-pkg-config
BuildRequires:  update-desktop-files
# Pam.List
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-pam >= 4.3.1
BuildRequires:  rubygem-rspec
BuildRequires:  rubygem-yast-rake >= 0.2.5
# CFA::SysctlConfig
BuildRequires:  yast2 >= 4.2.66
# Unfortunately we cannot move this to macros.yast,
# bcond within macros are ignored by osc/OBS.
%bcond_with yast_run_ci_tests
%if %{with yast_run_ci_tests}
BuildRequires:  rubygem-yast-rake-ci)
%endif

# new Pam.ycp API
Requires:       yast2-pam >= 2.14.0
# CFA::SysctlConfig
Requires:       yast2 >= 4.2.66
Requires:       yast2-ruby-bindings >= 1.0.0
# Pam.List
Requires:       yast2-pam >= 4.3.1

Provides:       y2c_sec
Provides:       y2t_sec
Provides:       yast2-config-security
Provides:       yast2-trans-security

Obsoletes:      y2c_sec
Obsoletes:      y2t_sec
Obsoletes:      yast2-config-security
Obsoletes:      yast2-trans-security

Supplements:    autoyast(security)

BuildArch:      noarch

%description
The YaST2 component for security settings configuration.

%prep
%setup -q

%build

%check
%yast_check

%install
%yast_install
%yast_metainfo

%post
# remove broken entry in /etc/login.defs, introduced during installation (bnc#807099)
if [ -f /etc/login.defs  ] ; then
  sed -e '/^[ \t]*LASTLOG_ENAB[ \t]*\"\"/d' -i /etc/login.defs
fi

%files
%{yast_yncludedir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_scrconfdir}
%{yast_schemadir}
%{yast_ydatadir}
%{yast_libdir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
* Thu Aug 13 2020 Ladislav Slezák <lslezak@suse.cz>
- Fixed randomly failing unit tests, do not query the installed
  PAM modules in the testing system (related to bsc#1171318)
- 4.3.3
* Mon Aug 10 2020 schubi@suse.de
- AutoYaST: Added supplements: autoyast(security) into the spec file
  in order to install this packages if the section has been defined
  in the AY configuration file (bsc#1146494).
- 4.3.2
* Tue Jul 28 2020 aschnell@suse.com
- Use pam_pwquality instead of pam_cracklib depending on
  availability (bsc#1171318)
- Fix setting dictpath for pam_pwquality (bsc#1174619)
- 4.3.1
* Tue May 12 2020 josef Reidinger <jreidinger@localhost>
- Autoyast schema: Allow optional types for string and map objects
  (bsc#1170886)
- 4.3.0
* Tue Mar 31 2020 Knut Anderssen <kanderssen@suse.com>
- Apply sysctl changes to the running system when the YaST sysctl
  configuration file is modified (bsc#1167234)
- 4.2.12
* Mon Feb  3 2020 schubi@suse.de
- Using SysctlConfig class: Handle sysctl entries in different
  directories (bsc#1151649).
- 4.2.11
* Thu Jan 23 2020 Steffen Winterfeldt <snwint@suse.com>
- don't use /bin/systemctl compat symlink (bsc#1160890)
- 4.2.10
* Mon Jan 13 2020 Josef Reidinger <jreidinger@suse.com>
- convert old init.d to systemd (jsc#SLE-10976)
- 4.2.9
* Thu Dec 12 2019 schubi@suse.de
- Added to rnc file: sys_gid_max, sys_gid_min, sys_uid_max,
  sys_uid_min, hibernate_system, kernel.sysrq, mandatory_services,
  net.ipv4.ip_forward, net.ipv4.tcp_syncookies,
  net.ipv6.conf.all.forwarding (bsc#1158301).
- 4.2.8
* Mon Nov 25 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- bsc#1155735, bsc#1157541:
  - Read /usr/etc/login.defs.
  - Write login.defs configuration to /etc/login.defs.d/.
- 4.2.7
* Fri Nov 22 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Change default encryption method from DES to SHA512 (bsc#1157541,
  CVE-2019-3700).
- 4.2.6
* Fri Oct 18 2019 schubi@suse.de
- Added extra_services to security.rnc file (bsc#1153623).
- 4.2.5
* Thu Oct  3 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Place sysctl settings in /etc/sysctl.d/ (jsc#SLE-9077).
- 4.2.4
* Fri Sep 27 2019 schubi@suse.de
- AY: Settings have not been exported. "console_shutdown" entry
  has not been evaluated (bsc#1150821).
- 4.2.3
* Thu Sep  5 2019 schubi@suse.de
- AY: Supporting user defined permission files like
  "/etc/permissions.ultra". (bsc#1147173)
- 4.2.2
* Thu Aug 22 2019 schubi@suse.de
- Using rb_default_ruby_abi tag in the spec file in order to
  handle several ruby versions (bsc#1146403).
- 4.2.1
* Fri May 31 2019 Stasiek Michalski <hellcp@mailbox.org>
- Add metainfo (fate#319035)
- Revamp spec
- Replace GenericName with Comment
- 4.2.0
* Mon Nov 26 2018 Noah Davis <noahadvs@gmail.com>
- Provide icon with module (boo#1109310)
- 4.1.2
* Fri Nov  2 2018 schubi@suse.de
- Writing security settings in first AY installation stage.
  So other modules (e.g. users) can rely on these settings now.
  (bnc#1112769)
- 4.1.1
* Tue Oct 16 2018 schubi@suse.de
- Added license file to spec.
* Thu Aug 23 2018 dgonzalez@suse.com
- Upate calls to YaST2 systemd classes (related to fate#319428)
- 4.1.0
* Mon Aug 20 2018 schubi@suse.de
- Switched license in spec file from SPDX2 to SPDX3 format.
* Fri Apr  6 2018 mfilka@suse.com
- bnc#1087957 - version bump
- 4.0.0
* Wed Aug 31 2016 jreidinger@suse.com
- mark string "Security" translatable (bnc#988764)
- 3.2.3
* Mon Mar  7 2016 knut.anderssen@suse.com
- Added support for multiple display managers (bnc#946889).
- Replaced testsuite tests by rspec tests.
- Removed autotools.
- Updated yast2 dependency for cfg_mail.scr
- 3.2.2
* Fri Feb 26 2016 knut.anderssen@suse.com
- Removed "Boot permissions - Interpretation of Ctrl + Alt + Del"
  combo box "Reboot" entry for s390 architecture. (fate#319711)
- 3.2.1
* Thu Sep 24 2015 ancor@suse.com
- Bumped version number in order to branch the SLE version due to
  different display manager behavior (bnc#946889).
- 3.2.0
* Wed Aug 19 2015 ancor@suse.com
- Added some entries to the list of optional services (bnc#942379)
- 3.1.11
* Fri Jun 19 2015 ancor@suse.com
- Settings of security levels moved to YAML files
- Redefined security levels (last part of fate#318425)
- 3.1.10
* Mon Jun 15 2015 ancor@suse.com
- Updated list of mandatory and optional services (part of
  fate#318425)
- 3.1.9
* Fri Jun 12 2015 ancor@suse.com
- When checking services, systemd aliases are now taken into
  account (so, for example, rsyslog is accounted as syslog).
* Thu Jun 11 2015 ancor@suse.com
- Removed references to runlevels (obsolete). Only current systemd
  target is analyzed. (fate#318425, bnc#941620)
- List of mandatory and optional services moved to a YAML file.
* Tue Jan 13 2015 ancor@suse.com
- Fixed an error setting the shutdown behaviour of KDM (bnc#907907)
- YaST agents moved to the right location in the source tree
- 3.1.8
* Thu Jan  8 2015 jsuchome@suse.cz
- fix paths for systemd target links (bnc#911523)
- 3.1.7
* Mon Dec 22 2014 ancor@suse.com
- Fixed the interface to show and process correctly values from
  sysctl.conf.
- Source code cleanup, including some minor fixes and new tests.
* Thu Dec  4 2014 jreidinger@suse.com
- remove X-KDE-Library from desktop file (bnc#899104)
* Mon Oct 27 2014 mvidner@suse.com
- Removed CWD_IN_ROOT_PATH, CWD_IN_USER_PATH also from the UI where
  they showed as empty lines in the overview (FATE#100011,
  boo#900829), by Antoine Belvire.
- 3.1.5
* Tue Aug  5 2014 ancor@suse.com
- Speedup Security.ReadServiceSettings (bnc#890349)
- Drop obsolete runlevel parameter from some methods
- 3.1.4
* Fri Mar 28 2014 vmoravec@suse.com
- Fix failing testsuite
- 3.1.3
* Thu Jan 30 2014 jreidinger@suse.com
- Remove writting to dropped /etc/sysconfig/suseconfig
  (FATE#100011)
- 3.1.2
* Wed Nov 13 2013 jreidinger@suse.com
- Add explicit COPYING file
* Thu Sep 19 2013 lslezak@suse.cz
- do not use *.spec.in template, use *.spec file with RPM macros
  instead
- 3.1.0
* Wed Jul 31 2013 yast-devel@opensuse.org
- converted from YCP to Ruby by YCP Killer
  (https://github.com/yast/ycp-killer)
- version 3.0.0
* Thu Apr 25 2013 jsuchome@suse.cz
- ignore case for encryption method names (bnc#810600)
- 2.23.6
* Fri Mar  8 2013 jsuchome@suse.cz
- remove broken LASTLOG_ENAB entry from /etc/login.defs (bnc#807099)
- 2.23.5
* Thu Mar  7 2013 jsuchome@suse.cz
- drop unused LASTLOG_ENAB support (bnc#807099)
- drop obsoleted GROUP_ENCRYPTION (bnc#802006)
- if key is not present in config file, do not write new value
  (bnc#807099)
- 2.23.4
* Wed Mar  6 2013 jsuchome@suse.cz
- added missing etc_polkit-default-privs_local.scr
- 2.23.3
* Wed Feb  6 2013 jsuchome@suse.cz
- /etc/default/useradd is dropped (bnc#802006)
- adapted to changes of /etc/login.defs (bnc#802006)
- 2.23.2
* Mon Feb  4 2013 jsuchome@suse.cz
- testsuite adapted to last changes (SuSEconfig removal)
- 2.23.1
* Wed Oct 24 2012 jsuchome@suse.cz
- remove SuSEconfig calls (fate#100011)
- 2.23.0
* Mon Apr  2 2012 jsuchome@suse.cz
- testsuite: explicitely set the output of target.stat
- 2.22.5
* Thu Mar 29 2012 jsuchome@suse.cz
- merge proofread texts
- 2.22.4
* Mon Mar 26 2012 jsuchome@suse.cz
- testsuite adapted to changes in FileUtils.ycp
- 2.22.3
* Mon Feb 20 2012 jsuchome@suse.cz
- corectly read/write ctrl-alt-delete behavior when systemd is used
  (bnc#742783)
- 2.22.2
* Tue Jan 31 2012 jsuchome@suse.cz
- use sha512 as default encryption value, not 'des' (bnc#743715)
- 2.22.1
* Wed Jan 25 2012 jsuchome@suse.cz
- confirmed license
- 2.22.0
* Mon Oct 10 2011 jsuchome@suse.cz
- include etc_polkit-default-privs_local.scr in rpm
- 2.21.6
* Mon Sep 26 2011 visnov@suse.cz
- set dialog title
- 2.21.5
* Mon Sep 19 2011 jsuchome@suse.cz
- fixed testsuite
- 2.21.4
* Fri Sep 16 2011 jsuchome@suse.cz
- added option to tune system hibernation rights (bnc#704997)
- 2.21.3
* Thu Sep  8 2011 jsuchome@suse.cz
- sysctl settings now in /etc/sysctl.conf (bnc#714405)
- 2.21.2
* Fri Aug  5 2011 tgoettlicher@suse.de
- fixed .desktop file (bnc #681249)
* Wed Jul 20 2011 jsuchome@suse.cz
- remove blowfish hash from selections (fate#312321)
- 2.21.1
* Tue Apr  5 2011 jsuchome@suse.cz
- added support for SHA-2 based crypto methods (fate309705)
- 2.21.0
* Wed Nov 10 2010 jsuchome@suse.cz
- remember the default value of CRACKLIB_DICT_PATH (bnc#650425)
- 2.20.2
* Mon Aug 16 2010 jsuchome@suse.cz
- removed 'disable' from descriptions of settings (bnc#610944)
- 2.20.1
* Fri Aug  6 2010 jsuchome@suse.cz
- testsuite adapted to changes in yast2-pam
- 2.20.0
* Fri Mar 12 2010 jsrain@suse.cz
- renamed the to Security Center and Hardening (fate#309121)
* Fri Feb  5 2010 jsuchome@suse.cz
- DISPLAYMANAGER_SHUTDOWN is not for GDM (bnc#570656)
- 2.19.1
* Wed Jan 13 2010 kmachalkova@suse.cz
- Adjusted .desktop file(s) to wrap /sbin/yast2/ calls in xdg-su
  where root privileges are needed, removed X-KDE-SubstituteUID key
  (bnc#540627)
* Mon Dec 21 2009 jsuchome@suse.cz
- new help text for PASS_MIN_LEN (bnc#535617)
- 2.19.0
* Thu Oct  1 2009 jsuchome@suse.cz
- do not save PASS_MIN_LEN if cracklib is disabled
- ensure polkit privileges are applied (bnc#541393)
- 2.18.3
* Thu Sep  3 2009 jsuchome@suse.cz
- added keywords to desktop file
- 2.18.2
* Mon Jun 22 2009 coolo@novell.com
- fix uild with automake 1.11
- 2.18.1
* Tue Jun  2 2009 jsuchome@suse.cz
- pam_pwcheck calls replaced with pam_cracklib/pam_pwhistory,
  removed obsolete "obscure checks" settings (fate#305468)
- 2.18.0
* Mon Feb  9 2009 lslezak@suse.cz
- added "SuSEfirewall" and "earlysyslog" service to ignore list
  of extra services in runlevel 3 and 5 (bnc#473345)
* Wed Jan 21 2009 jsuchome@suse.cz
- removed progress dialog during read (bnc#447584)
* Fri Nov 28 2008 ug@suse.de
- conflict in rnc file fixed
- 2.17.12
* Thu Nov 13 2008 ug@suse.de
- rnc file fixed
- 2.17.11
* Mon Nov 10 2008 jsuchome@suse.cz
- testsuite adapted to previous changes
- 2.17.10
* Fri Nov  7 2008 jsuchome@suse.cz
- fixes for bnc#442552:
- missing check for `finish
- check more carefuly pam-config output, correctly remove values
- remove GROUP_ENRYPTION from levels
- do not check service values against levels
- 2.17.9
* Fri Nov  7 2008 jsuchome@suse.cz
- fixed testsuite
- 2.17.8
* Thu Oct 30 2008 lslezak@suse.cz
- better check enabled mail services (bnc#437363)
- do not check "consolekit" service, it's started automatically
  (bnc#436797), added "boot.clock" as an optional service
- fixed location of "DISABLE_RESTART_ON_UPDATE" and
  "DISABLE_STOP_ON_REMOVAL" variables - they are in
  /etc/sysconfig/services now
- 2.17.7
* Fri Oct 24 2008 lslezak@suse.cz
- Disable "Change Status" button when the current value is
  "Unknown" (bnc#436796)
* Mon Oct 13 2008 lslezak@suse.cz
- fixed the label for option DISPLAYMANAGER_ROOT_LOGIN_REMOTE
  (bnc#434273)
- 2.17.6
* Wed Oct  8 2008 jsuchome@suse.cz
- unified help texts for IP forwarding (bnc#432186)
- use Table instead of RichText also for GTK UI (bnc#432446)
- 2.17.5
* Fri Sep 26 2008 lslezak@suse.cz
- fixed the Security Overview dialog in ncurses mode (use a table
  widget instead of richtext) (bnc#429965)
- 2.17.4
* Tue Sep 23 2008 jsrain@suse.cz
- fixed incorrect tags in helps (bnc #429063)
* Tue Sep 16 2008 lslezak@suse.cz
- check enabled services in runlevel 3 and 5, activate changes
  in Security::Write() (bnc#425864)
- testsuite update
- 2.17.3
* Mon Sep 15 2008 lslezak@suse.cz
- added new variables to the predefined security levels
- fixed build: updated the testsuite - added new variables
- 2.17.2
* Mon Sep 15 2008 lslezak@suse.cz
- overview dialog - display a warning in the help popup when the
  option could not be read
* Fri Sep 12 2008 lslezak@suse.cz
- added more options in the security overview dialog, added "Help"
  links (fate#303598)
- 2.17.1
* Tue Aug 12 2008 lslezak@suse.cz
- added security overview dialog (part of fate#303598)
- 2.17.0
* Mon Aug 11 2008 lslezak@suse.cz
- display tree navigationon on the left side, display only one
  dialog instead of the long workflow (part of fate#303598)
* Fri May 16 2008 jsrain@suse.cz
- added categories Settings and System into desktop file
  (bnc #382778)
* Wed Apr 30 2008 jsuchome@suse.cz
- new defaults in security levels (bnc#385159):
    CWD_IN_ROOT_PATH, CWD_IN_USER_PATH always "no",
    ENABLE_SYSRQ "yes" for Home Workstation
    RUN_UPDATEDB_AS always "nobody"
    OBSCURE_CHECKS_ENAB, PASSWD_USE_CRACKLIB always "yes"
- 2.16.1
* Mon Apr 14 2008 jsuchome@suse.cz
- 2.16.0
* Mon Mar 17 2008 jsrain@suse.cz
- added 'StartupNotify=true' to the desktop file (bnc #304964)
* Mon Dec  3 2007 jsuchome@suse.cz
- merged texts from proofread
* Thu Aug 23 2007 jsuchome@suse.cz
- check the output of tointeger before using it as integer (#295494)
- 2.15.1
* Thu Jun 21 2007 adrian@suse.de
- fix changelog entry order
* Fri May 25 2007 jsrain@suse.cz
- removed outdated translations from .desktop-files (#271209)
* Wed Jan 17 2007 jsuchome@suse.cz
- fixed help text to mention GDM (#216915)
- 2.15.0
* Thu Oct 26 2006 jsuchome@suse.cz
- schema file moved from autoyast package (#215249)
- 2.14.2
* Thu Sep 21 2006 jsuchome@suse.cz
- write correct SuSEconfig module for display manager (#205979)
- 2.14.1
* Fri Aug 25 2006 jsuchome@suse.cz
- adapted for pam-config usage (F300956)
- API of PamSettings module is obsolete
- 2.14.0
* Mon Aug 21 2006 jsuchome@suse.cz
- adapted layout to fit in 80x40 xterm (#200382)
- 2.13.5
* Tue Jun 13 2006 jsuchome@suse.cz
- use DISPLAYMANAGER_SHUTDOWN instead of KDM_SHUTDOWN (#183844)
- 2.13.4
* Mon Jun 12 2006 mvidner@suse.cz
- Moved cfg_security.scr from yast2-security.rpm to yast2.rpm
- 2.13.3
* Mon Feb 20 2006 jsuchome@suse.cz
- reduced BuildRequires
- 2.13.2
* Mon Dec 19 2005 jsuchome@suse.cz
- merged proofread texts
- 2.13.1
* Wed Nov 23 2005 jsuchome@suse.cz
- added option to store user password history (F300154)
- 2.13.0
* Thu Jun  9 2005 jsuchome@suse.cz
- text fixes from proofreader
- fixed wrong description of PASS_MAX_DAYS, PASS_MIN_DAYS
- 2.12.2
* Fri May 13 2005 jsuchome@suse.cz
- tell init to re-examine the /etc/inittab after modification (#83480)
- 2.12.1
* Mon Apr 18 2005 jsuchome@suse.cz
- removed support for FAILLOG_ENAB (feature 2669)
- 2.12.0
* Wed Mar  2 2005 jsuchome@suse.cz
- merged texts from proofreading
* Mon Feb  7 2005 jsuchome@suse.cz
- merged texts from proofreading
- 2.11.3
* Fri Jan 21 2005 jsuchome@suse.cz
- handle both "cracklib" and "use_cracklib" values in pam_pwcheck.conf
  (#49621)
- 2.11.2
* Fri Dec 17 2004 jsuchome@suse.cz
- removed select's and lookup's
- 2.11.1
* Tue Nov  2 2004 jsuchome@suse.cz
- do not set maximum password length (#29112)
- 2.11.0
* Mon Aug 30 2004 nashif@suse.de
- use modified flag (#43904) in auto clients
- 2.10.5
* Thu Aug 19 2004 jsuchome@suse.cz
- commandline function: "set"
- 2.10.3
* Wed Aug 18 2004 jsuchome@suse.cz
- fix: check correctly which security level is in use
- fix: read correctly value for password encryption
- commandline functions: summary, level
* Tue Jul 27 2004 jsuchome@suse.cz
- read also group encryption from /etc/default/passwd
- 2.10.2
* Mon Jun 28 2004 jsuchome@suse.cz
- updated to current yast2-pam usage
  (/etc/default/passwd used for storing password encryption)
- 2.10.1
* Tue Jun 15 2004 msvec@suse.cz
- updated testsuite
- 2.10.0
* Sun Apr  4 2004 msvec@suse.cz
- changed minimum UID from 500 to 1000 (#38181)
- 2.9.14
* Fri Apr  2 2004 msvec@suse.cz
- changed license to GPL
- 2.9.13
* Wed Mar 17 2004 jsuchome@suse.cz
- fixed testsuite (forced by change of PamSettings::Write)
- 2.9.12
* Fri Mar 12 2004 jsuchome@suse.cz
- flush changes of pam configuration (#35721)
- 2.9.11
* Thu Mar 11 2004 msvec@suse.cz
- enabled the testsuite again
- 2.9.10
* Wed Mar 10 2004 jsuchome@suse.de
- disabled testsuite
- 2.9.9
* Wed Mar 10 2004 nashif@suse.de
- Adapted for new wizard
* Mon Mar  8 2004 msvec@suse.cz
- set title icons
- 2.9.8
* Fri Mar  5 2004 msvec@suse.cz
- more strict type casts
- 2.9.7
* Mon Mar  1 2004 msvec@suse.cz
- proof-read messages
- 2.9.6
* Tue Feb 24 2004 msvec@suse.cz
- fix enabling of the remote XDM access (#34879)
- 2.9.5
* Fri Feb  6 2004 msvec@suse.cz
- use Sequencer module
- drop y2cc config file
- 2.9.4
* Mon Jan 26 2004 msvec@suse.cz
- updates for the new interpreter
- 2.9.3
* Thu Jan 22 2004 msvec@suse.cz
- NI updates
- 2.9.2
* Wed Oct 22 2003 msvec@suse.cz
- routines cleanup
- 2.9.1
* Fri Sep 26 2003 jsuchome@suse.cz
- read new settings from /etc/login.defs (SYSTEM_UID_MAX, USERADD_CMD etc.)
- 2.9.0
* Thu Sep 11 2003 msvec@suse.cz
- changed "UNIX system" to "UNIX like system" in helps (#30495)
- 2.8.6
* Thu Sep 11 2003 nashif@suse.de
- #30291: return list of required packages for autoinstallation
* Tue Sep  9 2003 msvec@suse.cz
- show correctly the current level (#30320)
- 2.8.5
* Fri Sep  5 2003 msvec@suse.cz
- proof read help texts
- 2.8.4
* Thu Aug 21 2003 msvec@suse.cz
- don't modify files when nothing changed (#28999)
- 2.8.3
* Wed Aug 20 2003 jsuchome@suse.de
- removed redundant "initialization dialog" (#28779)
- 2.8.2
* Mon Aug 11 2003 jsuchome@suse.de
- proofread texts (1st round)
* Tue Jul 22 2003 msvec@suse.cz
- simplify autoinstallation client
- updated testsuite
- 2.8.1
* Wed Jul 16 2003 jsuchome@suse.de
- updated to new Pam/PamSettings interface
* Sat May 10 2003 msvec@suse.de
- maximum password length is related to encryption method (#13291)
- support for enabling of SysRq keys
- define password lengths (#13291)
- improved documentation
- better help texts (#26791)
- updates for the new wizard functions
- 2.8.0
* Mon Mar  3 2003 msvec@suse.de
- autoinstallation fixes by nashif
- 2.7.8
* Sun Feb 16 2003 nashif@suse.de
- Set modified true when importing
- 2.7.7
* Sat Feb 15 2003 nashif@suse.de
- convert case when importing/exporting in autoinst mode
- _auto.ycp Result ->Export
- 2.7.6
* Mon Feb 10 2003 msvec@suse.de
- proofread texts
- 2.7.5
* Mon Feb  3 2003 msvec@suse.cz
- autoinst and texts fixes
- 2.7.4
* Thu Jan 30 2003 msvec@suse.de
- proofread texts
- 2.7.3
* Wed Jan 22 2003 msvec@suse.cz
- added missing module to the package
- 2.7.2
* Wed Jan 22 2003 nashif@suse.de
- Added import function to _auto client
- switch case to lower when exporting/upper when importing
* Tue Jan 21 2003 msvec@suse.de
- fixed some error popups (and added some more)
- fixed the autoinstallation client
- 2.7.1
* Tue Oct 22 2002 msvec@suse.cz
- completely rewritten internals
- major cleanup, simplification and speedup
- don't ask for save if nothing was changed
- support for CWD in user's path (#18274)
- complete support for blowfish (#12758)
- 2.7.0
* Thu Sep  5 2002 msvec@suse.cz
- fix the Next|Finish behavior (#18937)
- provide more old translations (y2t_sec)
- 2.6.10
* Tue Aug 27 2002 jsuchome@suse.cz
- provide/obsolete old translation packages (bug #18691)
* Wed Aug 14 2002 mvidner@suse.cz
- Merged proofread texts for the second translation round.
- 2.6.8
* Mon Jul 29 2002 msvec@suse.cz
- some general purpose agents moved to yast2
- blowfish password encryption (#17039) <jsrain@suse.cz>
- 2.6.7
* Wed Jul 24 2002 msvec@suse.cz
- fixed some error messages
- 2.6.6
* Mon Jul 22 2002 jsrain@suse.cz
- merged proofread texts
- version 2.6.5
* Mon Jul 15 2002 nashif@suse.de
- adapted for use with the autoinstallation configuration system
- security_auto now exports lower case values
* Fri Jul 12 2002 arvin@suse.de
- use proper namespace for Args and CallFunction (#16776)
* Mon Jul  8 2002 msvec@suse.cz
- use Wizard and other predefined functions
- drastic reduction and simplification of UI code
- split adduser dialog
- 2.6.3
* Thu Jul  4 2002 arvin@suse.de
- moved non binary files to /usr/share/YaST2
* Mon Jul  1 2002 msvec@suse.cz
- package renamed to yast2-security
- preliminary autoinstallation support
- 2.6.1
* Mon Jun  3 2002 msvec@suse.cz
- testsuite update
- shortened label (#15089)
- removed outdated docs #15875
- implement CONSOLE SHUTDOWN fully in yast2
- don't run full SuSEconfig
- use y2autoconf, create-spe
- 2.6.0
* Wed Feb 27 2002 msvec@suse.cz
- use buildroot (via y2spec)
- include the locate agent in the package
- 2.5.11
* Mon Feb 25 2002 msvec@suse.cz
- use proper sysconfig files (#13619)
- minor fix of permissions writing
- added agent for sysconfig/locate
- updated testsuite
- 2.5.10
* Mon Feb 18 2002 msvec@suse.cz
- fixed shortcuts
- fixed permissions reading and writing (#13106)
- updated testsuite
- 2.5.9
* Mon Feb 11 2002 mvidner@suse.cz
- Fixed login.defs agent to handle quoted values.
- Fixed test suite.
- 2.5.8
* Tue Feb  5 2002 kukuk@suse.de
- Add support for global pam_unix2 and pam_pwcheck config files
- Version 2.5.7
* Sat Jan 26 2002 nashif@suse.de
- Added agents to file list
- 2.5.6
* Wed Jan 16 2002 msvec@suse.cz
- added pam_unix2 and rlogin|gdm to MD5 settings (md5 is #9543)
- use_cracklib is now via pam (PASSWD_USE_CRACKLIB)
- drop telnet for root checkbox (ROOT_LOGIN_REMOTE)
- added /etc/login.defs agent (using ini agent right now)
- added /etc/sysconfig/security agent
- updated testsuite
- 2.5.5
* Thu Dec 20 2001 msvec@suse.cz
- new menuentry file format
- 2.5.3
* Tue Dec  4 2001 msvec@suse.cz
- 3rd params to select
- 2.5.2
* Wed Nov 21 2001 msvec@suse.cz
- added DISPLAYMANAGER_REMOTE_ACCESS setting (#10824)
- updated testsuite
- 2.5.1
* Mon Nov 19 2001 msvec@suse.cz
- fixed lookup 3rd parameters
- migration to yast2-devtools
- minor makefiles fixes
- 2.5.0
* Tue Aug 28 2001 msvec@suse.cz
- enlarge max uid to 32 bit (#9871)
- parseycp during check
- version 2.4.5
* Wed Aug 22 2001 msvec@suse.cz
- added requires (rcconfig and pam agents, wizard library)
- version 2.4.4
* Wed Aug 15 2001 msvec@suse.cz
- added MD5 password encryption suuport
- testsuite for the above
- removed Finish function
- removed UI(_(...))
- use of UI:: and SCR::
- version 2.4.3
* Thu Aug  9 2001 msvec@suse.cz
- use common_messages for button labels
- version 2.4.2
* Mon Jul 30 2001 msvec@suse.cz
- new libycp fixes
- minor variable fixes
- updated testsuite
- adapt to the new translator (locale useless)
- version 2.4.1
* Mon Jul  9 2001 ro@suse.de
- removed yast2-core-translator from neededforbuild
* Tue Jul  3 2001 msvec@suse.cz
- adapted to the system agent split
- added missing shortcuts (#9017)
- version 2.4.0
* Wed May  2 2001 msvec@suse.cz
- fix menuentry file
- version 2.3.5
* Mon Apr 23 2001 msvec@suse.cz
- removed isnils
- no more quick SuSEconfig
- help fix (#6912)
- version 2.3.4
* Fri Apr 13 2001 msvec@suse.cz
- enabled abuild checking
- fixed help text (#6190)
- version 2.3.3
* Wed Apr  4 2001 msvec@suse.cz
- updated comments and docs
- version 2.3.2
* Fri Mar 30 2001 msvec@suse.cz
- support for "auto" KDM setting
- new libycp adaptation
- autobuild checking
- removed 7.1 hacks
- source cleanup
- version 2.3.1
* Wed Mar  7 2001 msvec@suse.cz
- package rename
- version 2.3.0
* Mon Jan 15 2001 msvec@suse.cz
- minimal UID should be 500 (#5643)
- updated comments for translators
- Next button translatable and shortcut
* Fri Jan 12 2001 msvec@suse.de
- root telnet enabled means disabled and vice versa
- minor gui update
- saving fixed
* Wed Jan 10 2001 msvec@suse.de
- Translatable strings bugfix
* Fri Jan  5 2001 kkaempf@suse.de
- provide keyboard shortcuts for buttons
* Fri Jan  5 2001 kkaempf@suse.de
- mark strings as translatable
* Fri Dec 15 2000 msvec@suse.cz
- help text for the main screen added (#4619)
- check the minimum <= maximum (#4682)
* Wed Dec 13 2000 mike@suse.de
- new menuentry file
* Wed Dec 13 2000 msvec@suse.cz
- menuentry updated
* Tue Dec 12 2000 msvec@suse.cz
- helps
- GUI update
- version 1.1.3
* Mon Dec 11 2000 msvec@suse.cz
- minor GUI update
- fix the Custom writing
- ``Something() -> ``(Something())
-  version  1.1.2
* Sat Dec  9 2000 kukuk@suse.de
- Add group tag
* Fri Dec  8 2000 msvec@suse.cz
- also update the source
* Fri Dec  8 2000 msvec@suse.cz
- minor layout and functional updates
- version 1.1.1
* Wed Nov 29 2000 msvec@suse.cz
- new layout
- version 1.1.0
* Wed Oct 25 2000 msvec@suse.cz
- initial version
* Thu Jan  2 1997 msvec@suse.de
- bugfixes
