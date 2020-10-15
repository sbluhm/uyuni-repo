#
# spec file for package yast2-pam
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


Name:           yast2-pam
Version:        4.3.2
Release:        1.2
Summary:        YaST2 - PAM Agent
License:        GPL-2.0-only
Group:          System/YaST

URL:            http://github.com/yast/yast-pam
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 3.1.10

%if 0%{?suse_version}
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# cfa for parsing nsswitch
BuildRequires:  rubygem(%rb_default_ruby_abi:cfa) >= 0.6.4
# testsuite
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
# cfa for parsing nsswitch
Requires:       rubygem(%rb_default_ruby_abi:cfa) >= 0.6.4
%else
BuildRequires:  rubygem-yast-rake
# cfa for parsing nsswitch
BuildRequires:  rubygem-cfa >= 0.6.4
# testsuite
BuildRequires:  rubygem-rspec
# cfa for parsing nsswitch
Requires:       rubygem-cfa >= 0.6.4

%endif

# lenses are needed to use cfa
BuildRequires:  augeas-lenses
Requires:       yast2
# lenses are needed to use cfa
Requires:       augeas-lenses
Requires:       pam-config >= 0.8
Requires:       yast2-ruby-bindings >= 1.0.0

BuildArch:      noarch

%description
This agent is used by YaST2 to modify the PAM configuration files

%prep
%setup -n %{name}-%{version}

%check
rake test:unit

%build

%install
rake install DESTDIR="%{buildroot}"

%files
%defattr(-,root,root)
%dir %{yast_moduledir}
%{yast_moduledir}/*
%dir %{yast_scrconfdir}
%{yast_scrconfdir}/*.scr
%{yast_libdir}
%dir %{yast_agentdir}
%{yast_agentdir}/ag_passwd
%doc %{yast_docdir}
%license COPYING

%changelog
* Tue Jul 28 2020 Ancor Gonzalez Sosa <ancor@suse.com>
- Fixed a bug, introduced in the latest version, related to
  deletion of nsswitch entries (related to bsc#1173119).
- 4.3.2
* Tue Jul 28 2020 aschnell@suse.com
- Added function to query PAM modules (bsc#1171318).
- 4.3.1
* Fri Jul 24 2020 David Diaz <dgonzalez@suse.com>
- Support reading nsswitch.conf from /usr/etc  (bsc#1173119).
- 4.3.0
* Thu Aug 22 2019 schubi@suse.de
- Using rb_default_ruby_abi tag in the spec file in order to
  handle several ruby versions (bsc#1146403).
- 4.2.4
* Thu May 16 2019 Ladislav Slezák <lslezak@suse.cz>
- Fixed packager initialization (fixes missing GPG keys in the
  installed system) (bsc#1135295)
- 4.2.3
* Tue May 14 2019 Stefan Hundhammer <shundhammer@suse.com>
- Init pkg target with Installation.destdir, not "/" (bsc#1133541)
- 4.2.2
* Wed Apr 17 2019 Ladislav Slezak <lslezak@suse.cz>
- Skip loading the package manager in the test mode, fixes
  broken unit tests in yast2-users and yast2-nis-client
  (related to the previous fix bsc#1128385)
- 4.2.1
* Tue Apr 16 2019 Stefan Hundhammer <shundhammer@suse.com>
- Offer autologin only if a display manager that supports it is
  installed (bsc#1128385)
- 4.2.0
* Tue Feb 26 2019 José Iván López González <jlopez@suse.com>
- Version bump (bsc#1124009)
- 4.1.0
* Tue Oct 16 2018 schubi@suse.de
- Added license file to spec.
* Fri Aug 17 2018 schubi@suse.de
- Switched license in spec file from SPDX2 to SPDX3 format.
* Fri Apr  6 2018 mfilka@suse.com
- bnc#1087957 - version bump
- 4.0.0
* Thu Sep 22 2016 mvidner@suse.com
- Speed up build by not requiring yast2 (bsc#999203).
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
* Wed Feb  6 2013 jsuchome@suse.cz
- removed PamSettings.ycp, handler of obsolete /etc/default/passwd
  (bnc#802006)
- 2.23.1
* Thu Oct 11 2012 jsuchome@suse.cz
- remove obsolete SuSEconfig call
- 2.23.0
* Tue Jan 31 2012 jsuchome@suse.cz
- do not use MD5 as fallback (bnc#743715)
- 2.22.1
* Wed Jan 25 2012 jsuchome@suse.cz
- confirmed license
- 2.22.0
* Mon Oct 17 2011 jsuchome@suse.cz
- autologin: remove checking for display manager, now most of them
  support autologin
- 2.21.0
* Tue Feb  1 2011 jsuchome@suse.cz
- correctly package etc_sssd_conf.scr (bnc#666184)
- 2.20.1
* Fri Jan 21 2011 jsuchome@suse.cz
- agents for accessing krb5.conf and sssd.conf moved here,
  so they are available in more modules
- 2.20.0
* Thu Jul 15 2010 jsuchome@suse.cz
- use full path for pam-config
- 2.19.2
* Tue Feb 23 2010 jsuchome@suse.cz
- lxdm can also suport autologin (bnc#581477)
- 2.19.1
* Thu Dec 10 2009 jsuchome@suse.cz
- kde4-kdm is now kdm (bnc#561900)
- 2.19.0
* Tue Jun  2 2009 jsuchome@suse.cz
- removed obsolete functions from PamSettings
- 2.18.0
* Mon Nov 10 2008 visnov@suse.cz
- make it build
- 2.17.1
* Mon Nov 10 2008 jsuchome@suse.cz
- new version for new release
- 2.17.0
* Mon Apr 28 2008 jsuchome@suse.cz
- Autologin: kdm3/kdm4 values as DISPLAYMANAGER, no SuSEconfig.kdm
- 2.16.2
* Thu Mar 27 2008 jsuchome@suse.cz
- kdm could be in kde4-kdm package
- 2.16.1
* Fri Oct 19 2007 jsuchome@suse.cz
- check for empty lines in passwd/group/shadow (#333305)
- 2.16.0
* Thu Aug 24 2006 jsuchome@suse.cz
- adapted for pam-config usage (F300956)
- API of PamSettings module is obsolete
- 2.14.0
* Wed Jul 26 2006 jsuchome@suse.cz
- added Pam.ycp module to handle /etc/pam.d/* files (#190330)
- 2.13.5
* Tue Jul 25 2006 jsuchome@suse.cz
- added support for empty passwords (#144724)
- 2.13.4
* Thu Jun  1 2006 jsuchome@suse.cz
- API of Autologin, Nsswitch and PamSettings marked as stable
- 2.13.3
* Tue Feb 14 2006 jsuchome@suse.cz
- reduced BuildRequires and Requires (yast2-packager not needed)
- 2.13.2
* Wed Nov 16 2005 jsuchome@suse.cz
- adapted passwd-agent to index maps of users and groups by names,
  not by id's (thus allowing duplicated id's)
- 2.13.1
* Thu Sep 29 2005 jsuchome@suse.cz
- ag_passwd: return everything as strings to allow usernames (etc.)
  starting with 0 (#118371)
- 2.13.0
* Thu Aug 18 2005 jsuchome@suse.cz
- autologin: call correct SuSEconfig module for GDM (#74198)
- 2.12.3
* Thu Aug 11 2005 jsuchome@suse.cz
- do not set 0 as default for empty values (#103873)
- 2.12.2
* Mon Apr 25 2005 jsuchome@suse.cz
- enable autologin for GDM (#74198)
- 2.12.1
* Mon Apr 18 2005 jsuchome@suse.cz
- updated for new interface of ProductFeatures.ycp
- 2.12.0
* Thu Feb  3 2005 jsuchome@suse.cz
- dropped agent-pam
- 2.11.1
* Fri Jan 21 2005 jsuchome@suse.cz
- use Package instead of Require
- 2.11.0
* Wed Aug 18 2004 jsuchome@suse.cz
- correctly check if entries of /etc/default/passwd were modified
- 2.10.3
* Tue Jul 27 2004 jsuchome@suse.cz
- PamSettings: read/write also group encryption method
- Nsswitch: add Write function (write modified file to disk)
- 2.10.2
* Mon Jul 12 2004 jsuchome@suse.cz
- Moved nsswitch.conf agent here from yast2-network.
- Nsswitch.ycp provides YCP interface to nsswitch agent
- 2.10.1
* Mon Jun 28 2004 jsuchome@suse.cz
- /etc/default/passwd is used for handling encryption types
  (new agent + YCP routines)
- 2.10.0
* Thu May 27 2004 jsuchome@suse.cz
- ag_passwd: read group password (#41300)
- 2.9.13
* Tue May 18 2004 jsuchome@suse.cz
- ag_passwd can now read and write multiple +/- lines (#40571)
- ag_passwd: do not throw away the comments
- 2.9.12
* Fri Apr 16 2004 jsuchome@suse.cz
- fix: do not ignore additional user data (#38973)
- 2.9.11
* Fri Apr  2 2004 jsuchome@suse.cz
- changed license to GPL
- 2.9.10
* Tue Mar 30 2004 jsuchome@suse.cz
- ag_passwd fix: do not save NIS users to local files (#37508)
- 2.9.9
* Thu Mar 25 2004 jsuchome@suse.cz
- ag_passwd: check if all parts of shadow line exist during write
  (and set the default values otherwise)
- 2.9.8
* Mon Mar 22 2004 jsuchome@suse.cz
- use lowecase user/group attribute names
- 2.9.7
* Fri Mar 19 2004 mvidner@suse.cz
- added AGENT_LIBADD so that agents work from standalone Perl
* Wed Mar 17 2004 jsuchome@suse.cz
- fix of writing /etc/security/pam*conf files (#35721)
* Mon Mar 15 2004 jsuchome@suse.cz
- changed internal key names: "username" -> "uid", "groupname" -> "cn"
- 2.9.6
* Wed Mar 10 2004 jsuchome@suse.cz
- agent-passwd moved here from yast2-users
- 2.9.5
* Wed Mar 10 2004 jsuchome@suse.cz
- fixed NFB: yast2-indstalltion no more necessary
- 2.9.4
* Thu Mar  4 2004 jsuchome@suse.cz
- check ProductFeatures if Autologin is available (#35023)
- 2.9.3
* Mon Mar  1 2004 jsuchome@suse.cz
- map/list typing
* Mon Mar  1 2004 jsuchome@suse.cz
- merged texts from proofread
* Tue Feb  3 2004 jsuchome@suse.cz
- added Autologin::Use function (set 'use' variable from outside)
- 2.9.2
* Mon Jan 26 2004 msvec@suse.cz
- updated for the new interpreter
- 2.9.1
* Mon Jan 19 2004 jsrain@suse.de
- merged the new interpreter branch
* Fri Nov 28 2003 jsuchome@suse.cz
- syntax fixes for new interpreter
* Fri Nov 21 2003 jsuchome@suse.cz
- yast2-packager required
* Thu Nov 20 2003 jsuchome@suse.cz
- Autologin.ycp now part of yast2-pam
- 2.9.0
* Thu Nov 13 2003 msvec@suse.cz
- migrated to doxygen
- 2.8.6
* Thu Aug 21 2003 jsuchome@suse.cz
- added testsuite
- 2.8.5
* Tue Aug 12 2003 jsuchome@suse.de
- updated documentation
- 2.8.4
* Mon Aug  4 2003 jsuchome@suse.de
- \t is also separator in config files (besides space)
* Wed Jul 23 2003 msvec@suse.cz
- added some fallbacks for SCR access
- 2.8.3
* Wed Jul 16 2003 jsuchome@suse.de
- added YCP interface for agent (Pam.ycp, PamSettings.ycp) [initial]
- stand-alone agent for configuring /etc/security/*.conf
- 2.8.2
* Mon Nov 25 2002 msvec@suse.cz
- 2.7.0
* Wed Sep 11 2002 kukuk@suse.de
- Create temp file after checking if source exists [Bug #19374]
* Mon Jul 29 2002 kukuk@suse.de
- Change y2milestone to y2debug [Bug #17174]
- Version 2.6.4
* Sat Jul  6 2002 arvin@suse.de
- moved non binary files to /usr/share/YaST2
* Tue Jul  2 2002 msvec@suse.cz
- 2.6.2
* Mon Jun 24 2002 arvin@suse.de
- renamed from yast2-agent-pam to yast2-pam
* Wed May 15 2002 arvin@suse.de
- use %%{_libdir} in plugin path
* Mon Apr  8 2002 kukuk@suse.de
- Merge 8.0-branch with STABLE
- Fix for g++ 3.1
- Version 2.6.0
* Thu Feb 28 2002 kukuk@suse.de
- Return only boolean value in Write part of the agent [Bug #13965]
* Tue Feb 19 2002 kukuk@suse.de
- Treat the case correct where the only argument should be removed
- Increase version number to 2.5.3
* Sun Feb 17 2002 kukuk@suse.de
- Treat missing config files as warning, not error [Bug #13343]
- Increase version number to 2.5.2
* Fri Jan 25 2002 kukuk@suse.de
- Check always if fopen returns NULL [Bug #12893]
- Add support for /etc/security/pam_pwcheck.conf
- Increase version number to 2.5.1
* Sat Jan 19 2002 kukuk@suse.de
- Add support for /etc/security/pam_unix2.conf
- Don't remove spaces in comments
- Increase version number to 2.5.0
* Tue Aug 14 2001 kukuk@suse.de
- Fix order of arguments for rename() call
- restore owner and permissions of config file
* Mon Jul 16 2001 arvin@suse.de
- fixed to compile with gcc 3.0
* Sat Jul 14 2001 kukuk@suse.de
- Don't know who modiefied the CVS version without changes entries,
  but use the current CVS version now.
* Tue Jul 10 2001 kukuk@suse.de
- Initial version
