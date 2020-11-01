#
# spec file for package yast2
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


Name:           yast2
Version:        4.3.29
Release:        1.1
Summary:        YaST2 Main Package
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-yast2

Source0:        %{name}-%{version}.tar.bz2
Source1:        yast2-rpmlintrc

# for symlinking yardoc duplicates
BuildRequires:  fdupes
# Needed for tests
BuildRequires:  grep
# for some system directories
BuildRequires:  filesystem
%if 0%{?suse_version}
# for defining abstract methods in libraries
BuildRequires:  rubygem(%{rb_default_ruby_abi}:abstract_method)
# for file access using augeas
BuildRequires:  rubygem(%{rb_default_ruby_abi}:cfa)
# for used augeas lenses
BuildRequires:  augeas-lenses
# for running scripts
BuildRequires:  update-desktop-files
BuildRequires:  rubygem(%{rb_default_ruby_abi}:cheetah)
# For running RSpec tests during build
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
# For converting to/from punycode strings
BuildRequires:  rubygem(%{rb_default_ruby_abi}:simpleidn)
# Needed already in build time
BuildRequires:  yast2-core >= 2.18.12
BuildRequires:  yast2-devtools >= 3.1.10
# RPM dependency filters in Pkg.Resolvables()
BuildRequires:  yast2-pkg-bindings >= 4.3.0
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
# for XML module
BuildRequires:  rubygem(%rb_default_ruby_abi:nokogiri)
%else
# for defining abstract methods in libraries
BuildRequires:  rubygem(abstract_method)
# for file access using augeas
BuildRequires:  rubygem(cfa)
# for used augeas lenses
BuildRequires:  augeas-libs
# for running scripts
BuildRequires:  update-desktop-files
BuildRequires:  rubygem(cheetah)
# For running RSpec tests during build
BuildRequires:  rubygem(rspec)
# For converting to/from punycode strings
BuildRequires:  rubygem(simpleidn)
# Needed already in build time
BuildRequires:  yast2-core >= 2.18.12
BuildRequires:  yast2-devtools >= 3.1.10
# RPM dependency filters in Pkg.Resolvables()
BuildRequires:  yast2-pkg-bindings >= 4.3.0
BuildRequires:  rubygem(yast-rake)
# for XML module
#BuildRequires:  rubygem(nokogiri)
%endif
# To have Yast::WFM.scr_root
BuildRequires:  yast2-ruby-bindings >= 3.2.8
BuildRequires:  yast2-testsuite
# UI::.SetApplicationTitle
BuildRequires:  yast2-ycp-ui-bindings >= 3.2.0
# for the PackageExtractor tests, just make sure they are present,
# these should be installed in the default build anyway
BuildRequires:  cpio
BuildRequires:  rpm

# for ag_tty (/bin/stty)
# for /usr/bin/md5sum
Requires:       coreutils
# for GPG.ycp
Requires:       gpg2
%if 0%{?suse_version}
# for defining abstract methods in libraries
Requires:       rubygem(%{rb_default_ruby_abi}:abstract_method)
# for file access using augeas
Requires:       rubygem(%{rb_default_ruby_abi}:cfa)
# for used augeas lenses
Requires:       augeas-lenses
# For converting to/from punycode strings
Requires:       sysconfig >= 0.80.0
Requires:       rubygem(%{rb_default_ruby_abi}:simpleidn)
# for running scripts
Requires:       rubygem(%{rb_default_ruby_abi}:cheetah)
# for XML module
Requires:       rubygem(%rb_default_ruby_abi:nokogiri)
%else
# for defining abstract methods in libraries
Requires:       rubygem(abstract_method)
# for file access using augeas
Requires:       rubygem(cfa)
# for used augeas lenses
Requires:       augeas-libs
# For converting to/from punycode strings
Requires:       sysconfig >= 0.80.0
Requires:       rubygem(simpleidn)
# for running scripts
Requires:       rubygem(cheetah)
# for XML module
Requires:       rubygem(nokogiri)
%endif
# ag_ini section_private
# ag_ini with (un)quoting support
Requires:       yast2-core >= 2.23.0
Requires:       yast2-hardware-detection
# for SLPAPI.pm
Requires:       yast2-perl-bindings
# RPM dependency filters in Pkg.Resolvables()
Requires:       yast2-pkg-bindings >= 4.3.0
# for y2start
Requires:       yast2-ruby-bindings >= 3.2.10
# new UI::SetApplicationTitle
Requires:       yast2-ycp-ui-bindings >= 3.2.0
Requires:       yui_backend
# scripts for collecting YAST logs
Requires:       yast2-logs
# for the PackageExtractor class, just make sure they are present,
# these should be present even in a very minimal installation
Requires:       cpio
Requires:       rpm
# /usr/bin/hostname command
Requires:       hostname
# pre-requires for filling the sysconfig template (sysconfig.yast2)
#Requires(post):         %fillup_prereq

# xdg-su in .desktops
Recommends:     xdg-utils

# removed the XVersion API
Conflicts:      yast2-country < 4.2.3
# SrvStatusComponent moved to yast2.rpm
Conflicts:      yast2-dns-server < 3.1.17
# removed the XVersion API
Conflicts:      yast2-installation < 4.2.9
# moved cfg_mail.scr
Conflicts:      yast2-mail < 3.1.7
# anyxml droppped
Conflicts:      yast2-packager < 4.3.2
# anyxml droppped
Conflicts:      yast2-update < 4.3.0
# Older snapper does not provide machine-readable output
Conflicts:      snapper < 0.8.6

Obsoletes:      yast2-devel-doc

%description
This package contains scripts and data needed for SUSE Linux
installation with YaST2

%package logs
Summary:        Scripts for handling YAST logs
Group:          System/YaST

Provides:       yast2:/usr/sbin/save_y2logs

Requires:       tar

%description logs
This package contains scripts for handling YAST logs.

%prep
%setup -q

%check
export Y2STRICTTEXTDOMAIN=1
%yast_check

%build

# removed explicit adding of translations to group desktop files, since it is covered by the general call (they are in a subdirectory) and it caused build fail

%install
mkdir -p %{buildroot}%{yast_clientdir}
mkdir -p %{buildroot}%{yast_desktopdir}
mkdir -p %{buildroot}%{yast_imagedir}
mkdir -p %{buildroot}%{yast_localedir}
mkdir -p %{buildroot}%{yast_moduledir}
mkdir -p %{buildroot}%{yast_scrconfdir}
mkdir -p %{buildroot}%{yast_ybindir}
mkdir -p %{buildroot}%{yast_ydatadir}
mkdir -p %{buildroot}%{yast_yncludedir}
mkdir -p %{buildroot}%{yast_libdir}
mkdir -p %{buildroot}%{yast_vardir}
mkdir -p %{buildroot}%{yast_vardir}/hooks
mkdir -p %{buildroot}%{yast_schemadir}/control/rnc
mkdir -p %{buildroot}%{yast_schemadir}/autoyast/rnc
mkdir -p %{buildroot}%{_sysconfdir}/YaST2

%yast_install

# symlink the yardoc duplicates, saves over 2MB in installed system
# (the RPM package size is decreased just by few kilobytes
# because of the compression)
%fdupes -s %{buildroot}/%{_docdir}/yast2

%post
%{fillup_only -n yast2}

if [ -f "/etc/sysctl.d/30-yast.conf" ]; then
    if [ -f "/etc/sysctl.d/70-yast.conf" ]; then
        rm /etc/sysctl.d/30-yast.conf
    else
        mv /etc/sysctl.d/30-yast.conf /etc/sysctl.d/70-yast.conf
    fi
fi

%files

# basic directory structure

%dir %{yast_clientdir}
%dir %{yast_desktopdir}
%{yast_desktopdir}/groups
%dir %{yast_imagedir}
%dir %{yast_localedir}
%dir %{yast_moduledir}
%dir %{yast_scrconfdir}
%dir %{yast_ybindir}
%dir %{yast_ydatadir}
%dir %{yast_yncludedir}
%dir %{yast_vardir}
%dir %{yast_libdir}
%dir %{yast_schemadir}
%dir %{yast_schemadir}/control
%dir %{yast_schemadir}/control/rnc
%dir %{yast_schemadir}/autoyast
%dir %{yast_schemadir}/autoyast/rnc
%dir %{_sysconfdir}/YaST2
%dir %{yast_vardir}/hooks

# yast2

%{yast_ydatadir}/*.ycp
%{yast_clientdir}/*
%{yast_moduledir}/*
%{yast_libdir}/*
%{yast_scrconfdir}/*
%{yast_ybindir}/*
%{yast_agentdir}/ag_*
%{_fillupdir}/sysconfig.yast2

%{_datadir}/bash-completion/completions

# documentation (not included in devel subpackage)
%doc %dir %{yast_docdir}
%license %{yast_docdir}/COPYING
%doc %{yast_docdir}/README.md

%{_mandir}/*/*
%doc %{yast_vardir}/hooks/README.md

/sbin/yast*
%{_sbindir}/yast*

# wizard
%dir %{yast_yncludedir}/wizard
%{yast_yncludedir}/wizard/*.rb

# packages
%dir %{yast_yncludedir}/packages
%{yast_yncludedir}/packages/*.rb

# system
%dir %{yast_yncludedir}/hwinfo
%{yast_yncludedir}/hwinfo/*.rb
%{yast_desktopdir}/messages.desktop

# icons
%{yast_icondir}

%files logs
/usr/sbin/save_y2logs

%changelog
* Wed Sep 23 2020 Ladislav Slezák <lslezak@suse.cz>
- Added "--plain" and "--full" options for the "systemctl"
  calls, these are recommended when processing the output
  by scripts (bsc#1176714)
- 4.3.29
* Mon Sep 21 2020 Ladislav Slezák <lslezak@suse.cz>
- Decrease error logging to avoid false positives in the y2log
  (bsc#1176653)
- 4.3.28
* Wed Sep 16 2020 José Iván López González <jlopez@suse.com>
- Hide heading of the dialog when no title is defined or title is
  set to an empty string.
- Related to bsc#1175489.
- 4.3.27
* Tue Sep 15 2020 Ladislav Slezák <lslezak@suse.cz>
- Clear the download progres for the previous file when displaying
  an error popup (bsc#1175926)
- Enable additional callback logging when $Y2DEBUG_CALLBACKS is
  set to "1"
- 4.3.26
* Thu Sep 10 2020 Josef Reidinger <jreidinger@suse.com>
- Enhance GPG module with symmetric encryption
  (related to bsc#1176336)
- add new shared password dialog
- 4.3.25
* Thu Aug 27 2020 Ladislav Slezák <lslezak@suse.cz>
- Fixed accidentaly broken dependencies (related to bsc#1175317)
- 4.3.24
* Thu Aug 27 2020 Ladislav Slezák <lslezak@suse.cz>
- Yet another unit test architecture fix :-(
  (related to bsc#1175317)
- 4.3.23
* Thu Aug 27 2020 Ladislav Slezák <lslezak@suse.cz>
- Fix for the previous change: fixed unit test failure on non
  x86_64 archs (related to bsc#1175317)
- 4.3.22
* Wed Aug 26 2020 Ladislav Slezák <lslezak@suse.cz>
- Y2Packager::Resolvable.find(): improved error handling,
  added more unit tests (related to bsc#1175317)
- 4.3.21
* Tue Aug 25 2020 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Unify profile element paths (bsc#1175680).
- 4.3.20
* Tue Jul 28 2020 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- XML: do not export the system ID if it is not defined
  (boo#1174424).
- 4.3.19
* Tue Jul 28 2020 Josef Reidinger <jreidinger@suse.com>
- Handle exceptions when parsing xml file (related to bsc#1170886)
- 4.3.18
* Fri Jul 24 2020 Knut Anderssen <kanderssen@suse.com>
- Provide a way to determine which resources (zones, services...)
  have been modified from the default values (bsc#1171356)
- 4.3.17
* Fri Jul 24 2020 Jeff Kowalczyk <jkowalczyk@suse.com>
- update is_wsl function to match wsl1 and wsl2 osrelease spellings
  (boo#1174183)
* Thu Jul 23 2020 José Iván López González <jlopez@suse.com>
- Add Layout class to configure a Wizard layout.
- Related to jsc#PM-1998.
- 4.3.16
* Thu Jul 16 2020 Ancor Gonzalez Sosa <ancor@suse.com>
- Better management of libzypp repovars (eg. those enclosed in
  curly brackets) introducing the new Y2Packager::ZyppUrl class
- Do not crash during the upgrade process if some repository URL
  cannot be parsed (bsc#1172867)
- 4.3.15
* Fri Jul 10 2020 David Diaz <dgonzalez@suse.com>
- Make CFA::MultiFileConfig fully reusable (related to bsc#1155735,
  and bsc#1157541).
* Thu Jul  9 2020 Steffen Winterfeldt <snwint@suse.com>
- add space to SPACE_CHARS (bsc#1173907)
- 4.3.14
* Tue Jul  7 2020 schubi@suse.de
- Command line interface: Do not start an UI while evaluating
  current language settings (bsc#1173133).
- 4.3.13
* Mon Jun 29 2020 schubi@suse.de
- Products: Do not solve dependencies while checking libzypp
  connection (bsc#1170322).
- 4.3.12
* Mon Jun 29 2020 José Iván López González <jlopez@suse.com>
- Avoid failure when downloading release notes from an inoperative
  proxy (bsc#1173447).
- 4.3.11
* Fri Jun 26 2020 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- AutoClient#export method can receive a hash as an argument
  (bsc#1171356).
- 4.3.10
* Sun Jun 21 2020 Knut Anderssen <kandersen@suse.com>
- Add a method to change the selection of the network backend to be
  used (related to bsc#1172749)
- 4.3.9
* Thu Jun 18 2020 Ladislav Slezák <lslezak@suse.cz>
- Updated Yast::XML.validate arguments
- Distinguish between a String argument (containing a XML
  document/schema) and Pathname (path to a file)
- Related to bsc#1170886
- 4.3.8
* Tue Jun 16 2020 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Add a method to determine the default start mode for a system
  service (related to bsc#1172749).
- 4.3.7
* Tue Jun  9 2020 David Diaz <dgonzalez@suse.com>
- Fix Xen detection (bsc#1172742).
- 4.3.6
* Fri Jun  5 2020 José Iván López González <jlopez@suse.com>
- Improve actions to stop and start a system service.
- Related to bsc#1162514.
- 4.3.5
* Thu Jun  4 2020 Josef Reidinger <jreidinger@suse.com>
- Drop anyxml agent to unify used xml parsers. All usage replaced
  by rubygem-nokogiri
  (related to bsc#1170886)
- 4.3.4
* Mon Jun  1 2020 Ladislav Slezák <lslezak@suse.cz>
- Improved XML validation, raise exception for not well formed
  documents (related to bsc#1170886)
- 4.3.3
* Fri May 29 2020 schubi@suse.de
- autoinst_issues/list.add : Fixed documentation.
  (bsc#1171335).
* Mon May 18 2020 schubi@suse.de
- autoinst_issues/list.add : Changed first parameter from tag to
  classes (bsc#1171335).
- Added general AY issue classes: InvalidValue, MissingValue
- 4.3.2
* Mon May 18 2020 Ladislav Slezák <lslezak@suse.cz>
- Restore back the perl-XML-Simple dependency, it is needed for
  ag_anyxml (related to bsc#1170886)
- 4.3.1
* Thu May 14 2020 Josef Reidinger <jreidinger@suse.com>
- Re-implement XML parser (bsc#1170886):
-- use as backend nokogiri instead of hand written libxml2 wrapper
-- Use exceptions instead of silently ignoring issues
-- export map as type to xml
-- add new method #validate to validate against relax-ng schema
- 4.3.0
* Wed May  6 2020 schubi@suse.de
- AutoYaST: Cleanup/improve issue handling (bsc#1171335).
- 4.2.84
* Fri Apr 24 2020 Knut Anderssen <kanderssen@suse.com>
- Avoid using systemctl calls when already started with the
  installation and thus, running inside the chroot (bsc#1168849)
- 4.2.83
* Mon Apr 13 2020 Knut Anderssen <kanderssen@suse.com>
- Remove ip aliases that were marked to be deleted from the
  interface configuration files (bsc#1146020)
- 4.2.82
* Tue Apr  7 2020 Stefan Hundhammer <shundhammer@suse.com>
- Retranslate wizard help button in NCurses UI (bsc#1167224)
- 4.2.81
* Fri Apr  3 2020 Knut Anderssen <kanderssen@suse.com>
- Modify the way YaST detects whether systemd is running or not
  (bsc#1168307)
- 4.2.80
* Fri Mar 27 2020 Knut Anderssen <kanderssen@suse.com>
- Reread network interfaces configuration after writing it avoiding
  wrong values when reopen network configuration dialog during an
  installation (bsc#1166778)
- 4.2.79
* Thu Mar 26 2020 David Diaz <dgonzalez@suse.com>
- Remove no longer needed multi status selector since it
  does not work as expected (bsc#1167523).
- 4.2.78
* Tue Mar 24 2020 Ladislav Slezák <lslezak@suse.cz>
- Fixed alignment in the multi selection CWM widget
  (part of bsc#1167523)
- 4.2.77
* Mon Mar 23 2020 Josef Reidinger <jreidinger@suse.com>
- Add Popup#SuppressFeedback to allow to hide feedback for certain
  actions (needed for bsc#1165705)
- 4.2.76
* Sat Mar 21 2020 Knut Anderssen <kanderssen@suse.com>
- Force a reset of the firewalld API instance before reading the
  firewalld configuration (bsc#1166698)
- 4.2.75
* Tue Mar 17 2020 Ladislav Slezák <lslezak@suse.cz>
- Fixed CWM::MultiStatusSelector help text icons displayed during
  installation (related to bsc#1157780, bsc#1161308, bsc#1161200)
- 4.2.74
* Fri Mar 13 2020 David Diaz <dgonzalez@suse.com>
- CWM::MultiStatusSelector minor improvements (related to
  bsc#1157780).
- 4.2.73
* Thu Mar 12 2020 David Diaz <dgonzalez@suse.com>
- Add the new CWM::MultiStatusSelector custom widget (related to
  bsc#1157780, bsc#1161308, bsc#1161200).
- 4.2.72
* Thu Mar 12 2020 Ladislav Slezák <lslezak@suse.cz>
- Do not remove the installation repositories in the "Previously
  Used Repositories" step (bsc#1163081)
- 4.2.71
* Fri Mar  6 2020 David Diaz <dgonzalez@suse.com>
- Allow to restore the vertical scroll of a CWM::RichText
  (related to bsc#1049965)
- 4.2.70
* Fri Mar  6 2020 David Diaz <dgonzalez@suse.com>
- Read the list of network service properly, no matter where
  it is stored (bsc#1162853).
- 4.2.69
* Fri Mar  6 2020 Ladislav Slezák <lslezak@suse.cz>
- Skip repository reloading at installation to avoid unselecting
  products to install (bsc#1165501)
- 4.2.68
* Wed Feb 26 2020 schubi@suse.de
- Updated docu for SysctlConfig class (bsc#1151649).
* Mon Feb 24 2020 schubi@suse.de
- Creating an own Augeas instance for each parsed sysctl file
  (bsc#1151649).
- 4.2.67
* Mon Feb 17 2020 schubi@suse.de
- SysctlConfig class: Handle sysctl entries in different
  directories (bsc#1151649).
- 4.2.66
* Mon Feb 17 2020 Stefan Hundhammer <shundhammer@suse.com>
- Fixed user-visible messages (bsc#1084015)
- 4.2.65
* Tue Feb  4 2020 Josef Reidinger <jreidinger@suse.com>
- Show on WSL only WSL capable modules in control center
  (bsc#1162650)
- 4.2.64
* Fri Jan 31 2020 José Iván López González <jlopez@suse.com>
- Add new widgets CWM::ProgressBar and CWM::DynamicProgressBar.
- Needed for bsc#1135366.
- 4.2.63
* Thu Jan 30 2020 Ladislav Slezák <lslezak@suse.cz>
- Do not crash when the "software/base_products" is not defined
  in the control.xml (bsc#1161956)
- 4.2.62
* Wed Jan 29 2020 Josef Reidinger <jreidinger@suse.com>
- Speed up run on WSL (bsc#1157575)
- 4.2.61
* Tue Jan 28 2020 Ladislav Slezák <lslezak@suse.cz>
- Added classes for handling the old repository setup during
  upgrade (related to bsc#1159433)
- 4.2.60
* Thu Jan 23 2020 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Add an option to enable the online search in the package
  selector (jsc#SLE-9109).
- 4.2.59
* Thu Jan 23 2020 Steffen Winterfeldt <snwint@suse.com>
- don't use /bin/systemd compat symlink (bsc#1160890)
- 4.2.58
* Wed Jan 22 2020 Josef Reidinger <jreidinger@suse.com>
- CommandLine: Add ability to actions to skip writing.
  Useful for more CLI bug fixes e.g. bsc#1160928
- 4.2.57
* Wed Jan 22 2020 schubi@suse.de
- Evaluating system release/version in an more understandable form
  for the user e.g. "15-SP2" (improvement for fate#325834).
- 4.2.56
* Tue Jan 14 2020 David Diaz <dgonzalez@suse.com>
- Add a text helper to strip HTML tags (related bsc#1157780)
- Moves text helpers to String refinements, keeping backward
  compatibility.
- 4.2.55
* Fri Jan 10 2020 schubi@suse.de
- Do not refresh package installation overview if the medium has
  been changed and the user has switched to the release notes tab.
  (bsc#1129426, bsc#1159367)
- 4.2.54
* Fri Jan 10 2020 Ancor Gonzalez Sosa <ancor@suse.com>
- Fixed error during upgrade if Btrfs is used and '/var/lib/YaST2'
  is missing (bsc#1159562)
- 4.2.53
* Fri Jan 10 2020 Martin Vidner <mvidner@suse.com>
- Propagate an error status when a CommandLine module gets an
  unknown command (related to bsc#1144351).
- 4.2.52
* Wed Jan  8 2020 Ancor Gonzalez Sosa <ancor@suse.com>
- Fix an exception in the live installation caused by a missing
  "require" clause (bsc#1160362).
- 4.2.51
* Mon Jan  6 2020 Ladislav Slezák <lslezak@suse.cz>
- Persian is also an RTL language (related to bsc#1156437)
- 4.2.50
* Thu Dec 19 2019 Knut Anderssen <kanderssen@suse.com>
- Yast2::ServiceWidget: By default, propose to reload or restart
  the service when it is active (bsc#1158946)
- 4.2.49
* Thu Dec 19 2019 aschnell@suse.com
- Added helper to create UI sort-key term (bsc#1140018)
- 4.2.48
* Wed Dec  4 2019 Josef Reidinger <jreidinger@suse.com>
- Add backward compatible hash accessors to Resolvable which solve
  several crashes (related to bsc#1132650 and bsc#1140037)
- 4.2.47
* Mon Dec  2 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Use 70-yast.conf instead of 30-yast.conf to write YaST settings
  under /etc/sysctl.d (related to jsc#SLE-9077).
- 4.2.46
* Fri Nov 29 2019 schubi@suse.de
- Do not crash while reading the product info (related to
  bsc#1132650 and bsc#1140037).
- 4.2.45
* Thu Nov 28 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Do not crash when no base product is found (related to
  bsc#1132650 and bsc#1140037).
- 4.2.44
* Thu Nov 28 2019 schubi@suse.de
- Using Y2Packager::Resolvable.any? and Y2Packager::Resolvable.find
  in order to decrease the required memory (bsc#1132650,
  bsc#1140037).
- 4.2.43
* Thu Nov 28 2019 Knut Anderssen <kanderssen@suse.com>
- Network: drop support for obsolete network device types
  (jsc#SLE-7753)
- 4.2.42
* Wed Nov 27 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Use /etc/login.defs.d/70-yast.defs to write login.defs
  values that are overridden by YaST (related to bsc#1155735).
- 4.2.41
* Tue Nov 26 2019 Ludwig Nussel <lnussel@suse.de>
- add is_wsl function to detect wsl (boo#1154962)
- 4.2.40
* Mon Nov 25 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- bsc#1155735, bsc#1157541:
  - Read /usr/etc/login.defs.
  - Write login.defs configuration to /etc/login.defs.d/.
- 4.2.39
* Fri Nov 22 2019 Michal Filka <mfilka@suse.com>
- bnc#1157532
  - do not modify /etc/sysctl.conf in inst-sys as it is on r/o
    filesystem
- 4.2.38
* Thu Nov 21 2019 Knut Anderssen <kanderssen@suse.com>
- Linuxrc: Ensure the new opened SCR instace is closed when reading
  the /etc/install.inf file (bsc#1122493, bsc#1157476)
- 4.2.37
* Thu Nov 21 2019 Knut Anderssen <kanderssen@suse.com>
- Ensure /etc/install.inf is not read from the target system but
  from the local one. (bsc#1122493, bsc#1157476)
- 4.2.36
* Wed Nov 20 2019 David Diaz <dgonzalez@suse.com>
- Do not try to find licenses in the installation medium when they
  have been already downloaded from SCC (bsc#1153326).
- 4.2.35
* Fri Nov 15 2019 Josef Reidinger <jreidinger@suse.com>
- Fix crash in upgrade caused by wrong parameter to snapper
  (bsc#1156819)
- 4.2.34
* Tue Nov  5 2019 José Iván López González <jlopez@suse.com>
- Use new snapper machine-readable output to retrieve snapshots
  information (related to bsc#1149322).
- 4.2.33
* Tue Nov  5 2019 Oliver Kurz <okurz@suse.com>
- Add linuxrc option "reboot_timeout" to configure the timeout
  before reboot (bsc#1122493)
- 4.2.32
* Thu Oct 31 2019 Knut Anderssen <kanderssen@suse.com>
- Network: During an installation, check which backend is in use
  when Systemd is running. (bsc#1151291)
- 4.2.31
* Tue Oct 29 2019 Josef Reidinger <jreidinger@suse.com>
- fix showing release notes for online upgrade (bsc#1155134)
- 4.2.30
* Fri Oct 25 2019 Josef Reidinger <jreidinger@suse.com>
- Support for products on control file during upgrade
  (jsc#SLE-7214)
- 4.2.29
* Fri Oct 18 2019 Josef Reidinger <jreidinger@suse.com>
- Fix showing details for accessing media error (bsc#1153297)
- 4.2.28
* Wed Oct  9 2019 Ladislav Slezák <lslezak@suse.cz>
- Fixed evaluating the available package versions, fixed crash
  when trying to download a non-existing package (bsc#1151824)
- 4.2.27
* Mon Oct  7 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Remove old values from /etc/sysctl.conf (jsc#SLE-9077).
- 4.2.26
* Thu Oct  3 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Add a CFA based class to adjust sysctl settings (jsc#SLE-9077).
- 4.2.25
* Wed Sep 25 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Fix module name inference when reading .desktop files
  (bsc#1151954)
- 4.2.24
* Mon Sep 23 2019 Ladislav Slezák <lslezak@suse.cz>
- Use "display_name" tag for the product label, "label" marks a
  translatable text (jsc#SLE-7214)
- 4.2.23
* Thu Sep 19 2019 Ladislav Slezák <lslezak@suse.cz>
- Added support for reading products from control.xml file
  (jsc#SLE-7104)
- 4.2.22
* Tue Sep 10 2019 Steffen Winterfeldt <snwint@suse.com>
- support reading licenses from tar archive (jsc#SLE-7214)
- 4.2.21
* Fri Sep  6 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Fix a problem when long warnings reports in command line
  (bsc#1149776).
- 4.2.20
* Fri Aug 30 2019 Steffen Winterfeldt <snwint@suse.com>
- yast completions have to be named after their respective command
  name (bsc#1122259)
- 4.2.19
* Thu Aug  8 2019 Martin Vidner <mvidner@suse.com>
- Remove the obsolete XVersion API (bsc#1144627).
- Detect missing textdomain during testing (bsc#1130822)
- 4.2.18
* Mon Aug  5 2019 David Diaz <dgonzalez@suse.com>
- Allow to know if there is a forced base product
  (bsc#1124590, bsc#1143943).
- 4.2.17
* Wed Jul 31 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Add a dependency on hostname, as it is needed by the Hostname
  module (boo#1142595).
- 4.2.16
* Mon Jul 29 2019 Martin Vidner <mvidner@suse.com>
- Stop "ls: write error: Broken pipe" messages (bsc#1128032)
- 4.2.15
* Thu Jul 25 2019 Ladislav Slezák <lslezak@suse.cz>
- Release the sources to avoid using up all server connections
  (bsc#1141127)
- 4.2.14
* Tue Jul 23 2019 Ladislav Slezák <lslezak@suse.cz>
- Fixed evaluating the base products to avoid the "No base product
  found" error message at upgrade, for reading the product data
  prefer the new products (bsc#1142522)
- 4.2.13
* Tue Jul  9 2019 Josef Reidinger <jreidinger@suse.com>
- fixed symlink creation in jenkins
* Wed Jul  3 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Infer the right module name from desktop files (bsc#1140233).
- 4.2.12
* Mon Jul  1 2019 Knut Anderssen <kanderssen@suse.com>
- bsc#1138668
  - Fixed failing old testsuite in yast2-dns-server package: do not
    depend on the environment, skip bind absence in Mode.test()
- 4.2.11
* Fri Jun 21 2019 Josef Reidinger <jreidinger@suse.com>
- deprecate Arch.ia64 and drop all support for ia64 (last seen in
  SLE 11)
* Thu Jun 20 2019 Knut Anderssen <kanderssen@suse.com>
- bsc#1137992
  - PackageSystem.Installed: Fixed typo when passing the allowed
    return codes to Execute.
- 4.2.10
* Wed Jun 19 2019 Knut Anderssen <kanderssen@suse.com>
- bsc#1137992
  - PackageSystem.Installed: Use Yast::Execute instead of SCR
    to avoid false positives.
- 4.2.9
* Tue Jun 18 2019 schubi@suse.de
- Slideshow: Flag for switching on/off release notes tab.
  (bsc#1136708)
- 4.2.8
* Thu Jun 13 2019 Knut Anderssen <kanderssen@suse.com>
- bsc#1137992
  - PackageSystem.Installed: Increase the logs details.
- 4.2.7
* Wed Jun  5 2019 Knut Anderssen <kanderssen@suse.de>
- bsc#1086454
  - Recognize IB interfaces based on IPOIB_MODE ifcfg attribute
- 4.2.6
* Fri May 31 2019 Stasiek Michalski <hellcp@mailbox.org>
- Use new schema of desktop files (boo#1084864)
- Clean up spec
- Rename desktop files
- 4.2.5
* Thu May 30 2019 Josef Reidinger <jreidinger@suse.com>
- Drop old testsuite
- Convert from autotools to rake based installation
* Fri May 17 2019 aschnell@suse.com
- create log directory with control.xml and merged installation.xml
- 4.2.4
* Thu May 16 2019 Stefan Hundhammer <shundhammer@suse.com>
- Make sure the wizard buttons always remain visible in NCurses
  (bsc#1133367)
- 4.2.3
* Tue May  7 2019 Steffen Winterfeldt <snwint@suse.com>
- give more verbose feedback in 'view_anymsg' client (bsc#1132658)
- 4.2.2
* Fri Apr 26 2019 Ladislav Slezák <lslezak@suse.cz>
- Uninstall the "SUSE-Manager-Proxy" product when upgrading from
  SLES12 + SUMA Proxy + SUMA Branch Server (bsc#1133215)
- 4.2.1
* Wed Apr 17 2019 Rodion Iafarov <riafarov@suse.com>
- Allow not prescribing UI in yast2, to use YUILoader::loadUI.
  Required to load integration tests framework
  (poo#36712, bsc#1132247)
- 4.2.0
* Tue Apr  9 2019 schubi@suse.de
- Updated map for evaluating upgraded products
  (e.g. for SUSE-Manager). (bsc#1131503)
- Upgrade: Evaluating product obsoletes in order to show it in
  the proposal overview.
- 4.1.68
* Tue Apr  9 2019 Jan Engelhardt <jengelh@inai.de>
- Use noun phrase in summary.
* Tue Mar 26 2019 kanderssen@suse.com
- Firewall: Zone name has been removed from the common attributes
  declaration as it cannot be modified through the firewalld API.
  (bsc#1130354)
- 4.1.67
* Tue Mar 19 2019 David Díaz <dgonzalez@suse.com>
- Require tar as a dependency for yast2-logs (bsc#1125142).
- 4.1.66
* Thu Mar 14 2019 Ladislav Slezak <lslezak@suse.cz>
- Fixed evaluating the base product, the same products with
  the available and selected status must be treated as duplicate
  products (bsc#1129257)
- 4.1.65
* Wed Mar 13 2019 Ladislav Slezak <lslezak@suse.cz>
- Process the "specialproduct" value like a linuxrc parameter
  (ignore "-_." characters, ignore case) (bsc#1128901)
- 4.1.64
* Wed Mar 13 2019 David Díaz <dgonzalez@suse.com>
- Fix how a product features is read in a running system.
- Update default path for base product licenses
  (fate#324053, jsc#SLE-4173).
- 4.1.63
* Tue Mar 12 2019 lslezak@suse.cz
- Fixed product filtering in product_reader.rb, fixes problem
  when upgrading SLE15-SP1 to SLE15-SP1 (usually used to fix
  a broken system) (bsc#1128459)
- 4.1.62
* Fri Mar  8 2019 Michal Filka <mfilka@suse.com>
- bnc#1127798
  - do not crash with internal error when enabling a network
    network service when no network service is active.
- 4.1.61
* Wed Mar  6 2019 aschnell@suse.com
- added "Modify" button label (related to bsc#1128279, or just as
  good gh#yast/yast-yast2#713)
- 4.1.60
* Tue Mar  5 2019 Ladislav Slezák <lslezak@suse.cz>
- Added command line support also for the other Report module
  methods (related to bnc#1127685)
- 4.1.59
* Tue Mar  5 2019 Ladislav Slezák <lslezak@suse.cz>
- Fixed a failing testsuite, the Report.LongError used in the
  global exception handler did not support the command line mode
  (related to bnc#1127685)
- 4.1.58
* Mon Mar  4 2019 Michal Filka <mfilka@suse.com>
- bnc#1127685
  - made Report module long message reporting popups adjustable
- 4.1.57
* Wed Feb 27 2019 mvidner@suse.com
- Use /sbin/rpcinfo only, /usr/sbin/rpcinfo is gone (bsc#1127138).
- Use the correct path for /usr/bin/ifconfig (bsc#1127138).
- 4.1.56
* Mon Feb 18 2019 lslezak@suse.cz
- Fixed license file ordering issue causing a random test failure
  (bsc#1125722)
- 4.1.55
* Thu Feb  7 2019 knut.anderssen@suse.com
- Firewall: added some help methods for moving interfaces between
  zones in a safe way (fate#324662).
- 4.1.54
* Thu Jan 17 2019 knut.anderssen@suse.com
- CWM: Added date field and time field widgets (fate#322722)
- 4.1.53
* Wed Jan 16 2019 schubi@suse.de
- Support special products which will be enabled via linuxrc
  (flag "specialproduct") (fate#327099)
- 4.1.52
* Wed Jan 16 2019 jreidinger@suse.com
- Firewall: drop not needed relations and its related methods
- Firewall: move export method to yast2-firewall (fate#324662)
- 4.1.51
* Mon Jan 14 2019 Josef Reidinger <jreidinger@suse.com>
- CWM: Add method focus to object CWM widgets (FATE#324662)
- CWM: Add rspec helper for common CWM widgets
- CWM: Allow CWM dialogs/popups to have own help
- CWM: Fix showing help for CWM Popup (FATE#324662)
- 4.1.50
* Thu Jan 10 2019 Josef Reidinger <jreidinger@suse.com>
- Fix crashes of many modules when invoking from ncurses control
  center (bsc#1121425)
- 4.1.49
* Mon Jan  7 2019 lslezak@suse.cz
- Ignore the old packages when fetching the release notes
  (bsc#1112866)
- 4.1.48
* Thu Jan  3 2019 dgonzalez@suse.com
- Fix a fragile unit test (related to changes introduced
  for fate#325482)
- 4.1.47
* Thu Jan  3 2019 dgonzalez@suse.com
- Fetch and display properly the license content from the
  fallback rpm when using a product definition located at
  /usr/share/installation-products (part of fate#325482)
- 4.1.46
* Wed Jan  2 2019 jreidinger@suse.com
- Drop no longer used ALog module without replacement
- Drop no longer used Cron module without replacement
- Drop obsolete DebugHooks module for installation. Replaced by
  integrated installation debugger and installation hooks.
- Drop no longer used SuSEFirewallExpertRules module. Replaced by
  firewalld related classes.
- replace old testsuite for Wizard module by rspec tests
- Drop no longer installed desktop files for remotechooser and
  remoteinstall from git.
- Drop obsolete ycp syntax checker check-all-syntax without
  replacement.
* Fri Dec 28 2018 dgonzalez@suse.com
- Add missing help for the service configuration
* Wed Dec 19 2018 jreidinger@suse.com
- NetworkService: fix invoking forced enable (bsc#1119657)
- 4.1.45
* Tue Dec 18 2018 igonzalezsosa@suse.com
- Add a <configuration_management/> section to the control file
  (fate#322722).
- 4.1.44
* Tue Dec 18 2018 aschnell@suse.com
- avoid use of shellescape function on non string types
  (bsc#1119678)
- 4.1.43
* Mon Dec 17 2018 jlopez@suse.com
- Extend Yast::Execute API (needed for bsc#1118291)
- Add method Yast::Execute.stdout
- Allow to chain methods
- 4.1.42
* Mon Dec 17 2018 Ancor Gonzalez Sosa <ancor@suse.com>
- WorkflowManager: find product definitions located at
  /usr/share/installation-products/ (part of fate#325482)
- 4.1.41
* Wed Dec 12 2018 schubi@suse.de
- Added more testcases if e.g. system is running in chroot
  environment and systemd does not work properly (bsc#1113732)
* Wed Dec 12 2018 Stefan Hundhammer <shundhammer@suse.com>
- Removed dead code (bsc#1118291)
- 4.1.40
* Thu Dec  6 2018 Josef Reidinger <jreidinger@suse.com>
- always use absolute path to binaries (bsc#1118291)
- properly escape shell arguments (bsc#1118291)
- 4.1.39
* Wed Dec  5 2018 Stasiek Michalski <hellcp@mailbox.org>
- Ship only primary icons with module to avoid conflicts (boo#1118521)
- 4.1.38
* Fri Nov 30 2018 jreidinger@suse.com
- firewalld: add ability to add/edit/remove zones (fate#324662)
- 4.1.37
* Mon Nov 26 2018 Noah Davis <noahadvs@gmail.com>
- Provide icon with module (boo#1109310)
- Move virtualization group from yast-vm to yast2
- 4.1.36
* Wed Nov 21 2018 Stefan Hundhammer <shundhammer@suse.com>
- Added global parameter enable_local_users (Fate#326447)
- Added ProductFeatures::GetBooleanFeatureWithFallback
- 4.1.35
* Fri Nov 16 2018 aschnell@suse.com
- check return value of OpenDialog to prevent crash (bsc#1115745)
- 4.1.34
* Tue Nov  6 2018 jreidinger@suse.com
- WorkflowManager: Allow system roles to live in
  /usr/share/system-roles/*.xml (bsc#1108176)
- 4.1.33
* Fri Oct 26 2018 jreidinger@suse.com
- view_anymsg: allow user to switch to yast2-journal if file does
  not exist or is empty (bsc#948729)
- 4.1.32
* Wed Oct 24 2018 schubi@suse.de
- Added flag save_y2logs to control.xml file in order to save
  YaST logs at the end of installation (fate#325737)
- 4.1.31
* Wed Oct 24 2018 jreidinger@suse.com
- Ensure that Installation.sourcedir exists (bsc#1097700)
- Use LSB compliant Installation.sourcedir
- 4.1.30
* Wed Oct 24 2018 knut.anderssen@suse.com
- CWMFirewallInterfaces: make some "current state" methods public
  needed by yast2-rmt (fate#326634)
- 4.1.29
* Tue Oct 23 2018 knut.anderssen@suse.com
- Network (Firewall): Added modify_masquerade method to zones API
  unifying the way changes are applied to single value attributes.
  (bsc#1112547)
- 4.1.28
* Thu Oct 18 2018 aschnell@suse.com
- adapted to extended output of snapper (fate#326479, bsc#1111831)
- 4.1.27
* Thu Oct 18 2018 mvidner@suse.com
- Small CWM optimization by avoiding deep_copy on big data
  (bsc#1112402).
- 4.1.26
* Wed Oct 17 2018 knut.anderssen@suse.com
- CWMFirewallInterfaces: Improved the user UX replacing the api
  calls for checking supported services once the list supported
  ones are already known by the firewalld instance (fate#324662)
- 4.1.25
* Mon Oct 15 2018 schubi@suse.de
- Splitting yast2 package into yast2 and yast2-logs. yast2-logs
  contains only scripts for handling YaST logs (fate#325737).
- 4.1.24
* Fri Oct 12 2018 schubi@suse.de
- Added tags full_system_media_name and full_system_download_url
  in control.xml which describe the location for the
  "all-packages" medium. This information will be shown if the
  registration has been scipped by the user. No hint will be shown
  if these tags have not been defined. (fate#325834)
- 4.1.23
* Tue Oct  9 2018 schubi@suse.de
- Added new methods to firewalld_wrapper in order to switch
  yast2-dhcp-server to new firewall module. (bsc#1108942)
- 4.1.22
* Tue Oct  9 2018 lslezak@suse.cz
- Log viewer: replace invalid UTF-8 characters from the displayed
  log to avoid a crash (bsc#1110549)
- 4.1.21
* Wed Oct  3 2018 knut.anderssen@suse.com
- Network (Firewall):
  - Added some methods needed for AutoYaST configuration
  (fate#324662)
* Tue Oct  2 2018 lslezak@suse.cz
- Make the service status label stretchable so the updated status
  is displayed correctly (bsc#1110407)
- 4.1.20
* Mon Oct  1 2018 mfilka@suse.com
- bnc#964856
  - fixed internal error - do not crash when updating device config
- 4.1.19
* Fri Sep 28 2018 knut.anderssen@suse.com
- Y2Firewall::Firewalld: Single attributes setter will not modify
  the value of the attribute in case it is the same (bsc#1109812)
- 4.1.18
* Wed Sep 19 2018 igonzalezsosa@suse.com
- Improve Y2Firewall::Firewalld::Interface#zone to return an
  Zone object (fate#324662).
- 4.1.17
* Wed Sep 19 2018 mfilka@suse.com
- bnc#964856
  - removed obsolete parts of NetworkInterfaces API:
    ifcfg_part, device_type, device_num, alias_num,
    GetFreeDevices, GetFreeDevice, LocateNOT, ListDevicesExcept
- 4.1.16
* Wed Sep 19 2018 knut.anderssen@suse.com
- Network (Firewall)
  - Added Y2Firewall::Firewalld::Interface class.
  - Adapted interfaces helpers to work with the new class.
  (fate#324662)
- 4.1.15
* Wed Sep 19 2018 igonzalezsosa@suse.com
- Add a new popup widget (fate#324662).
- Add a helper class UIState to keep the UI states when using CWM.
* Tue Sep 18 2018 knut.anderssen@suse.com
- Y2Firewall::Firewalld: Added convenience method to obtain the
  firewalld service object (fate#324662)
- 4.1.14
* Mon Sep 17 2018 lslezak@suse.cz
- Allow reading the installation.xml (skelcd-* package) from other
  repository than the initial one (e.g. the self update), select
  the highest version of the package (instead of the first found)
  (bsc#1101016)
- 4.1.13
* Mon Sep 17 2018 knut.anderssen@suse.com
- Firewalld: Fixed the API cmd call for removing services from
  zones when the firewall is in offline mode (bsc#1108628)
- 4.1.12
* Wed Sep 12 2018 jlopez@suse.com
- CWM: avoid to always return :next when accepting a dialog.
- Needed for Expert Partitioner (fate#318196).
- 4.1.11
* Wed Sep 12 2018 knut.anderssen@suse.com
- Added the missing SuSEFirewallProposal.rb file to the Makefile
  (bsc#1087867)
- 4.1.10
* Wed Sep 12 2018 knut.anderssen@suse.com
- Bring back the SuSEFirewallProposal fixing the class unit tests
  until yast2-network drops the import of the module completely.
  (bsc#1087867)
- 4.1.9
* Mon Sep 10 2018 knut.anderssen@suse.com
- Extended the firewall API supporting the use of single-value
  attributes and also prepared it for introducing  more complex
  relations like 'forward-ports' and 'rich-rules' in the future.
  (fate#324662)
- Improved the parser for zones and added a parser for services.
- Improved test mocking fixing a Polkit popup shown when running the
  test (bsc#1087867)
- 4.1.8
* Wed Sep  5 2018 jlopez@suse.com
- CWM: allow to define next handler for CWM#show.
- CWM: define default next handler in CWM::Dialog.
- Needed for Expert Partitioner (fate#318196).
- 4.1.7
* Thu Aug 30 2018 igonzalezsosa@suse.com
- Add missing CompoundService#support_start_on_boot?
  (bsc#1106591).
- 4.1.6
* Thu Aug 30 2018 dgonzalez@suse.com
- Increase timeout for the execution of systemctl commands
  (bsc#1098910).
- 4.1.5
* Fri Aug 24 2018 igonzalezsosa@suse.com
- Fix the Yast2::ServiceWidget to not show the "On Boot" option
  when it is not supported (related to fate#319428).
- 4.1.4
* Tue Aug 21 2018 dgonzalez@suse.com
- Refactor systemd classes, reorganizing them in real classes
  under the Yast2::Systemd namespace instead of using modules
  (related to fate#319428).
- 4.1.3
* Mon Aug 20 2018 schubi@suse.de
- Changed dir of COPYING file
* Tue Aug 14 2018 igonzalezsosa@suse.com
- Add support for systemd services that can only be started
  on-demand (fate#319428 and bsc#1104568).
- 4.1.2
* Thu Aug  9 2018 igonzalezsosa@suse.com
- Improve systemd socket detection (related to fate#319428).
- SystemService#find_many does not raise an exception anymore.
- 4.1.1
* Wed Aug  8 2018 jlopez@suse.com
- Added widget to configure services (part of fate#319428).
- 4.1.0
* Wed Aug  8 2018 igonzalezsosa@suse.com
- Add a method to detect whether a systemd service exists in
  the underlying system or not (related to fate#319428).
- Fix systemd socket detection.
- 4.0.83
* Wed Aug  1 2018 igonzalezsosa@suse.com
- Fix support to handle services during early 1st stage
  (related to fate#319428).
- 4.0.82
* Tue Jul 31 2018 lslezak@suse.cz
- Do not display "download failed" error when using unsigned
  packages (bsc#1096027)
- 4.0.81
* Wed Jul 25 2018 jlopez@suse.com
- Services: add class to manage systemd services with associated
  socket (needed for bsc#1080738 and fate#319428).
- 4.0.80
* Mon Jul 16 2018 knut.anderssen@suse.com
- Replace the deprecated firewallctl command with firewall-cmd for
  obtaining the firewalld state (bsc#1093111)
* Tue Jul  3 2018 knut.anderssen@suse.com
- Network: Prevent from crashing when trying to delete some ip
  aliases from the original devices (bsc#1098919)
- 4.0.79
* Wed Jun 27 2018 schubi@suse.de
- Added additional searchkeys to desktop file (fate#321043).
- 4.0.78
* Wed Jun  6 2018 jsrain@suse.cz
- display proper release notes for product (bsc#1096138)
- 4.0.77
* Tue May 29 2018 jsrain@suse.cz
- rename SLES_HPC -> SLE_HPC (bsc#1095053)
- 4.0.76
* Wed May 23 2018 schubi@suse.de
- Calling YAST module: Do not create a post Snapper image if the
  pre Snapper image has already been failed (bnc#1093374)
- 4.0.75
* Mon May 14 2018 lslezak@suse.cz
- Support multiple "system-installation()" provides in one
  package (bsc#1092965)
- 4.0.74
* Tue May  8 2018 jlopez@suse.com
- CWM: allow to define back handler for CWM#show.
- CWM: define default handlers for back and abort in CWM::Dialog.
- Needed for Expert Partitioner fate#318196.
- 4.0.73
* Mon Apr 23 2018 igonzalezsosa@suse.com
- Add a text helper to wrap richtext in directional markers
  (bsc#1089846).
- 4.0.72
* Mon Apr 16 2018 igonzalezsosa@suse.com
- Do not crash when reading trying to determine available locales
  for some licenses (bsc#1089610).
- 4.0.71
* Mon Apr 16 2018 snwint@suse.de
- save_y2logs: save kernel messages and udev log (bsc#1089647,
  bsc#1085212)
- 4.0.70
* Thu Apr 12 2018 igonzalezsosa@suse.com
- Handle input/output errors in the DoneProvide package callback
  (bsc#1088682).
- 4.0.69
* Thu Apr 12 2018 knut.anderssen@suse.com
- Wizard: Fall back to smaller and/or hicolor icon if the icon for
  the launched module cannot be found (bsc#1087224)
- 4.0.68
* Tue Apr 10 2018 lslezak@suse.cz
- Do not use the solver for finding the best product upgrade
  candidate, it does not work correctly in the SLES + sle-module-hpc
  => SLES_HPC case (bsc#1086734)
- 4.0.67
* Tue Apr 10 2018 jreidinger@suse.com
- Fix early exit of installation when initial install url is
  invalid and later fixed (bsc#1086840)
- 4.0.66
* Fri Apr  6 2018 jreidinger@suse.com
- improve wayland support (bsc#1083907)
- 4.0.65
* Thu Apr  5 2018 igonzalezsosa@suse.com
- Use SHA2 instead of MD5 when determining whether a license
  was already accepted or not (related to fate#325461).
- 4.0.64
* Thu Apr  5 2018 knut.anderssen@suse.com
- Add a new API to handle product licenses.
- Given a license, remember whether another one with the same
  content was already accepted (fate#325461).
- 4.0.63
* Tue Apr  3 2018 lslezak@suse.cz
- Added ProductUpgrade class to better evaluate the product for
  upgrading (related to bsc#1086259)
- 4.0.62
* Tue Mar 27 2018 ancor@suse.com
- Make possible to use the Yast2::Popup class from the Report
  module (part of bsc#1082542).
- 4.0.61
* Fri Mar 23 2018 jreidinger@suse.com
- fix behavior of showing timed error popup (found during
  debugging bsc#1083672)
- 4.0.60
* Fri Mar  9 2018 jreidinger@suse.com
- Fix extracting kernel parameters from installation when there is
  parameter with '=' in value like
  pci=hpiosize=0,hpmemsize=0,nobar (bsc#1081353)
- 4.0.59
* Wed Mar  7 2018 igonzalezsosa@suse.com
- Use the correct release notes URL during upgrade (bsc#1073488).
- 4.0.58
* Wed Feb 28 2018 ancor@suse.com
- Fixed a typo and the list item marker in the firewall widget
  (bsc#1083058).
- 4.0.56
* Tue Feb 27 2018 schubi@suse.de
- NIS configuration fails while executing firewall-offline-cmd.
  Fix: Ensure that the firewalld configuration is read before
  writing. (bnc#1082827)
- 4.0.55
* Fri Feb 23 2018 knut.anderssen@suse.com
- Added missing textdomain to firewalld zone class for translations
  (bsc#1082246).
- 4.0.54
* Thu Feb 15 2018 lslezak@suse.cz
- Fixed list of the URL schemes without host, fixes processing
  URLs with the "hd:/" scheme (bsc#1077310)
- 4.0.53
* Wed Feb 14 2018 igonzalezsosa@suse.com
- Add a method to get the list of available license translations
  for a given product (related to FATE#322276).
- 4.0.52
* Mon Feb 12 2018 knut.anderssen@suse.com
- Firewalld: Added interfaces helpers (fate#323460)
- 4.0.51
* Thu Feb  8 2018 knut.anderssen@suse.com
- Drop (x)inetd agents
- CWMServiceStart: Replace xinetd by systemd socket activation
  (fate#323373)
- 4.0.50
* Fri Feb  2 2018 igonzalezsosa@suse.com
- Y2Packager::Product does not depend on Yast::Language module
  anymore (related to bsc#1079045)
- 4.0.49
* Thu Feb  1 2018 igonzalezsosa@suse.com
- Replace idnconv with simpleidn library (related to bsc#1071552).
- Move some Y2Packager classes from yast2-packager here to
  fix the package build.
- 4.0.48
* Thu Feb  1 2018 knut.anderssen@suse.com
- Firewalld: Cache modifications for performance improvements.
  (fate#323460)
- 4.0.47
* Thu Feb  1 2018 lslezak@suse.cz
- Move some Y2Packager classes from yast2-packager here to avoid
  circular dependency (related to fate#323163)
- 4.0.46
* Wed Jan 31 2018 knut.anderssen@suse.com
- Firewalld API: Cache whether the configuration has been read
  (fate#323460)
- 4.0.45
* Tue Jan 30 2018 knut.anderssen@suse.com
- Installation::AutoClient: modified packages default and improved
  documentation (fate#323460 bsc#1077987)
- 4.0.44
* Tue Jan 30 2018 ancor@suse.com
- Fixed a bug causing pages of all CWM::TreePager to be rendered
  twice on every page switch (bsc#1078212)
- 4.0.43
* Mon Jan 29 2018 knut.anderssen@suse.com
- Firewalld API: reload and complete reload return true in offline
  mode (fate#323460)
- 4.0.42
* Mon Jan 29 2018 knut.anderssen@suse.com
- Fixed logging typo (fate#1076513)
- 4.0.41
* Fri Jan 26 2018 lslezak@suse.cz
- Improved base product detection at upgrade (fate#1076513)
- 4.0.40
* Wed Jan 24 2018 knut.anderssen@suse.com
- Firewalld: Added methods to the wrapper class for opening ports
  by YaPI modules (fate#323460 bsc#1071548 bsc#1076837)
- 4.0.39
* Wed Jan 24 2018 jreidinger@suse.com
- CWM: Add possibility to define abort handler for CWM.show
  (needed for expert partitioner fate#318196)
- 4.0.38
* Tue Jan 23 2018 knut.anderssen@suse.com
- Firewalld: Added missing firewalld service file to the Makefile
  (fate#323460).
- 4.0.37
* Tue Jan 23 2018 knut.anderssen@suse.com
- CWMFirewallInterfaces: Replaced SuSEFirewall2 by firewalld.
  (fate#323460)
- 4.0.36
* Tue Jan 16 2018 jreidinger@suse.com
- fix having some roles without description when choosing
  different extensions during installation (bsc#1070726)
- 4.0.35
* Fri Jan 12 2018 schubi@suse.de
- Firewalld export: Return empty hash if the package has not
  been installed. (fate#323460)
- 4.0.34
* Wed Jan 10 2018 schubi@suse.de
- Adding a workflow from other products: If there are no modules
  have beed defined we are using the modules defined in
  append_modules. (bnc#1075182)
- 4.0.33
* Mon Jan  8 2018 knut.anderssen@suse.com
- Firewalld: Allow to modify default zone and export configuration
  (fate#323460).
- 4.0.32
* Mon Jan  8 2018 mfilka@suse.com
- bnc#1073727
  - ignored some of typical backup extensions (like .bak, .orig)
    when loading ifcfg files
- 4.0.31
* Wed Dec 20 2017 knut.anderssen@suse.com
- Firewalld: Extend handling of zones for AutoYaST configuration
  (fate#323460).
- 4.0.30
* Fri Dec 15 2017 knut.anderssen@suse.com
- Firewalld API: Use string command with all api methods which
  expect string outputs (bsc#1070559)
- 4.0.29
* Thu Dec 14 2017 knut.anderssen@suse.com
- Firewalld API: Added convenient methods for query commands and
  string expected output commands (bnc#1070559).
- 4.0.28
* Mon Dec 11 2017 schubi@suse.de
- Warn the user if the infrastructure is not available for running
  the second stage (bnc#1061754)
- 4.0.27
* Mon Dec 11 2017 jlopez@suse.com
- Improve tests for CWM::Pager (part of fate#318196).
- 4.0.26
* Fri Dec  8 2017 mvidner@suse.com
- Recognize CTC devices named like slc600 (bsc#1058227).
- Stopped treating old-style hotplug devices specially.
- 4.0.25
* Fri Dec  8 2017 lslezak@suse.cz
- save_y2logs: save also /linuxrc.config and /etc/os-release files
  for easier debugging
* Tue Dec  5 2017 jlopez@suse.com
- CWM: make method Pager#current_page public.
- Necessary for fate#318196.
- 4.0.24
* Mon Dec  4 2017 mfilka@suse.com
- bnc#1061306
  - provided new function for querying net device configuration to
    avoid internal errors when querying cached devices
    inconsistently
- 4.0.23
* Thu Nov 30 2017 rbrown@suse.com
- Replace references to /var/adm/fillup-templates with new
  %%_fillupdir macro (boo#1069468).
- 4.0.22
* Wed Nov 29 2017 knut.anderssen@suse.com
- Added missing y2firewall/firewalld/zone.rb file to the Makefile
  (fate#323460).
- 4.0.21
* Wed Nov 29 2017 ancor@suse.com
- Fixed a bug selecting rows programmatically for CWM::Table
  (bsc#1070287).
- 4.0.20
* Tue Nov 28 2017 jreidinger@suse.com
- Add new Yast2::Popup class providing nicer API for invoking
  popups (hackweek project)
- 4.0.19
* Tue Nov 28 2017 mfilka@suse.com
- bnc#956755, bnc#1061306 (mfilka)
  - fixed storing device information to avoid incorrect "not found"
    states when querying NetworkInterfaces subsequently
- 4.0.18
* Fri Nov 24 2017 knut.anderssen@suse.com
- Network:
  - Do not depent on SuSEFirewall to list the known zones anymore.
  - NetworkInterfaces: Remove ZONE attribute if it is empty when
    writing.
- 4.0.17
* Wed Nov 22 2017 knut.anderssen@suse.com
- Added RSpec shared example for CWM::CheckBox (bsc#1068354).
- 4.0.16
* Thu Nov 16 2017 knut.anderssen@suse.com
- SuSEFirewall: Export minimal firewalld configuration until the
  AY firewall schema is adapted (bsc#1067193)
- 4.0.15
* Thu Nov  9 2017 knut.anderssen@suse.com
- fate#323460
  - Firewalld API: added change_interface method
- 4.0.14
* Fri Nov  3 2017 knut.anderssen@suse.com
- Firewalld API: running? return false if the package is not
  installed (fate#323460)
- 4.0.13
* Thu Oct 26 2017 knut.anderssen@suse.com
- Network (Firewall):
  - Added support for firewalld offline command
  - Dropped SuSEFirewall (module) support for SuSEFirewall2 backend
  - Adapted some SuSEFirewalldClass methods to work properly during
    installation.
  - Skipped some tests to make it build properly (should be
    replaced by new ones with a new API design)
  (fate#323460)
- 4.0.12
* Thu Oct 26 2017 knut.anderssen@suse.com
- Adapted SuSEFirewallIsInstalled() to return true only when the
  package is already installed or checked and installed in normal
  mode.
- Added SuSEFirewallIsSelectedOrInstalled() which behaves as the
  old SuSEFirewallIsInstalled() method.
  (bnc#1037214)
- Adapted calls to use SuSEFirewallIsSelectedOrInstalled() when
  the methods can be called even with just Pkg selection.
* Thu Oct 19 2017 locilka@suse.com
- Fixing disabling vnc, ssh, ... installation to handle service
  names independently on using upper/lower case as they are used
  in different context at different places of the code
  (bsc#1055279).
- 4.0.11
* Thu Oct  5 2017 schubi@suse.de
- Disable vnc, ssh,... installation in install.inf if it is not
  supported. (bnc#1055279, bnc#1058071)
- 4.0.10
* Thu Oct  5 2017 mvidner@suse.com
- Stop using tmpnam, it is no longer supported in perl 5.26
  (bsc#1061620)
- 4.0.9
* Tue Sep 26 2017 jreidinger@suse.com
- Add support for merging to workflow extensions from modules
  (bsc#1049297)
- 4.0.8
* Fri Sep 15 2017 jreidinger@suse.com
- fix starting gnome control center (bsc#1058376)
- 4.0.7
* Thu Sep 14 2017 mvidner@suse.com
- systemd services (bsc#1045658)
  - reverted a command change that broke brittle tests
- 4.0.6
* Thu Sep  7 2017 mvidner@suse.com
- systemd services (bsc#1045658)
  - add SystemdService.find_many for a speed-up
  - SystemdUnit fix for units with multiple dots in name
  - consistent logging of systemctl calls
- 4.0.5
* Thu Sep  7 2017 igonzalezsosa@suse.com
- Fix handling of PGP signatures when running in insecure mode
  (bsc#1054663)
- 4.0.4
* Mon Sep  4 2017 ancor@suse.com
- Added methods to Yast2::FsSnapshot allowing to finish the
  Snapper configuration (part of fate#318196).
- 4.0.3
* Thu Aug 31 2017 igonzalezsosa@suse.com
- Add support to disable buttons on CWM::Dialog
- Add a method WorkflowManager#merge_product_workflow which allows
  to merge a product workflow (fate#322267)
- 4.0.2
* Wed Aug 30 2017 knut.anderssen@suse.com
- Added UI:TextHelpers with a wrap_text method moved from
  yast2-network (bsc#1055643)
- 4.0.1
* Tue Aug 29 2017 lslezak@suse.cz
- Fixed the cursor theme in the installation (the DMZ theme has
  been replaced by DMZ-White and DMZ-Black) (bsc#1051664)
- 4.0.0
* Fri Aug 25 2017 igonzalezsosa@suse.com
- Restore Packages::Repository and Packages::Product in order
  to retain compatibility with yast2-packager 3.3.2 which is
  the version on Factory until storage-ng is finally
  merged (bsc#1055677)
- 3.3.10
* Fri Aug 11 2017 igonzalezsosa@suse.com
- Move Packages::Repository and Packages::Product to yast2-packager
  (FATE#322276)
- 3.3.9
* Wed Aug  9 2017 jreidinger@suse.com
- workaround false warning from Forwardable when using OpenStruct
  in ruby 2.4 (bsc#1049433)
- 3.3.8
* Thu Aug  3 2017 lslezak@suse.cz
- run_ifconfig.scr - make "inet" section optional, handle
  additional whitespace characters (bsc#811760)
- 3.3.7
* Wed Aug  2 2017 jlopez@suse.com
- More robust systemctl test to avoid possible timeout error
* Mon Jul 31 2017 jreidinger@suse.com
- WorkflowManager: allow to extend workflow from rpm package
  (needed for FATE#323450)
- WorkflowManager: drop never used support to extend workflow from
  pattern
- 3.3.6
* Thu Jul 27 2017 jreidinger@suse.com
- drop reading /content file (FATE#322386)
- 3.3.5
* Fri Jul 21 2017 lslezak@suse.cz
- cwm/rspec.rb: added tests in "CWM::RadioButtons" group for
  optional #hspacing and #vspacing methods
* Thu Jul 20 2017 jreidinger@suse.com
- CWM::WrapperWidget#cwm_defintion: also include widget id,
  otherwise the widget would not show in a Pager, eg. Tabs
  (bsc#1049595)
- 3.3.4
* Tue Jul 18 2017 igonzalezsosa@suse.com
- Add YaST2 logs to the default list of files for System Log browser
  (bsc#1049138)
- 3.3.3
* Thu Jul 13 2017 jreidinger@suse.com
- Add Yast::Execute.on_target! and Yast::Execute.locally! variants
  which raise a Cheetah exception if the command fails (bsc#1048512)
- 3.3.2
* Wed Jul 12 2017 jreidinger@suse.com
- convert Object#timeout usage to Timeout.timeout as ruby2.4 makes
  it obsolete ( ruby2.4 will be for SLE15 so part of bsc#1044312)
- 3.3.1
* Mon Jul 10 2017 jreidinger@suse.com
- Fix omitting button in CWM::Dialog and make API consistent with
  CWM.show (boo#1039901)
- 3.3.0
* Fri Jun 23 2017 mvidner@suse.com
- Support for the new Expert Partitioner (boo#1039901):
- Added UI::Sequence, UI::Greasemonkey
- Added CWM::Dialog
- RSpec.shared_examples for CWM: Page, PushButton, RadioButtons,
  RichText.
- 3.2.40
* Thu Jun 22 2017 jreidinger@suse.com
- Add hint for UI about application name and its icon (bsc#1037891)
- 3.2.39
* Tue Jun  6 2017 jreidinger@suse.com
- Fix showing help text when CWM::ReplacePoint contains another
  CWM::ReplacePoint. Fix including new
  CWM::AbstractWidget#refresh_help functionality for widgets where
  help text can change during its lifetime. (boo#1039901)
- 3.2.38
* Fri Jun  2 2017 jlopez@suse.com
- Add EventDispatcher#event_handler to allow custom events
  management, for example to delegate to a widget. Part of
  (fate#305633)
- 3.2.37
* Thu Jun  1 2017 jreidinger@suse.com
- Fix distribution of new CWM::WrapperWidget (bsc#1032725)
- 3.2.36
* Thu Jun  1 2017 jreidinger@suse.com
- CWM: Add object wrapper to allow running object CWM with old
  hash style widgets (bsc#1032725)
- fix nested pagers to have unique ids
- 3.2.35
* Wed May 31 2017 jreidinger@suse.com
- Fix CWM::ReplacePoint to work with CWM::Custom widget and use it
  in all pagers (boo#1039901)
- Fix calling handle in CWM::RadioButtons
- 3.2.34
* Wed May 31 2017 gsouza@suse.com
- Warning messages shouldn't open UI in command-line mode
  (bsc#1036440).
- 3.2.33
* Mon May 22 2017 mvidner@suse.com
- Added CWM::Pager, CWM::Tree + CWM::TreeItem,
  CWM::TreePager + CWM::PagerTreeItem (boo#1039901)
- 3.2.32
* Fri May 19 2017 mvidner@suse.com
- Added CWM::Table (boo#1039901)
- 3.2.31
* Thu May 18 2017 lslezak@suse.cz
- Translation fix: Ruby gettext cannot extract translatable texts
  from interpolated strings (bsc#1038077)
- 3.2.30
* Tue May 16 2017 mvidner@suse.com
- Added cwm/rspec with shared_examples for CWM::AbstractWidget
  and its children (boo#1039302)
- 3.2.29
* Wed Apr 19 2017 lslezak@suse.cz
- Fixed parsing whitespace lines in /etc/fstab (bsc#1030425)
- 3.2.28
* Mon Apr 10 2017 jreidinger@suse.com
- Set correct title when wizard is supported (bsc#1033161#c4)
- 3.2.27
* Fri Apr  7 2017 jreidinger@suse.com
- start using y2start instead of y2base (bsc#1027181)
- 3.2.26
* Mon Apr  3 2017 mgerstner@suse.de
- don't generate multiline entries, it's against SuSEfirewall2 recommendation
  multiline entries create trouble with fillup, see bsc#798468
- 3.2.25
* Thu Mar 30 2017 lslezak@suse.cz
- Fixed downloading installer extension package (FATE#320772)
- 3.2.24
* Tue Mar 28 2017 knut.anderssen@suse.com
- SlideShow: Escape plain text release notes being shown properly
  in RichText (bsc#1028721).
- 3.2.23
* Fri Mar 24 2017 lslezak@suse.cz
- Download the addon installation.xml file from a package
  referenced by the "installerextension" provides dependency
  (FATE#320772)
- 3.2.22
* Wed Mar 22 2017 jreidinger@suse.com
- Use for Yast::TargetFile and Yast::Execute real path where scr
  operates. It allows easier switching scr in unit tests.
  (needed for testing fix for bsc#1023204)
- 3.2.21
* Wed Mar 22 2017 ancor@suse.com
- Added options to CWM::RadioButtons to set some extra spaces
  (related to poo#14936 and bsc#1025415).
- 3.2.20
* Mon Mar 20 2017 lslezak@suse.cz
- Added PackageDownloader and PackageExtractor classes for sharing
  the package downloading and extracting functions (fate#320772)
- 3.2.19
* Mon Mar 20 2017 mfilka@suse.com
- bnc#1026027
  - removed insserv calls
- 3.2.18
* Thu Mar 16 2017 schubi@suse.de
- UnitFileState will be used for evaluating enable state of
  services. If it has an invalid value "systemctl is-enabled...."
  has to be called instead. (bnc#1012047)
- 3.2.17
* Wed Mar 15 2017 ancor@suse.com
- Added FileChanges.created_files (part of fix for bsc#1027582)
- 3.2.16
* Wed Mar  8 2017 igonzalezsosa@suse.com
- Support to add roles through addons (FATE#320772)
- 3.2.15
* Wed Feb  8 2017 jreidinger@suse.com
- Allow Pattern selector to have more generic button names and
  enablement (needed for poo#14936, bsc#1025415)
- 3.2.14
* Fri Jan 20 2017 jreidinger@suse.com
- Fix error popup when replacing widget with CWM::ReplacePoint
  (FATE#322328)
- 3.2.13
* Thu Jan 19 2017 jreidinger@suse.com
- Added a CWM::ReplacePoint widget
- 3.2.12
* Wed Jan 18 2017 jreidinger@suse.com
- CWM: when skipping storing of widget values, skip also its
  validation (FATE#322328)
* Thu Jan  5 2017 mfilka@suse.com
- bnc#1017716
  - do not cache ifcfg files with empty device name part (ifcfg-).
    Such file cannot be mapped to any existing device and providing
    empty device name could lead to unexpected crashes in other
    parts of yast.
- 3.2.11
* Thu Jan  5 2017 lslezak@suse.cz
- Fixed tests to pass with the latest yast2-core package
  (related to the bsc#932331 fix)
- 3.2.10
* Tue Dec 20 2016 igonzalezsosa@suse.com
- Add a method to read the ID property from the /etc/os-release
  file (related to bsc#1016004)
- 3.2.9
* Wed Dec 14 2016 jreidinger@suse.com
- add generic cwm widget for keyboard layout (used for FATE#321754)
- 3.2.8
* Wed Nov 30 2016 lslezak@suse.cz
- Enhanced PackagesProposal API to handle required and optional
  resolvables separately (bsc#885496)
- 3.2.7
* Wed Nov 23 2016 igonzalezsosa@suse.com
- Fix replacement of workflow modules (bsc#1011869)
- 3.2.6
* Fri Nov 18 2016 lslezak@suse.cz
- Remove the restart file when starting YaST to avoid possible
  infinite loop (bsc#842910)
- 3.2.5
* Wed Nov 16 2016 schubi@suse.de
- Added needed include in Kernel.rb. Found while testing
  bnc#1009023
- 3.2.4
* Thu Nov  3 2016 jreidinger@suse.com
- fix do not show again for packages downloaded to temporary
  directory (bsc#481011)
- remove icons from signature check dialogs (bsc#875201)
- 3.2.3
* Tue Oct 18 2016 schubi@suse.de
- Add-on module: Do not escape characters like ":" in the path
  string (bnc#966413).
- 3.2.2
* Sat Oct 15 2016 kanderssen@suse.com
- Network: Added method to adapt old configuration of enslaved
  interfaces. (bsc#962824)
- 3.2.1
* Thu Oct 13 2016 igonzalezsosa@suse.com
- Set installer theme when Screenmode is specified at boot time
  (related to bsc#780621)
- 3.2.0
* Wed Sep 28 2016 snwint@suse.de
- save_y2logs: use canonical path (bsc#1001454)
- 3.1.208
* Tue Sep 20 2016 mvidner@suse.com
- Removed build dependency on yast2-perl-bindings (bsc#999203)
- 3.1.207
* Fri Sep 16 2016 kanderssen@suse.com
- Network: Fix bug introduced during NetworkInterfaces.Read cleanup
  The method Networkinterfaces.Locate now returns the interface
  name of the interfaces that match the given condition instead of
  the type. (bsc#998717)
- 3.1.206
* Fri Aug 26 2016 kanderssen@suse.com
- Packages: remove warning icon from package callbacks.
  (bnc#988949)
- 3.1.205
* Thu Aug 25 2016 schubi@suse.de
- Set AutoYaST default timeout entries for reporting errors
  correctly and do not overwrite AutoYaST profile settings.
  (bnc#988949)
- 3.1.204
* Tue Aug  9 2016 igonzalezsosa@suse.com
- Popup.Error will escape the text when message is too long and
  richtext is used (bsc#992506)
- 3.1.203
* Mon Aug  8 2016 igonzalezsosa@suse.com
- Fixed handling of cd:/ and dvd:/ URLs (bsc#991935)
- 3.1.202
* Thu Aug  4 2016 mvidner@suse.cz
- Declare textdomain to fix untranslated texts (bsc#992084).
- 3.1.201
* Thu Aug  4 2016 jsrain@suse.cz
- show release notes during package installation even if slide
  show is not available (bsc#978700)
- 3.1.200
* Fri Jul 29 2016 mvidner@suse.com
- Fixed ArgumentError in Popup.AnyTimedMessage (bsc#988739).
- 3.1.199
* Mon Jul 25 2016 kanderssen@suse.com
- Fixed Yast::NetworkInterfaces.FilterNOT regexp matching
  (bsc#990482) added in previous release.
- 3.1.198
* Mon Jul 25 2016 kanderssen@suse.com
- Clean up of NetworkInterfaces Read method to make it more
  readable (bsc#982850)
- 3.1.197
* Mon Jul 11 2016 jreidinger@suse.com
- define 32-bit arm architecture (thanks to @afaerber)
  (FATE#310070)
- 3.1.196
* Thu Jun 30 2016 jreidinger@suse.com
- fix cyclic dependencies caused by split of firewall classes
  (bsc#987059)
- 3.1.195
* Wed Jun 22 2016 lslezak@suse.cz
- Use a high resolution window icon (64x64) instead of the low
  resolution (22x22) one (bsc#985432)
- 3.1.194
* Wed Jun  8 2016 lslezak@suse.cz
- Fixed displaying the file conflicts callbacks when the Progress
  dialog is not displayed (bsc#983464)
- 3.1.193
* Thu Jun  2 2016 igonzalezsosa@suse.com
- Drop yast2-devel-doc package (fate#320356)
- 3.1.192
* Fri May 20 2016 mchandras@suse.de
- Split SuSEFirewall and SuSEFirewallServices classes to separate
  files as recommended by the Yast coding style (fate#318356,
  gh#yast/yast-yast2#471)
- 3.1.191
* Thu May 19 2016 mchandras@suse.de
- Refactor SuSEFirewall backend code to support FirewallD. This allows
  yast2 modules to be firewall agnostic and handle firewall services in
  either SuSEFirewall2 or FirewallD (fate#318356, gh#yast/yast-yast2#457)
  * Do a bit of code cleanup.
  * Add FirewallD tests.
- 3.1.190
* Wed May 18 2016 mfilka@suse.com
- bnc#972575
  - filter out INTERFACETYPE option from ifcfg files. This option
    used to be written with incorrect value by older versions of
    yast.
- 3.1.189
* Tue May 17 2016 snwint@suse.de
- remove invalid_hostname check (fate#319639)
- 3.1.188
* Mon May  9 2016 igonzalezsosa@suse.com
- Add Repository and Repository products classes to the packages
  library API (part of FATE#320494)
- 3.1.187
* Mon May  9 2016 igonzalezsosa@suse.com
- Fix "when" key in FinishClient#info
* Fri Apr 22 2016 knut.anderssen@suse.com
- Added restarting state to Installation to for example recover
  data  or skip dialogs until the one wich restarted yast.
  (related to bsc#974409)
- 3.1.186
* Tue Apr 19 2016 jreidinger@suse.com
- CWM: fix showing help for tabs widgets
  found during fixing bnc#952633)
- 3.1.185
* Mon Apr 11 2016 lslezak@suse.cz
- Make the "Abort" button default in the file conflict popup
  (safe default compatible with zypper) (bsc#923590)
- 3.1.184
* Mon Apr  4 2016 schubi@suse.de
- Added system_time to ylib_DATA.
  Cleanup for bnc#956730.
- 3.1.183
* Fri Apr  1 2016 schubi@suse.de
- Moved "uptime" from package autoyast2 to yast2.
  Cleanup for bnc#956730.
- 3.1.182
* Tue Mar 29 2016 lslezak@suse.cz
- Display a confirmation dialog when a file conflict is detected
  during package installation (bsc#923590)
- 3.1.181
* Wed Mar 23 2016 cwh@suse.com
- Added proc_modules.scr from yast-installation to avoid that
  yast-sound depends on yast-installation (bsc#972310)
- 3.1.180
* Wed Mar 16 2016 knut.anderssen@suse.com
- Added cfg_mail.scr from yast-mail to avoid circular dependencies
  with yast2-security, yast2-users and yast2-mail (FATE#319711)
- 3.1.179
* Thu Mar 10 2016 dvaleev@suse.com
- Introduce PowerNV platform (boo#970582)
- 3.1.178
* Fri Mar  4 2016 mvidner@suse.com
- Added ProductFeatures.SetOverlay,ClearOverlay for System Roles
  (FATE#317481)
- 3.1.177
* Wed Mar  2 2016 jreidinger@suse.com
- Require rubygems using system ruby version to avoid YaST failures
  (bnc#969113)
- 3.1.176
* Mon Feb 22 2016 igonzalezsosa@suse.com
- Add support for showing update messages from libzypp
  (related to bsc#943805)
- 3.1.175
* Fri Feb  5 2016 kanderssen@suse.com
- SuSEFirewall module reads system configuration during
  autoinstallation. It behaves in the same way as
  regular installation or normal operation (bsc#963585)
- AutoYaST settings for SuSEFirewall will be merged
  with the existing configuration (instead of being fully
  overwritten).
- Add a read_and_import method to SuSEFirewall module.
- 3.1.174
* Fri Feb  5 2016 mfilka@suse.com
- bsc#960040
  - put valid hostname into AY profile generated at the end of
    installation
- 3.1.173
* Mon Feb  1 2016 jreidinger@suse.com
- Yast::Execute do not crash for missing '_' method (found during
  FATE#317701)
- 3.1.172
* Mon Feb  1 2016 jreidinger@suse.com
- fix packaging of TargetFile and Execute classes (FATE#317701)
- 3.1.171
* Thu Jan 28 2016 jreidinger@suse.com
- fix string processing for frames in CWM causing crash in
  yast2-network (bnc#963966)
- 3.1.170
* Wed Jan 27 2016 jreidinger@suse.com
- Added Yast::Execute, a class to run programs with Cheetah
- Added Yast::TargetFile, a handler suitable for CFA::BaseModel
- Both respect Yast::Installation.destdir ( needed for FATE#317701)
- 3.1.169
* Tue Jan 26 2016 jreidinger@suse.com
- Allow CWM to specify which events do not cause storing of widget
  content ( needed for FATE#317701)
- 3.1.168
* Tue Jan 26 2016 ancor@suse.com
- Added UI::InstallationDialog as specialization of UI::Dialog
  (part of bsc#893825)
- 3.1.167
* Wed Jan 20 2016 jreidinger@suse.com
- Added CWM::Tabs that is object oriented API replacement for
  CWMTab
- 3.1.166
* Mon Jan 18 2016 igonzalezsosa@suse.com
- Add a default value for firewall setting FW_BOOT_INIT_FULL
  (bsc#955400)
- 3.1.165
* Mon Jan 18 2016 jreidinger@suse.com
- Added CWM::AbstractWidget.
- Added CWM.show method working with AbstractWidgets kids
- Added few basic CWM widgets for easier CWM.show usage
- 3.1.164
* Tue Jan 12 2016 jsrain@suse.cz
- fixed semantics of SCR call for zKVM detection (bsc#961485)
- 3.1.163
* Fri Dec 11 2015 jsrain@suse.cz
- added detection of zKVM to Arch.rb (for proper fix of bsc#956736)
- 3.1.162
* Fri Nov 27 2015 ancor@suse.com
- Renamed some arguments and methods in the UI::ServiceStatus API
  (fate#318771)
- 3.1.161
* Thu Nov 26 2015 ancor@suse.com
- New methods CWM.save_current_widgets and
  CWM.validate_current_widgets
- Replaced UI::SrvStatusComponent with UI::ServiceStatus
  (fate#318771)
- 3.1.160
* Tue Nov 24 2015 snwint@suse.de
- rewrite save_y2logs (and log linuxrc.log and wickedd.log)
- 3.1.159
* Mon Nov 23 2015 lslezak@suse.cz
- Fixed idnkit dependency to allow building YaST HEAD in SLE12
- 3.1.158
* Fri Nov 20 2015 lslezak@suse.cz
- Fixed Puny code processing - the idnconv tool has been moved to
  a different package (idnkit) (bsc#953442)
- 3.1.157
* Wed Nov  4 2015 lslezak@suse.cz
- Fixed clipped dialog label (bsc#948381)
- 3.1.156
* Fri Oct 23 2015 mvidner@suse.com
- Fixed clipped labels in Arabic on some widgets (bsc#880701).
- Fixed that also for the installation (bsc#880701#c43)
- 3.1.155
* Thu Oct 22 2015 mfilka@suse.com
- bnc#946047
  - use proper hostname / domain defaults when network is
    configured by linuxrc
- 3.1.154
* Wed Oct 21 2015 igonzalezsosa@suse.com
- Replace "Skip" with "Ignore" in the dialog that is shown when
  there's a problem during packages installation (bsc#948608)
- 3.1.153
* Thu Oct  8 2015 jreidinger@suse.com
- Fix "stack level too deep" exception if cd-rom repository is
  needed (bnc#945879)
- 3.1.152
* Fri Oct  2 2015 ancor@suse.com
- UI component for services handling moved from yast2-dns-server
  to yast2 (fate#318771)
- 3.1.151
* Wed Sep 30 2015 lslezak@suse.cz
- Properly format the package license in the confirmation dialog
  to make it better readable (bsc#819311)
- 3.1.150
* Fri Sep 11 2015 lslezak@suse.cz
- Avoid too many snapshots created during the online migration
  (bsc#944019)
* Wed Aug 26 2015 mfilka@suse.com
- bnc#897129
  - AutoYaST will no longer ignore firewall settings if
    keep_install_network is enabled
- 3.1.149
* Wed Aug 26 2015 igonzalezsosa@suse.com
- Add a Mode#auto method
* Wed Aug 26 2015 schubi@suse.de
- Checking cpuinfo_flags correctly while evaluating kernel packages
  for i586. (bnc#943297)
- 3.1.148
* Thu Aug 20 2015 lslezak@suse.cz
- "yast2" script - handle also the reboot flag the same way as
  the installation script (bsc#942461)
- 3.1.147
* Wed Aug 19 2015 mfilka@suse.com
- bnc#941881
  - displays hostname / domain as set in /etc/hostnmae
- 3.1.146
* Mon Aug 10 2015 mfilka@suse.com
- bnc#916013
  - keeps routing state when firewall is enabled/disabled
- 3.1.145
* Mon Aug  3 2015 ancor@suse.com
- Fixed a conflict between Wizard and CommandLine components that
  was breaking the CLI for some modules (bnc#940341)
- 3.1.144
* Tue Jul 28 2015 ancor@suse.com
- Properly display information about exceptions when running in
  command line mode (bnc#939565).
- Fixed a bug preventing Yast::CommandLine to be executed twice
  in the same script.
- 3.1.143
* Tue Jul 21 2015 jreidinger@suse.com
- Allow Dialog class to support alternative ways how to get user
  input (needed for yast2-vnc module) (bnc#938944)
- 3.1.142
* Fri Jul 17 2015 igonzalezsosa@suse.com
- Do not try to load snapper extension as it does not exists anymore
  (bsc#938377).
- 3.1.141
* Thu Jul  9 2015 jreidinger@suse.com
- do not crash if desktop file does not exist for setting icon
  (bnc#937549)
- 3.1.140
* Mon Jul  6 2015 shundhammer@suse.de
- Cleanup for snapshots made during installation (bnc#935923)
- 3.1.139
* Wed Jul  1 2015 jreidinger@suse.com
- fix using desktop icon for yast(bnc#894220)
- 3.1.138
* Tue Jun 30 2015 mvidner@suse.com
- Added /etc/sysconfig/yast2:PKGMGR_RECOMMENDED=yes to control
  whether the YaST packager UI installs recommended dependencies
  (boo#900853).
- Removed /etc/sysconfig/yast2:PKGMGR_REEVALUATE_RECOMMENDED,
  making the setting not persistent (boo#902394).
- 3.1.137
* Mon Jun 29 2015 mfilka@suse.com
- bnc#858908
  - use /etc/hostname instead of /etc/HOSTNAME
- bnc#922765, bnc#923990
  - do not propose TLD
- 3.1.136
* Thu Jun 25 2015 locilka@suse.com
- Starting the Installer (YaST2.First-Stage) directly from yast2
  startup script if we are in inst-sys (FATE#317637, bnc#877447)
- 3.1.135
* Mon Jun 22 2015 cwh@suse.com
- bnc#922765
  - changed default TLD from .site to .suse
- 3.1.134
* Thu Jun 18 2015 ancor@suse.com
- Changed implementaton of view_anymsg to rely more on standard
  Yast mechanisms (bnc#935192)
- 3.1.133
* Thu Jun 11 2015 mfilka@suse.com
- fate#318804
  - dropped no longer used group from YaST Control Centre
- 3.1.132
* Thu Jun 11 2015 ancor@suse.com
- Added new method Directory.find_data_file (needed for the
  implementation of fate#318425)
- Deprecated Directory.datadir and Directory.ydatadir
- 3.1.131
* Thu Jun  4 2015 igonzalezsosa@suse.com
- Fix a typo when calling Linuxrc.value_for method
- 3.1.130
* Tue Jun  2 2015 locilka@suse.com
- Implemented possibility to temporarily disable creating
  snapshots via parameter on Linuxrc commandline:
    disable_snapshots=(single|around|all)
  or using their comma-separated combination (fate#317973)
- 3.1.129
* Tue Jun  2 2015 jreidinger@suse.com
- reduce count of extending inst-sys with snapper for snapshotting
  (fate#317973)
- 3.1.128
* Mon Jun  1 2015 locilka@suse.com
- Added Linuxrc.value_for (fate#317973)
- 3.1.127
* Wed May 27 2015 jreidinger@suse.com
- Add persistent storage for fs pre snapshots (fate#317973)
- 3.1.126
* Mon May 25 2015 locilka@suse.com
- Fixed proposal to open fallback ports for services (bsc#916376)
- Removed opening iSCSI ports from firewall proposal (bsc#916376)
- 3.1.125
* Fri May 22 2015 jreidinger@suse.com
- InstExtensionImage: add block variant for loading extension
  (needed for FATE#317900)
- 3.1.124
* Tue May 19 2015 igonzalezsosa@suse.com
- Add a class FsSnapshot for managing filesystem snapshots
  (fate#317973).
* Mon May 18 2015 locilka@suse.com
- Making SuSEFirewallProposal.propose_iscsi function public
  (bsc#916376)
- 3.1.123
* Wed May 13 2015 locilka@suse.com
- Propose SuSEfirewal2 to fully initialize (e.g. open ports)
  already in the init phase to allow using iSCSI (bsc#916376)
- 3.1.122
* Tue Feb  3 2015 ancor@suse.com
- Better handling of line breaks in system log viewer (bnc#912169)
- 3.1.121
* Mon Feb  2 2015 jreidinger@suse.com
- fix typo in method call to package bindings (found by openQA)
- separate dummy Pkg callbacks from common ones
- 3.1.120
* Thu Jan 29 2015 jreidinger@suse.com
- remove depreacated legacy Patch callbacks
* Tue Jan 27 2015 jreidinger@suse.com
- fixed \r, \f, \v and \b  characters lost during conversion to
  Ruby
* Tue Jan 27 2015 cwh@suse.com
- Removed more icons from other dialogs (bnc#875201)
- 3.1.119
* Thu Jan 22 2015 jsrain@suse.cz
- added handling of new created configuration files (bsc#860856)
- 3.1.118
* Wed Jan 21 2015 cwh@suse.com
- Removed icons from all kinds of popups (bnc#875201)
- 3.1.117
* Tue Jan 20 2015 jreidinger@suse.com
- remove unused module for tracking config history in svn
- remove unused module for writing to system log that is obsolete
  by systemd
- remove never used feature to lock proposal by administrator
- improve the most horrible nesting of blocks in code
* Fri Jan 16 2015 jreidinger@suse.com
- enable automatic rubocop style checker and adjust code to YaST
  style guide
* Fri Jan 16 2015 dvaleev@suse.com
- Treat PowerNV platform as CHRP
* Tue Jan 13 2015 cwh@suse.com
- Use native Ruby implementation (IPAddr) for Yast::IP.
- 3.1.116
* Wed Jan  7 2015 jsrain@suse.cz
- keep kernel cmdline options during live installation (bsc#793065)
* Thu Dec 18 2014 lslezak@suse.cz
- 3.1.115
* Wed Dec 17 2014 schwab@suse.de
- Add Arch.aarch64
* Thu Dec  4 2014 jreidinger@suse.com
- remove X-KDE-Library from desktop file (bnc#899104)
* Mon Dec  1 2014 lslezak@suse.cz
- PackageCallbacks: fixed progress reporting (progress overflow was
  caused by missing stage count)
- 3.1.113
* Wed Nov 26 2014 jreidinger@suse.com
- Add base class for installation proposal and finish clients
- 3.1.112
* Wed Nov 26 2014 gber@opensuse.org
- remove support for the unmaintained GTK UI plugin (bnc#901511)
* Wed Nov 12 2014 lslezak@suse.cz
- removed RegistrationStatus.pm module (obsolete, not supported
  by the new SCC registration)
- 3.1.110
* Fri Oct 31 2014 jreidinger@suse.com
- do not crash for non-english locale if log file does not exist
  (bnc#898204)
- 3.1.109
* Wed Sep 17 2014 jsrain@suse.cz
- change order in mode initialization so that selected Upgrade
  entry in boot menu does not override AutoUpgrade (bnc#897044)
- 3.1.108
* Wed Sep 17 2014 schubi@suse.de
- Checking nil for repository name. (bnc#896466)
- 3.1.107
* Tue Sep 16 2014 ancor@suse.com
- Added an extra help message when authentication against a
  registration server fails while refreshing repositories
  (bnc#895719)
- 3.1.106
* Fri Sep  5 2014 lslezak@suse.cz
- do not write /etc/sysconfig/kernel:INITRD_MODULES, it has been
  dropped (bnc#895084)
- 3.1.105
* Thu Sep  4 2014 mvidner@suse.com
- Use a more flexible rubygem requirement syntax (bnc#895069)
- 3.1.104
* Thu Aug 28 2014 jreidinger@suse.com
- fix using changed root in netd agent so it can be used in
  installation (bnc#893965)
- 3.1.103
* Wed Aug 27 2014 locilka@suse.com
- Lazy-loading SuSEfirewall2 services - some new services can be
  added when Yast is already running, and the config has been read
  already (bnc#872960)
- Preventing from showing incorrect service name or description if
  they are coming from TEMPLATE file (bnc#893583)
- Fixed service file parsing - comments starting with more than one
  '#' characters were reported as unexpected input (just warning)
- 3.1.102
* Thu Aug 21 2014 locilka@suse.com
- Fixed checking whether SuSEfirewall2 package is selected or
  installed - in inst_finish, the package is already installed
  (bnc#892935)
- 3.1.101
* Wed Aug 20 2014 locilka@suse.com
- Fixed RPM description (bnc#888994)
- 3.1.100
* Wed Aug 13 2014 ancor@suse.com
- Untrusted repositories are disabled during installation to avoid
  asking for the key import over and over during the installation.
- Fixed bnc#723019 and bnc#886572
- 3.1.99
* Wed Aug 13 2014 schubi@suse.de
- Package.rb: Each call is polling which installation mode is
  active currently. So Mode.rb has not to take care about modules
  which are using Mode.rb. (Fixing current testcases)
- 3.1.98
* Tue Aug 12 2014 locilka@suse.com
- Fixed checking for SuSEfirewall2 package installed/selected
  for installation depending on the current stage/mode (bnc#887406)
- 3.1.97
* Tue Aug 12 2014 schubi@suse.de
- When changing installation mode in "Mode.rb" the mode in Package.rb
  has to be updated too. (bnc#888212)
- 3.1.96
* Thu Aug  7 2014 locilka@suse.com
- SuSEFirewall: Reading SuSEfirewall2 configuration whenever it's
  possible instead of simply skipping it in Stage.initial - package
  can be already available at the end of installation (bnc#887406)
- 3.1.95
* Thu Aug  7 2014 ancor@suse.com
- Added two new generic 'waiting' messages, needed in yast-country
  to fix bnc#888804
- 3.1.94
* Wed Aug  6 2014 jsrain@suse.cz
- read products from system (not repository) also during live
  installation (bnc#889157)
- 3.1.93
* Wed Jul 30 2014 lslezak@suse.cz
- fixed a crash in package management when running in Qt UI with
  libproxy1-config-kde4 package installed (bnc#866692)
- 3.1.92
* Wed Jul 30 2014 locilka@suse.com
- Fixed setting the default target during installation - systemctl
  doesn't return any target properties while running in chroot so
  we have to guess the Id and AllowIsolate properties (bnc#889323)
- 3.1.91
* Tue Jul 29 2014 jreidinger@suse.com
- Fix timing of slideshow - now slides goes in cycle and all have
  equal time to display which improve user experience (bnc#885973)
- 3.1.90
* Tue Jul 29 2014 ancor@suse.com
- Fixed .proc.cmdline parsing to support more situations
  (bnc#889241)
- 3.1.89
* Tue Jul 29 2014 jreidinger@suse.com
- fix hidding cd statistics in text only mode (bnc#864507)
- 3.1.88
* Thu Jul 24 2014 locilka@suse.com
- Fixed checking for :active state of a systemd unit - it's :active
  already even if it's just being activated (bnc#884756)
- 3.1.87
* Tue Jul 22 2014 locilka@suse.com
- Added new ServicesProposal library to hold and export services
  enabled/disabled during installation (bnc#887688)
- 3.1.86
* Thu Jul 10 2014 lslezak@suse.cz
- Product.rb: do not stop initialization on solver errors
  (bnc#886588)
- 3.1.85
* Tue Jul  8 2014 locilka@suse.com
- Fixed Product.get_property by ensuring that we don't try to get
  property of an undefined product (bnc#886151)
- 3.1.84
* Fri Jul  4 2014 lslezak@suse.cz
- view_anymsg: remove escape sequences from input log file
  (bnc#879629)
- 3.1.83
* Tue Jul  1 2014 vmoravec@suse.com
- Fix SystemdTarget.all not to return nil in the collection
- 3.1.82
* Tue Jun 24 2014 jreidinger@suse.com
- add option to disable os probing for some products (bnc#884007)
- 3.1.81
* Mon Jun 23 2014 mfilka@suse.com
- bnc#864619
  - old network service is also disabled when switching to new one.
- 3.1.80
* Tue Jun 17 2014 schubi@suse.de
- Fixed error message for missing services
  (bnc#882609)
- 3.1.79
* Wed Jun 11 2014 mfilka@suse.com
- bnc#878719
  - improved handling of inactive network service
- 3.1.78
* Tue Jun 10 2014 lslezak@suse.cz
- make sure the total installation progress is always 100%%
  (adjust the rounding issues when computing the subprogress
  percentages) (bnc#865585)
- 3.1.77
* Mon Jun  9 2014 mfilka@suse.com
- bnc#864619
  - stop wicked service(s) properly when switching network services
- 3.1.76
* Wed Jun  4 2014 locilka@suse.com
- Adjusted textdomain for OSRelease library
- 3.1.75
* Fri May 30 2014 vmoravec@suse.com
- Add Service.call method to make available all systemctl commands
- 3.1.74
* Fri May 30 2014 lslezak@suse.cz
- DonePackage callback: remove invalid UTF-8 characters to avoid
  crash (bnc#876459)
- 3.1.73
* Fri May 30 2014 locilka@suse.com
- Fixed network backend handling during upgrade - unified with
  installation (bnc#879594)
- 3.1.72
* Wed May 28 2014 locilka@suse.com
- Removed warning message when starting Yast in Qt instead of GTK
  and vice versa (bnc#861807)
- 3.1.71
* Wed May 28 2014 jreidinger@suse.com
- split too wide urls for accepting GnuGP key (bnc#870822)
- 3.1.70
* Wed May 28 2014 lslezak@suse.cz
- removed system verification check when yast module installs
  required packages (bnc#866256)
- 3.1.69
* Wed May 28 2014 jreidinger@suse.com
- save_y2logs: store also pbl.log from target system, if bootloader
  installation failed (bnc#879622)
- 3.1.68
* Fri May 23 2014 locilka@suse.com
- Added check for existence of /etc/modules.d/ directory in Kernel
  library, the directory is created when missing (bnc#879428)
- 3.1.67
* Fri May 23 2014 mfilka@suse.com
- bnc#879399
  - offer /var/log/boot.log in SysLog module for view
- 3.1.66
* Mon May 19 2014 locilka@suse.com
- Always using special InstallationProperties for systemd_unit
  while called in first stage (bnc#878560)
- 3.1.65
* Mon May 19 2014 locilka@suse.com
- Changed dialog label for updating/installing in SlideShow
  depending on the selected method (bnc#874995)
- 3.1.64
* Tue May 13 2014 aschnell@suse.de
- added error handing for viewing log files (bnc#876895)
- 3.1.63
* Mon May 12 2014 jsrain@suse.cz
- avoid hiding release notes button when new wizard window is
  opened (bnc#876668)
- 3.1.62
* Fri May  9 2014 lslezak@suse.cz
- Product.rb - fixed base product detection (do not check the
  product status, always use the product from the initial
  repository during installation) (bnc#876836)
- 3.1.61
* Mon May  5 2014 vmoravec@suse.com
- Fix getting the status of sysvinit services (bnc#876144)
- 3.1.60
* Fri May  2 2014 jreidinger@suse.com
- save_y2logs: store target of symlinks as symlinks are useless
- 3.1.59
* Fri May  2 2014 jsrain@suse.cz
- fixed incorrect function name (bnc#876105)
- 3.1.58
* Tue Apr 29 2014 locilka@suse.com
- Fixed Product lazy loading in Update mode (bnc#875605)
- 3.1.57
* Tue Apr 29 2014 gs@suse.de
- Add support for 'stop' and 'restart' of services in inst-sys
  (related to bnc #873057, bnc #873448)
- 3.1.56
* Mon Apr 28 2014 locilka@suse.com
- Fixed SlideShow table header to match the reality (bnc#874823)
- 3.1.55
* Thu Apr 24 2014 locilka@suse.com
- Product library changed to read data only from os-release and
  libzypp (bnc#873877), no more from content file
- 3.1.54
* Tue Apr 22 2014 locilka@suse.com
- Published Service.Active (used from Perl)
- 3.1.53
* Tue Apr 22 2014 locilka@suse.com
- Removed Product.patterns (replaced by Packages.default_patterns)
  (bnc#873923)
- 3.1.52
* Thu Apr 17 2014 mvidner@suse.com
- rewrote URLRecode.pm to URLRecode.rb so that 'yast2 repositories'
  can run without Perl bindings
- 3.1.51
* Thu Apr 17 2014 locilka@suse.com
- Decreased number of logs coming from Hooks (to enhance logs
  readability)
- 3.1.50
* Thu Apr 17 2014 vmoravec@suse.com
- Add path to deprecation warnings (bnc#873973)
- Fix enabling LSB services during installation (bnc#873929)
- 3.1.49
* Wed Apr 16 2014 jreidinger@suse.com
- ensure that dialog was closed even if exception is raised
  (bnc#873916)
- save_y2logs: store versions of packages in inst-sys
- 3.1.48
* Wed Apr 16 2014 mfilka@suse.com
- bnc#869661
  - fixed internal error raised in inst_lan during update
- 3.1.47
* Tue Apr 15 2014 locilka@suse.com
- Changed Product.FindBaseProducts to throw an exception if no
  base products are found in installation (bnc#873458, bnc#873377)
- 3.1.46
* Mon Apr 14 2014 locilka@suse.com
- Changed OSRelease not to read content file instead of os-release
  file in inst-sys (bnc#873366)
- Changed Product to use OSRelease.ReleaseInformation as :name
  instead of creating it from ReleaseName and ReleaseVersion,
  these are only used as fallback (bnc#873366)
- 3.1.45
* Thu Apr 10 2014 locilka@suse.com
- Prefering os-release file to content file (which is used only as
  a fallback now) both in installation and on a running system
  (bnc#871261)
- 3.1.44
* Thu Apr 10 2014 mvidner@suse.com
- Enable wizard title on the left instead of on top during the
  installation (bnc#868859).
- 3.1.43
* Thu Apr 10 2014 jsrain@suse.cz
- adjusted Product.FindBaseProducts to be usable during
  installation (needed for fix of bnc#871158)
- 3.1.42
* Wed Apr  9 2014 jsrain@suse.cz
- added tabs for release notes into slide show dialog (bnc#871158)
- 3.1.41
* Wed Apr  9 2014 jreidinger@suse.com
- save_y2logs: save also log from perl-Bootloader (bnc#872486)
- 3.1.40
* Tue Apr  8 2014 locilka@suse.com
- Changed way of reading the product information: Reads it from
  /content file if it exists, then from /etc/os-release, then it
  throws exception if there is no other place to read (bnc#871261)
- 3.1.39
* Tue Apr  8 2014 lslezak@suse.cz
- fixed "uninitialized constant Yast2::HwDetection::SCR" error
  (bnc#871783), fixed testsuite
- 3.1.38
* Wed Apr  2 2014 jreidinger@suse.com
- add control option to enable sshd in installation (bnc#865056)
- 3.1.37
* Tue Apr  1 2014 gs@suse.de
- Add info about text mode navigation in trees to general help
  (bnc #840672)
* Mon Mar 31 2014 vmoravec@suse.com
- Fix failing tests
- 3.1.36
* Mon Mar 31 2014 vmoravec@suse.com
- Fix enabling services in inst-sys (bnc#870949)
- 3.1.35
* Fri Mar 28 2014 vmoravec@suse.com
- Add more systemd unit commands to SystemdService
- 3.1.34
* Fri Mar 28 2014 vmoravec@suse.com
- Don't change service name which might be frozen string
  (bnc#870803)
- 3.1.33
* Thu Mar 27 2014 vmoravec@suse.com
- Fix for template systemd units properties
- 3.1.32
* Thu Mar 27 2014 lslezak@suse.cz
- fixed popup_test
- 3.1.31
* Wed Mar 26 2014 lslezak@suse.cz
- fixed syntax error in Popup.Feedback()
- 3.1.30
* Wed Mar 26 2014 vmoravec@suse.com
- Deprecate and refactor Service module with SystemdService backend
- Add support for /bin/service_start script in installation system
  that has no running systemd
- 3.1.29
* Wed Mar 26 2014 locilka@suse.com
- Throwing exception Yast::OSReleaseFileMissingError from
  OSRelease if /etc/os-release file is missing (bnc#869091)
- 3.1.28
* Wed Mar 26 2014 locilka@suse.com
- Refactored SUSEFirewallServices to throw exceptions when user
  or code tries to handle unknown services (bnc#867377)
- Adjusted CWMFirewallInterfaces to handle the new exception
  and inform user about it (bnc#867377)
- 3.1.27
* Tue Mar 25 2014 lslezak@suse.cz
- added Popup.Feedback for displaying progress popup when running
  a block of code
- 3.1.26
* Tue Mar 25 2014 jsuchome@suse.cz
- better check if chef-client is running (bnc#868483)
* Mon Mar 24 2014 vmoravec@suse.com
- Add support for systemd target with SystemdTarget module
* Thu Mar 13 2014 gs@suse.de
- Check IPv4 and IPv6 for running network (bnc#868001)
- 3.1.25
* Tue Mar 11 2014 vmoravec@suse.com
- Adapt System.Status for latest systemctl (bnc#867378)
- 3.1.24
* Thu Mar  6 2014 vmoravec@suse.com
- Allow raising exceptions for not found systemd units;
  updates the expectations for bnc#853300
- 3.1.23
* Thu Mar  6 2014 vmoravec@suse.com
- Add systemd service support; needed by fate#314946
- 3.1.22
* Tue Mar  4 2014 vmoravec@suse.com
- Allow the Service module to configure services witout
  systemd unit files (bnc#864934)
- 3.1.21
* Thu Feb 27 2014 vmoravec@suse.com
- Add systemd socket support (bnc#853300)
- 3.1.20
* Mon Feb 10 2014 lslezak@suse.cz
- added memory detection code (gh#yast/yast-packager#33)
- 3.1.19
* Wed Feb  5 2014 jsuchome@suse.cz
- Check for Chef outside in the yast2 shell script to catch modules
  not using CommandLine (bnc#803358)
- 3.1.18
* Thu Jan 30 2014 mfilka@suse.com
- bnc#861078
  - detected network service set properly when running in
    installation mode
- 3.1.17
* Tue Jan 21 2014 jreidinger@suse.com
- remove from wizard icons for title as proposed by Ken
  (fate#314695)
- 3.1.16
* Tue Jan 21 2014 mfilka@suse.com
- fate#316768
  - use wicked tools for network service restart / reload when
    running in installation mode
- 3.1.15
* Thu Jan 16 2014 jreidinger@suse.com
- make the package owner of /usr/share/YaST2/lib
- 3.1.14
* Wed Jan  8 2014 locilka@suse.com
- Upgrade mode in installer is newly set by Linuxrc (bnc#857847)
- 3.1.13
* Fri Dec 20 2013 vmoravec@suse.com
- Add fail and abort hooks for installation
- 3.1.12
* Thu Dec 12 2013 mfilka@suse.com
- changed API for querying network configuration backend
- 3.1.11
* Tue Dec 10 2013 mfilka@suse.com
- bnc#851769
  - fixed reading bridge configuration
  - thanks to Waldemar Spitz <wspitz@uni-bonn.de>
- 3.1.10
* Tue Dec 10 2013 vmoravec@suse.com
- add hook file #output method
- 3.1.9
* Wed Dec  4 2013 jreidinger@suse.com
- deprecate yast --install, --upgrade and --remove and use zypper
  instead. Suggest using zypper directly from command line.
  (FATE#316458)
- 3.1.8
* Tue Dec  3 2013 vmoravec@suse.com
- Update hooks
- 3.1.7
* Thu Nov 28 2013 vmoravec@suse.com
- Add hook into installation workflow
- 3.1.6
* Mon Nov 25 2013 jreidinger@suse.com
- Make sure the system ruby is used (BNC#845897)
  ( thanks to Marc Schütz <schuetzm@gmx.net>)
- Add hooks module (FATE#315992) (vmoravec)
- Fix rspec run on OS-12.3
- 3.1.5
* Thu Nov 21 2013 lslezak@suse.cz
- PKGMGR_ACTION_AT_EXIT: change the default action to "summary",
  added combobox for changing the value
* Wed Nov 20 2013 lslezak@suse.cz
- removed support for automatic 2nd stage (the 2nd stage has been
  dropped completely) (FATE#314695)
- 3.1.4
* Fri Nov 15 2013 jsuchome@suse.cz
- Warn the user if Chef could overwrite her changes (bnc#803358).
* Fri Nov 15 2013 jreidinger@suse.com
- Removed unused API from NetworkInterfaces
* Wed Nov 13 2013 aschnell@suse.de
- use correct binary prefix (see bnc#849276)
* Mon Nov 11 2013 jsrain@suse.cz
- added dedicated "Show Release Notes" button support for NCurses
  (fate#314695)
* Mon Nov  4 2013 locilka@suse.com
- Removed obsolete clients: password, remotechooser, remoteinstall
  (gh#yast/yast-yast2#100)
* Fri Nov  1 2013 locilka@suse.com
- Removed checking for a fallback control file, that file is always
  outdated and cannot work for all products
  (gh#yast/yast-installation#86)
- 3.1.3
* Thu Oct 31 2013 locilka@suse.com
- Configuration of Kernel modules loaded on boot has been moved
  to /etc/modules-load.d/*.conf files. Adapted Kernel library
  internal handling (bnc#838185).
- 3.1.2
* Tue Oct 22 2013 mfilka@suse.com
- bnc#846550
  - deleting aliases works even for devices with name according
    new scheme
* Tue Oct 22 2013 locilka@suse.com
- Added Linuxrc.keys (FATE#314982)
- 3.1.1
* Wed Oct  9 2013 jreidinger@suse.com
- Install binaries to /usr/sbin instead of /sbin to be consistent
  with rest of world and use common specs. Symlinks are kept for
  backward compatibility.
- do not create sym links in sbin for zast or camel case yast
* Thu Sep 26 2013 lslezak@suse.cz
- do not use *.spec.in template, use *.spec file with RPM macros
  instead
- 3.1.0
* Tue Sep 24 2013 jreidinger@suse.com
- allow nested ipv4 in ipv6 (BNC#828683)
- 3.0.9
* Tue Sep  3 2013 mfilka@suse.com
- bnc#837517
  - fixed misinterpreting IPv6 prefixes when converting to netmask
- 3.0.8
* Thu Aug 29 2013 jreidinger@suse.com
- use ruby builtin IP regexp and clean a bit code
- 3.0.7
* Wed Aug 28 2013 jreidinger@suse.com
- removed output redirection for /sbin/yast2, now it ends up in
  ~/.xsession-errors like for every other X program (BNC#766555)
- 3.0.6
* Thu Aug 22 2013 jsuchome@suse.cz
- prevent accessing /etc/os-release during tests from Product.rb
  constructor
- 3.0.5
* Thu Aug 22 2013 jsuchome@suse.cz
- replace SuSERelease with OSRelease, which uses /etc/os-release
  (bnc#833955,fate#316268)
- 3.0.4
* Tue Aug 13 2013 locilka@suse.com
- Changed some y2milestone into y2debug in GetTypeFrom* in
  NetworkInterfaces to decrease overfilling Yast log
- 3.0.3
* Fri Aug  9 2013 mfilka@suse.com
- bnc#798620
  - disabled starting firewall during second stage. It could
    cause deadlock in systemd initialization sequence.
- 3.0.2
* Thu Aug  8 2013 tgoettlicher@suse.de
- fixed navigation in yast2-cc without mouse (bnc#651350)
* Mon Aug  5 2013 jsuchome@suse.cz
- added support for handling product profiles (port of fate#310730)
- 3.0.1
* Wed Jul 31 2013 yast-devel@opensuse.org
- converted from YCP to Ruby by YCP Killer
  (https://github.com/yast/ycp-killer)
- version 3.0.0
* Mon Jul 29 2013 lslezak@suse.cz
- PackageSystem.ycp - do not initialize the target system in the
  first installation stage when running in instsys, there is no RPM
  DB in the RAM disk image (bnc#742420#c7)
* Thu Jul 18 2013 mfilka@suse.com
- added net device type detection based on sysfs
- fixed type detection workflow
- 2.24.5
* Fri Jul 12 2013 mfilka@suse.com
- fixed device type detection when commiting new device into
  NetworkInterfaces' cache. Fixes bnc#809053.
- changes API for device type detection - incompatible to previous
  versions
- 2.24.4
* Fri Jun 28 2013 mfilka@suse.com
- bnc#817797
  - data imported into NetworkInterfaces cannot be overwritten by
    subsequent Read anymore
- 2.24.3
* Thu Jun 27 2013 jsuchome@suse.cz
- show gpg key info in a term that allows copying the text
  (bnc#611456)
  - 2.24.2
* Thu Jun 13 2013 lslezak@suse.cz
- updated the testsuite to make the transition to Ruby easier
* Mon May 27 2013 locilka@suse.com
- Reverted resetting disabled steps (bnc#813072)
- 2.24.1
* Tue May 21 2013 jsuchome@suse.cz
- do not propose desktop kernel for minimal installation
  (bnc#819335)
- 2.24.0
* Thu May 16 2013 jsrain@suse.cz
- handle GPG keys in AutoUpgrade the same as in AutoYaST
  (bnc#820166)
- 2.23.29
* Tue May 14 2013 mfilka@suse.com
- bnc#819327
  - InfiniBand device is not available on s390 arch.
- 2.23.28
* Tue May 14 2013 tgoettlicher@suse.de
- accept any version of libyui
- 2.23.27
* Mon May 13 2013 locilka@suse.com
- Fixing resetting steps in installation (bnc#813072)
- 2.23.26
* Fri May  3 2013 locilka@suse.com
- Added functionality for checking network entry with optional
  netmask in IP or CIDR format (bnc#800592).
- Using new IP::CheckNetwork in Firewall (bnc#800592).
- ValidNetwork definition moved to IP module.
- 2.23.25
* Thu May  2 2013 locilka@suse.com
- Re-enabling all disabled items (steps, proposals) if stagemode
  has changed (bnc#813072)
- 2.23.24
* Thu May  2 2013 lslezak@suse.cz
- correct function signature for Pkg::CallbackErrorScanDb()
  callback
* Fri Mar 15 2013 jsuchome@suse.cz
- testsuite adapted to previous change (new code in Enable call)
* Wed Mar  6 2013 tgoettlicher@suse.de
- applied lnussel's patch:
  Don't use Info function to check enable state (bnc#807507)
- 2.23.23
* Tue Mar  5 2013 mvidner@suse.cz
- Changed to use network.service alias link, that is installed by
  the NetworkManager.service while "systemctl enable" and obsoletes
  the NETWORKMANAGER=yes/no variable in /etc/sysconfig/network/config
  (bnc#764055,bnc#764336,bnc#798348, by mt@suse.com)
- Requires sysconfig >= 0.80.0
- 2.23.22
* Wed Feb 13 2013 aschnell@suse.de
- added CommandLine::PrintTable, String::Repeat and
  String::SuperPad
- 2.23.21
* Fri Feb  1 2013 lslezak@suse.cz
- added perl-XML-XPath dependency (needed by RegistrationStatus.pm)
- 2.23.20
* Thu Jan 17 2013 locilka@suse.com
- Extended checking for service in Service module by also checking
  in /etc/init.d as a fallback (bnc#795929 comment#20).
- 2.23.19
* Wed Jan 16 2013 locilka@suse.com
- Testcase for Service module moved here from yast2-iscsi-client
* Mon Jan 14 2013 locilka@suse.com
- Runlevel definitions (targets) are now in /usr/lib/systemd/system
  (bnc#795929)
- Checking for systemd scripts in more directories (bnc#795929)
- 2.23.18
* Mon Jan  7 2013 locilka@suse.com
- SuSEfirewall2 has merged *_init and *_setup services into one
  systemd service (bnc#795929).
- 2.23.17
* Fri Jan  4 2013 aschnell@suse.de
- fixed path for get_kernel_version (bnc#794084)
- 2.23.16
* Tue Dec 18 2012 locilka@suse.com
- Adapted Service module to use systemd directly instead of via
  init.d (FATE #312568)
- 2.23.15
* Fri Dec  7 2012 lslezak@suse.cz
- allow some characters in URL password field (bnc#786757)
* Thu Nov 29 2012 tgoettlicher@suse.de
- fixed bnc#791294: frame for firewall settings
- 2.23.14
* Tue Nov 27 2012 gs@suse.de
- Added sysconfig variables (solver options) PKGMGR_VERIFY_SYSTEM,
  PKGMGR_AUTO_CHECK, PKGMGR_REEVALUATE_RECOMMENDED
* Mon Nov 26 2012 locilka@suse.com
- Dropped obsolete Runlevel YCP module
* Tue Nov 20 2012 jdsn@suse.de
- move RegistrationStatus.pm from wagon to yast2 (fate#312712)
- new version for proper package dependencies in wagon
- 2.23.13
* Tue Nov 13 2012 tgoettlicher@suse.de
- confirmed license GPL v2
- 2.23.12
* Fri Nov  2 2012 jsuchome@suse.cz
- move Log Viewer client here from dropped repair module
  (bnc#787070)
- 2.23.11
* Tue Oct 30 2012 jsuchome@suse.cz
- Kernel::InformAboutKernelChange - always return boolean
- fixed build dependencies
- 2.23.10
* Mon Oct 29 2012 jsuchome@suse.cz
- use Kernel::InformAboutKernelChange after package installation
- do not read SuSEconfig log
- 2.23.9
* Thu Oct 25 2012 jsuchome@suse.cz
- added Kernel::InformAboutKernelChange - replacement for only
  non-SuSEconfig part of inst_suseconfig
- 2.23.8
* Fri Oct 19 2012 jsuchome@suse.cz
- added Syslog module, simple API to write into system log
- 2.23.7
* Thu Oct 11 2012 jsuchome@suse.cz
- removed calls to /sbin/SuSEconfig, packages should care of
  updating configurations on their own
* Mon Oct  1 2012 mfilka@suse.com
- extended support for IPv6
- 2.23.6
* Mon Sep 24 2012 locilka@suse.com
- Fixed detection whether firewall is running (BNC #779455) and
  unified with starting and stopping the service via Service API.
* Tue Sep 18 2012 jsuchome@suse.cz
- added San Marino to the list of countries (bnc#780639)
- 2.23.5
* Mon Aug 27 2012 tgoettlicher@suse.de
- fix bnc#776567 YaST doesn't support input method
- 2.23.4
* Fri Aug 17 2012 locilka@suse.com
- Fixed a typo (BNC #766703)
- Added support for iSCSI Target into the Firewall proposal
  (BNC #766300)
* Tue Aug  7 2012 jsuchome@suse.cz
- fixed checking for systemd status (bnc#774799)
- 2.23.3
* Tue Jun 26 2012 gs@suse.de
- added color schemes "highcontrast" and "inverted" to description
  of Y2NCURSES_COLOR_THEME in sysconfig.yast2
* Fri Jun 22 2012 tgoettlicher@suse.de
- search for UI plugins at new and old location
- 2.23.2
* Thu May 10 2012 mfilka@suse.com
- removed ShellSafeWrite as it is not needed anymore with new ag_ini - bnc#750325
- 2.23.0
* Thu Mar 29 2012 jsuchome@suse.cz
- merged proofed texts
- 2.22.6
* Wed Mar 28 2012 gs@suse.de
- Revert the change in FileUtils::Exists() (change is not needed
  here but will cause failure of testsuites)
- 2.22.5
* Wed Feb 22 2012 mfilka@suse.com
- bnc#694582 - added @ as it is allowed in authority part of URI.
- improve Exists(), don't return 'true' if SCR::Read() returned nil
- fixed testsuite for WorkFlow.ycp - corrupted due to above Exists() fix
- added String::YesNo
- 2.22.4
* Tue Jan 31 2012 tgoettlicher@suse.de
- Fixed typo
* Fri Jan 13 2012 mvidner@suse.cz
- Internet test: fail early if NetworkManager has crashed
  (bnc#739390).
- 2.22.3
* Fri Jan  6 2012 mvidner@suse.cz
- Relicensed ConfigHistory from GPL-2.0 to GPL-2.0+
  to match the rest of the package (bnc#728950).
- 2.22.2
* Fri Jan  6 2012 jreidinger@suse.com
- forbid appending to IPADDR additional suffix if there is already
  one. Original name have preference (bnc#735109).
* Fri Jan  6 2012 mvidner@suse.cz
- create user-unreadable ifcfg files without a race (bnc#713661, CVE-2011-3177)
- 2.22.1
* Fri Jan  6 2012 mvidner@suse.cz
- Moved NetworkStorage from yast2.rpm to yast2-network.rpm
  (bnc#726057)
- 2.22.0
* Wed Nov  2 2011 locilka@suse.cz
- Unified starting, stopping and checking for firewall status
  (bnc#727445)
- 2.21.25
* Tue Oct 25 2011 locilka@suse.cz
- Added new function String::ReplaceWith that is a replacement for
  often used mergestring(splitstring(...))
* Thu Oct 20 2011 locilka@suse.cz
- Fixed script for generating translations for firewall services
  defined by other packages
- Regenerated translations for firewall services defined by other
  packages (bnc#722877)
* Wed Oct  5 2011 jsrain@suse.cz
- removed list of controller modules not to be included in ititrd
  (bnc#719696)
- 2.21.24
* Thu Sep 29 2011 lslezak@suse.cz
- Service::RunInitScriptWithTimeOut() - fixed memory leak,
  release the process info at the end
* Mon Sep 26 2011 jsrain@suse.cz
- simplify usage of save_y2logs (bnc#673990)
* Fri Sep 23 2011 lslezak@suse.cz
- use Pkg::ResolvableProperties() instead of obsoleted
  Pkg::TargetProducts()
- removed obsoleted Pkg::CallbackAcceptNonTrustedGpgKey() and the
  related dialog
- 2.21.23
* Fri Sep 16 2011 visnov@suse.de
- Added UIHelper library module - contains useful
  UI helpers from now obsolete Wizard_hw
- Drop Wizard_hw
- Added Wizard::SetDesktopTitleAndIcon
- Added Desktop::ParseSingleDesktopFile
- 2.21.22
* Thu Sep 15 2011 mvidner@suse.cz
- Added the interface name patterns emN, pN and pNpM.
  It fixes recognizing them as configured (bnc#713644)
  and unbreaks the proposed bridged configuration (bnc#713048).
- 2.21.21
* Wed Sep 14 2011 lslezak@suse.cz
- .etc.sysctl_conf agent - support also ';' comment character
- 2.21.20
* Tue Sep 13 2011 locilka@suse.cz
- Fixed SuSEfirewall2 SCR agent to understand single-quoted and
  double-quoted, single and multi-line variables and also
  single-line variables without any quotes (bnc#716013).
- 2.21.19
* Fri Sep  9 2011 locilka@suse.cz
- Using ButtonBox in Wizard where possible (bnc#571939)
* Thu Sep  8 2011 lslezak@suse.cz
- adapted to systemd (bnc#664548)
- 2.21.18
* Thu Sep  8 2011 jsuchome@suse.cz
- added agent for /etc/sysctl.conf (fate#312343)
- 2.21.17
* Thu Sep  8 2011 lslezak@suse.cz
- GPG.ycp - fixed initialization after creating a new GPG key,
  fixed creating a GPG key in KDE desktop or after logging via
  plain "su" (gpg agent problem) (bnc#715242)
* Mon Sep  5 2011 lslezak@suse.cz
- added new Systemd.ycp module for handling systemd configuration,
  (needed for bnc#707418)
- 2.21.16
* Thu Sep  1 2011 jsrain@suse.cz
- enhanced the help command-line parameters (bnc#712271)
- 2.21.15
* Wed Aug 31 2011 mvidner@suse.cz
- Update Deleted and OriginalDevices in NetworkInterfaces::Write.
  Thanks to Justus Winter
- 2.21.14
* Wed Aug 31 2011 lslezak@suse.cz
- fixed trusting a GPG key (wrong id check) (bnc#713068)
- added String::FindMountPoint() function (moved from yast2-wagon
  to share it with other modules)
- 2.21.13
* Fri Aug 26 2011 locilka@suse.cz
- Fixed handling of FW_SERVICES_ACCEPT_* in SuSEFirewall modules to
  understand flags as the fifth parameter (bnc#712670)
- Fixed SuSEfirewall2 SCR agent to parse the sysconfig file
  properly (bnc#712670)
- 2.21.12
* Mon Aug  8 2011 lslezak@suse.cz
- improved GPG key import dialog: changed "Import" button to
  "Trust" (bnc#694213), display expiration warning for expired
  keys, better layout for displaying GPG key properties, hide
  additional help text in ncurses UI (so the GPG key properties are
  displayed completely)
- 2.21.11
* Fri Aug  5 2011 tgoettlicher@suse.de
- fixed .desktop file (bnc #681249)
* Wed Aug  3 2011 lslezak@suse.cz
- use term "Software manager" instead of "Package manager"
  (bnc#585679)
- 2.21.10
* Tue Aug  2 2011 locilka@suse.cz
- Fixed Get/SetBroadcastAllowedPorts in SuSEFirewall to keep
  user-entered values instead of translating them magically into
  list of ports (bnc#694782).
- 2.21.9
* Thu Jul 28 2011 mvidner@suse.cz
- Fixed NetworkInterfaces::GetTypeFromIfcfg to recognize bridges (bnc#704999).
- 2.21.8
* Wed Jul 27 2011 lslezak@suse.cz
- command line - properly display multiline help texts (bnc#708553)
- 2.21.7
* Fri Jul 22 2011 mvidner@suse.cz
- FCoE detection in NetworkStorage::isDiskOnNetwork (bnc#677251, FATE#306855).
- Added NetworkInterfaces::GetTypeFromIfcfg which knows
  ETHERDEVICE=>vlan (FATE#311380).
- 2.21.6
* Fri Jul 22 2011 locilka@suse.cz
- Removed obsoleted X-KDE-SubstituteUID from desktop files
  (bnc#540627)
* Thu Jul 21 2011 locilka@suse.cz
- Fixed SuSEfirewall2 config library: By default any unassigned
  network interface is automatically assigned to the external
  firewall zone (bnc#547309).
- Fixed CWM library for opening ports in firewall not to list any
  empty strings returned by network module, just interface names
  (bnc#547309).
- 2.21.5
* Mon Jul 18 2011 jsrain@suse.cz
- fixed typo (bnc#702662)
* Tue Jun 28 2011 lslezak@suse.cz
- Suppress decimal zeroes for kB sizes (e.g. display "743 kB"
  instead of "743.00 kB") (bnc#495045)
- 2.21.4
* Thu Jun 23 2011 lslezak@suse.cz
- read GPG keys in UTF-8 locale to properly read non-ASCII
  characters, UTF-8 characters caused SLMS webyast module crashing
  (bnc#696312)
- 2.21.3
* Thu Jun 23 2011 lslezak@suse.cz
- Fixed abort callback to abort installation completely
  (bnc#673629)
- 2.21.2
* Tue Jun 21 2011 locilka@suse.cz
- Fixed group desktop files by adding Exec=/sbin/yast2 (BNC#470482)
* Thu Jun 16 2011 tgoettlicher@suse.de
- Fixed crushed progress bar (bnc #675443)
- Version bump
- 2.21.1
* Thu Jun 16 2011 locilka@suse.cz
- Fixed regexp in Custom broadcast definition in
  SuSEFirewallExpertRules (BNC #676972).
- 2.20.15
* Thu May 19 2011 mvidner@suse.cz
- Don't assume YaST has crashed (and scare the user with a pop-up)
  simply if a YCP script returns false (bnc#645434).
- 2.20.14
* Wed Mar 16 2011 tgoettlicher@suse.de
- Fixed dependencies (bnc #667938)
- 2.20.13
* Tue Feb  8 2011 jsrain@suse.cz
- do not define splash screen resolution to mkinitrd if boot splash
  is not installed (bnc#670225)
- 2.20.12
* Wed Jan 19 2011 jsrain@suse.cz
- adaptations for unattended migration (fate#310481)
- 2.20.11
* Tue Jan 18 2011 aschnell@suse.de
- call snapper from yast2 script
* Tue Jan  4 2011 lslezak@suse.cz
- check PackageKit status, suggest to quit the daemon if it is
  running (bnc#659522)
- 2.20.10
* Mon Jan  3 2011 lslezak@suse.cz
- fixed VLAN config type detection (wrong regexp)
- 2.20.9
* Mon Jan  3 2011 lslezak@suse.cz
- don't abort when package checksum verification failes, ask to
  download the file again (bnc#657608)
- 2.20.8
* Wed Dec 22 2010 mzugec@suse.cz
- ifcfg-ethX.Y style config files for VLAN(fate#309240)
- 2.20.7
* Mon Dec 20 2010 mzugec@suse.cz
- fate#306855: FCoE boot support
- 2.20.6
* Tue Nov 16 2010 mzugec@suse.cz
- save log file into home directory by default (bnc#653601)
- 2.20.5
* Fri Nov 12 2010 mzugec@suse.cz
- FileChanges: fixed testsuite
* Fri Nov 12 2010 mzugec@suse.cz
- yast2 added bind-utils dependency (bnc#651893)
- 2.20.4
* Fri Nov 12 2010 mzugec@suse.cz
- FileChanges: test rpm command exit value
* Fri Nov  5 2010 lslezak@suse.cz
- PackageCallbacks: removed the retry/abort/skip dialog from
  DoneProvide callback - the user is asked via MediaChange
  callback, don't ask twice when aborting.
- 2.20.3
* Tue Nov  2 2010 lslezak@suse.cz
- updated to match the changed StartPackage callback signature
- 2.20.2
* Mon Oct 18 2010 lslezak@suse.cz
- don't display extra error popup when a download fails, the error
  is reported later via MediaChange callback anyway (bnc#625987)
- 2.20.1
* Wed Oct 13 2010 jsuchome@suse.cz
- open LongError popup instead of Error if the message is too long
  (bnc#611596)
* Thu Oct  7 2010 lslezak@suse.cz
- just log problemDeltaDownload callbacks - libzypp automatically
  tries full rpm if patch/delta cannot be downloaded, displaying
  error popup breaks unattended installation (bnc#377569)
- 2.20.0
* Mon Jul 19 2010 mzugec@suse.cz
- yast2 bash completion - show all yast modules (bnc#621848)
- thanks to Andrea Florio
* Fri Apr 30 2010 jsuchome@suse.cz
- ag_anyxml: do not die on broken XML (bnc#600928)
- 2.19.13
* Thu Apr 29 2010 jsrain@suse.cz
- fixed typo (bnc#594384)
* Mon Apr 19 2010 lslezak@suse.cz
- URLRecode.pm - fixed "deprecated defined(%%hash)" warning
  (bnc#596920)
- 2.19.12
* Thu Apr  8 2010 gs@suse.de
- yast2 start script: don't start YaST on console in UTF-8 mode
  by default and don't fix settings, but respect and trust the
  locale ('testutf8' is removed, see bnc#556555 and bnc#436378).
- 2.19.11
* Fri Mar 26 2010 cmeng@novell.com
- Add a new category High Availability (bnc #575787)
* Mon Mar 22 2010 mzugec@suse.cz
- L3: autoinstallation with manual setup (bnc#568653)
- 2.19.10
* Tue Mar 16 2010 jsuchome@suse.cz
- SERVICES.pm moved to webyast-services-ws (bnc#587876)
- 2.19.9
* Wed Mar 10 2010 locilka@suse.cz
- Added special comments for translators to RTL languages
  (BNC #584466).
* Wed Mar 10 2010 mvidner@suse.cz
- Mode::test(): check getenv instead of the UI
  so that it works also in WebYaST (bnc#243624#c13).
- 2.19.8
* Wed Mar  3 2010 jsuchome@suse.cz
- SERVICES.pm: added support for enabling/disabling service
- 2.19.7
* Wed Feb 17 2010 jsrain@suse.cz
- do not save unmodified interfaces (fate#308978)
* Thu Feb 11 2010 juhliarik@suse.cz
- added fix for deleting splash from initrd (bnc#292013)
* Mon Feb  8 2010 locilka@suse.cz
- Fixed SuSEFirewall::ActivateConfiguration to return a boolean
  value in all scenarios (BNC #577932).
* Mon Feb  8 2010 locilka@suse.cz
- Showing also zone of interface for 'Open Port in Firewall'
  details (BNC #483455).
- 2.19.6
* Tue Feb  2 2010 locilka@suse.cz
- Fixed generating unique step IDs for Wizard too keep the same
  durign one YaST run (BNC #575092).
* Mon Jan 18 2010 jsuchome@suse.cz
- SERVICES.pm: read descriptions (bnc#570298); get single service
  status from the Read function (bnc#570968)
- 2.19.5
* Fri Jan 15 2010 aschnell@suse.de
- extended Report and Popup module (needed for fate #304500)
- 2.19.4
* Thu Jan 14 2010 mzugec@suse.cz
- NetworkStorage: adapt functions needed for iBFT (bnc#551380)
- 2.19.3
* Thu Jan 14 2010 kmachalkova@suse.cz
- Added Recommends: xdg-utils. xdg-su is now used in .desktop files
  of root-only YaST modules (bnc#540627)
- 2.19.2
* Tue Jan 12 2010 lslezak@suse.cz
- GPG.ycp - run gpg in C locale (bnc#544680)
- GPG.ycp - return success/error result in GPG::Init() and
  GPG::CreateKey() functions (bnc#544682)
* Thu Jan  7 2010 jsrain@suse.cz
- updated start-up script to behave correctly if QT CC is to be
  used without QT back-end (bnc#545331)
* Tue Jan  5 2010 lslezak@suse.cz
- added missing UI::SetProductName() call - display the proper
  product name in help texts (using &product; macro) (bnc#535483)
- 2.19.1
* Mon Dec  7 2009 jsrain@suse.cz
- translate module names properly in NCurses CC (bnc#553644)
* Thu Nov 26 2009 locilka@suse.cz
- Fixed access rights for /etc/install.inf (bnc #500124)
* Thu Nov 26 2009 kmachalkova@suse.cz
- Fixed striping trailing \n from Hostname::CurrentHostname()
  (bnc#553213)
- 2.19.0
* Thu Nov 26 2009 lslezak@suse.cz
- PackageLock - use "Software Management" term consistently
  (bnc#558625)
* Thu Nov 19 2009 locilka@susue.cz
- REGISTERPRODUCT from content file moved to control file to
  globals->require_registration (FATE #305578)
- Extended SuSEFirewallServices module (FATE #306804)
* Tue Nov 10 2009 jsuchome@suse.cz
- SERVICES.pm: use ruby-bindings to read yml file (bnc#551276)
* Fri Nov  6 2009 jsrain@suse.cz
- issue an error message instead of trying to start YaST in
  NCurses without a terminal available (bnc#502688)
* Mon Oct 26 2009 mzugec@suse.cz
- NetworkPopup: display link state (FaTE#307166)
- 2.18.28
* Wed Oct 21 2009 mzugec@suse.cz
- Internet.ycp: skip interface status test in case of NM (bnc#535837)
- 2.18.27
* Mon Oct 19 2009 lslezak@suse.cz
- added explicit gpg2 Requires (bnc#544683)
* Fri Sep 25 2009 mzugec@suse.cz
- separation of netmask and prefix validation in Netmask module
- 2.18.26
* Mon Sep 14 2009 mvidner@suse.cz
- YaST would not start from the GNOME menu (Unknown option -S) bnc#537470.
- 2.18.25
* Mon Sep  7 2009 jsuchome@suse.cz
- package new YaPI file SERVICES.pm (fate #306696)
- 2.18.24
* Fri Sep  4 2009 kmachalkova@suse.cz
- ProductControl: support for disabling AC sub-items and sub-proposals
  (related to FaTE #303859 and bnc#534862)
- 2.18.23
* Mon Aug 10 2009 mvidner@suse.cz
- save_y2logs: print usage to stderr (bnc#522842).
  This is to notify users who use "$0 > l.tgz" instead of "$0 l.tgz"
* Wed Jul 29 2009 jsrain@suse.cz
- select kernel-desktop by default if exists
- 2.18.22
* Thu Jul 16 2009 jsuchome@suse.cz
- Wizard.ycp: use Fancy UI for 1024x576 screen size (fate#306298)
- 2.18.21
* Thu Jul  9 2009 lslezak@suse.cz
- Call UI::RecalcLayout() after changing push button label
  (bnc#510282)
- Improved automatic retry after download failure (more attepts,
  logarithmic back-off, retry download in more cases) (bnc#119813)
- 2.18.20
* Wed Jul  8 2009 aschnell@suse.de
- added GetIntegerFeature() and SetIntegerFeature() to
  ProductFeatures module
- 2.18.19
* Fri Jun 19 2009 jsrain@suse.cz
- removed cyclic dependency between YCP modules preventing from
  correct build
- 2.18.18
* Tue Jun 16 2009 mvidner@suse.cz
- Using autodocs-ycp.ami, which contains a fix for automake 1.11.
* Thu Jun 11 2009 lslezak@suse.cz
- use float::tolstring() function in String::FormatSize() and
  String::FormatSizeWithPrecision() to use the current
  locale decimal separator (bnc#372671)
* Thu Jun 11 2009 jsrain@suse.cz
- Getting hostname info from /etc/HOSTNAME only if the file exists.
* Wed Jun  3 2009 jsrain@suse.cz
- prefer Gtk front-end when running xfce (bnc#509121)
* Mon Jun  1 2009 mzugec@suse.cz
- new variable Internet::test to store status of test (bnc#506721)
- 2.18.17
* Tue May 26 2009 juhliarik@suse.cz
- added fix for problem with parsing command line (bnc#462276)
* Fri May 22 2009 mvidner@suse.cz
- yast2-completion.sh: removed <(process substitution) so that it
  works even with POSIXLY_CORRECT=1 (bnc#504844).
* Wed May 20 2009 aschnell@suse.de
- moved .proc.mounts agent from yast2-installation to yast2 (bnc
  [#504429])
* Tue May  5 2009 jsrain@suse.cz
- remove all passwords from install.inf in save_y2log (bnc#500130)
* Wed Apr 29 2009 lslezak@suse.cz
- media change popup - display also the URL in the short summary
  (bnc#439069)
- 2.18.15
* Tue Apr 28 2009 lslezak@suse.cz
- URL.ycp - escape also non-ASCII characters in URL, added
  URLRecode.pm module (bnc#446395)
- URL.ycp - fixed processing of smb:// URLs (bnc#495109)
* Mon Apr 20 2009 jsrain@suse.cz
- at start-up, check that /sys, /proc and /dev are not empty and
  prevent YaST from start if they are (bnc#450643)
* Thu Apr  9 2009 lslezak@suse.cz
- PackageSystem.ycp - check nil result of Pkg::PkgCommit() call
  which indicates an error (bnc#157551)
* Wed Apr  8 2009 lslezak@suse.cz
- PackageCallbacks.ycp - don't read non existing y2logRPM file
  (bnc#456446)
* Tue Apr  7 2009 jreidinger@suse.cz
- Add to CWM widget for unified table CWMTable
- 2.18.14
* Fri Apr  3 2009 lslezak@suse.cz
- Do not display "No package source" popup, just log a warning
  (bnc#485587)
* Fri Apr  3 2009 jsrain@suse.cz
- save_y2logs additionally collects /var/log/zypper.log and
  /var/log/pk_backend_zypp
* Wed Mar 25 2009 lslezak@suse.cz
- Fixed layout of the authentication popup
* Tue Mar 17 2009 lslezak@suse.cz
- moved functions RunCommandWithTimeout() and RunDumbTimeout()
  from SourceManager.ycp to Misc.ycp
* Tue Mar 17 2009 jsrain@suse.cz
- fixed typo (bnc #483915)
- report when GTK UI is wanted but not installed (bnc #472448)
* Mon Mar 16 2009 ug@suse.de
- docu for Popup::ShowTextTimed fixed
* Fri Mar  6 2009 aschnell@suse.de
- added Event.ycp to easy use of UI events
- 2.18.13
* Fri Mar  6 2009 jsrain@suse.cz
- fixed textdomain
* Thu Mar  5 2009 jsuchome@suse.cz
- GPG.ycp: --batch option is needed for hiding password popup
* Tue Feb 24 2009 mzugec@suse.cz
- - NetworkInterfaces - possible to not use LABEL for aliases
  (bnc#471253)
- 2.18.12
* Tue Feb 24 2009 locilka@suse.cz
- Added support for `reboot_same_step return value (bnc #475650).
- 2.18.11
* Mon Feb 23 2009 locilka@suse.cz
- Fixing ProductControl to avoid leaving a workflow with the `auto
  result - reruns the very first dialog (bnc #468677).
* Wed Feb 18 2009 mzugec@suse.cz
- NetworkInterfaces.GetDeviceTypes-added bond for s390 (bnc#476490)
- 2.18.10
* Wed Feb 18 2009 jsrain@suse.cz
- use PAE kernel only if there is >3GB of RAM or NX flag is present
  (bnc#467328)
* Mon Feb 16 2009 mzugec@suse.cz
- assign to GetInstArgs.args first map, not first argument (bnc#475169)
- 2.18.9
* Thu Feb 12 2009 coolo@suse.de
- add dummy Exec line to the group desktop files to shutup kbuildsycoca
- 2.18.8
* Fri Feb  6 2009 ug@suse.de
- read X-SuSE-DocTeamID from desktop files
- 2.18.7
* Fri Feb  6 2009 locilka@suse.cz
- InstError module moved here from yast2-installation-2.18.5
- 2.18.6
* Wed Feb  4 2009 aschnell@suse.de
- avoid broken pipe in scripts (bnc #467891)
- 2.18.5
* Tue Feb  3 2009 mvidner@suse.cz
- Fixed prefix detection if called "bash -x yast2" (bnc#458385 c12).
* Fri Jan 30 2009 jsrain@suse.cz
- fixed bash completion (bnc #470544)
* Wed Jan 28 2009 lslezak@suse.cz
- PackagesUI - removed textdomain switches
* Tue Jan 27 2009 locilka@suse.cz
- Added ag_freespace - SCR agent for checking free space in
  directories (mounted partitions) (bnc #460477).
- 2.18.4
* Tue Jan 27 2009 aschnell@suse.de
- added String::StartsWith() function
- 2.18.3
* Mon Jan 26 2009 mzugec@suse.cz
- new Wizard::OpenCancelOKDialog() function
- 2.18.2
* Mon Jan 26 2009 locilka@suse.cz
- Fixing ProductControl to avoid leaving a workflow by with the
  `back result - reruns the very first dialog (bnc #468677).
* Thu Jan 22 2009 lslezak@suse.cz
- added String::FormatTime() for formatting time in seconds to
  a printable string (HH:MM:SS or MM:SS format)
- PackagesUI - added installation summary dialog (bnc#431854)
- added PKGMGR_ACTION_AT_EXIT sysconfig variable for configuring
  the default package manager behavior at exit
- 2.18.1
* Mon Jan 19 2009 lslezak@suse.cz
- URL.ycp - fixed parsing and building IPv6 URLs, testsuite update
  (bnc#465820)
* Tue Jan  6 2009 jsrain@suse.cz
- added String::RemoveShortcut to allow using widget labels in help
  texts to ensure translations are in sync (bnc #307220)
- 2.18.0
* Tue Dec 30 2008 lslezak@suse.cz
- use "Installed Size" label in the summary table during package
  installation (bnc#355326)
- better help text for package installation progress dialog
  (bnc#443142)
* Tue Dec 23 2008 lslezak@suse.cz
- CommandLine.ycp - fixed handling of multiline help texts in
  'xmlhelp' command (bnc#430848)
* Mon Dec 22 2008 lslezak@suse.cz
- PackageCallbacks.ycp - do not log a password in URL (bnc#460978)
* Wed Dec 17 2008 lslezak@suse.cz
- PackageSystem::DoInstallAndRemove() - check the system and offer
  to fix it when there are inconsistencies, do not commit the
  changes if there are unresolved dependencies (bnc#439373)
* Wed Dec 17 2008 locilka@suse.cz
- Escaping parameters when calling /usr/bin/genDDNSkey
  (bnc #459739)
* Mon Dec 15 2008 lslezak@suse.cz
- PackageSystem::DoInstallAndRemove() - reset the fixsystem solver
  flag and do not install extra (unrelated) packages (bnc#439373)
- 2.17.60
* Mon Dec  8 2008 jsuchome@suse.cz
- menu.ycp: do not wait for integer return value of YOU (bnc#457167)
- 2.17.59
* Fri Dec  5 2008 lslezak@suse.cz
- PackagesUI.ycp - properly pass the mode parameter to the packager
  widget (bnc#456472)
- 2.17.58
* Fri Dec  5 2008 lslezak@suse.cz
- PackageSystem::DoInstallAndRemove() - updated to API change in
  pkg-bindings (bnc#450528)
- 2.17.57
* Wed Dec  3 2008 kmachalkova@suse.cz
- Take translations of group and module names in ncurses CC from
  system-wide desktop_translations.mo - they are not part of YaST
  .desktop files anymore (bnc#450494)
* Wed Dec  3 2008 aschnell@suse.de
- save xorg conf and log in save_y2logs
- 2.17.56
* Wed Dec  3 2008 lslezak@suse.cz
- PackageSystem::DoInstallAndRemove() - do not install recommended
  packages for already installed packages (bnc#445476)
- 2.17.55
* Tue Dec  2 2008 mzugec@suse.cz
- NetworkStorage:: for LVM detection use pvs instead of pvscan
* Tue Dec  2 2008 mzugec@suse.cz
- improved rootfs on network-based disk detection (bnc#445004)
- 2.17.54
* Mon Dec  1 2008 mzugec@suse.cz
- Confirm::Detection() - exception for s390 (bnc#429562)
* Fri Nov 28 2008 locilka@suse.cz
- Fixed the ag_netd agent to reset the STDOUT handler to :raw just
  for itself, otherwise UTF-8 chars read from disk are broken
  (bnc #447487).
- 2.17.53
* Thu Nov 27 2008 locilka@suse.cz
- Fixed counting the current overall SlideShow progress status
  (bnc #449792).
* Tue Nov 25 2008 lslezak@suse.cz
- reverted back the kernel-maxcpus change (bnc#444658)
- 2.17.52
* Tue Nov 18 2008 lslezak@suse.cz
- select kernel-maxcpus on x86_64 when there are more than 128
  processors (bnc#444658)
- register AcceptUnknownGpgKey callback (bnc#445664)
- 2.17.51
* Fri Nov 14 2008 sh@suse.de
- Consistent behaviour for Wizard::HideAbortButton() (bnc #444176)
  Still broken usability-wise, but now broken in a consistent way
- V 2.17.50
* Wed Nov 12 2008 jdsn@suse.de
- revert change to disable x11 setup on Itanium(ia64) (bnc#439612)
- 2.17.49
* Fri Nov  7 2008 locilka@suse.cz
- Checking downloaded files signatures (WorkflowManager)
  (bnc #409927).
- 2.17.48
* Fri Nov  7 2008 lslezak@suse.cz
- added URL::HidePassword() and URL::HidePasswordToken() functions
  (bnc#441944)
- 2.17.47
* Thu Nov  6 2008 jdsn@suse.de
- disable x11 setup on Itanium/ia64 (bnc#439612)
- 2.17.46
* Wed Nov  5 2008 aschnell@suse.de
- added Integer::Clamp (also used for #429908)
- 2.17.45
* Wed Nov  5 2008 aschnell@suse.de
- added Integer::Min and Integer::Max (needed for bnc #429908)
- 2.17.44
* Tue Nov  4 2008 mzugec@suse.cz
- UI::TimeoutUserInput() instead of UI::UserInput() for Hardware
  Detection (bnc#429562)
- 2.17.43
* Thu Oct 30 2008 lslezak@suse.cz
- added .sysconfig.services agent for reading/writing
  /etc/sysconfig/services file (bnc#440243)
- 2.17.42
* Mon Oct 27 2008 visnov@suse.cz
- SlideShow: check stage progress against overflow
- 2.17.41
* Mon Oct 20 2008 lslezak@suse.cz
- moved PackagesUI.ycp from yast2-packager, added
  RunPackageSelector() and RunPatternSelector() functions
  (bnc#435479)
- 2.17.40
* Mon Oct 20 2008 kmachalkova@suse.cz
- bash ag_showexports moved from yast2-nfs-client package here
  (bnc#257910)
* Thu Oct 16 2008 locilka@suse.cz
- Enhancing ProductControl to show internal steps names if debug
  mode is enabled (needed for WAGON);
* Wed Oct 15 2008 locilka@suse.cz
- Removing SetFocus from Popup::AnyQuestion (bnc #435399).
* Mon Oct 13 2008 lslezak@suse.cz
- fixed syntax error in media change callback (bnc#434721)
- 2.17.39
* Mon Oct 13 2008 locilka@suse.cz
- Used Ricardo's patch for Popup dialog layout (bnc #433183).
* Wed Oct  8 2008 lslezak@suse.cz
- display "Skip Autorefresh" button instead of "Abort" when an
  error occurs during autorefresh (bnc#427017)
* Tue Oct  7 2008 lslezak@suse.cz
- fixed reference markers (%%1) in a popup message (bnc#432518)
- 2.17.38
* Mon Oct  6 2008 locilka@suse.cz
- Module PackagesProposal extended to handle also patterns
  (bnc #431580, bnc #431503)
* Mon Oct  6 2008 visnov@suse.cz
- Added icon to hardware detection confirmation (bnc #431276)
- 2.17.37
* Thu Oct  2 2008 locilka@suse.cz
- Fixed Makefiles by using [[:upper:]]*.ycp where needed.
- 2.17.36
* Thu Oct  2 2008 locilka@suse.cz
- Added new PackagesProposal module which provides unified API for
  YaST modules in installation that want to select resolvables for
  installation (bnc #431580).
* Thu Oct  2 2008 mzugec@suse.de
- Service  - log output in case of error
* Thu Oct  2 2008 kmachalkova@suse.cz
- Hostname.ycp: Improved FQDN lookup - read /etc/HOSTNAME and use
  'linux.site' if all else fails (bnc#429792)
* Wed Oct  1 2008 visnov@suse.cz
- Show old action logs when rebuilding slideshow dialog (bnc #431261)
* Tue Sep 30 2008 tgoettlicher@suse.de
- Fixed forgotten unregister from agent
* Mon Sep 29 2008 visnov@suse.cz
- updated man page with exit codes
- save also zypp history in save_y2logs
- 2.17.35
* Mon Sep 29 2008 tgoettlicher@suse.de
- Fixed bnc #418443: Yast modules windows have no title
- 2.17.34
* Mon Sep 29 2008 locilka@suse.cz
- Added possibility to restart YaST from any module by checking for
  /var/lib/YaST2/restart_yast (FATE #304118).
- 2.17.33
* Fri Sep 26 2008 locilka@suse.cz
- Disabling firewall functions in Stage::initial (bnc #429861).
- 2.17.32
* Fri Sep 26 2008 lslezak@suse.cz
- SlideShow.ycp - fixed division by zero when the installed
  packages are very small (bnc#429933)
* Thu Sep 25 2008 jdsn@suse.de
- added new control center group: support (fate#303458)
- 2.17.31
* Thu Sep 25 2008 lslezak@suse.cz
- reverted back the base product detection, fixed in pkg-bindings
  (bnc#413444)
- display the affected repository while importing a GPG key,
  updated GPG callbacks (bnc#370223)
- 2.17.30
* Thu Sep 25 2008 locilka@suse.cz
- Fixed VNC handling in Firewall Proposal (bnc #427708).
* Tue Sep 23 2008 locilka@suse.cz
- Fixed Popup::ErrorDetails (bnc #429068).
- 2.17.29
* Tue Sep 23 2008 kmachalkova@suse.cz
- Added Service::Find function - return the first of the list of
  services which is available (has init script)
  (needed for bnc#423026)
- 2.17.28
* Mon Sep 22 2008 visnov@suse.cz
- don't initialize UI in SlideShow.ycp if not necessary (bnc#427345)
* Thu Sep 18 2008 lslezak@suse.cz
- fixed base product detection (use /etc/products.d/baseproduct
  symlink) (bnc#413444)
- 2.17.27
* Wed Sep 17 2008 locilka@suse.cz
- Handling new 'add_on_mode' key in product control file
  (bnc #427002).
* Wed Sep 17 2008 locilka@suse.cz
- Fixed aborting the installation/upgrade (bnc #406401).
* Wed Sep 17 2008 lslezak@suse.cz
- PackageCallbacks.ycp - fixed `ButtonBox definition (bnc#426965)
* Wed Sep 17 2008 lslezak@suse.cz
- Progress.ycp - check whether widget `progress_replace_point
  exists (bnc#412453)
- display a link to Yast Bug Reporting Howto page in the "crash"
  dialog (bnc#421805)
- 2.17.26
* Tue Sep 16 2008 lslezak@suse.cz
- added Service::EnabledServices() and .sysconfig.cron agent
  (access to /etc/sysconfig/cron file) (bnc#425864)
- 2.17.25
* Tue Sep 16 2008 locilka@suse.cz
- Fixed ncurses menu (bnc #426507).
- 2.17.24
* Mon Sep 15 2008 locilka@suse.cz
- Ignoring backslashes at ends of lines in SuSEfirewall
  configuration file (bnc #426000).
- Using one-record-perl-line style in SuSEfirewall for some
  variables to keep them human-readable (bnc #426000).
* Fri Sep 12 2008 lslezak@suse.cz
- display a warning when a package installation or download error
  is ignored, suggest verification of the system (fate#303527)
- 2.17.23
* Thu Sep 11 2008 jsrain@suse.cz
- require yast2-branding instead of yast2-theme (fate #301794)
- 2.17.22
* Thu Sep 11 2008 jsrain@suse.cz
- merged texts from proofread
* Wed Sep 10 2008 aschnell@suse.de
- allow whitespace at line-end in /etc/fstab (see bnc #401521)
* Wed Sep 10 2008 lslezak@suse.cz
- fixed UI definition in MediaChange callback (incorrectly defined
  ButtonBox widget) (bnc#424349)
- 2.17.21
* Tue Sep  9 2008 locilka@suse.cz
- .barexml SCR agent dropped (bnc #424263).
* Tue Sep  9 2008 mzugec@suse.de
- fixed NetworkInterfaces::FreeDevice() function
- 2.17.20
* Tue Sep  9 2008 locilka@suse.cz
- Modules 'Slides' and 'SlideShow' moved here from packager.
- 2.17.19
* Mon Sep  8 2008 mzugec@suse.cz
- fix for testsuite
* Fri Sep  5 2008 mzugec@suse.cz
- added support for InfiniBand network devices (fate#304870),
  (fate#304115)
- 2.17.18
* Thu Sep  4 2008 locilka@suse.cz
- Adding question icon for ModuleLoading::Load (bnc #421002).
- Fixed Confirm module (bnc #423272).
* Thu Sep  4 2008 locilka@suse.cz
- Fixing Popup YCP module to workaround a UI Syntax Error while
  using ButtonBox widget (bnc #422612).
- Checking UI::OpenDialog return value and closing the dialog only
  if successful (bnc #422612).
- 2.17.17
* Thu Sep  4 2008 jsuchome@suse.cz
- InstExtensionImage.ycp: added function for unloading image;
  LoadExtension and UnLoadExtension have argument for progress text
* Thu Sep  4 2008 locilka@suse.cz
- One more `ButtonBox in SignatureCheckDialogs (bnc #392171).
* Tue Sep  2 2008 locilka@suse.cz
- Extended control file handling to accept 'execute' module
  parameter to be called instead of 'name'/inst_'name'
  (BNC #401319).
- 2.17.16
* Thu Aug 28 2008 locilka@suse.cz
- Adapted Popup, Confirm, CWM, ALog, GPGWidgets, NetworkPopup,
  PackageCallbacks, SignatureCheckDialogs, FileChanges, Initrd,
  and ModuleLoading libraries to use new YButtonBox widget
  (FATE #303446).
- Adjusted RPM dependencies.
- 2.17.15
* Wed Aug 27 2008 jsrain@suse.cz
- added configuration files changes tracking in SNV as preview
* Mon Aug 25 2008 ug@suse.de
- post-patterns for autoyast added
- 2.17.14
* Fri Aug 22 2008 jsrain@suse.cz
- remove 'usbhid' from blacklisted modules for initrd (bnc #398420)
* Wed Aug 20 2008 ug@suse.de
- fixed the Linuxrc::SaveInstallInf function to copy the
  install.inf
- 2.17.13
* Tue Aug 19 2008 mvidner@suse.cz
- Use zenity or kdialog instead of xmessage if available, for
  accessibility (bnc#418032, bnc#343903).
* Mon Aug 18 2008 jsrain@suse.cz
- fixed bash completion (bnc #417755)
- 2.17.12
* Tue Aug 12 2008 mvidner@suse.cz
- /sbin/yast, network.scr: Fedora portability, thanks to Oracle.
- Added Distro, a module to distinguish between distributions,
  to facilitate porting YaST.
* Mon Aug 11 2008 kmachalkova@suse.cz
- Hostname::Current.*: Do not split FQDN into pieces if it is of the
  form of IP address (bnc#415109)
- CWMFirewallInterfaces: widget-exists check added
- 2.17.11
* Mon Aug 11 2008 locilka@suse.cz
- Fixing PortAliases to recover from faulty data.
* Fri Aug  8 2008 locilka@suse.cz
- Fixed the latest Progress patch to pass the testsuite.
- 2.17.10
* Fri Aug  8 2008 jsuchome@suse.cz
- anyxml agent documentation added to anyxml.scr (bnc#405291)
* Wed Aug  6 2008 tgoettlicher@suse.de
- Fixed bnc #413516: HideBackButton() always hides back button
  in wizard
* Wed Aug  6 2008 locilka@suse.cz
- Converting old built-in allowed services configuration in
  firewall to services defined by packages (bnc #399217).
* Wed Jul 30 2008 lslezak@suse.cz
- PackageLock::Connect() - display more details about owner of the
  zypp lock (bnc#280537)
* Fri Jul 25 2008 mzugec@suse.cz
- support for tunnel devices in NetworkInterfaces (FaTE#302184)
- 2.17.9
* Tue Jul 22 2008 locilka@suse.cz
- Added new DnsServerAPI::GetReverseIPforIPv6 function.
- 2.17.8
* Thu Jul 17 2008 jsuchome@suse.cz
- ag_anyxml: return every value as string (bnc#409491)
* Wed Jul 16 2008 locilka@suse.cz
- Support for conflicting services has been dropped from
  SuSEFirewall* modules (replaced by services defined by packages).
* Tue Jul 15 2008 locilka@suse.cz
- Fixed Linuxrc::SaveInstallInf function to really copy the
  /etc/install.inf at the end of the installation.
- Fixed ycpdoc warnings for SuSEFirewall*.ycp (added/fixed docu.)
* Fri Jul 11 2008 locilka@suse.cz
- Unified icons in Popup library using Icon library.
- Extended Icon library with 'question' icon.
- 2.17.7
* Thu Jul 10 2008 mvidner@suse.cz
- CWMTab: Added a nesting stack (bnc#406138); added LastTab() so
  that some modules continue to work (bnc#134386).
* Wed Jul  9 2008 locilka@suse.cz
- Making ProductControl::InitAutomaticConfiguration public to make
  it possible to call it directly from first stage installation
  worker (bnc #404122).
* Tue Jul  8 2008 locilka@suse.cz
- By default, firewall packages are just checked whether they are
  installed. CWM Firewall Interfaces does not offer to install them
  (bnc #388773).
- 2.17.6
* Mon Jul  7 2008 locilka@suse.cz
- Dropped deprecated functions from Wizard module:
  ReplaceNextButton, ReplaceBackButton, ReplaceAbortButton.
- Added more documentation (examples).
* Sun Jul  6 2008 mzugec@suse.de
- possibility to disable FileChanges popup (bnc#383718)
* Tue Jul  1 2008 mzugec@suse.de
- new function is NetworkService::Networkv6Running()
- rewrite IP/PREFIXLEN for aliases in NetworkInterfaces
- 2.17.5
* Fri Jun 27 2008 lslezak@suse.cz
- adapted to the new patch messages and patch scripts callbacks
  (bnc#401220)
- 2.17.4
* Thu Jun 19 2008 aschnell@suse.de
- added Integer::RangeFrom, Integer::IsPowerOfTwo and Integer::Sum
- 2.17.3
* Wed Jun 18 2008 mzugec@suse.de
- moved DnsServerAPI testsuites to yast2-dns-server
- 2.17.2
* Wed Jun 18 2008 mzugec@suse.de
- use PREFIXLEN in NetworkInterfaces
- fixed testsuites (added IPv6 tests)
- 2.17.1
* Mon Jun 16 2008 locilka@suse.cz
- Added "ellipsis" to the "Firewall Details" generic button
  (bnc #395433).
* Fri Jun 13 2008 aschnell@suse.de
- added Integer.ycp module with Range function
- 2.17.0
* Fri Jun 13 2008 locilka@suse.cz
- Opening fallback ports in case of SSH and / or VNC installation
  when firewall services (defined by packages) are not installed
  (bnc #398855).
- DnsServerAPI testsuites moved here from yast2-dns-server.
- Adjusted RPM dependencies (Conflicts: yast2-dns-server < 2.17.0).
* Wed Jun 11 2008 locilka@suse.cz
- All SUSEFirewallServices were dropped, since now we only support
  services defined by packages.
* Mon Jun  9 2008 mzugec@suse.cz
- DnsServerApi.pm moved from dns-server (bnc#392606)
* Fri Jun  6 2008 mzugec@suse.cz
- installation onto nfs - STARTMODE='nfsroot' (bnc#397410)
* Fri Jun  6 2008 locilka@suse.cz
- Fixed Progress stages layout, stage-mark has a reseved space now
  (bnc #395752).
- Using 'rpmqpack' in PackageSystem::PackageInstalled because it is
  a way faster than 'rpm' itself.
* Wed Jun  4 2008 lslezak@suse.cz
- added PackageLock::Connect() - similar to PackageLock::Check()
  but [Abort] is always displayed and [Continue] is optional
  (bnc#293356)
* Tue Jun  3 2008 locilka@suse.cz
- Always calling NetworkInterfaces::Read in SuSEFirewall::Read
  (bnc #396646)
* Fri May 23 2008 jsrain@suse.cz
- adjusted button handling in CWM (bnc#392983)
- 2.16.71
* Thu May 22 2008 lslezak@suse.cz
- Added Product::ReadProducts() to explicitly read products from
  the package manager (bnc#390738)
- 2.16.70
* Thu May 22 2008 mzugec@suse.cz
- test if disk is network based in NetworkStorage (bnc#384420)
- 2.16.69
* Tue May 20 2008 locilka@suse.cz
- Updated SuSEfirewall2 service-translations (generated from PDB).
* Fri May 16 2008 jsrain@suse.cz
- added categories Settings and System into desktop file
  (bnc #382778)
* Fri May 16 2008 sh@suse.de
- Fixed bnc #374704: Missing wizard icons
  Now providing a default icon until the YCP app sets one
- V 2.16.68
* Wed May 14 2008 jsrain@suse.cz
- propagate the yast2 --gtk and --qt switches from control center
  to running individual modules (bnc #389714)
- 2.16.67
* Tue May 13 2008 mzugec@suse.cz
- isDiskOnNetwork::NetworkStorage added test for nfs (bnc#384420)
- 2.16.66
* Tue May 13 2008 lslezak@suse.cz
- PackageSystem::EnsureSourceInit() - do not display "No package
  source defined" when installing from liveCD (bnc#389688)
- 2.16.65
* Mon May 12 2008 mvidner@suse.cz
- Report::{Long,}{Message,Warning,Error}: log the text before popping
  up a dialog so that eager bug reporters have the last message in the
  log (bnc#381594#c15).
* Fri May  9 2008 aschnell@suse.de
- Fixed keyboard on PPC during installation (bnc #387567)
- 2.16.64
* Fri May  9 2008 locilka@suse.cz
- Fixed TSIG key generation (bnc #387099).
- 2.16.63
* Wed May  7 2008 lslezak@suse.cz
- Progress:: store the current values correctly when a nested
  progress is started
* Mon May  5 2008 mvidner@suse.cz
- Pass client arguments as literal strings, not YCP values.
  It broke for "/tmp/windomain\theuser-tmpdir" (bnc#382883).
- Fixed the bnc#382216 fix for non-/usr prefix.
- 2.16.62
* Fri May  2 2008 lslezak@suse.cz
- Mode::test(), PakageCallbacks - do not call UI:: functions in
  command line mode (do not initialize UI) (another fix for
  bnc#374259)
- 2.16.61
* Wed Apr 30 2008 lslezak@suse.cz
- Product.ycp - properly set 'name' and 'short_name' (bnc#368104)
* Tue Apr 29 2008 lslezak@suse.cz
- moved ag_content agent (.content_file path) from yast2-instserver
  package here so it can be shared by yast2-instserver and
  yast2-product-creator (bnc#339126)
- 2.16.60
* Mon Apr 28 2008 lslezak@suse.cz
- Abort completete autorefresh when [Abort] is pressed after
  a download problem (bnc #382377)
- 2.16.59
* Fri Apr 25 2008 lslezak@suse.cz
- do not use UI:: call while importing PackageCallbaks module
  (initializes UI even in command line mode) (bnc#374259)
- 2.16.58
* Thu Apr 24 2008 jsuchome@suse.cz
- added missing anyxml.scr
- 2.16.57
* Wed Apr 23 2008 locilka@suse.cz
- Fixing CWMFirewallInterfaces to appropriately handle interfaces
  in unprotected internal zone (bnc #382686).
- 2.16.56
* Wed Apr 23 2008 mvidner@suse.cz
- Make the yast2 script work even with trailing slashes in $PATH
  (bnc#382216).
* Wed Apr 23 2008 lslezak@suse.cz
- PackageSystem.ycp - do not initialize the package callbacks,
  they are already initialized in PackageCallbacks constructor
- Product.ycp - do not initialize the package manager, read the
  installed product from /etc/SuSE-relase file instead (bnc#380652)
- 2.16.55
* Tue Apr 22 2008 jsrain@suse.cz
- rename MODLIST variable to YAST_MODLIST to prevent conflicts
  with zypper (bnc #382097)
* Mon Apr 21 2008 jsrain@suse.cz
- fixed CWM testsuite
- 2.16.54
* Fri Apr 18 2008 lslezak@suse.cz
- Kernel.ycp - check XEN detection result for nil, nil means XEN
  was not found
* Thu Apr 17 2008 locilka@suse.cz
- Using `InputFiled instead of obsolete `TextEntry (in CWM).
- Adjusted CWM testsuite.
- 2.16.53
* Wed Apr 16 2008 kmachalkova@suse.cz
- Wizard.ycp: Generic tree dialog introduced - left help panel
  might be removed, but menu tree must stay (FaTE #303291 related)
* Tue Apr 15 2008 lslezak@suse.cz
- PackageCallbacks.ycp - added RegisterEmptyProgressCallbacks() and
  RestorePreviousProgressCallbacks() functions for disabling and
  restoring progress callbacks (bnc#377919)
- 2.16.52
* Mon Apr 14 2008 sh@suse.de
- Open wizard dialogs with `opt(`wizardDialog) in Wizard.ycp
- V 2.16.51
* Mon Apr 14 2008 lslezak@suse.cz
- Products.ycp - the target and the sources must be initialized
  and the solver must be run to obtain the list of installed
  products (bnc #368104)
* Mon Apr 14 2008 locilka@suse.cz
- Enhanced firewall-services translations script to generate a bit
  more usefule output for translators.
* Mon Apr 14 2008 jsrain@suse.cz
- regenerated yast2-services-translations (bnc #373969)
- 2.16.50
* Sun Apr 13 2008 aschnell@suse.de
- refactoring and fixing LogView.ycp (bnc #371983)
- 2.16.49
* Fri Apr 11 2008 locilka@suse.cz
- New Wizard::OpenOKDialog() (FATE #120373).
* Fri Apr 11 2008 mvidner@suse.cz
- FileChanges::FileChangedFromPackage: fixed to actually consider the
  file parameter
* Thu Apr 10 2008 kmachalkova@suse.cz
- Hostname.ycp: new functions for retrieving current FQDN, hostname
  and domain name (for FaTE #302863)
- 2.16.48
* Thu Apr 10 2008 kmachalkova@suse.cz
- Progress.ycp: use UI::GetDisplay info only when it is really
  needed, not on global level (it instantiates UI and makes CLI
  deaf-dumb in ncurses which set terminal echo to off) (bnc #374259)
* Wed Apr  9 2008 jsrain@suse.cz
- use only one 'tail' command in LogView if not using grep to
  filter a log in order to avoid buffering (bnc #371983)
- 2.16.47
* Wed Apr  9 2008 locilka@suse.cz
- Added support for Samba Broadcast Reply (FATE #300970).
- Updated Firewall Services translations.
- Renamed SuSEfirewall2 SCR agent to help to make SCR lazy.
* Tue Apr  8 2008 lslezak@suse.cz
- call Pkg::TargetInit() in PackageSystem::EnsureTargetInit()
  to load installed packages
- only PAE version of kernel-xen is shipped (kernel-xenpae is now
  kernel-xen)
* Fri Apr  4 2008 locilka@suse.cz
- Added GetInstArgs::automatic_configuration for easier handling
  of the automatic configuration process.
- InstExtensionImage changed to use new 'extend' command
  (bnc #376870).
- Function AddXenSupport doesn't change FW_FORWARD_ALWAYS_INOUT_DEV
  anymore. The whole functionality is handled by SuSEfirewall2
  itself (bnc #375482).
- 2.16.46
* Fri Apr  4 2008 jsrain@suse.cz
- avoid calling PackageCallbacksInit::InitPackageCallbacks () to
  prevent testsuites of other packages from failing
- 2.16.45
* Thu Apr  3 2008 lslezak@suse.cz
- fixed build (missing in -M option in Makefile.am)
- 2.16.44
* Wed Apr  2 2008 mzugec@suse.de
- added type "password" into CWM
- 2.16.43
* Wed Apr  2 2008 lslezak@suse.cz
- moved package callbacks implementation from yast2-packager
  to yast2 (to break cyclic dependency) (fate#302296)
- 2.16.42
* Wed Apr  2 2008 locilka@suse.cz
- SCR Agent for managing /etc/ssh/sshd_config has been moved here
  from yast2-sshd.
- Adjusted RPM dependencies.
- 2.16.41
* Tue Apr  1 2008 aschnell@suse.de
- let String::FormatSizeWithPrecision return "1 MB" instead of
  "1024 kB" and alike
- fixed String::FormatSizeWithPrecision to return a unit for small
  values
* Tue Apr  1 2008 jsrain@suse.cz
- merged texts from proofread
* Mon Mar 31 2008 mvidner@suse.cz
- Don't document a feature that is unclear and was never there
  (bnc#373187).
* Wed Mar 26 2008 jsuchome@suse.cz
- added new anyxml agent, now using perl-XML-Simple library
  (bnc #366867)
- 2.16.40
* Wed Mar 19 2008 locilka@suse.cz
- anyxml agent renamed to barexml (bnc #366867)
- 2.16.39
* Wed Mar 19 2008 jsrain@suse.cz
- fixed efika detection (bnc #369045)
* Tue Mar 18 2008 locilka@suse.cz
- Changed the default value for use-automatic-configuration in
  ProductControl module, now it's false (Also because of AutoYaST).
- Better logging.
- 2.16.38
* Mon Mar 17 2008 aschnell@suse.de
- added LogViewCore.ycp
- added WaitForEvent to Wizard.ycp
- 2.16.37
* Mon Mar 17 2008 jsrain@suse.cz
- added 'StartupNotify=true' to the desktop file (bnc #304964)
* Fri Mar 14 2008 locilka@suse.cz
- Several changes in ProductControl modules for automatic
  configuration and easies enabling and disabling modules.
- DisabledModules and DisabledProposals were made local and acces
  to them is available via functional API only. Both for
  (fate #303396).
- 2.16.36
* Fri Mar 14 2008 jsrain@suse.cz
- fixed textdomain
* Wed Mar 12 2008 locilka@suse.cz
- Adjusted ProductControl to evaluate `accept and `ok as if it was
  `next (bnc #369846).
- 2.16.35
* Tue Mar 11 2008 jsrain@suse.cz
- added infrastructure to detect configuration files changed not
  by YaST and warn users about such changes possibly getting lost
  (fate #303374)
* Tue Mar 11 2008 lslezak@suse.cz
- improved String::FormatRateMessage() (needed for bnc #168935)
- 2.16.34
* Wed Mar  5 2008 lslezak@suse.cz
- register Refresh callbacks (required for FATE #30962, bnc #231745)
- 2.16.33
* Wed Mar  5 2008 aschnell@suse.de
- set Qt style during installation
* Wed Mar  5 2008 locilka@suse.cz
- Do not try to change the Wizard widget if no such widget exists
  (ncurses) reuse the Back button instead (bnc #367213).
- 2.16.31
* Tue Mar  4 2008 locilka@suse.cz
- Replacing obsolete ag_background with new ag_process in Service
  YCP module.
- Adjusted RPM dependencies.
* Wed Feb 27 2008 coolo@suse.de
- new version
- V 2.16.30
* Fri Feb 22 2008 jsuchome@suse.cz
- added ProductControl::EnableModule, ProductControl::DisabledModule
* Thu Feb 21 2008 sh@suse.de
- Added new UI packages to Requires/BuildRequires in .spec file
- No more fullscreen for sw_single (coolo's wish)
- V 2.16.29
* Mon Feb 18 2008 coolo@suse.de
- fix build
- 2.16.28
* Mon Feb 18 2008 mzugec@suse.de
- NetworkService::NetworkRunningPopup() changed to confirmation
* Mon Feb 18 2008 lslezak@suse.cz
- URL::Parse() - parse "dir:///" correctly
* Fri Feb 15 2008 jsrain@suse.cz
- added variables to define whether installing from RPM packages
  or images
* Thu Feb 14 2008 mzugec@suse.de
- added Confirm::RunningNetwork() for bnc#360571
- 2.16.27
* Wed Feb 13 2008 jsrain@suse.cz
- Defined filename of file to force update instead of installation
* Fri Feb  8 2008 locilka@suse.cz
- Umounts performed by InstExtensionImage use -f -l -d (force,
  lazy, free the used loop device as well).
* Thu Feb  7 2008 locilka@suse.cz
- Module InstExtensionImage moved here from installation.
- Added possibility to disintegrate extensions integrated by
  InstExtensionImage module.
- 2.16.26
* Wed Feb  6 2008 locilka@suse.cz
- Restoring buttons in ProductControl after every single client
  call to prevent from breaking the installation workflow.
* Tue Feb  5 2008 kmachalkova@suse.cz
- Progress.ycp: Use the presence of progress bar widget to determine
  whether some progress is running (querying progress counter is not
  enough, previous modules might have failed to reset it correctly)
* Mon Feb  4 2008 mzugec@suse.de
- Confirm::RunningNetwork() moved to
  NetworkService::NetworkRunningPopup()
* Fri Feb  1 2008 locilka@suse.cz
- Added new functions into the URL module: MakeMapFromParams and
  MakeParamsFromMap.
- Fixed deprecated find() calls in URL module.
- 2.16.25
* Mon Jan 28 2008 locilka@suse.cz
- Adjusted SCR agent for SuSEfirewall2 sysconfig file. Values can
  use also single quotes, not only double-quotes (bnc#327565).
* Mon Jan 28 2008 locilka@suse.cz
- Removing useless Wizard() calls in ProductControl to minimize the
  Wizard redrawing.
* Mon Jan 28 2008 aschnell@suse.de
- support Qt and Gtk frontend in startup scripts
- 2.16.24
* Sun Jan 27 2008 coolo@suse.de
- fixing changelog
* Thu Jan 24 2008 mzugec@suse.cz
- replace deprecated NetworkDevices by NetworkInterfaces
- 2.16.23
* Thu Jan 24 2008 lslezak@suse.cz
- Fixed testing UI::WidgetExists() call result (it can return nil,
  it must be explicitly compared to true)
- Added pre-requires for fillup into .spec file (for filling up
  sysconfig.yast2 template)
- 2.16.23
* Tue Jan 22 2008 lslezak@suse.cz
- Progress::New() can be called recursively - a nested progress
  can run inside the main progress (part of bug #352007)
- added wizard/doc/examples/progress_*.ycp examples how to use
  this feature
- 2.16.22
* Mon Jan 21 2008 locilka@suse.cz
- Disabled HTTP and HTTPS services in list of hard-coded
  SuSEfirewall2 services (replaced with services defined by pkgs).
- Disabled also SSH, DHCP server/client, NIS client.
- Function GetFilenameFromServiceDefinedByPackage has been made
  global.
- Fixed SuSEFirewall testsuite and possibly conflicting services.
* Fri Jan 18 2008 kmachalkova@suse.cz
- Re-enabled threading in ncurses UI (bug #164999, FaTE #301899)
* Thu Jan 17 2008 lslezak@suse.cz
- use `BusyIndicator widget for `tick subprogress in Progress::
  (#351933)
- register AcceptWrongDigest AcceptUnknownDigest callbacks
- 2.16.21
* Fri Jan 11 2008 mzugec@suse.de
- remove ocurrences of deprecated NetworkInterfaces::device_name
* Tue Jan  8 2008 mzugec@suse.cz
- added NetworkInterfaces module (NetworkDevices will be deprecated)
- 2.16.20
* Tue Jan  8 2008 jsrain@suse.cz
- disable tab-completion after -i, --install, --remove and
  - - update (#341706)
* Tue Jan  8 2008 kmachalkova@suse.cz
- Fixed crash when running text-mode menu as non-root user (new
  libyui throws an exception if SelectionBox entry is nil)
* Tue Jan  8 2008 jsrain@suse.cz
- offer possibility to define UI via cmdline parameter (#348817)
* Fri Jan  4 2008 lslezak@suse.cz
- Progress:: do not replace the subprocess widget, try to reuse the
  existing widget if possible (avoids screen flickering) (#350584)
- 2.16.19
* Thu Dec 13 2007 mzugec@suse.de
- NetworkDevices::CleanCacheRead() to reset and re-read
  .sysconfig.network.ifcfg* because of network proposal (#170558)
- NetworkDevices::GetDeviceTypes() - list of netcard devices for
  this architecture
- NetworkDevices::GetDevTypeDescription() moved from network module
  (routines/summary device_types, routines/complex device_names)
- 2.16.18
* Mon Dec 10 2007 locilka@suse.cz
- Adjusted RPM dependencies:
  * Conflicts yast2-country < 2.16.3 because of moving some files
    from that package here.
  * yast2-pkg-bindings >= 2.16.5 needed already in build-time.
* Fri Dec  7 2007 lslezak@suse.cz
- Progress:: - added support for subprogress
  (see Progress::Subprogress*() functions)
- InitPackageCallbacks() - register Process* callbacks
- 2.16.17
* Fri Dec  7 2007 jsuchome@suse.cz
- country.ycp and country_long.ycp moved here from yast2-country
  to remove a dependency on yast2-country by some packages
* Fri Dec  7 2007 jsrain@suse.cz
- fixed validation of CWM tab widget (#346751)
* Thu Dec  6 2007 mzugec@suse.cz
- added vlan into device types list
* Wed Dec  5 2007 sh@suse.de
- Dropped obsolete --noborder option for /sbin/yast2
* Mon Dec  3 2007 locilka@suse.cz
- Adjusted RPM dependencies: mod_UI in yast2-core.
- Updated Progress with icons to rather use Image-Dimm support
  if available.
- Added new Icon YCP module to provide basic acces to icon files.
- Popup::ConfirmAbort now uses Icons.
- 2.16.16
* Mon Dec  3 2007 ug@suse.de
- XMLToYCPString added to convert an XML string to
  YCP data
* Thu Nov 29 2007 locilka@suse.cz
- Progress module has been extended to show icons for stages.
  Function NewProgressIcons() just extends the New() function
  with list of images to be shown.
* Thu Nov 29 2007 mzugec@suse.cz
- for AY Confirm::Detection popup has timeout 10 seconds (#192181)
- 2.16.15
* Tue Nov 27 2007 sh@suse.de
- Require yast2-core >= 2.16.10 in .spec
- 2.16.14
* Tue Nov 27 2007 mvidner@suse.cz
- Wizard::ShowReleaseNotesButton id is string, not any.
- 2.16.13
* Tue Nov 27 2007 mvidner@suse.cz
- /sbin/yast2: Factored out the y2base loop. Exit it on failure (#343258).
* Fri Nov 23 2007 mzugec@suse.cz
- fixed URL module for "smb" type
- 2.16.12
* Thu Nov 22 2007 locilka@suse.cz
- Fixed URL.ycp documentation, added some examples.
* Wed Nov 21 2007 mzugec@suse.cz
- title-style capitalization of GetDeviceType() (#223873)
* Tue Nov 20 2007 locilka@suse.cz
- Added new Internet::ShutdownAllLocalDHCPClients function
  for killing dhcpcd (#308577).
* Mon Nov 19 2007 kmachalkova@suse.cz
- Initialize locale variables (UTF-8 or not) properly to prevent
  displaying garbled characters in console (#335246) (thanks, mfabian
  and werner)
* Fri Nov 16 2007 locilka@suse.cz
- SCR agent for any_XML has been moved from yast2-packager-2.16.5
  to yast2-2.16.11 (#332187).
- Adjusted RPM dependencies.
- 2.16.11
* Fri Nov  9 2007 jsrain@suse.cz
- added manpage for yast (#336004)
- initialize product name during live installation properly
  (#297609)
- changed labels of software confirmation popup to Install/Cancel,
  resp. Uninstall/Cancel (#215195)
- 2.16.10
* Wed Nov  7 2007 mzugec@suse.cz
- added new function ListDevicesExcept(string)
- 2.16.9
* Tue Nov  6 2007 locilka@suse.cz
- Added new YCP module AutoinstData (which holds all data shared
  between Autoinstallation and other YaST modules) to break cyclic
  dependencies.
- Adjusted RPM dependencies.
- 2.16.8
* Mon Nov  5 2007 locilka@suse.cz
- Dirinstall-related global data added to Installation YCP module.
- 2.16.7
* Fri Nov  2 2007 locilka@suse.cz
- YCP module Internet moved from yast2-network to yast2 to remove
  RPM dependencies.
- Adjusted RPM dependencies.
- Added some more texts for firewall services defined by packages.
- Some functions from Internet were moved to newly created
  InternetDevices because of dependency on Provirer module.
- 2.16.6
* Thu Nov  1 2007 locilka@suse.cz
- Update/backup-related variables were moved from  Update::* to
  Installation::update_* to remove RPM dependencies.
- 2.16.5
* Wed Oct 31 2007 locilka@suse.cz
- installedVersion and updateVersion moved from 'Update' to
  'Installation' YCP module to remove dependencies.
- 2.16.4
* Tue Oct 30 2007 locilka@suse.cz
- Modules Hotplug and HwStatus moved here from yast2-installation
  to remove yast2-storage dependency on yast2-installation.
- Adjusted RPM dependencies.
- 2.16.3
* Tue Oct 23 2007 jsrain@suse.cz
- kernel-bigsmp renamed to kernel-pae
- 2.16.2
* Thu Oct 11 2007 locilka@suse.cz
- New function FileUtils::MD5sum.
- Merging every single workflow only once, skipping duplicate
  additional workflows even if provided by a different file name
  (#332436).
- Merging control-file texts in WorkflowManager as well (#271608).
* Thu Oct  4 2007 jsrain@suse.cz
- install bigsmp kernel regardless the memory size (Fate #159006)
- 2.16.1
* Wed Oct  3 2007 mvidner@suse.cz
- Do not try to package COPYRIGHT.english, it is gone from
  devtools (#299144).
- 2.16.0
* Wed Sep 26 2007 kmachalkova@suse.cz
- Text-mode control center: do not show groups containing no modules
  to the user (#309452)
* Wed Sep 12 2007 jsrain@suse.cz
- reverted Fate #159006 (always using bigsmp kernel if PAE detected)
  (#309468)
- 2.15.58
* Tue Sep 11 2007 varkoly@suse.de
- Fixed Provides list (#309420)
* Mon Sep 10 2007 locilka@suse.cz
- Fixed agent for /content file to correctly identify the key and
  the value (#305495).
- 2.15.57
* Thu Sep  6 2007 tgoettlicher@suse.de
- fixed mouse cursor for links (#304679)
- 2.15.56
* Wed Sep  5 2007 jsrain@suse.cz
- handle missing /usr/bin/id properly (#307375)
- 2.15.55
* Mon Sep  3 2007 mvidner@suse.cz
- Mail via AutoYaST: do not omit the colon separator in /etc/aliases;
  fixed warnings about undefined variables (#304190).
- 2.15.54
* Mon Sep  3 2007 lslezak@suse.cz
- added fallback for "kernel-iseries64" - use "kernel-ppc64",
  when it's not available (#302246)
- properly check whether a kernel package is available (use package
  name instead of 'provides' capability), fixed check in 'repair'
  mode (#302246, #299683)
- added Package::PackageAvailable() and Package::PackageInstaled()
  functions to check whether a package is available or installed
  (they check package name in contrast to Package::IsAvailable()
  and Package::IsInstalled() which check 'provides' capability)
- 2.15.53
* Mon Sep  3 2007 mvidner@suse.cz
- Use xmessage only if y2base fails. Don't use it for harmless
  warnings (#265263#c59).
- 2.15.52
* Fri Aug 31 2007 locilka@suse.cz
- Fixing evaluation of unreadable cpuflags in Kernel.ycp (#303842).
- 2.15.51
* Thu Aug 30 2007 jsrain@suse.cz
- removed the -s/--style option from manpage and help (#300362)
* Thu Aug 30 2007 jsrain@suse.cz
- updated list of fallback kernels (no longer kernel-smp) (#304646)
- 2.15.50
* Thu Aug 30 2007 jsrain@suse.cz
- updated list of modules not to add to initrd (#298726)
- 2.15.49
* Tue Aug 28 2007 mzugec@suse.cz
- add filter and log for output of NetworkDevices::List() (#303858)
* Tue Aug 28 2007 locilka@suse.cz
- Fixed SuSEFirewall to better handle erroneous data from
  NetworkDevices module (#303858).
* Mon Aug 27 2007 sh@suse.de
- Fixed bug #304776: save_y2logs usage message
* Fri Aug 24 2007 mzugec@suse.cz
- add "ath" into "netcard" macro in NetworkDevices (#288450)
- 2.15.48
* Sun Aug 12 2007 coolo@suse.de
- avoid conflicts without version
* Fri Aug 10 2007 locilka@suse.cz
- Preselect "Add Online Repositories Before Installation" check-box
  in the "Installation Mode" dialog (#299207).
- 2.15.47
* Fri Aug 10 2007 jsrain@suse.cz
- conflict older versions of packages which files were moved here
  from (#294054)
- 2.15.46
* Fri Aug 10 2007 locilka@suse.cz
- Updated firewall-related texts for services defined by packages.
* Thu Aug  2 2007 lslezak@suse.cz
- register download callbacks (#292629)
- 2.15.45
* Mon Jul 30 2007 jsrain@suse.cz
- install bigsmp kernel regardless the memory size (Fate #159006)
- 2.15.42
* Thu Jul 26 2007 jsrain@suse.cz
- added Provides: yast2-devel to yast2-devel-doc
- 2.15.43
* Wed Jul 25 2007 locilka@suse.cz
- Renamed yast2-devel to yast2-devel-doc (FATE #302461).
- 2.15.42
* Sun Jul 22 2007 mzugec@suse.de
- don't use getcfg in IsConnected function
- 2.15.41
* Wed Jul 18 2007 lslezak@suse.cz
- PackageCallbacksInit.ycp - register ProgressReport callbacks
- 2.15.40
* Thu Jul 12 2007 jsrain@suse.cz
- disabled rpmlint checks for .desktop files in order to build
- 2.15.39
* Wed Jul  4 2007 locilka@suse.cz
- Fixed initrd testsuite
- 2.15.38
* Mon Jul  2 2007 locilka@suse.cz
- Fixed adding of firewall custom rules in case of empty
  destination port but source port set (#284998).
* Thu Jun 28 2007 jsrain@suse.cz
- added mode for live CD installation
- several updates for live CD installation
* Thu Jun 21 2007 adrian@suse.de
- fix changelog entry order
* Wed Jun 20 2007 locilka@suse.cz
- Extending Installation module to provide persistent information
  in Instalaltion Mode dialog.
* Tue Jun 19 2007 kmachalkova@suse.cz
- Respect user's choice and never unset LANG (yast2-funcs)
- Do not append .UTF-8 suffix to POSIX and C locale (/sbin/yast2)
  (#285178)
- 2.15.37
* Tue Jun 19 2007 locilka@suse.cz
- Allowing to go back in the installation workflow even if the
  workflow has changed. The condition must be explicitly set in
  the control file.
* Mon Jun 18 2007 jsrain@suse.cz
- check patch lenght before calling substring (#283146)
* Thu Jun 14 2007 kmachalkova@suse.cz
- Enable setting color theme of ncurses UI (Y2NCURSES_COLOR_THEME
  variable added to sysconfig, exported by /sbin/yast2 if defined)
  (FaTE #301893))
* Tue Jun 12 2007 mzugec@suse.cz
- fixed CheckDomain function - allow "." character at the end
  of domain name (suse.cz.)
- 2.15.36
* Thu Jun  7 2007 lslezak@suse.cz
- speed up PackageSystem::InstallKernel() - call rpm directly
  instead of starting the package manager
- display licenses in the command line mode properly,
  fixed prompt when removing packages (#270910)
* Tue Jun  5 2007 locilka@suse.cz
- Extended PackageLock::Check function to allow to 'Retry' getting
  the package management lock (#280383).
* Fri Jun  1 2007 mzugec@suse.cz
- add function NetworkService::isNetworkRunning()
- NetworkStorage moved here from yast2-network
- 2.15.35
* Wed May 30 2007 sh@suse.de
- Fixed bug #278790: save_y2logs complains about missing RPM DB
* Tue May 29 2007 lslezak@suse.cz
- updated metadata in the sysconfig file (#278612)
* Fri May 25 2007 jsrain@suse.cz
- fixed spec file (removed duplicate .desktop files translations)
- removed translations from .desktop-files (#271209)
- 2.15.34
* Mon May 21 2007 kmachalkova@suse.cz
- Do not show empty xmessage window if nothing is printed to stderr
  after yast module has exited (mvidner's patch for #265263)
* Mon May 21 2007 jsrain@suse.cz
- fixed chrp board detection (PPC) (#273606)
- do not check UI mode when enabling the 'Use LDAP' widget in
  service dialog (#274649)
* Thu May 17 2007 lslezak@suse.cz
- Fixed testsuite for String.ycp
- 2.15.33
* Thu May 17 2007 kmachalkova@suse.cz
- Do not request link state of network devices from ethtool (ask
  sysfs instead) so that yast2 does not require ethtool (#256382)
* Wed May 16 2007 locilka@suse.cz
- Added checking for allowed "ssh" TCP port into
  SuSEFirewallProposal module additionaly to "service:sshd"
  (related to #274761).
* Wed May  9 2007 lslezak@suse.cz
- fixed units - use "kB" instead of "KB" in strings (#270935)
* Mon May  7 2007 mvidner@suse.cz
- save_y2logs: do not query the RPM database if there is none, as
  in the inst-sys (#270321).
* Fri May  4 2007 locilka@suse.cz
- Added new refresh-srv-def-by-pkgs-trans.sh script that creates
  a YCP file containing translations for services defined by
  packages (FATE #30068).
- Added yast2-services-translations.ycp file with translations,
  textdomain is "firewall-services".
- Changed SuSEFirewallProposal to use new definition of services
  instead the old one from SuSEFirewallServices.
- Fixed BuildRequires (yast2-perl-bindings) after moving
  Mail-related perl modules to yast2 package.
- 2.15.32
* Thu May  3 2007 varkoly@suse.de
- Add new module file MailAlias.ycp (269867 - build cycle between
  yast2-users and yast2-mail)
- 2.15.31
* Thu May  3 2007 locilka@suse.cz
- Present more information to the user when calling a YaST client
  fails (#267886).
* Thu Apr 19 2007 mzugec@suse.cz
- added GetIP(device) function to get first+additional addresses (#264393)
- 2.15.30
* Thu Apr 19 2007 jsrain@suse.cz
- fixed path to GNOME control center (#245970)
* Wed Apr 18 2007 locilka@suse.cz
- FileUtils::CheckAndCreatePatch function has been fixed not to
  turn "/" into empty string (#203363).
- 2.15.29
* Fri Apr 13 2007 locilka@suse.cz
- Added 'modified' flag into SuSEFirewallServices module. This
  makes SuSEFirewall module to restart SuSEfirewall2 in case of
  changed only SuSEFirewallServices settings.
* Thu Apr 12 2007 locilka@suse.cz
- Added new SetNeededPortsAndProtocols() function into
  SuSEFirewallServices module. It allows to modify services defined
  by packages described in FATE #300687.
- 2.15.28
* Thu Apr 12 2007 mvidner@suse.cz
- Detect Efika board type, handle it like Pegasos (#259827).
- Fixed /sbin/yast2 to pass on the return value of y2base and of the
  control center (#263412).
- Let /sbin/yast2 redirect its output to xmessage if appropriate
  (#211392).
- 2.15.27
* Wed Apr 11 2007 lslezak@suse.cz
- properly detect PV/FV Xen machine (#255217)
- 2.15.26
* Fri Apr  6 2007 locilka@suse.cz
- Adding new Installation::reboot_net_settings that will point to
  a file storing current nework services settings when rebooting
  a computer during installation (#258742).
- Adding comments for Installation::* variables
- 2.15.25
* Fri Apr  6 2007 lslezak@suse.cz
- register Pkg::CallbackAuthentication() callback (#190609)
- 2.15.24
* Mon Apr  2 2007 jsuchome@suse.cz
- fixed restarting after Patch CD update (#259825)
- 2.15.23
* Mon Apr  2 2007 lslezak@suse.cz
- register new callbacks Pkg::CallbackSourceCreateInit/Destroy()
  and Pkg::CallbackSourceReportInit/Destroy() (#251726)
* Mon Apr  2 2007 locilka@suse.cz
- Changed Firewall proposal to be unified with other network
  proposals, e.g., "Firewall is enabled (disable)" (#259778).
* Fri Mar 30 2007 locilka@suse.cz
- SCR agent proc_meminfo.scr moved from yast2-storage to yast2
* Thu Mar 29 2007 locilka@suse.cz
- Added new WorkflowManager testsuite
- Added some debugging functions into WorkflowManager
- Changed ProductControl for easier testing
* Wed Mar 28 2007 locilka@suse.cz
- Some testsuites have been moved from yast2-packager to yast2
- 2.15.22
* Wed Mar 28 2007 locilka@suse.cz
- A new YCP module WorkflowManager has been created in order to
  unifys Add-On and Patterns in their possibility to influence the
  installation and configuration workflow (FATE #129).
- 2.15.21
* Fri Mar 23 2007 jsrain@suse.cz
- use Qt control center instead of Gtk and vice versa if the preffered
  one doesn't exist, fixed path to Gtk control center (#255745)
- fixed focus switching when changing dialogs in tree dialog (#239775)
* Wed Mar 21 2007 locilka@suse.cz
- Using SuSEFirewall::SuSEFirewallIsInstalled also internally in
  some SuSEFirewall functions.
* Wed Mar 21 2007 lslezak@suse.cz
- added hwinfo/classnames.ycp (from yast2-tune) (#253486)
- 2.15.20
* Mon Mar 19 2007 jsrain@suse.cz
- fixed selecting proper dialog in DialogTree in case of widget
  validation failed (#253488)
* Tue Mar 13 2007 jsrain@suse.cz
- added yast2-perl-bindings to Requires (#253514)
* Mon Mar 12 2007 mzugec@suse.cz
- sysconfig/network: use IPADDR/PREFIXLEN as default instead of NETMASK (#231997)
- 2.15.19
* Mon Mar 12 2007 locilka@suse.cz
- Modules 'Product' and 'Installation' (installation settings) were
  moved from 'yast2-installation' to 'yast2' to minimize
  cross-package dependencies.
- Adjusted package-conflicts.
- 2.15.18
* Fri Mar  9 2007 locilka@suse.cz
- Changing 'xenbr0' in SuSEfirewall2's FW_FORWARD_ALWAYS_INOUT_DEV
  to 'xenbr+' to match all XEN bridges. XEN bridge name is newly
  dependent on network interface number (#233934).
* Thu Mar  8 2007 jsuchome@suse.cz
- added SLPAPI.pm, Perl API for SLP agent (#238680)
- 2.15.17
* Thu Mar  8 2007 locilka@suse.cz
- Module GetInstArgs moved from yast2-installation to yast2, many
  clients required yast2-installation only because of this module.
- Added documentation of functions into that module.
* Thu Mar  8 2007 jsrain@suse.cz
- added xinetd support to the CWM service start widget
* Wed Mar  7 2007 jsrain@suse.cz
- build correctly URL in case of multiple leading slashes in the
  path (#179623)
* Tue Mar  6 2007 locilka@suse.cz
- Adding more documentation into the FileUtils module (examples).
* Tue Mar  6 2007 locilka@suse.cz
- When updating the SuSEfirewall2 network interfaces, consider that
  interfaces needn't be assigned to zones only by SuSEFirewall but
  also by network modules. Do not change assignments which have
  been made already.
* Mon Mar  5 2007 locilka@suse.cz
- fixed SuSEFirewall testsuite
- 2.15.16
* Mon Mar  5 2007 jsrain@suse.cz
- fixed testsuite
* Fri Mar  2 2007 lslezak@suse.cz
- install Xen paravirtual drivers (xen-kmp-* package) if running in
  a fully virtualized guest (#241564)
- register new yast agents when a patch or a package has been
  installed (#250179)
- 2.15.15
* Thu Mar  1 2007 kmachalkova@suse.cz
- Added checking for root user into ncurses menu. If the user is not
  root, show notify popup and list only the modules that do not need
  root privileges (#246015)
* Thu Mar  1 2007 jsuchome@suse.cz
- Added command line help text describing format of the [string]
  type options (#248201)
* Wed Feb 28 2007 locilka@suse.cz
- Making yast2.rpm independent on SuSEfirewall2. The package is
  checked and installed in SuSEFirewall::Read() function. If user
  decides not to install it, Firewall functionality is disabled.
  Installing the SuSEfirewall2 package is possible only on the
  running system (#245506).
- Checking for firewall definitions installed during one YaST run.
  This check is forced when something tries to use unknown service
  definition.
- Disabling possibility to configure firewall in Installation in
  Network proposal when SuSEfirewall2 package is not installed.
- Changing directory of service definitions to
  /etc/sysconfig/SuSEfirewall2.d/services (bugzilla #247352
  comment #13).
* Wed Feb 28 2007 lslezak@suse.cz
- ProductControl::Run() - return `abort also in the firstboot
  stage (#247552)
- 2.15.14
* Tue Feb 27 2007 locilka@suse.cz
- Added and fixed support for Firewall Custom Rules (FATE #100068,
  FATE #120042).
- 2.15.13
* Fri Feb 23 2007 lslezak@suse.cz
- error handling in Package::Available*() - return nil if no
  installation source is available (#225484)
- 2.15.12
* Mon Feb 19 2007 lslezak@suse.cz
- NetworkPopup - fixed NFS browsing (the same problem was
  in #71064), display scan results in a simple popup
- 2.15.11
* Fri Feb 16 2007 lslezak@suse.cz
- added String::FormatFilename() and URL::FormatUrl() - functions
  for removing the middle part of an URL/file name (#221163)
- 2.15.10
* Thu Feb 15 2007 aosthof@suse.de
- Fixed ComputePackage() in library/system/src/Kernel.ycp to be
  able to check provided kernel packages in installed system
* Thu Feb 15 2007 lslezak@suse.cz
- register ScanDB callbacks (#219953)
- String.ycp - functions for formatting dowload rate string
  (required for #168935)
- /sbin/yast2 - added control center switching, configurable via
  sysconfig (fate #301082) (mmeeks)
- 2.15.9
* Tue Feb 13 2007 mvidner@suse.cz
- ModulesConf::RunDepmod: do it also on s390 (#192120).
* Mon Feb 12 2007 lslezak@suse.cz
- register TrustGpgKey() callback handler (#242087, #240771)
- 2.15.8
* Mon Feb 12 2007 jsrain@suse.cz
- added control center switching, configurable via sysconfig
  (fate #301082) (mmeeks)
* Fri Feb  9 2007 mvidner@suse.cz
- Set Mode::testMode () == "testsuite" automatically when running with
  yast2-testsuite (#243624).
- Adjusted SuSEFirewall testsuite to match the current
  Mode::testMode () implementation
- 2.15.7
* Fri Feb  9 2007 locilka@suse.cz
- Using SCR::UnregisterAgent() instead of SCR::UnmountAgent in
  SetDesktopIcon() in Wizard.ycp (#244046).
* Thu Feb  8 2007 locilka@suse.cz
- Tuning firewall services defined by packages (FATE #300687).
- Added a lot of documentation and examples and comments into the
  SuSEFirewall YCP module.
- 2.15.6
* Thu Feb  8 2007 kmachalkova@suse.cz
- Use UI::RunInTerminal in menu.ycp for text-mode only. In all other
  cases run appropriate module in Qt(Gtk)
- 2.15.5
* Wed Feb  7 2007 locilka@suse.cz
- Added support for firewall services defined by packages
  (FATE #300687).
- Adjusted SuSEFirewall testsuite.
* Mon Jan 29 2007 mzugec@suse.de
- Internet connection test fails on s390 (#238246)
- 2.15.4
* Tue Jan 23 2007 jsrain@suse.cz
- use --whatprovides when quering for an installed package (#76181)
* Mon Jan 22 2007 mzugec@suse.cz
- 2.15.3
- #237353 - use cache to avoid multiple confirmations for the same purpose
* Fri Jan 19 2007 jsuchome@suse.cz
- added new API to Popup: MessageDetails, WarningDetails, ErrorDetails,
  NotifyDetails (popup with text and Details button for extra info)
* Fri Jan 19 2007 locilka@suse.cz
- Added two new remarkable functions GetFirewallKernelModules and
  SetFirewallKernelModules into the SuSEFirewall module. They will
  allow to open FTP service in SuSEfirewall2.
- Adjusted testsuite on Firewall
* Thu Jan 18 2007 kmachalkova@suse.cz
- Avoid displaying empty strings in NetworkPopup (#220813, #223498)
* Tue Jan  9 2007 mzugec@suse.cz
- add bond device
* Mon Jan  8 2007 locilka@suse.cz
- Fixed handling Y2_GEOMETRY="-geometry XxY[+OffsX+OffsY]" and
  "--geometry XxY[+OffsX+OffsY]" in /sbin/yast2 call (#232568).
* Fri Jan  5 2007 lslezak@suse.cz
- gpg library: fixed export of a key, export key in ASCII or
  binary format, added passphrase widget/popup, API documentation,
  example code
- 2.15.2
* Thu Jan  4 2007 locilka@suse.cz
- Changed y2error() to y2warning() when using default value is
  Misc::SysconfigRead() (#231744).
* Thu Dec 21 2006 lslezak@suse.cz
- added a gpg library - a wrapper for gpg binary (GPG.ycp),
  CWM widgets (GPGWidgets.ycp)  (initial version)
* Thu Dec 14 2006 lslezak@suse.cz
- added Label::SkipButton() (#228370)
* Wed Dec 13 2006 lslezak@suse.cz
- URL.ycp: fixed url building and checking in Estonian locale
  (use [[:alpha:]] instead of [a-z] in regexps) (#227256)
- 2.15.1
* Thu Dec  7 2006 lslezak@suse.cz
- menu.ycp: `restart_menu is not needed anymore (#148683)
* Tue Dec  5 2006 kmachalkova@suse.cz
- Adapt ncurses menu.ycp for running yast modules as separate
  processes (#148683, #221254, #222547)
- Do not change LANG and LC_CTYPE when stdin does not support
  utf8 (testutf8 returns 0) (partly #179989)
- 2.15.0
* Tue Nov 28 2006 jsrain@suse.cz
- fixed board detection on PPC (#223872)
- 2.14.15
* Tue Nov 21 2006 mvidner@suse.cz
- Implemented yast2 --remove and yast2 --update (#222757).
  (It needs yast2-packager-2.14.8 to work.)
- 2.14.14
* Tue Nov 14 2006 kmachalkova@suse.cz
- Better selection of fastest available network device (checking
  for cable connection and status for NICs) (#214897)
- 2.14.13
* Mon Nov 13 2006 locilka@suse.cz
- Tuning the previous change not to use .target.tmpdir but using
  "/var/lib/YaST2" instead.
- 2.14.12
* Mon Nov 13 2006 locilka@suse.cz
- Calling /sbin/SuSEfirewall2 (start|stop) instead of
  Service::Start()/Service::Stop() for SuSEfirewall2_(init && setup)
  (#215416).
- Extended testsuite of SuSEFirewall module.
- 2.14.11
* Wed Nov  8 2006 mvidner@suse.cz
- Resubmitting to fix the build.
- 2.14.10
* Mon Nov  6 2006 mzugec@suse.cz
- #177560 - fixed corrupting sysconfig files after setting locale to et_EE
- set value to boolean if contains "yes" or "no"
- 2.14.9
* Fri Nov  3 2006 locilka@suse.cz
- Fixed handling of missign SuSE-release files (partly #217013).
* Fri Nov  3 2006 mvidner@suse.cz
- Manual page: documented the command line interface (jfriedl).
* Mon Oct 30 2006 locilka@suse.cz
- Stopping/Starting and/or Enabling/Disabling all SuSEfirewall2
  services even if one of them fails. Partly preventing from not
  writing the new status of services (bugzilla #215416).
- Restarting firewall in SuSEFirewall::ActivateConfiguration() even
  if the configuration is not changed but there are some RPC
  services in the configuration (bugzilla #186186).
- 2.14.8
* Wed Oct 25 2006 locilka@suse.cz
- Writing the client's return value to the log (ProductControl)
  for easier debugging (#214886).
* Tue Oct 24 2006 lslezak@suse.cz
- .etc.policykit agent - added documentation
- fixed script callback registration
* Tue Oct 24 2006 jsrain@suse.cz
- lazy initialization of list of YaST modules for bash completion
  (#212928)
* Mon Oct 23 2006 lslezak@suse.cz
- added .etc.policykit agent (reads/writes
  /etc/PolicyKit/privilege.d/*.privilege files), used for
  handling powermanagement permissions (fate #301180, bug #214272)
- 2.14.7
* Wed Oct 18 2006 locilka@suse.cz
- Returning `abort from ProductControl::Run in case of Abort button
  pressed during the second stage installation (FATE #300422).
- 2.14.6
* Wed Oct 18 2006 kmachalkova@suse.cz
- NetworkDevices: return device type (e.g. netcard, modem,..) in
  human readable form
- NetworkPopup: display more information (besides device id also
  type, name and IP address)
- Moved NetworkPopup.ycp from library/wizard to library/network
- 2.14.5
* Mon Oct 16 2006 lslezak@suse.cz
- register script callbacks (feature #100233)
- 2.14.4
* Mon Oct 16 2006 mvidner@suse.cz
- /sbin/yast2: make ldd "not found" messages visible so that there is
  a hint about why a UI plugin is not working (#211392).
* Tue Oct 10 2006 mvidner@suse.cz
- It is now configurable whether to use Qt or GTK GUI,
  see "man yast2" (F#301083).
- 2.14.3
* Tue Oct  3 2006 jsrain@suse.cz
- reverted bigsmp kernel usage
- 2.14.2
* Mon Oct  2 2006 jsrain@suse.cz
- merged texts from proofread
- install bigsmp kernel regardless the memory size
- 2.14.1
* Wed Sep 27 2006 jsrain@suse.cz
- merged 10.2-only patches to SVN repository
- fixed Cell detection (#206539)
- 2.14.0
* Mon Sep 18 2006 lslezak@suse.cz
- use the new source callbacks (feature #1466),
  require yast2-pkg-bindigs >= 2.13.95
- 2.13.81
* Fri Sep 15 2006 mvidner@suse.cz
- Refactored Progress.ycp (but reverted the interface change).
- 2.13.80
* Wed Aug 30 2006 sh@suse.de
- Added output of "rpm -qa" to save_y2logs
  upon request at all-hands meeting 2006-08-29
- 2.13.79
* Wed Aug 30 2006 locilka@suse.cz
- DnsServerPunycode module moved from yast2-dns-server to yast2
  as Punycode module.
- 2.13.78
* Wed Aug 23 2006 jsrain@suse.cz
- added release-specific Xvnc parameters
- 2.13.77
* Wed Aug 23 2006 jsrain@suse.cz
- kernel-smp package is dropped for 10.2
- simplified kernel package detection for PPC for 10.2 (#195049)
- 2.13.76
* Tue Aug 22 2006 mvidner@suse.cz
- CWM::ShowAndRun: documented disable_buttons.
* Thu Aug 17 2006 jsrain@suse.cz
- initialize patch/delta RPM callbacks
- 2.13.75
* Thu Aug 10 2006 locilka@suse.cz
- Moved (x)inetd agent from yast2-inetd to yast2
- 2.13.74
* Wed Aug  9 2006 jsrain@suse.cz
- fixed recognizing pegasos, cell and maple boot requirements (PPC)
  (#192957)
* Wed Aug  9 2006 kmachalkova@suse.cz
- Added new Address::CheckMAC() and Address::ValidMAC() functions.
- 2.13.73
* Mon Aug  7 2006 locilka@suse.cz
- Added new IP::IPv4ToBits() and IP::BitsToIPv4() functions.
* Fri Aug  4 2006 jsrain@suse.cz
- added mode X-version-specific paths
- 2.13.72
* Thu Aug  3 2006 mvidner@suse.cz
- Start-up speed-up: don't read all desktop files to find our icon.
  Thanks to Michael Meeks for profiling.
- 2.13.71
* Wed Aug  2 2006 jsrain@suse.cz
- Added more X-version-specific paths
- 2.13.70
* Wed Aug  2 2006 locilka@suse.cz
- Added new module SuSEFirewallExpertRules managing expert ACCEPT
  rules of SuSEfirewall2.
- Port-ranges-related functionality in SuSEFirewall module moved
  to new module PortRanges.
* Tue Aug  1 2006 jsrain@suse.cz
- Added module and data file specifying X11 paths
* Wed Jul 26 2006 locilka@suse.cz
- Added new FileUtils::CheckAndCreatePath function that checks the
  current system for path existency and offers its creation if it
  doesn't exist.
- 2.13.69
* Tue Jul 25 2006 jsrain@suse.cz
- fixed error popup if log of mkinitrd could not be run (#156762)
- prevent from crash in DialogTree.ycp (#191237)
* Mon Jul 24 2006 locilka@suse.cz
- Fixed handling of multiline entries in the SuSEfirewall2
  sysconfig file. Newline characters were removed when joining
  multiline entries together. By now, .sysconfig.SuSEfirewall2
  returns values as it reads them, newlines are replaced with
  spaces in SuSEFirewall::Read() (#194419).
* Tue Jul 18 2006 jsrain@suse.cz
- fixed handling of translated strings in control file (eg.
  congratulate string)
- 2.13.68
* Tue Jul 18 2006 locilka@suse.cz
- Fixed proposal to reflect the current status better. Network
  interfaces might be assigned to the zone with 'any' in 'EXT'.
  If there are no network interfaces but SSH port is open, proposal
  informs about it (#154401).
- If there are only dial-up interfaces, SSH port can be also
  enabled and correctly informs about the current state.
* Sun Jul 16 2006 olh@suse.de
- introduce a Linuxrc::display_ip and use it instead of Arch::s390
- 2.13.67
* Fri Jul 14 2006 locilka@suse.cz
- Added better checking for wrong port-ranges. Invalid ones are
  stored in the configuration but ignored for firewall functions,
  such as joining port ranges.
- Joining ranges is possible only for TCP and UDP because other
  protocols don't support port ranges.
- Removing notes about NetworkManager from the SuSEFirewall
  documentation because it isn't needed to mention it there.
- 2.13.66
* Sat Jun 24 2006 locilka@suse.cz
- Adding special Xen interface "xenbr0" into the
  FW_FORWARD_ALWAYS_INOUT_DEV variable in the Network Proposal in
  case of "kernel-xenpae" package installed (#154133) (Similar to
  change in 2.13.43).
- 2.13.65
* Tue Jun 13 2006 jsrain@suse.cz
- fixed encoding/decoding query part of URL (#179913)
- 2.13.64
* Mon Jun 12 2006 mvidner@suse.cz
- Moved cfg_security.scr from yast2-security.rpm to yast2.rpm
- Do not sit in a networked directory when reconfiguring network
  (#61055, reapplied lost fix).
- 2.13.63
* Mon Jun 12 2006 locilka@suse.cz
- Do not register Signature Callbacks in case of AutoInst (#183821)
- 2.13.62
* Fri Jun  2 2006 jsrain@suse.cz
- Marked global API of following modules as stable:
    ProductFeatures, WizardHW
- 2.13.61
* Thu Jun  1 2006 locilka@suse.cz
- Global API or parts of these modules were marked as Stable:
    Address, Arch, Confirm, Crash, FileUtils, Hostname, HTML,
    HWConfig, IP, Label, Map, Message, Mode, Netmask, Package,
    PackageAI, PackageSystem, Popup, Report, RichText, Sequencer,
    Service, Stage, TypeRepository, URL and Wizard
- Added some more documentation into the Wizard module
- Fixing documentation of global modules (for generated docu.)
- 2.13.60
* Thu May 18 2006 locilka@suse.cz
- Fixing exporting the $QT_HOME_DIR according to $user's home
  directory (#162114).
- 2.13.59
* Mon May 15 2006 locilka@suse.cz
- Fixed CWMFirewallInterfaces behavior in the basic view for all
  interfaces at once. When the status of the firewall checkbox is
  changed, the current configuration is checked and possible errors
  are reported to user (#158520 c17).
- 2.13.58
* Mon May 15 2006 jsrain@suse.cz
- provide more information about restart of YaST during
  installation from ProductControl (#167561)
* Thu May 11 2006 lslezak@suse.cz
- select kernel-xenpae package if Xen PAE kernel is running
  (#172978)
- 2.13.57
* Wed May 10 2006 locilka@suse.cz
- Added more logging into the Service.ycp module (for bug #173418)
* Thu May  4 2006 jsrain@suse.cz
- read texts from control file (#170881)
- 2.13.56
* Wed May  3 2006 locilka@suse.cz
- Properly handle special string 'any' in 'EXT' zone in CWM for
  firewall. Creating special functions in SuSEFirewall module for
  that (#158520).
- 2.13.55
* Tue Apr 25 2006 jsrain@suse.de
- properly parse FTP URL (#166248, many others)
- 2.13.54
* Tue Apr 25 2006 visnov@suse.cz
- ensure importing trusted RPM keys before initializing sources (#169121)
- 2.13.53
* Thu Apr 20 2006 jsrain@suse.de
- handle installation restart with repeating last step (#167561)
- 2.13.52
* Wed Apr 19 2006 jsuchome@suse.cz
- menu.ycp: check for `restart_menu possible return value (#162966)
- scripts/yast2: enable restarting curses menu
- 2.13.51
* Tue Apr 18 2006 jsuchome@suse.cz
- menu.ycp: better check if menu should exit after online-update
- 2.13.50
* Fri Apr 14 2006 jsrain@suse.de
- fixed handling of disabling back button (#165832)
- 2.13.49
* Fri Apr 14 2006 jsuchome@suse.cz
- restart online update if there are some selected patches left to
  installation (#165540)
- 2.13.48
* Tue Apr 11 2006 locilka@suse.cz
- Registering callback Pkg::CallbackAcceptFileWithoutChecksum
- 2.13.47
* Fri Apr  7 2006 jsrain@suse.de
- fixed content file parser (#163702)
- 2.13.46
* Wed Apr  5 2006 locilka@suse.cz
- Registered new Pkg:: callbacks
  - Pkg::CallbackAcceptUnsignedFile
  - Pkg::CallbackAcceptUnknownGpgKey
  - Pkg::CallbackImportGpgKey
  - Pkg::CallbackAcceptVerificationFailed
  - Pkg::CallbackTrustedKeyAdded
  - Pkg::CallbackTrustedKeyRemoved
- 2.13.45
* Wed Apr  5 2006 sh@suse.de
- V 2.13.44
- Fixed bug #116356: save_y2logs saves into a different directory
* Wed Apr  5 2006 fehr@suse.de
- changed some very verbose debug output in AsciiFile.ycp
- 2.13.43
* Wed Apr  5 2006 locilka@suse.cz
- Adding special Xen interface "xenbr0" into the
  FW_FORWARD_ALWAYS_INOUT_DEV variable in the Network Proposal in
  case of "kernel-xen" package installed (#154133).
* Wed Apr  5 2006 mvidner@suse.cz
- Added CWM::DisableButtons (jsuchome, #157125).
* Wed Apr  5 2006 locilka@suse.cz
- Fixed wrong handling of special 'any' string in the internal
  function ArePortsOrServicesAllowed(). This part was forgotten
  from the first implementation of NetworkManager support (#162512).
- Adding FW_FORWARD_ALWAYS_INOUT_DEV variable into the Read()
  function to prepare fix for Xen handling (#154133).
* Tue Apr  4 2006 locilka@suse.cz
- Added mapping for Pkg::CallbackAcceptUnsignedFile() callback
  (#162858)
- 2.13.42
* Wed Mar 29 2006 mvidner@suse.cz
- Added PackageLock, a module to handle the big Zypp lock (#160319).
- 2.13.41
* Mon Mar 27 2006 locilka@suse.cz
- TERM=raw -> TERM=dumb in Service::RunInitScriptWithTimeOut()
* Wed Mar 22 2006 locilka@suse.cz
- better testing of UTF-8 support using the testutf8 binary
  (#158001)
- 2.13.40
* Mon Mar 20 2006 locilka@suse.cz
- removed yast2 starting script from /usr/lib/YaST2/bin/, leaving
  it only in /sbin/ (#144237).
- replacing relative paths in /sbin/yast2 with absolute ones.
- 2.13.39
* Wed Mar 15 2006 jsrain@suse.de
- changed the name of kernel package on S/390 (#157605)
- 2.13.38
* Wed Mar 15 2006 locilka@suse.cz
- checking for testutf8 binary before running it in /sbin/yast2
  starting script (#158001)
- 2.13.37
* Mon Mar 13 2006 jsuchome@suse.cz
- fixed long buttons (#157420)
- 2.13.36
* Fri Mar 10 2006 jsrain@suse.de
- store all installation options in /etc/YaST2/Productfeatures
  (#156388)
- 2.13.35
* Fri Mar 10 2006 mvidner@suse.cz
- Start ncurses UI in non-threaded mode to enable spawning of
  interactive processes (like w3m for suseRegister, #150799).
- Added String::Random (#157107).
- 2.13.34
* Mon Feb 27 2006 lslezak@suse.cz
- Arch::is_xen0() and Arch::is_xenU() (#153235)
- 2.13.33
* Thu Feb 23 2006 mvidner@suse.cz
- ag_initscripts: no need to use absolute paths to awk and friends
  (#152840)
- 2.13.32
* Mon Feb 20 2006 mvidner@suse.cz
- Added Arch::is_laptop as a better alternative to
  Arch::has_pcmcia (#151813).
- 2.13.31
* Thu Feb 16 2006 olh@suse.de
- fix two typos in error path in Mode.ycp
* Tue Feb 14 2006 jsrain@suse.de
- added possibility to disable individual proposals
- 2.13.30
* Tue Feb 14 2006 olh@suse.de
- remove nubus support
* Mon Feb 13 2006 lslezak@suse.cz
- don't try to install kernel-*-nongpl packages
- 2.13.29
* Mon Feb 13 2006 locilka@suse.cz
- Killing the .background agent in the
  Service::RunInitScriptWithTimeOut function to prevent from
  undefined behavior when calling this function one by one
  without any sleep (#144891).
- Ignoring all 'skeleton' and 'skeleton.*' init scripts in the
  Rulevel editor since they are not a real init scripts.
* Mon Feb 13 2006 locilka@suse.cz
- Removing obsolete support for NetworkManager which have changed
  its behavior again (#149075). Changing firewall, firewall
  proposal and CWM firewall.
- 2.13.28
* Thu Feb  9 2006 locilka@suse.cz
- Added support for the iscsi-target (#149548) into the Firewall
  services
* Wed Feb  8 2006 jsrain@suse.de
- added support for localization of workflows updated from add-on
  products
* Tue Feb  7 2006 mvidner@suse.cz
- Use rcnetwork restart insted of rcnetwork start to handle the switch
  between ifup and NetworkManager (#148263).
- Use BuildRequires, but without openslp-devel, popt-devel.
- 2.13.27
* Thu Jan 26 2006 locilka@suse.cz
- Added new function String::WrapAt() to ease wrapping texts in
  dialogs and pop-up windows.
  Useful particulary for translated strings with unknown length.
* Mon Jan 23 2006 locilka@suse.cz
- Added new function NetworkService::ConfirmNetworkManager() to be
  called in the Read dialogs of services configuration. User has to
  confirm continuing the configuration when NetworkManager is
  enabled.
- Merged texts from proofreading.
- 2.13.26
* Mon Jan 23 2006 mvidner@suse.cz
- Start the network using rcnetwork start, not rcnetwork status.
  Fixes the internet test (#144829).
- 2.13.25
* Sun Jan 15 2006 mvidner@suse.cz
- NetworkService: use /etc/sysconfig/network/config:NETWORKMANAGER
  instead of rcnetworkmanager (#135595).
- 2.13.24
* Fri Jan 13 2006 jsrain@suse.cz
- hide disabled steps from installation workflow
- 2.13.23
* Fri Jan 13 2006 locilka@suse.cz
- Added missing function Progress::status()
  Returning whether progress 'is' on or 'off'
* Wed Jan 11 2006 mvidner@suse.cz
- CWMTab::CleanUp: do not reset current_tab_id, the caller may want to
  remember it for revisiting the dialog (#134386).
- Added String::NonEmpty (stringlist) and NewlineItems (string).
- Added XML::XmlError () (ug).
- 2.13.22
* Wed Jan 11 2006 jsrain@suse.cz
- added possibility to hide Edit button in Table/Popup
- 2.13.21
* Wed Jan 11 2006 locilka@suse.cz
- Fixing bug #142502
  Firewall still reported 'closed' SSH port when the Network Manager
  was used.
  Added more debugging logs.
- 2.13.20
* Mon Jan  9 2006 locilka@suse.cz
- Teaching SuSEFirewallProposal to work well with Network Manager
  enabled.
- 2.13.19
* Fri Jan  6 2006 locilka@suse.cz
- Tuning SuSEFirewall known Services
  Adding "TCP: 427" and "Broadcast: 427" to the definition of
  SLP-daemon by the feature #117 "SLP configuration module"
* Thu Jan  5 2006 mvidner@suse.cz
- CWM: implemented valid_chars property; added InitNull and StoreNull.
- CWM::Run: generate a fake event to allow a handler to enable/disable
  widgets before the first real UserInput takes place
- Dropped commandline.ycp, really now.
- 2.13.18
* Thu Jan  5 2006 locilka@suse.cz
- Adjusting environment for bugfix #129679
  Preventing Service::RunInitScript() from stuck by adding a new
  function Service::RunInitScriptWithTimeOut() using the
  .background agent
- Fixing bug #139587
  Firewall Functions IsEnabled() and IsStarted() expected that the
  firewall is not enabled or started by default in the
  installation. The [Back] button from the connection test (and
  changing firewall "enabled" to "disabled") has broken this
  expectation.
* Wed Jan  4 2006 visnov@suse.cz
- Dropped Require.ycp, long time obsolete library
- Dropped commandline.ycp obsolete wrapper
* Wed Jan  4 2006 locilka@suse.cz
- Adding Network Manager support into
  - SuSEFirewall Proposal
  - SuSEFirewall itself
  - CWM Firewall Interfaces (for other modules)
- 2.13.17
* Tue Jan  3 2006 visnov@suse.cz
- Show progress in command-line mode (F300349)
* Tue Jan  3 2006 mvidner@suse.cz
- Prevented NetworkService::Managed() from returning nil.
* Thu Dec 22 2005 visnov@suse.cz
- ignore .desktop comments starting with #
* Tue Dec 20 2005 visnov@suse.cz
- Include bash completion script
- 2.13.16
* Mon Dec 19 2005 mvidner@suse.cz
- Consider also NetworkManager if there are no ifcfgs during the
  firewall proposal (#139402).
- 2.13.15
* Mon Dec 19 2005 jsuchome@suse.cz
- merged texts from proofreading
- 2.13.14
* Wed Dec 14 2005 mvidner@suse.cz
- Added a bash completion script, thanks to choeger.
* Wed Dec  7 2005 locilka@suse.cz
- Changing firewall summary texts due to the bug/enhancement
  [#119810]. A bit misleading text "SSH is enabled" was changed to
  the "SSH port is open" etc. Also translatios should be now much
  more clearer.
* Tue Nov 29 2005 locilka@suse.cz
- Adding feature #5998 from FaTE: Port ranges
  Port ranges are supported in the whole configuration of
  SuSEFirewall2 for TCP, UDP and Broadcast. Port range has a higher
  priority than a port itsef, which means that adding a port which
  is already mentioned in some port alias will not add it again. If
  there is some port range next to the new port it will join it
  with the port range. Port ranges can be flatten when one is a
  neighbor of any other or if one covers any other. Removing a port
  from the port range will split the port range up into two port
  ranges.
- Adding port range support into port aliases
- Changing searching for port alias from grep-regexp to the
  perl-regexp (because of buggy behaviour with the 'mysql' port).
- Fixing variable types in documentation of some functions
- 2.13.13
* Thu Nov 24 2005 locilka@suse.cz
- Fixed the misleading documentation for GetEnableService()
  function in the SuSEFirewall module, thanks to jsmeix
* Wed Nov 23 2005 mvidner@suse.cz
- CWM::ProcessTerm now handles all container widgets
  (added `MarginBox, `MinWidth, `MinHeight, `MinSize).
* Wed Nov 23 2005 visnov@suse.cz
- 2.13.12
* Tue Nov 22 2005 lslezak@suse.cz
- do not log passwords (#134886)
* Wed Nov 16 2005 jsrain@suse.cz
- read list of modules to clone at the end of installation from
  control file
* Wed Nov 16 2005 lslezak@suse.cz
- Kernel.ycp - some PPC kernel RPMs have been dropped, kernel
  package selection updated (#64206)
- 2.13.11
* Tue Nov 15 2005 mvidner@suse.cz
- CWM:
  - added `menu_button
  - explicitly specifying an empty help produces no errors, like no_help
  - actually implemented validate_help
  - added validate_type: `function_no_popup so that the function bodies
  can be shared and only validate_help needs to differ
- CWMTab:
  - widget_names is now optional
  - generate a fake event when switching to a new tab to allow a handler
  to enabled/disable widgets before the first real UserInput takes place
  - prevent double tab initialization at tab set initialization
- 2.13.10
* Fri Nov 11 2005 jsrain@suse.cz
- initialize package source only if needed when installing kernel
  modules package (#132458)
* Tue Nov  8 2005 lslezak@suse.cz
- add %%2f when the begining of FTP URL path starts with /
- 2.13.9
* Tue Nov  8 2005 lslezak@suse.cz
- The reserved characters can be part of URL (#96960),
  properly handle the escape sequences in parsing/building of URL
- 2.13.8
* Wed Nov  2 2005 mvidner@suse.cz
- CWM
  - PrepareDialog recognizes *Squash and alignment widgets.
  - "widget_names" can be omitted in ShowAndRun.
  - Added section: Widget Description Map Reference.
  - Factored out rules to format the docbook documentation.
- CWMTab
  - CreateWidget recognizes "fallback_functions" in the main map
  and the tab maps.
  - Also call "clean_up" functions for widgets inside the tabs.
* Wed Nov  2 2005 locilka@suse.cz
- Removing TCP port 135 from samba-server firewall definition.
- Adding "Portable Batch System (PBS)" definition into firewall
- Adding MySQL definition into firewall, enhancement #131478
* Thu Oct 27 2005 mvidner@suse.cz
- CLI XML help: changed document structure, hopefully for the better.
- 2.13.7
* Fri Oct 21 2005 lslezak@suse.cz
- CommandLine:: supports printing texts without trailing
  newline character (useful for progress messages); added YesNo()
  functionality for the command line mode
- Package:: supports installing packages in the command line mode
  (#91033)
- 2.13.6
* Thu Oct 20 2005 jsuchome@suse.cz
- added Misc::CustomSysconfigRead for reading custom sysconfig files
- 2.13.5
* Mon Oct 10 2005 mvidner@suse.cz
- Do not use modules marked with BrokenModules (#97655).
- 2.13.4
* Fri Sep 30 2005 mvidner@suse.cz
- Fixed the configuration of ESCON and FICON (#82891).
- 2.13.3
* Thu Sep 29 2005 visnov@suse.cz
- require yast2-hardware-detection for probing
* Tue Sep 27 2005 jsrain@suse.cz
- do not prevent USB modules from being added to initrd (#66733)
* Tue Sep 27 2005 lslezak@suse.cz
- Popup - display long error "as is" - escape rich text tags,
  format lines; layout fixes
- version 2.13.2
* Fri Sep 23 2005 lslezak@suse.cz
- command line - multiline description of a command is possible
  (help can be string or list of strings)
* Fri Sep 23 2005 locilka@suse.cz
- Adding support for VNC and SSH installations. Firewall proposal
  enables SSH on non-dial-up interfaces when installing over SSH,
  enables VNC on non-dial-up interfaces when installing over VNC.
  Firewall proposal warns when installing over SSH/VNC and SSH/VNC
  is not enabled. (enahancement #113211)
- Adding XDMCP (Remote Acces to Display Manager) support
  (enhancement #118200)
- Adding FAM (Remote File Alteration Monitor) support
  (enhancement #118196)
- 2.13.1
* Wed Sep 21 2005 lslezak@suse.cz
- Support for long error and long warning messages
  (e.g. Report::LongError) (#79161)
- new popups in Popup:: module (e.g. Popup::TimedLongError)
- added [Stop] button to all timed popups
- version 2.13.0
* Wed Sep  7 2005 mvidner@suse.cz
- Fixed deleting an interface after writing and returning
  to the network proposal (#115448).
- WIRELESS_WPA_PASSWORD is also secret (#65741).
- 2.12.27
* Mon Sep  5 2005 locilka@suse.cz
- fixing default SuSEfirewall2 logging values using the
  GetDefaultValue() function for undefined and newly also for
  empty values  for security reasons (#100692).
- 2.12.26
* Mon Sep  5 2005 jsrain@suse.cz
- translate proposal tab headers (#114677)
- 2.12.25
* Mon Aug 22 2005 jsuchome@suse.cz
- added check for `cancel to ncurses menu loop (#105507)
- 2.12.24
* Thu Aug 18 2005 lslezak@suse.cz
- added simple XEN detection (workaround for #100726)
- select kernel-xen if XEN is detected
- 2.12.23
* Thu Aug 18 2005 locilka@suse.cz
- Do not Read() NetworkDevices when running CWMFirewallInterfaces
  in Installation or Update.
- Set SuSEFirewallProposal as 'modified' when changing the firewall
  counfiguration via CWMFirewallInterfaces in Installation or
  Update (bug #105170).
* Mon Aug 15 2005 jsrain@suse.cz
- check whether VGA kernel parameter is correct (#103150)
* Fri Aug 12 2005 jsrain@suse.cz
- don't prevent xfs and jfx module from being added to initrd on
  PPC (#104037)
- 2.12.22
* Fri Aug 12 2005 locilka@suse.cz
- Fixed YaST in console. It had been using LANG set to "POSIX"
  which was supporsed to be empty or to contain "xx_XX" string
  (#103007).
* Fri Aug 12 2005 visnov@suse.cz
- added comments for translators
* Tue Aug  9 2005 mvidner@suse.cz
- Fixed init script parsing with special backslash and whitespace
  combination (#103013).
* Tue Aug  9 2005 locilka@suse.cz
- Fixing bug #102951
  Adding SLP Daemon to the firewall as a known service
- 2.12.21
* Mon Aug  8 2005 jsrain@suse.cz
- disable "Edit" and "Delete" buttons in hardware dialog if no item
  is present in the list (#102526)
- store vendor URL in the installed system (#102542)
- do not add unneeded modules to initrd (#102588)
- 2.12.20
* Fri Aug  5 2005 jsrain@suse.cz
- added initialization of source refresh callbacks
- changed label of the menubutton in the hardware dialog
- 2.12.19
* Thu Aug  4 2005 lslezak@suse.cz
- move sysconfig metadata parsing functions from Sysconfig
  to String module.
- 2.12.18
* Tue Aug  2 2005 lslezak@suse.cz
- format function in WizardHW module
- 2.12.17
* Tue Aug  2 2005 jsrain@suse.cz
- added support not to allow to go back in the installation
  workflow if started from the middle
- 2.12.16
* Mon Aug  1 2005 locilka@suse.cz
- Changing firewall definition for samba-server by the Samba-Howto
  Allowed ports/functionality is: TCP 135, 139, 445; UDP: 137, 138;
  Broadcast: 137, 138;
  Bugzilla #81254
* Thu Jul 28 2005 jsrain@suse.cz
- merged texts from proofreading
* Thu Jul 28 2005 jsrain@suse.cz
- fixed stopping the workflow in the middle to reboot (eg. in case
  of kernel update)
- 2.12.15
* Thu Jul 21 2005 sh@suse.de
- Now using `opt(`hvstretch) in wizard to restore old laoyut
  behaviour: center content by default
- V 2.12.14
* Thu Jul 21 2005 jsrain@suse.cz
- don't report void errors in CWM
* Wed Jul 20 2005 jsrain@suse.cz
- fixed incorrecr wizard command causing crash at the begin of the
  installation
- 2.12.13
* Wed Jul 20 2005 jsrain@suse.cz
- added libxml2(-devel) to neededforbuild
- 2.12.12
* Tue Jul 19 2005 jsrain@suse.cz
- fixed installation workflow re-load on switch from installation
  to update or vice versa
- added possibility to start the workflow from the middle
- added possibility for having more stages in the installation
  wizard navigation bar
- added support for specifying textdomain for translatable texts
  for installation wizard
- 2.12.11
* Mon Jul 18 2005 sh@suse.de
- Properly check if KDE is running in /sbin/yast so the sw_single
  module is started full-screen if that works flawlessly (KDE)
- V 2.12.10
* Mon Jul 11 2005 sh@suse.de
- Fixed NCurses wizard layout behaviour:
  Properly propagate content strechability to layout parent
- V 2.12.9
* Fri Jul  8 2005 visnov@suse.cz
- adapt build dependencies for blocxx
- 2.12.8
* Fri Jul  1 2005 jsrain@suse.cz
- added support functions fir general hardware summary dialog
- added possibility to get selected tab from CWMTab
- 2.12.7
* Tue Jun 14 2005 lslezak@suse.cz
- command line - fixed example definition in xmlhelp output
- 2.12.6
* Mon Jun 13 2005 lslezak@suse.cz
- command line - 'xmlhelp' command (store command line help of
  a client in XML format)
* Mon Jun  6 2005 jsrain@suse.cz
- keep order of initrd modules from installation system in the
  target system
- 2.12.5
* Tue May 31 2005 jsrain@suse.cz
- create initial ProductFeatures file via fillup (#79278)
* Wed May 25 2005 locilka@suse.cz
- Fixed SuSEFirewall testsuite after adding 'bootps' port to the
  DHCP Server definition
* Wed May 25 2005 mvidner@suse.cz
- CWM: added a standalone radio button widget
* Thu May 19 2005 locilka@suse.cz
- Fixed bug in CWMTsigKeys
  Key name containing the 't' letter had been ending on that
  character because of wrong implementation of regexp with '\\t'
* Mon May  9 2005 locilka@suse.cz
- Adding "Requires: SuSEfirewall2" into the yast2 package instead
  of the yast2-firewall
* Tue May  3 2005 jsrain@suse.cz
- made the hardcoded fallback list of VGA modes in Initrd.ycp
  public (via global function)
* Tue May  3 2005 locilka@suse.cz
- Added 'bootps' port allowing broadcast into the DHCP Server
  definition for SuSEFirewallServices
* Thu Apr 28 2005 jsrain@suse.cz
- if YOU updates any YaST package, restart NCurses control center
  (#80591)
* Thu Apr 28 2005 jsrain@suse.cz
- updated ProductControl.ycp to privide inst_finish steps
- 2.12.4
* Fri Apr 22 2005 mvidner@suse.cz
- Do not use "default" as an identifier.
* Mon Apr 18 2005 jsrain@suse.cz
- added testsuite for new ProductFeatures.ycp
- 2.12.3
* Mon Apr 18 2005 jsrain@suse.cz
- updated manual page and help of yast2 (#70892)
- changed interface of ProductFeatures.ycp
- 2.12.2
* Tue Apr  5 2005 visnov@suse.cz
- fix NFB
- 2.12.1
* Mon Apr  4 2005 jsrain@suse.cz
- after running online update, exit ncurses control center (#63542)
* Thu Mar 31 2005 jsrain@suse.cz
- initialize product macro for help texts from /etc/*-release
  (#61247)
* Thu Mar 31 2005 locilka@suse.cz
- Changed firewall proposal texts to be clearly translatable
  (#73612)
* Thu Mar 24 2005 jsrain@suse.cz
- changed kernel packages for PPC (#72344)
* Mon Mar 21 2005 sh@suse.de
- Fixed bug #72799: Help/Steps buttons not translated
- V 2.11.48
* Mon Mar 21 2005 jsrain@suse.cz
- fixed setting bootsplash resolutino if framebuffer modes couldn't
  be detected (#74052)
- 2.11.47
* Fri Mar 18 2005 jsrain@suse.cz
- fixed determining if firewall is enabled (#73819)
- 2.11.46
* Wed Mar 16 2005 visnov@suse.cz
- 2.11.45
* Tue Mar 15 2005 visnov@suse.cz
- added check-all-syntax script for validating all YCP clients
  and modules (#63942)
* Mon Mar 14 2005 mvidner@suse.cz
- Don't allow single quotes inside ifcfg-* variables,
  especially NAME (#72164).
- NetworkDevices::ConcealSecrets: only nonempty; also WIRELESS_WPA_PSK.
- 2.11.44
* Sat Mar 12 2005 nashif@suse.de
- optionally add addon selections using the control file (#72257)
- 2.11.43
* Fri Mar 11 2005 mvidner@suse.cz
- Added NetworkDevices::ConcealSecrets not to log sensitive
  information (#65741).
- 2.11.42
* Fri Mar 11 2005 locilka@suse.cz
- Added new testsuite for SuSEFirewall module
- Added new testsuite for PortAliases module
* Wed Mar  9 2005 locilka@suse.cz
- Adjusting to changed /etc/services
  "ipsec-msft" has been changed to "ipsec-nat-t"
- 2.11.41
* Fri Mar  4 2005 lslezak@suse.cz
- HWConfig.ycp - /etc/sysconfig/hardware/hwcfg-* file access
- 2.11.40
* Fri Mar  4 2005 locilka@suse.cz
- fixed bug #67335
  Aborting unchanged SuSEfirewall configuration
- 2.11.39
* Thu Mar  3 2005 jsrain@suse.cz
- prevent Initrd module from automatical reading in Mode::config
  (#67256)
* Wed Mar  2 2005 locilka@suse.cz
- merged proofed texts
- 2.11.38
* Fri Feb 25 2005 lslezak@suse.cz
- command line - fixed checking of the mandatory keys - don't
  abort in "unsupported" mode, testsuite updated
- 2.11.37
* Fri Feb 25 2005 visnov@suse.cz
- 2.11.35
* Fri Feb 25 2005 lslezak@suse.cz
- commandline - don't check mandatory keys when the command line
  mode is "unsupported", testsuite updated
- 2.11.36
* Thu Feb 24 2005 fehr@suse.de
- Add AsciiFile::ReplaceLine
- 2.11.34
* Thu Feb 24 2005 visnov@suse.cz
- reading INCOMPLETE_TRANSLATION_TRESHOLD enabled
- 2.11.33
* Wed Feb 23 2005 lslezak@suse.cz
- command line - use command 'abort' instead of 'quit',
  testsuite updated
* Mon Feb 21 2005 nashif@suse.de
- Fixed reading of global variable which breaks testsuites
* Mon Feb 21 2005 nashif@suse.de
- Added incomplete_translation_treshold to product features
* Fri Feb 18 2005 visnov@suse.cz
- Don't show desktop files with "Hidden" set to yes in ncurses menu
* Thu Feb 17 2005 nashif@suse.de
- Added function to reset install.inf data to initiate a reread of
  the file
* Tue Feb 15 2005 locilka@suse.cz
- added name of the device for configuring interfaces
- added missing comments for SuSEFirewall functions
* Mon Feb 14 2005 jsrain@suse.cz
- added functions to disable and enable the CWM Firewall Interfaces
  widget
- 2.11.30
* Thu Feb 10 2005 mvidner@suse.cz
- Do not propose a dynamic address if the product (OES) says
  force_static_ip (#50524).
- 2.11.29
* Wed Feb  9 2005 nashif@suse.de
- control file and saved features from installation is now saved
  into /etc/YaST2,  /var/lib is too risky
* Wed Feb  9 2005 jsrain@suse.cz
- merged variables for kernel parameters in ProductFeatures into
  one (#50369)
* Wed Feb  9 2005 locilka@suse.cz
- Fixed reading SuSEfirewall2 configuration to be done only once
  in network proposal.
* Tue Feb  8 2005 sh@suse.de
- Added icons to standard popups
- V 2.11.26
* Tue Feb  8 2005 nashif@suse.de
- Moved ProductControl. Hooks from installation
* Tue Feb  8 2005 nashif@suse.de
- Moved XML module to library
* Tue Feb  8 2005 jsrain@suse.cz
- added richtext and (multi)selection box widget support to CWM
- enable release notes in inst. proposal also for NCurses
* Tue Feb  8 2005 jsuchome@suse.cz
- merged texts from proofreading
- 2.11.25
* Tue Feb  8 2005 jsuchome@suse.cz
- build with CustomDialogs.ycp
- 2.11.24
* Mon Feb  7 2005 nashif@suse.de
- Fixed call to inst_suseconfig
- Added variable to Directory used for custom workflows
* Fri Feb  4 2005 mvidner@suse.cz
- Added String::OptParens, String::OptFormat.
- 2.11.23
* Tue Feb  1 2005 lslezak@suse.cz
- fixed finish call handling (don't call finish handler (Write)
  when module is not initialized)
- 2.11.22
* Mon Jan 31 2005 sh@suse.de
- Added Show|HideReleaseNotesButton() to Wizard::
- V 2.11.21
* Mon Jan 31 2005 locilka@suse.cz
- added samba-server allowing broadcast feature (#50311)
- 2.11.20
* Fri Jan 28 2005 mlazar@suse.cz
- fixed runlevel agent: don't dump error msg if service script
  isn't readable
* Thu Jan 27 2005 mvidner@suse.cz
- NetworkDevices: canonicalize STARTMODE (~#50095), also on Import.
- 2.11.19
* Thu Jan 27 2005 locilka@suse.cz
- Rewritten SuSEFirewall::ActivateConfiguration() function
- Fixed some y2error message
* Wed Jan 26 2005 mvidner@suse.cz
- Fixed a typo preventing from adding an Altix XP interface (#50044).
* Tue Jan 25 2005 locilka@suse.cz
- removed SuSEfirewall2_final init script (bugzilla #50157)
- 2.11.18
* Fri Jan 21 2005 lslezak@suse.cz
- an option in command line mode specification can have
  more help texts (depending on command)
- improved command line mode support test (test also empty map)
- version 2.11.17
* Tue Jan 18 2005 lslezak@suse.cz
- command line - new simple mode (no commands),
  lazy initialization (bug #44083)
- version 2.11.16
* Wed Jan 12 2005 lslezak@suse.cz
- command line mode enhancements: accept integer type,
  added CommandLine::PrintVerbose(), cutom help option,
  testsuite update, small fixes
- version 2.11.15
* Tue Jan 11 2005 jsrain@suse.cz
-reverted fix of #49483
* Mon Jan 10 2005 jsrain@suse.cz
- added new function to compute additional packages (eg. -nongpl)
  for any base kernel package to Kernel.ycp
* Fri Jan  7 2005 locilka@suse.cz
- added new functions into String module
  TextTable() & UnderlinedHeader()
* Thu Jan  6 2005 jsrain@suse.cz
- prevent vga= kernel parameter from being used on IA64 (#49483)
* Wed Jan  5 2005 jsrain@suse.cz
- changed Kernel.ycp to functional interface
- 2.11.14
* Tue Jan  4 2005 jsrain@suse.cz
- fixed handling of sysconfig/kernel:MODULES_LOADED_ON_BOOT if
  changed externally during installation (#46971)
* Mon Jan  3 2005 locilka@suse.cz
- Added new implementation of SuSEfirewall2 broadcast configuration
  into SuSEFirewall module
- 2.11.13
* Tue Dec 21 2004 mvidner@suse.cz
- Added Hostname::Validhost (#22802).
- Substitute VERSION in Version.ycp also at "make" time (#40492).
- Support FW_ALLOW_FW_BROADCAST_* (locilka).
- 2.11.12
* Tue Dec 21 2004 jsrain@suse.cz
- fixed validation of widgets inside CWM Tab widget
- added possibility to set functions for immediate service
  start/stop in the CWMServiceStart widget
* Tue Dec 14 2004 mvidner@suse.cz
- Added Progress::set, fixed docs a bit.
- 2.11.11
* Fri Dec  3 2004 mvidner@suse.cz
- NetworkDevices: Canonicalize netmask data (#46885).
* Wed Dec  1 2004 locilka@suse.cz
- Added handling for 'all' parameter in old firewall functions
  in SuSEFirewall module
- Added CharacterDevice file-type into FileUtils.ycp.
- Created testsuite for FileUtils module.
* Wed Dec  1 2004 mvidner@suse.cz
- NetworkDevices: Improved ifcfg name handling,
  particularly mobile ipv6 (#48696).
* Tue Nov 30 2004 locilka@suse.cz
- Moved CWMFirewallInterfaces from yast2-firewall to yast2 rpm
* Tue Nov 30 2004 visnov@suse.cz
- added testsuite infrastructure for library/modules
* Thu Nov 25 2004 locilka@suse.cz
- added SuSEFirewallServices and PortAliases YCP Modules into
  library/network.
* Wed Nov 17 2004 arvin@suse.de
- fixed handling of command line arguments with space (bug #48264)
* Tue Nov 16 2004 fehr@suse.de
- add evms logfiles to save_y2logs if present
* Fri Nov 12 2004 mvidner@suse.cz
- Added NetworkDevices::DeleteAlias (#48191).
* Fri Nov 12 2004 locilka@suse.cz
- FileUtils have now GetFileRealType and GetFileType functions
  with output depending on the type of requested file.
- Increased documentation for FileUtils.
* Thu Nov 11 2004 arvin@suse.de
- always use Directory::logdir
* Thu Nov 11 2004 locilka@suse.cz
- Created FileUtils module for getting information about system
  files and directories.
* Thu Nov 11 2004 mvidner@suse.cz
- Added String::ValidCharsFilename, NetworkDevices::ValidCharsIfcfg
  (#46803)
- Added character set functions to String.
- PackageSystem::InstallKernel: return early if the module list is
  empty, thus slashing "yast2 lan" startup time.
- Desktop::RunViaDesktop now accepts arguments (#46828).
* Wed Nov 10 2004 mvidner@suse.cz
- Moved NetworkDevices from yast2-network to yast2.
- 2.11.7
* Mon Nov  8 2004 visnov@suse.cz
- yast2-pkg-bindings added to requires
* Mon Nov  8 2004 jsrain@suse.cz
- added optional "no_help" key to CWM widget description map
  in order to suppress errors in log if no help wanted (#47938)
- added protection against removing used TSIG keys to the CWM
  TSIG keys management widget (#47480)
* Thu Nov  4 2004 sh@suse.de
- Added save_y2logs script for easier bug reporting
- V 2.11.6
* Thu Nov  4 2004 mvidner@suse.cz
- Added String::FirstChunk.
- 2.11.5
* Wed Nov  3 2004 arvin@suse.de
- removed deprecated lookup
* Tue Nov  2 2004 mvidner@suse.cz
- Allow overriding sbindir so that we can install to a prefix.
- Merged changes from the 9.2 branch.
* Mon Nov  1 2004 visnov@suse.cz
- set product name in wizard when opening a dialog (#46247)
* Mon Nov  1 2004 visnov@suse.cz
- fix processing of command line arguments in Mode and Stage
* Mon Nov  1 2004 msvec@suse.cz
- use ll_LL in .desktop files (#47668)
* Mon Nov  1 2004 jsrain@suse.cz
- fixed parameters to sformat in Commandline.ycp
- 2.11.3
* Tue Oct 26 2004 jsrain@suse.cz
- Mode.ycp split to Mode.ycp, Stage.ycp, Linuxrc.ycp and
  Installation.ycp (yast2-installation), clean-up
- adapted the code to the clean-up
- 2.11.2
* Tue Oct 19 2004 locilka@suse.de
- added several messages into Message.ycp
- added several labels into Label.ycp
- added two functions into Confirm.ycp
- 2.11.1
* Mon Oct 11 2004 jsrain@suse.cz
- changed Arch.ycp to functional interface, probing the settings
  when they are needed (instead of constructor)
- update Initrd.ycp not to use Arch:: in its constructor
- 2.11.0
* Mon Oct  4 2004 mvidner@suse.cz
- Moved the "cd /" workaround to yast2-network (#46055).
- 2.10.27
* Fri Oct  1 2004 sh@suse.de
- Fixed bug #46598: Layout broken due to 800x600 default size
- V 2.10.24
* Wed Sep 29 2004 visnov@suse.cz
- always reinitialize target (#45356)
- 2.10.23
* Wed Sep 29 2004 mvidner@suse.cz
- Fixed Package::FunctionsAI["DoInstall" and "DoRemove"] (#45463).
- 2.10.22
* Mon Sep 27 2004 arvin@suse.de
- fixed generation of desktop files
* Sat Sep 25 2004 mvidner@suse.cz
- Change directory to / in /sbin/yast2 (#46055).
- 2.10.20
* Fri Sep 24 2004 mvidner@suse.cz
- Added Desktop::RunViaDesktop (#37864).
- 2.10.19
* Fri Sep 24 2004 visnov@suse.cz
- always initialize SourceCache when installing packages
- use installed kernel to compute kernel packages (#45905)
- 2.10.18
* Thu Sep 23 2004 mvidner@suse.cz
- Fixed empty runlevel editor (#45858).
* Tue Sep 21 2004 arvin@suse.de
- adapted path for qtrc (bug #44803)
* Tue Sep 14 2004 mvidner@suse.cz
- Ignore /etc/init.d/Makefile (#45198).
* Tue Sep 14 2004 jsrain@suse.cz
- added ProductFeatures::enable_firewall and firewall_ssh_enable
  to control firewall behavior in the proposal
* Mon Sep 13 2004 jsrain@suse.cz
- fixed reordering of items in Table/Popup's table (#45097)
- added ProductFeatures::fam_local_only
- 2.10.14
* Mon Sep  6 2004 visnov@suse.cz
- moved ComputeKernelPackages to Kernel.ycp
- use Kernel::ComputePackages in Package (#44394)
- 2.10.13
* Mon Sep  6 2004 jsrain@suse.cz
- mark licenses as confirmed when accepted (in PackageSystem.ycp
  and Require.ycp)
* Thu Sep  2 2004 locilka@suse.cz
- added String::escapetags - function for escaping HTML/XML tags
* Mon Aug 30 2004 arvin@suse.de
- add nongpl kernel package during installation (bug #44394)
* Fri Aug 27 2004 arvin@suse.de
- merged proof read messages
* Fri Aug 27 2004 mvidner@suse.cz
- LogView grep: properly quote the regex; it is a basic regex.
* Fri Aug 20 2004 nashif@suse.de
- Own schema directory
- 2.10.10
* Thu Aug 19 2004 visnov@suse.cz
- allow in commandline also GUI handler returning symbols (#43935)
* Tue Aug 17 2004 jsrain@suse.cz
- fixed function type casting in Table/Popup routines
- prevent 'usbhid' module from being added to initrd (#36766)
* Mon Aug 16 2004 nashif@suse.de
- fixed testsuites (added Testsuite.ycp to testedfiles or modified output
  according to the change of logging function references) (jsrain)
- type cast fixes
- CWM: fixed structure validation
* Thu Aug 12 2004 nashif@suse.de
- Disable Commandline interface during firstboot phase
- 2.10.7
* Tue Aug  3 2004 jsrain@suse.cz
- fixed types in CWM, changed interface of CWM::ShowAndRun ()
- split the CWMServiceStart widget into multiple widgets (one for
  each part)
- 2.10.6
* Fri Jul 30 2004 jsrain@suse.cz
- adapted CWMServiceStart.ycp functionality for box product
* Thu Jul 29 2004 nashif@suse.de
- New module for interaction with linuxrc(yast.inf and install.inf
  handling)
- Move functions from misc to Linuxrc
* Thu Jul 29 2004 nashif@suse.de
- Defined more variables in ProductFeatures
- Removed live_eval variable
* Tue Jul 20 2004 jsrain@suse.cz
- enhanced the TSIG keys management widget to do more checks before
  creating a new TSIG key (#40845)
* Mon Jul 19 2004 jsrain@suse.cz
- enhnced functionality of Package*.ycp modules (popups with custom
  message, package check for read functions with error feedback)
* Wed Jul 14 2004 jsrain@suse.cz
- fixed typos in CWMServiceStart.ycp
* Tue Jul 13 2004 locilka@suse.de
- added new Message module
- 2.10.3
* Mon Jun 21 2004 jsrain@suse.cz
- added CWM widget for TSIG keys management
* Fri Jun 18 2004 lslezak@suse.cz
- CommandLine: read text or password from console
* Fri Jun 18 2004 jsrain@suse.cz
- added CWM widget for service starting (like the Start-up dialog
  in DNS server component)
* Thu Jun 17 2004 msvec@suse.cz
- updated testsuite
- 2.10.2
* Wed Jun 16 2004 jsrain@suse.cz
- added suport for navigation tree and tabs to CWM
- updated the LogView popup to be able to be used as widget for CWM
- do not add 'desktop' to kernel command line
* Wed Jun 16 2004 msvec@suse.cz
- fixed 'yast2 -l' output (#42087)
- 2.9.75
* Thu Jun 10 2004 nashif@suse.de
- Added software-proposal variable to product features
* Tue Jun  8 2004 nashif@suse.de
- Fixed bug #41696: yast uses elevator=anticipatory instead of
  elevator=as
- URL with empty host is valid (i.e. file:///test.xml )
* Fri May 28 2004 sh@suse.de
- Fixed bug #41305: License agreement after abort in NCurses
* Wed May 26 2004 mvidner@suse.cz
- Fixed agent definition for /etc/sysconfig/hardware
  to handle multiline values (#39350).
- 2.9.72
* Tue May 25 2004 arvin@suse.de
- install kernel-bigsmp even with a bit less than 4GB of RAM
  (bug #40729)
* Tue May 25 2004 jsrain@suse.cz
- set the I/O scheduler in ProductFeatures (#41038)
- 2.9.70
* Wed May 19 2004 nashif@suse.de
- Added a timeout for ShowText popup when called via
  Report. (Report::ShowText)
* Mon May 17 2004 msvec@suse.cz
- added PadZero general function for padding with zeros
* Wed May 12 2004 msvec@suse.cz
- improved ncurses menu responsiveness (#38363)
- 2.9.68
* Wed May  5 2004 gs@suse.de
- yast2 start script: check whether the terminal supports UTF-8
  and adapt language settings (bug #39606)
- 2.9.67
* Tue May  4 2004 arvin@suse.de
- merged proofread messages
* Fri Apr 23 2004 mvidner@suse.cz
- do not copy network aliases from install.inf
  to modprobe.conf (#39135)
- 2.9.65
* Thu Apr 22 2004 arvin@suse.de
- run unicode_{start,stop} only if they are present (bug #35714)
* Mon Apr 19 2004 arvin@suse.de
- merged proofread messages
* Fri Apr 16 2004 nashif@suse.de
- Save runtime product variables
* Thu Apr  8 2004 jsrain@suse.cz
- use the 'desktop' kernel parameter only for desktop products
* Wed Apr  7 2004 nashif@suse.de
- #38596: Also use saved id
* Wed Apr  7 2004 nashif@suse.de
- Workaround for #38596, broken recursion for iterators
* Tue Apr  6 2004 nashif@suse.de
- update/upgrade defaults added to product feature set (#38486)
* Mon Apr  5 2004 nashif@suse.de
- Removed unconfigurable options from report summary
- Added optional list of package to product features
- 2.9.60
* Fri Apr  2 2004 nashif@suse.de
- Fixed wrapper functions for new wizard
- 2.9.59
* Fri Apr  2 2004 arvin@suse.de
- finally changed license to GPL for good
* Fri Apr  2 2004 nashif@suse.de
- added wrapper functions around Tree and Menu enabled Wizards to
  support ncurses mode (#37581)
* Thu Apr  1 2004 arvin@suse.de
- don't set download callbacks globaly (bug #37151)
* Wed Mar 31 2004 nashif@suse.de
- New ProductFeature variables
* Wed Mar 31 2004 msvec@suse.cz
- added /etc/YaST2 dir (for log.conf)
- 2.9.54
* Wed Mar 31 2004 gs@suse.de
- show header of ShowText popup (bug #37171)
* Wed Mar 31 2004 arvin@suse.de
- added product feature about suboptimal distribution (bug #36823)
* Wed Mar 31 2004 jsrain@suse.de
- remove ide-scsi from initrd during update (#37591)
* Tue Mar 30 2004 jsrain@suse.de
- fixed map validator of CWM
* Mon Mar 29 2004 jsrain@suse.de
- fixed behavior of combo box for adding new option if it is
  editable (#37267)
- 2.9.52
* Mon Mar 29 2004 adrian@suse.de
- hide YaST groups desktop files in the desktop world
* Mon Mar 29 2004 arvin@suse.de
- fixed kernel selection on i386 smp systems (bug #35876)
* Mon Mar 29 2004 jsrain@suse.de
- adapted CWM to updated 'is' builtin
- fixed Initrd testsuite
- 2.9.50
* Fri Mar 26 2004 arvin@suse.de
- added uml detection to Arch module
* Wed Mar 24 2004 adrian@suse.de
- fix yast qt ui themeing, export QT_HOME_DIR again
  (got broken due to login shell usage bye kdesu)
* Wed Mar 24 2004 arvin@suse.de
- fixed function name (bug #36783)
* Tue Mar 23 2004 mvidner@suse.cz
- added Confirm::MustBeRoot to easily alert the user (#35363)
* Tue Mar 23 2004 lslezak@suse.cz
- fixed parsing quoted string in String::ParseOptions() (#36223)
- testsuite update
* Mon Mar 22 2004 msvec@suse.cz
- support for sort keys in ncurses menu (#36466)
- 2.9.47
* Mon Mar 22 2004 jsrain@suse.cz
- fixed unwanted hiding of helps during progress bar run
- don't abort installing packages via Require and PackageSystem
  if dependency solving fails and system wasn't consistent before
  installing them
* Mon Mar 22 2004 sh@suse.de
- V 2.9.46
- Fixed bug #35768: Wizard buttons not retranslated
* Fri Mar 19 2004 sh@suse.de
- V 2.9.45
- Improved handling for all Popup::*timed*() dialogs:
  Use UI::TimeoutUserInput() now, no more confusing busy cursor,
  less delays (no more sleep() )
* Wed Mar 17 2004 fehr@suse.de
- add functions {Set,Get}Utf8Lang() to Encoding module
* Wed Mar 17 2004 arvin@suse.de
- added download progress callbacks (bug #31445)
* Mon Mar 15 2004 fehr@suse.de
- add functions {Set,Get}EncLang() && GetCodePage() to Encoding module
- add global boolean evms_config to ProductFeatures.ycp
* Mon Mar 15 2004 arvin@suse.de
- adapted "yast -l" to desktop files (bug #35019)
* Fri Mar 12 2004 nashif@suse.de
- Custom wizard added (sh@suse.de)
* Thu Mar 11 2004 msvec@suse.cz
- proper event ID type handling (#35602)
* Wed Mar 10 2004 msvec@suse.cz
- accept nil from some UI calls (should fix the failing testsuites)
- added function for creation of FQ hostname
* Wed Mar 10 2004 arvin@suse.de
- install kernel-um in uml
* Wed Mar 10 2004 nashif@suse.de
- Fixed Progress for new Wizard
- 2.9.39
* Wed Mar 10 2004 sh@suse.de
- V 2.9.37
- Migration to new wizard
* Mon Mar  8 2004 sh@suse.de
- Changed X cursor theme (adrian)
* Mon Mar  8 2004 msvec@suse.cz
- Added Wizard::SetDesktopIcon to set the title icon
- 2.9.35
* Fri Mar  5 2004 mvidner@suse.cz
- Added Popup::AnyQuestionRichText.
- {Require,PackageSystem}::DoInstallAndRemove:
  ask for license acceptance (#35250).
* Fri Mar  5 2004 msvec@suse.cz
- make runlevel testsuite use Service
- add warnings about usage of obsolete interface
- 2.9.33
* Thu Mar  4 2004 visnov@suse.cz
- 2.9.32
- late initialization of Wizard and Progress (for command line)
* Thu Mar  4 2004 msvec@suse.cz
- fixed docu installation dirs
- replaced sequencer include with dummy one using Sequencer
* Thu Mar  4 2004 visnov@suse.cz
- added type info (kkaempf, visnov)
* Thu Mar  4 2004 msvec@suse.cz
- improved the packages testing client
- fixed ncurses menu generation (#35186)
* Tue Mar  2 2004 msvec@suse.cz
- fixed Package interface
- added documentation and testing client
* Tue Mar  2 2004 msvec@suse.cz
- improved (fixed) agent for sysconfig/hardware
- 2.9.31
* Fri Feb 27 2004 nashif@suse.de
- Adapt for new control file based installation
* Thu Feb 26 2004 jsrain@suse.de
- preventing modules uhci-hcd, ehci-hcd, ohci-hcd from being put
  into initrd (#35032)
* Tue Feb 24 2004 visnov@suse.cz
- don't duplicate history entries in interactive command line (#34610)
* Tue Feb 24 2004 kkaempf@suse.de
- treat x86_64 as 'wintel' architecture (#34853)
* Mon Feb 23 2004 mvidner@suse.cz
- Services: don't omit boot.hotplug-beta, boot.restore_permissions (#34775)
- 2.9.28
* Fri Feb 20 2004 arvin@suse.de
- disable accept button during Progress (bug #30303)
* Fri Feb 20 2004 jsrain@suse.de
- fixed redrawing of fields in Table/Popup table widget after an
  option was changed
* Thu Feb 19 2004 jsrain@suse.de
- added agent for handling /etc/sysconfig/hardware/hwcfg-*
* Thu Feb 19 2004 arvin@suse.de
- removed function Kernel::IDERecorders since "ide-scsi" is not
  used anymore (bug #34694)
* Thu Feb 19 2004 mvidner@suse.cz
- changed sort to use "<" instead of "<=" because of the switch
  to std::sort
* Thu Feb 19 2004 visnov@suse.cz
- restore AsciiFile::AssertLineValid behavior as in 9.0
* Tue Feb 17 2004 sh@suse.de
- Use correct kernel image name on S/390
- 2.9.25
* Tue Feb 17 2004 sh@suse.de
- Fixed bug #34617: New kernel names on S/390
- 2.9.24
* Tue Feb 17 2004 sh@suse.de
- Applied olh's patch for bug #34602: PPC kernel renamed
- 2.9.23
* Mon Feb 16 2004 arvin@suse.de
- recognize newer macs (bug #34587)
* Mon Feb 16 2004 jsrain@suse.de
- kernel image is now /boot/vmlinux on all PPC subarchs (#34588)
- 2.9.21
* Mon Feb 16 2004 arvin@suse.de
- removed obsolete Mode::hardBoot
* Thu Feb 12 2004 lslezak@suse.cz
- CWM: added better `back event handling, correctly displaying
  option names in the new option checkbox (jsrain)
- added function String::FormatSizeWithPrecision,
  updated testsuite
- version 2.9.19
* Wed Feb 11 2004 msvec@suse.cz
- adapt remote clients for the new interpreter
* Tue Feb 10 2004 arvin@suse.de
- adapted kernel determination to kernel 2.6 names
* Tue Feb 10 2004 arvin@suse.de
- finally removed configdir from file list (doesn't help anymore)
* Sat Feb  7 2004 arvin@suse.de
- removed config files (*.y2cc)
* Sat Feb  7 2004 msvec@suse.cz
- own configdir until all modules are updated
- 2.9.15
* Fri Feb  6 2004 msvec@suse.cz
- call %%suse_update_desktop_file for the group files
- use the group .desktop files also in the ncurses menu
- 2.9.14
* Tue Feb  3 2004 msvec@suse.cz
- added yast2 groups .desktop files
- 2.9.13
* Tue Feb  3 2004 visnov@suse.cz
- implemented non-strict checking of command line options
* Sat Jan 31 2004 arvin@suse.de
- added function to build a url from tokens
* Fri Jan 30 2004 mvidner@suse.cz
- removed lookups in Service to fix configuration modules testsuites
- 2.9.11
* Thu Jan 29 2004 msvec@suse.cz
- more testsuite fixes
- 2.9.10
* Thu Jan 29 2004 jsrain@suse.de
- fixed cwm testsuite
- fixed file list
- 2.9.9
* Tue Jan 27 2004 jsrain@suse.de
- removed hwinfo from neededforbuild
- fixed testsuite for initrd
* Mon Jan 26 2004 jsrain@suse.de
- added hwinfo to neededforbuild
- 2.9.8
* Mon Jan 26 2004 msvec@suse.cz
- converted wizard sequencer to module
- 2.9.7
* Fri Jan 23 2004 msvec@suse.cz
- added agents for sysconfig/sysctl and /suseconfig
- 2.9.6
* Fri Jan 23 2004 arvin@suse.de
- fixed Require.ycp for brand new interpreter
* Mon Jan 19 2004 jsrain@suse.de
- merged the new interpreter branch
* Mon Dec 15 2003 jsrain@suse.de
- Moved Label.ycp and Popup.ycp from source/yast2/library/wizard/src
  to source/yas t2/library/module because of building with the new
  interpreter
* Mon Dec 15 2003 msvec@suse.cz
- better services handling: Service (from Runlevel)
* Fri Dec  5 2003 jsrain@suse.de
- added Mode::commandline variable, setting it an appropriate way
* Wed Dec  3 2003 msvec@suse.cz
- use common Makefile.am (needs recent devtools)
* Sun Nov 23 2003 ro@suse.de
- remove file conflict with yast2-pam (Autologin.ycp moved there)
* Mon Nov 17 2003 arvin@suse.de
- adapted plugindir detection for NPTL
* Fri Nov 14 2003 gs@suse.de
- use ncurses file selection widgets
* Wed Oct 29 2003 visnov@suse.cz
- fix testsuite
- 2.9.2
* Fri Oct 24 2003 ms@suse.de
- moved x11 subdir to installation
* Fri Oct 17 2003 jsrain@suse.de
- Fixed "blinking" of Table/Popup's buttons when table content was
  reordered
* Fri Oct  3 2003 jsrain@suse.de
- Table/Popup stuff splitt off from CWM.ycp to separate file
- Added support for "Changed" column to Table/Popup
* Wed Oct  1 2003 jsuchome@suse.cz
- added Autologin.ycp module to handle autologin configuration
- 2.9.0
* Wed Sep 17 2003 gs@suse.de
- script/yast2: start textmode yast in UTF-8 environment (bug #30512)
- 2.8.31
* Wed Sep 17 2003 visnov@suse.de
- enable interactive mode for command line again
- 2.8.30
* Mon Sep 15 2003 jsrain@suse.de
- fixed X11Version.ycp to prefix Require:: when calling function
  from Require.ycp module
- 2.8.29
* Mon Sep 15 2003 ms@suse.de
- fixed X11Version.ycp to use 'import "Require"' instead of
  'include "require.ycp"'
* Thu Sep 11 2003 arvin@suse.de
- cool mouse cursor theme for 2nd stage installation (bug #30552)
* Thu Sep 11 2003 gs@suse.de
- file_popups.ycp: bugfix for SaveFileAs() bug #29745
* Wed Sep 10 2003 gs@suse.de
- V 2.8.27
- menu/menu.ycp: replace <key> by [key] in help text (to avoid
  misinterpretation in RichText)
* Fri Sep  5 2003 visnov@suse.de
- library/commandline: care about command line only in normal mode (#30144)
* Thu Sep  4 2003 arvin@suse.de
- proof-read messages
* Mon Sep  1 2003 visnov@suse.de
- do not print module help twice in the header
- revert capitalization for the command line actions/options from
  proofreader
- 2.8.25
* Mon Sep  1 2003 jsrain@suse.de
- added support for immutable options to Table/Popup
* Mon Sep  1 2003 arvin@suse.de
- handle repair mode in Popup::ConfirmAbort
* Fri Aug 29 2003 visnov@suse.de
- fix error reporting, use RichText::Rich2Plain()
* Wed Aug 27 2003 msvec@suse.cz
- new module for confirmation of detection (#26515)
- 2.8.23
* Wed Aug 27 2003 gs@suse.de
- yast2 script: set language to english only on console if LANG is
  japanese, korean or chinese
* Tue Aug 19 2003 arvin@suse.de
- removed include file common_functions.ycp
* Tue Aug 19 2003 arvin@suse.de
- optimized String::CutBlanks
* Fri Aug 15 2003 arvin@suse.de
- added Popup::ShowText
* Thu Aug 14 2003 arvin@suse.de
- removed y2menu for good
- added /usr/share/YaST2/include to file list (bug #28807)
- removed common_popups.ycp and common_messages.ycp for good
* Mon Aug 11 2003 gs@suse.de
- yast2 script: start y2base menu ncurses (instead of y2menu)
* Fri Aug  8 2003 gs@suse.de
- bugfix in file_popups.ycp/PopupDir(dir) (if the argument is an
  empty string, 'pwd' is the directory)
- menu.ycp: improved layout and usability
* Wed Aug  6 2003 fehr@suse.de
- added function CutRegexMatch to String.ycp it can be used to
  remove matches of a regular expression from a string
- 2.8.16
* Mon Aug  4 2003 jsrain@suse.de
- added possiblity to restart command getting log after performing
  operation from LogView popup
- 2.8.15
* Fri Aug  1 2003 arvin@suse.de
- added directory for desktop files
* Tue Jul 29 2003 jsrain@suse.de
- passing whole event information from CWM to handlers
* Wed Jul 23 2003 jsrain@suse.de
- updated CWM to use WaitForEvent instead of UserInput, tables of
  table/popup dialogs display popup on double-click or enter key
- allow to specify command to display log directly, not only as
  filename and argument for grep for LogView
* Tue Jul 22 2003 msvec@suse.cz
- further String updates and fixes
- 2.8.13
* Wed Jul  9 2003 fehr@suse.de
- remove Mode::language, now handled in Laguage module (#27115)
* Mon Jul  7 2003 visnov@suse.de
- let TypeRepository module use the simple types
* Fri Jul  4 2003 msvec@suse.cz
- added a first library of simple types:
    IP, Netmask, Hostname, Address, String, URL
- 2.8.12
* Wed Jul  2 2003 visnov@suse.de
- propagate y2base exit code from yast2 script
* Tue Jul  1 2003 jsrain@suse.de
- updates of CWM module, added validation of used structures and
  some wrappers for more complex tasks
* Thu Jun 26 2003 visnov@suse.de
- print to stderr in non-interactive mode
* Wed Jun 25 2003 visnov@suse.de
- fixed Perl/encoding problem in commandline agent
- fixed padding of helps in commandline
- quiet is now default, verbose an option
* Tue Jun 24 2003 visnov@suse.de
- 2.8.11
* Tue Jun 24 2003 jsrain@suse.de
- added testsuite for CWM module
* Tue Jun 24 2003 visnov@suse.cz
- removed modules directory at the top-level
* Mon Jun 23 2003 jsrain@suse.de
- moved YCP libraries to own subdirectory (visnov@suse.cz)
- added CWM module for simple manipulation with widgets, including
  common routines for Table/Popup-style dialogs
- added LogView module for displaying logs with advanced
  functionality
- 2.8.10
* Fri Jun 20 2003 mvidner@suse.cz
- Runlevel editor: call insserv with force
  when writing multiple services (#27370).
- Moved MailAliases out, to be put to yast2-mail-aliases (#18212).
- Reverted yast2-network from Requires
- 2.8.9
* Wed Jun 18 2003 visnov@suse.de
- disabled ipaddress type for command line
- disabled interactive mode for command line
- reverted yast2-network from neededforbuild
- version 2.8.8
* Wed Jun 18 2003 lslezak@suse.de
- spec file: added yast2-network to Requires/neededforbuild
- version 2.8.7
* Mon Jun 16 2003 lslezak@suse.cz
- new NetworkPopup:: module (common network browsing popups)
- version 2.8.6
* Wed Jun 11 2003 arvin@suse.de
- added /usr/share/doc/packages/yast2 to file list (2nd try)
* Wed Jun 11 2003 visnov@suse.de
- added command line interface
- 2.8.4
* Wed Jun 11 2003 arvin@suse.de
- added /usr/share/doc/packages/yast2 to file list
* Fri Jun  6 2003 mvidner@suse.cz
- common_popups: fixed an embarassing syntax error
- 2.8.3
* Fri Jun  6 2003 mvidner@suse.cz
- common_popups: revert from Label to common_messages.
- Fixed file list (lslezak).
- Directory: added tmpdir (msvec).
- 2.8.2
* Tue Jun  3 2003 sh@suse.de
- Fixed bug #27213: Default sort order in NCurses control center
* Fri May 30 2003 mvidner@suse.cz
- Added Label and Popup, replacements for common_{messages,popups}.
- ag_initscripts: recognize X-UnitedLinux-Default-Enabled.
- 2.8.1
* Thu Apr 24 2003 kkaempf@suse.de
- rename 'axp' to 'alpha'
* Wed Apr 23 2003 ms@suse.de
- added getX11Link function to solve the X11 link
  within the installed system
* Wed Mar 19 2003 ms@suse.de
- added textdomain to X11Version.ycp (#25627)
- added sax2 to RequireAndConflict() (#25628)
* Mon Mar 17 2003 arvin@suse.de
- correctly remove ampersand in button lables in y2menu (bug
  [#25364])
* Fri Mar 14 2003 sh@suse.de
- V 2.7.29
- Removed excess quotes in yast2 script when starting in kcontrol
* Fri Mar 14 2003 sh@suse.de
- V 2.7.28
- Moved yast2_kde functionality into yast2 script
  (Fix for 25230: kcontrol YaST2 module not working)
* Wed Mar 12 2003 sh@suse.de
- Applied Adrian's patch to use the correct ~/.qtrc in yast2-funcs
* Tue Mar 11 2003 arvin@suse.de
- fixed syntax in start script (bug #25080)
* Mon Mar 10 2003 gs@suse.de
- Fixed bugs #24866/#24865 in ncurses file selector (show links;
  set focus to the directory list)
* Sun Mar  9 2003 nashif@suse.de
- Fixed bug #24953: beta message during installation does not time out
* Fri Mar  7 2003 sh@suse.de
- Dropped "Notify" header for notify popups (#24782)
* Fri Mar  7 2003 sh@suse.de
- Fixed bug #24809: sw_single window outside screen
  Now only using --fullscreen for sw_single with KDE running
* Fri Mar  7 2003 sh@suse.de
- Fixed bug #24790 - Wrong Qt style in y2cc modules after inst.
  (Adrian)
* Wed Mar  5 2003 ms@suse.de
- added scr agent for /etc/sysconfig/displaymanager handling (#24669)
- do not check for packages in autoinst mode (#24706)
* Mon Mar  3 2003 jsrain@suse.de
- added scr agent for /etc/sysconfig/hotplug handling (#22580)
* Mon Mar  3 2003 arvin@suse.de
- once more merged proofread texts
* Mon Mar  3 2003 arvin@suse.de
- fixed testsuite
* Fri Feb 28 2003 ms@suse.de
- use require.ycp for package checks in X11Version.ycp (#24488)
* Fri Feb 28 2003 kkaempf@suse.de
- honor 'manual' on kernel command line (#24462)
* Tue Feb 25 2003 kkaempf@suse.de
- fix mkdir silence option.
* Tue Feb 25 2003 kkaempf@suse.de
- suppress warning if /tmp/.qt already exists (#24243)
* Mon Feb 24 2003 jsrain@suse.de
- added `opt (`notify) to Wizard_hw::ConfiguredContent table to
  allow double click handling (#24095)
- 2.7.15
* Thu Feb 20 2003 arvin@suse.de
- use title-style capitalization for menu names (bug #23848)
* Wed Feb 19 2003 arvin@suse.de
- fixed DoNotAcceptButtonLabel (used during beta notice)
* Tue Feb 18 2003 arvin@suse.de
- added AsciiFile module from yast2-storage
* Mon Feb 17 2003 arvin@suse.de
- disable x11 setup on mips
- make Next and Accept the default button
* Mon Feb 10 2003 arvin@suse.de
- setup complete environment for qt during installation
* Mon Feb 10 2003 arvin@suse.de
- make anti aliased fonts work
* Thu Feb  6 2003 sh@suse.de
- New command line options for "yast2" script: --fullscreen --noborder
- Always start "sw_single" in full screen mode
* Wed Feb  5 2003 arvin@suse.de
- merged proofread messages
* Mon Feb  3 2003 sh@suse.de
- V 2.7.7
- Added default function key handling
* Mon Feb  3 2003 arvin@suse.de
- new pot file handling
* Mon Jan 27 2003 arvin@suse.de
- added popt to neededforbuild
* Mon Jan 27 2003 msvec@suse.de
- network groups: Network Devices and Network Services
- 2.7.4
* Fri Jan 24 2003 mvidner@suse.de
- Added readconfig.ycp to the file list. Fixes autoyast.
* Fri Jan 17 2003 mvidner@suse.de
- Reverted sequencer checking: allow superfluous aliases.
- 2.7.3
* Tue Jan 14 2003 mvidner@suse.de
- Added function key shortcuts to common dialogs (try F1 in curses).
- Report: added global settings for easier access (nashif).
- 2.7.2
* Mon Jan 13 2003 jsrain@suse.de
- added crashes handling module
* Fri Jan 10 2003 mvidner@suse.de
- mail table agent: Prevent returning strings as integers/booleans (~#21804).
* Fri Dec 20 2002 mvidner@suse.de
- file_popups: in qt, use the new widgets
- Arch: fallback for .probe.system being nil (msvec)
- workaround for CallFunction scope bug (#22486) (msvec)
- sequencer: check that all aliases are used (msvec)
- common_messages: DoNotAcceptButtonLabel (arvin)
- Wizard: use opt(key_F1) for Help (gs)
- 2.7.1
* Wed Nov 13 2002 ms@suse.de
- forgot to add hwinfo and hwinfo-devel to neededforbuild
* Wed Nov 13 2002 ms@suse.de
- fixed GetVersion() function within the X11Version module. The code
  to obtain the XFree86 version used to configure the installed
  card was really broken. I add a libhd based C program to check
  whether XFree86 4 or 3 is used to configure the card. This program
  is called from the GetVersion() function now.
* Mon Oct 21 2002 arvin@suse.de
- print warning if qt frontend is installed but does not work
  (bug #20805)
* Thu Oct 17 2002 arvin@suse.de
- fixed arrows in ncurses menu (#19902)
* Fri Oct 11 2002 msvec@suse.cz
- fixed translations in the ncurses menu (#20801)
- 2.6.39
* Fri Oct 11 2002 arvin@suse.de
- added lost password.ycp (bug #20087)
* Fri Sep 20 2002 kkaempf@suse.de
- access content only in initial mode
- 2.6.37
* Fri Sep 20 2002 kkaempf@suse.de
- read initial language from content file
- 2.6.36
* Wed Sep 18 2002 arvin@suse.de
- does not provides/obsoletes the old yast
* Thu Sep 12 2002 kkaempf@suse.de
- define IgnoreButtonLabel in WFM and UI
- 2.6.34
* Tue Sep 10 2002 arvin@suse.de
- added provide/obsolete y2t_menu (bug #19325)
* Sat Sep  7 2002 arvin@suse.de
- added help text in y2menu
* Thu Sep  5 2002 arvin@suse.de
- wizard loads it's images from the theme dir
* Wed Sep  4 2002 mvidner@suse.cz
- ncurses menu: fixed shortcut cycling in the group menu (#18258).
- 2.6.30
* Mon Sep  2 2002 mvidner@suse.cz
- ag_initscripts: fixed parsing Short-Descriptions.
* Fri Aug 30 2002 schwab@suse.de
- Don't waste tons of memory in y2menu.
* Fri Aug 30 2002 arvin@suse.de
- moved X11Version.ycp from yast2-installation here
* Thu Aug 29 2002 sh@suse.de
- Adapted wizard colors to new grey style images by wimer@suse.de
* Thu Aug 29 2002 mvidner@suse.cz
- wizard: prevent temporary (but visible) truncations
  of dialog captions (#18517).
* Wed Aug 28 2002 mvidner@suse.cz
- mail aliases: fixed line continuation processing (#18487).
- file_popups::PopupDir: fixed the Selected directory heading.
- 2.6.28
* Tue Aug 27 2002 jsuchome@suse.cz
- provide/obsolete old translation packages
* Thu Aug 22 2002 arvin@suse.de
- make links to yast2 relative (bug #18170)
* Tue Aug 20 2002 arvin@suse.de
- added variable Mode::x11_setup_needed and Arch::x11_setup_needed
* Tue Aug 20 2002 arvin@suse.de
- added ncurses based y2menu by Marco Skambraks
* Sun Aug 18 2002 kkaempf@suse.de
- honor /etc/install.inf:UseSSH (#18053)
* Fri Aug 16 2002 arvin@suse.de
- marked more texts for translation
* Wed Aug 14 2002 arvin@suse.de
- removed links to /sbin/yast2 with non ascii characters to
  prevent screen corruption is some locales
* Tue Aug 13 2002 arvin@suse.de
- merged proofread texts
* Mon Aug 12 2002 kkaempf@suse.de
- read /etc/install.inf:InstMode correctly for Mode::boot
- 2.6.20
* Sun Aug 11 2002 mvidner@suse.cz
- Runlevel: use full path of service scripts; force removal
  (#17608 workaround)
- 2.6.19
* Fri Aug  9 2002 mvidner@suse.cz
- Fixed falling back to ncurses when DISPLAY is set
  but yast2-qt is not installed.
- Added Runlevel::error_msg, to inform the user what went wrong.
- 2.6.18
* Tue Aug  6 2002 arvin@suse.de
- fixed detection of autoinst in Mode.ycp
* Mon Aug  5 2002 arvin@suse.de
- adaption for new /etc/install.inf agent
* Wed Jul 31 2002 mvidner@suse.cz
- Moved private runlevel files back to yast2-runlevel.
- 2.6.15
* Mon Jul 29 2002 msvec@suse.cz
- included some general purpose agents
- 2.6.14
* Wed Jul 24 2002 jsuchome@suse.cz
- Added runlevel module files.
* Fri Jul 19 2002 mvidner@suse.cz
- Moved aliases handling from yast2-mail (bug #11730).
- 2.6.13
* Fri Jul 19 2002 mvidner@suse.cz
- Added Wizard::{Set,Restore}ScreenShotName ().
- Moved sysconfig/ypserv definition from yast2-nis-server.
- 2.6.12
* Fri Jul 19 2002 sh@suse.de
- Wizard now uses consistent image names for easier OEM logo
  handling
* Tue Jul 16 2002 sh@suse.de
- V 2.6.11
- provide/obsolete yast2-trans-wizard
* Fri Jul 12 2002 kkaempf@suse.de
- fix sequencer and wizard testsuite
- call sequencer testsuite during build
- 2.6.10
* Fri Jul 12 2002 msvec@suse.cz
- added doc and autodocs
- new module Directory: contains definitions of all directories
* Tue Jul  9 2002 mvidner@suse.cz
- Provides/Obsoletes fixed for the devel subpackage
* Thu Jul  4 2002 arvin@suse.de
- move non binary file from /usr/lib/YaST2 to /usr/share/YaST2
* Mon Jul  1 2002 kkaempf@suse.de
- split of images to separate package
* Thu Jun 27 2002 kkaempf@suse.de
- merged yast2-lib-sequencer and yast2-lib-wizard.
* Tue Jun 11 2002 arvin@suse.de
- the yast2 script now handels all arguments as strings when
  calling y2base
* Thu Jun  6 2002 arvin@suse.de
- various minor fixes for installation
* Wed Jun  5 2002 kkaempf@suse.de
- recode shell output properly for UI (#16178)
- don't require trans packages (#16285)
* Wed May 29 2002 arvin@suse.de
- fixed yast2 start scripts for lib/lib64
* Tue May 28 2002 sh@suse.de
- V 2.6.4
- dropped obsolete hw_setup_launcher.ycp
- fixed file list in spec file
- fixed Makefile.am to work with new automake
* Wed May 22 2002 tom@suse.de
- Moved X11 functionality from x11 to y2c_x11.
* Tue May 14 2002 arvin@suse.de
- prevent ncurses frontend to start with languages that
  are known to not work correct
* Wed May  8 2002 tom@suse.de
- Removed keyboard, mouse, timezone, language (now extra packages)
* Tue Apr 23 2002 fehr@suse.de
- remove subdirectories storage and partitioning they are now in
  a separate package yast2-storage.
- new version 2.6.2
* Wed Apr 17 2002 tom@suse.de
- (#15565) monitors.ycp newly generated with uppercase vendor and
  model strings.
* Tue Apr 16 2002 gs@suse.de
- (#15600, #15727) Package Installation: check again the package
  dependencies if the user deselects an additional required package
* Mon Apr 15 2002 tom@suse.de
- (#15546) Now changing lilo.conf correctly.
* Thu Apr 11 2002 tom@suse.de
- (#15546) Handle VESA mode correctly for fbdev graphics.
* Wed Apr 10 2002 tom@suse.de
- (#15690) Now the probe button really probes.
* Wed Apr 10 2002 lnussel@suse.de
- merged modifications for certification/product CD
* Wed Mar 27 2002 kkaempf@suse.de
- Unpack driver update data in chrooted directory.
- y2update.tar.gz is alread copied by linuxrc, don't expect
  it below /media/floppy.
* Wed Mar 27 2002 kkaempf@suse.de
- Evaluate "partition" and "serverdir" when installing from
  harddisk (#15525).
* Wed Mar 27 2002 gs@suse.de
- Change source medium: use "serverdir" instead of "partition"
  (concerns installation from hard disk)
* Tue Mar 26 2002 kkaempf@suse.de
- Set all hardware to a defined state after update (#15532).
- For installation from harddisk, use "serverdir" instead of
  "partition" from install.inf (#15525).
- linuxrc mounts CD1 to /var/adm/mount during harddisk install
  (#15525).
* Tue Mar 26 2002 sh@suse.de
- Fixed bug #15520: can't boot into installed system
* Tue Mar 26 2002 ms@suse.de
- need blank as first sign for VESA and LCD vendor to ensure
  proper display at top of the monitors list (#15521)
* Tue Mar 26 2002 sh@suse.de
- Fixed bug #15512: Can't install base pkgs in installed system
* Tue Mar 26 2002 tom@suse.de
- (#15518) Renamed YaST-internal IDs in sysconfig:
  keyboard: YAST_TYPE --> YAST_KEYBOARD
  mouse:    YAST_TYPE --> YAST_MOUSE
* Tue Mar 26 2002 kkaempf@suse.de
- Delete runme_at_boot after updating all packages.
* Tue Mar 26 2002 tom@suse.de
- (#15515) YaST-internal IDs are now: keyboard: YAST_TYPE, mouse: YAST_TYPE
* Tue Mar 26 2002 sh@suse.de
- Fixed bug #15506: Disable "Change" menu when skipping HW config
* Mon Mar 25 2002 tom@suse.de
- (#14852) inst_config_x11.ycp:
  The variables currentMode and Selected_3D were first stored into the
  X11 module and then queried from the UI. Fixed.
* Mon Mar 25 2002 sh@suse.de
- Fixed bug #15418: selbox in inst_rootpart not wide enough
* Mon Mar 25 2002 kkaempf@suse.de
- make update.post script executable before starting it.
- Allow either packed or unpacked extension disk.
* Mon Mar 25 2002 fehr@suse.de
- make reading of exiting fstab work again (#15482)
* Mon Mar 25 2002 schubi@suse.de
- kdoc added in forceupdate list
* Mon Mar 25 2002 kkaempf@suse.de
- adapt probing for usb controllers to changed libhd requirements
  (#15483).
- dont re-calculate bootloader location if it was set manually
  (#15446).
- fix typo in monitors.ycp ("90,47" is no valid vsync).
* Mon Mar 25 2002 sh@suse.de
- Fixed bug #15419: confusing message in inst_suseconfig
* Mon Mar 25 2002 gs@suse.de
- Update: change status from "u" to "i" for uninstalled packages
  (#14727)
* Mon Mar 25 2002 sh@suse.de
- Fixed bug #15412: One log line for each package installed
* Mon Mar 25 2002 fehr@suse.de
- moved static dialog definitions for fs options into function
  GetNormalFilesystems() to make translations work (#15460)
* Mon Mar 25 2002 ms@suse.de
- update monitors.ycp to currently used CDB entries (#15421).
* Sun Mar 24 2002 kkaempf@suse.de
- delete runme_at_boot after package installation (#15430).
- remember device (index) where (wrong) SuSE medium was found (#15432).
* Fri Mar 22 2002 gs@suse.de
- package selection: show correct status of the package (#15400)
* Fri Mar 22 2002 fehr@suse.de
- removed superfluous warning about fsid change when assigning a
  mount point to LVM LV (#15388)
- changed fstab options for /proc/bus/usb from "defaults,noauto"
  to "noauto" (#15389)
* Fri Mar 22 2002 kkaempf@suse.de
- Call /usr/bin/setfont without parameters when Braille enabled (#13801).
* Fri Mar 22 2002 gs@suse.de
- Change source of installation: umount /var/adm/mount before mounting
  the new source medium (#14425)
* Fri Mar 22 2002 sh@suse.de
- Fixed bug #15356: killed mwm message
* Fri Mar 22 2002 schubi@suse.de
- bugix: Xf86config module has been overwritten while update #15376
  ( wrong if statement in inst_finish.ycp )
* Fri Mar 22 2002 gs@suse.de
- Update: show packages with status "d" in the "No Update" list
  (#15350)
* Thu Mar 21 2002 tom@suse.de
- (#14936) Now capturing `cancel and treating like `abort.
* Thu Mar 21 2002 arvin@suse.de
- check for yast2-qt-plugin and it's libraries in the YaST2 and
  yast2 start scripts (bug #15300 and probably bug #13831)
* Thu Mar 21 2002 tom@suse.de
- (#14882) Now marking probed but unused monitor-hw-data with configured = no.
* Thu Mar 21 2002 kkaempf@suse.de
- Drop intermediate textdomain calls, they're useless (#15294).
* Thu Mar 21 2002 gs@suse.de
- Package installation: respect product information AND release number
  of the source medium (#15278)
* Thu Mar 21 2002 schubi@suse.de
- Checking mouse protocol before calling update_Xf86config
* Thu Mar 21 2002 sh@suse.de
- Fixed bug #15220: Wizard buttons not translated
* Thu Mar 21 2002 sh@suse.de
- Fixed endless loop in language with some weird NCurses combinations
* Thu Mar 21 2002 gs@suse.de
- Update: do not allow status "delete" for packages which are not
  installed (#14727)
* Thu Mar 21 2002 ms@suse.de
- fixed check script to be valid with the new firegl driver [fglr200]
* Thu Mar 21 2002 schubi@suse.de
- Checking broken update correctly #13597
* Wed Mar 20 2002 kkaempf@suse.de
- fallback to (chipset related) vendor/device if graphics card
  doesn't provide (manufacturer related) subvendor/subdevice (#15099)
* Wed Mar 20 2002 tom@suse.de
- (#15098) Now reading file with default value.
* Wed Mar 20 2002 kkaempf@suse.de
- Also show SuSE release number when choosing root partiton (#15243).
- Properly probe cdroms during installation/update (#15275).
* Wed Mar 20 2002 fehr@suse.de
- fix problem with map access to non-map in GetEntryForMountpoint
  (#15229)
- fix problem with wrong partition proposal
- fix problem with wrong default filesystem (#15057)
* Wed Mar 20 2002 tom@suse.de
- (#15093) New frequency range: [60,62,65,68,70,72,75,78,80,85,90,100]
* Wed Mar 20 2002 sh@suse.de
- Fixed bug #15214: Control center after HW proposal english only
- Fixed bug #15201: Disable WM decorations for first control center
* Wed Mar 20 2002 lnussel@suse.de
- added -S option to yast2 shell script (for susewm)
* Wed Mar 20 2002 schubi@suse.de
-  Installing vnc (if needed ) while updating the system #14707
* Wed Mar 20 2002 tom@suse.de
- Added norwegian language.
* Wed Mar 20 2002 sh@suse.de
- Fixed bug #13894: Slide show progress bar shows wrong value
* Wed Mar 20 2002 schubi@suse.de
- Starting raidstart for partitions which are not / and have
  raid systems ( update ). #14798
* Wed Mar 20 2002 kkaempf@suse.de
- remember language in Mouse in order to trigger re-translation
  (#15197).
* Tue Mar 19 2002 sh@suse.de
- Fixed bug #14530: Explicit file names in .spec rather than *.scr
* Tue Mar 19 2002 gs@suse.de
- Update: re-evaluate the update packages if the status of the
  "Clean up the system ..." checkbox has changed
* Tue Mar 19 2002 schubi@suse.de
- Call substring with the correct parameters #15184
  ( inst_rpmupdate.ycp)
* Tue Mar 19 2002 kkaempf@suse.de
- Also write hardware status for already active ide, floppy, usb
  controllers, and framebuffer (#15195).
- Preliminary fix for YaST2.firstboot (#15187).
* Tue Mar 19 2002 tom@suse.de
- (#15096) Do not use undefined variable any more.
- (#15091) Now restoring saved monitor data in normal mode.
* Tue Mar 19 2002 sh@suse.de
- Fixed "update finished, empty proposal dialog" bug
* Tue Mar 19 2002 kkaempf@suse.de
- Properly check return code from inst_mode if update was choosen.
- just pass 'Framebuffer' entry from install.inf to lilo, don't
  look at probe results (#15168)
- add comments to /etc/sysconfig/bootloader.
* Mon Mar 18 2002 tom@suse.de
- (#14238) Now writing sysconfig comments for the mouse.
* Mon Mar 18 2002 sh@suse.de
- Fixed bug #15101: Checkboxes truncated in 80x24 ncurses proposal
* Mon Mar 18 2002 kkaempf@suse.de
- re-probe cdroms in installed system in order to get proper status
  for ide cdwriter devices which couldn't be detected at boot-time
  (#15126).
* Mon Mar 18 2002 lnussel@suse.de
- added -i option for installing packages to yast2 shell script
- added some shell magic to allow more than two parameters for modules
* Mon Mar 18 2002 gs@suse.de
-  Recode for copyright and author added (#15058)
* Mon Mar 18 2002 kkaempf@suse.de
- Bugfix for lilo/dolilo: drop "vga" from append, pass via "-v"
  to dolilo.
* Mon Mar 18 2002 sh@suse.de
- Fixed bug #15090: "No" in "really install" interpreted as "yes"
* Mon Mar 18 2002 sh@suse.de
- Fixed bug #15100: Default "off" for "start control center"
* Mon Mar 18 2002 snwint@suse.de
- mk_lilo_conf: put 'vga' entry into image section
* Fri Mar 15 2002 tom@suse.de
- (#13878) Added Estonian keyboard.
* Fri Mar 15 2002 tom@suse.de
- (#14855) Language: Added Slovene language.
- (#14855) Keyboard: Added Slovene keyboard to YaST2 keyboards.
- (#14855) Timezone: Cleaned up existing lang --> timezone mess (new: Slovene).
* Fri Mar 15 2002 kkaempf@suse.de
- drop workaround for author/copyright twist from libpkg.
- Replace "\n" in author list with ", "
* Fri Mar 15 2002 fehr@suse.de
- fix wrong nameing for windows mount points (#15031)
* Fri Mar 15 2002 kkaempf@suse.de
- ignore more cmdline parameters
- don't pass "-v" (for global vga=) to dolilo, the "vga=" in the
  append line is sufficient.
* Fri Mar 15 2002 gs@suse.de
- Update: do not delete "aps" if it is in use (#15015)
- Package Selection: correct update of the disk space information
* Fri Mar 15 2002 snwint@suse.de
- updated 'failsafe' options for lilo.conf
- append user specified boot options to 'failsafe' entry
* Fri Mar 15 2002 sh@suse.de
- Fixed bug #13894: Slide show pkg sizes garbled from CD2 on
* Fri Mar 15 2002 tom@suse.de
- (#15021) Now only removing X11-link in case of "No X11".
* Fri Mar 15 2002 kkaempf@suse.de
- Check also /proc/modules besides the "active" flag from hwinfo
  in order to find out if a module is already loaded (#15007).
* Thu Mar 14 2002 sh@suse.de
- Fixed bug #14161: wrong background grey
* Thu Mar 14 2002 sh@suse.de
- Fixed bug #13186: Start Y2 control center after installation
- Fixed bug #14975: Final "All is ready" popup
* Thu Mar 14 2002 zoz@suse.de
- fix PCMCIA startup (#14661).
* Thu Mar 14 2002 tom@suse.de
- Added turkish language again in language.ycp.
* Thu Mar 14 2002 tom@suse.de
- (#14518) Added Irish.
* Thu Mar 14 2002 tom@suse.de
- (#14814) Now translating old lang codes to ISO codes on entry.
* Thu Mar 14 2002 kkaempf@suse.de
- scripts/yast2_kde: set LANG from /etc/sysconfig/language:RC_LANG (#14607).
- scripts/yast2: honor $LANG (#14607).
- install k_smp if > 4GB physical memory detected (#14287).
* Thu Mar 14 2002 gs@suse.de
- (#14592) Now ask the user whether YaST2 shall delete unmaintained
  packages from the system
- (#14406), (#14805) Package selection dialog: help text added for "X"
  status and popup text changed
* Wed Mar 13 2002 tom@suse.de
- (#14882) Now marking faked GENERIC Monitor with cfg=no.
* Wed Mar 13 2002 tom@suse.de
- (#14885) Now writing "/dev/mouse" into XF86Config so xmset works in the
  running system.
* Wed Mar 13 2002 nashif@suse.de
- Don't probe hardware in Mode::config
* Wed Mar 13 2002 fehr@suse.de
- prevent upward rounding in combination of
  ByteToHumanString/kmgt_str_to_byte (#14673)
* Wed Mar 13 2002 tom@suse.de
- (#14446) Now also restoring hwclock-param from sysconfig
  and setting timezone again in continue mode.
* Wed Mar 13 2002 kkaempf@suse.de
- Fix locale for greek (ISO8859-7 -> ISO-8859-7, #14898).
- Set "acpismp=force" for UP and SMP systems if "ht" flag detected (#13531).
- Install k_smp if "BOOT_IMAGE=apic" given in cmdline (#14022).
- Dont change initrd modules aic7xxx vs. aic7xxx_old on update (#14614).
- Override instmode "cd" in install.inf, if setup/descr/info knows better
  (#14469).
- Start ncurses "menu" with first group preselected (instead of all),
  general code cleanup of menu code (#14909).
* Tue Mar 12 2002 gs@suse.de
- equal button size in package conflict popups (#13302)
* Tue Mar 12 2002 mvidner@suse.cz
- Provide keyboard shortcuts for the group and package tables in
  ncurses detailed package selection. #14737.
* Tue Mar 12 2002 tom@suse.de
- (#13198) Changed mouse probing strategy.
  Applied sleep before mouse probing in inst_startup.ycp.
* Tue Mar 12 2002 fehr@suse.de
- add hibernation partition to expert partitioner menue (#14668)
- handle raids present on system to install reasonably
* Mon Mar 11 2002 tom@suse.de
- (#14491) Now using new "manual" probing to get the new unique key (mouse).
* Mon Mar 11 2002 kkaempf@suse.de
- Skip all non-data lines in "parted print" output (#14793).
- Don't pass "manual" option to installed system.
* Mon Mar 11 2002 tom@suse.de
- Detect language change to avoid unnecessary package selection recalculation.
* Mon Mar 11 2002 sh@suse.de
- Fixed bug #14164: inst_mode should be a popup
* Mon Mar 11 2002 tom@suse.de
- New script by ms@suse.de for changing X11-mouse-protocol during update.
* Fri Mar  8 2002 kkaempf@suse.de
- clean up firsboot script to fix pcmcia/usb and usbdevfs (#14416)
- don't 'hard' probe for cdroms when checking for installation
  sources but rely on libhd configuration database instead.
  Fallback to /dev/cdrom if even this fails (#14555).
- add "vnc" package to installation list if running under vnc (#14707).
- remove duplicate portmap start from firstboot script.
* Fri Mar  8 2002 tom@suse.de
- (#14663) Added textdomains to import-modules.
* Fri Mar  8 2002 tom@suse.de
- (#13951) After having talked to ke@suse.de removed (commented out):
  ca_ES, gl_ES, hr_HR, ru_RU, tr_TR
  Added again:
  pt_BR
* Thu Mar  7 2002 tom@suse.de
- (#14227 addendum) Just discovered that the faked monitor also fooled the
  automatic insertion of probed but unknown monitors into the monitor DB.
  This is done so that those monitors can be selected in the monitor selection
  dialog. Furthermore for user convenience such a monitor is preselected when
  entering the monitor selection dialog. Unfortunately the libhd-faked monitor
  does fulfil all those criteria and triggered this mechanism. Fixed.
* Thu Mar  7 2002 tom@suse.de
- (#14227) Erroneously there was still a branch where the new behaviour of
  libhd was not honored. YaST now takes this into consideration in any case
  (hopefully) and leads the user to the monitor selection dialog again as it
  was before.
* Thu Mar  7 2002 tom@suse.de
- (#14606) Solved by now displaying date in numerical form because in inst-sys
  not all translations for all languages are available for system commands.
  Invented new function Timezone::GetDateTime().
* Thu Mar  7 2002 sh@suse.de
- Added missing "textdomain" in BootSILO.ycp
* Thu Mar  7 2002 sh@suse.de
- Addes missing translation markers in inst_root
* Thu Mar  7 2002 schubi@suse.de
- patch xf86config in update mode
* Thu Mar  7 2002 fehr@suse.de
- handle editing of encrypted partitions in running system correct
- change handling of back-button in LVM lv dialog
* Wed Mar  6 2002 schubi@suse.de
- textdomain added for software proposal #14538
* Wed Mar  6 2002 schubi@suse.de
- Showing error popup, if the package agent has not been initialized
  correctly
* Wed Mar  6 2002 tom@suse.de
- (#14540) Now setting sysconfig var DISPLAYMANAGER to  "console"  instead
  of DISPLAYMANAGER_STARTS_XSERVER to "no" if user selects "No X11".
* Wed Mar  6 2002 sh@suse.de
- Fixed bug #14011: Switching laguages does not switch all texts
* Wed Mar  6 2002 fehr@suse.de
- fix bug in handling crypto fs in running system (#13781)
* Wed Mar  6 2002 kkaempf@suse.de
- Drop "-a" (activate parition) flag from dolilo call if no primary
  partition can be found for activation (#13884).
- Hide information box if user de-selected "Show details" checkbox
  in "Please insert CD n" popup.
- When checking for a medium, always start with the last active
  device and check other devices only on failure.
* Tue Mar  5 2002 schubi@suse.de
- copy *.pkd to target system
* Tue Mar  5 2002 tom@suse.de
- (#4849) Corrected if-clause in constructor. Now functional in continue mode.
* Tue Mar  5 2002 kkaempf@suse.de
- Require "yast2-trans-inst-proposal" for yast2-instsys to get
  proper translations for the "proposal" screen.
- fix textdomain for 'proposal_bootloader' to "proposal".
* Tue Mar  5 2002 tom@suse.de
- (#14457) Now date/time is redisplayed on any change in the UI.
* Tue Mar  5 2002 schubi@suse.de
- Bugfix while changing update-upgrade-status #14473
* Tue Mar  5 2002 lnussel@suse.de
- filter out "\n" in helptexts (#14337)
- create the list of all modules only once when the splashscreen is displayed
  and recycle this list later when the "All" button is selected (#14472)
* Tue Mar  5 2002 tom@suse.de
- (#14211) Now executing SuSEconfig.3ddiag instead of switch2mesasoft.
* Tue Mar  5 2002 kkaempf@suse.de
- Copy setup/descr/en.pkd instead of setup/descr/english.pkd to
  installed system.
* Mon Mar  4 2002 tom@suse.de
- (#14116) Now considering Win partitions when assuming GMT vs. local time.
* Mon Mar  4 2002 fehr@suse.de
- add module loading info for xfs
* Mon Mar  4 2002 fehr@suse.de
- support more than 26 scsi disks (#13983)
- various fixes for usage in running system
* Mon Mar  4 2002 zoz@suse.de
- check usb/pci hotplug on first start and rewrite sysconfig
  properly (#14428).
* Mon Mar  4 2002 sh@suse.de
- Fixed the YaST2 part of bug #1218: Linuxrc displays an error
  message if the user aborted the installation
* Mon Mar  4 2002 kkaempf@suse.de
- check old lilo destination on update and re-use it.
- when writing lilo on update, check better if floppy or harddisk.
- write bootloader related settings to sysconfig/bootloader.
- run /sbin/raidautorun after all storage modules are loaded.
* Mon Mar  4 2002 sh@suse.de
- Fixed bug #14363: Don't execute SuSEconfig once more when going back
* Mon Mar  4 2002 gs@suse.de
- show the packages of first set or group (#14339)
* Mon Mar  4 2002 lnussel@suse.de
- added comment header to menu.ycp (#14379)
- replaced "Quit" with QuitButtonLabel()
* Mon Mar  4 2002 gs@suse.de
- add button and popup for Samba installation in dialog Choose
  installation source (#14010)
* Mon Mar  4 2002 tom@suse.de
- (#14117) Now showing static date/time in timezone window and proposal.
* Mon Mar  4 2002 sh@suse.de
- Fixed bug #14351: YaST2 SuSEconfig executes *.rpmsave modules
* Mon Mar  4 2002 gs@suse.de
- don't destroy the user defined software selection if the
  partitioning is changed (bug #14103)
* Mon Mar  4 2002 schubi@suse.de
- Showing error message after update #14250
- Deleting unsupported packages while update #14194
- Showing delete packages correctly while update #14235
* Sat Mar  2 2002 kkaempf@suse.de
- remember state of "details" checkbox if media not found (#14018).
- restore "instmode" properly (#14170).
* Sat Mar  2 2002 schubi@suse.de
- Postifx added in force update #13995
* Fri Mar  1 2002 fehr@suse.de
- set passno to 0 for partitions without mount point (#14130)
- determine bootable windows partitions independent of entry in
  /etc/fstab (#13884)
* Fri Mar  1 2002 tom@suse.de
- (#14174) X11 configuration.
  Now also considering the xserver name when deciding to use framebuffer.
* Fri Mar  1 2002 sh@suse.de
- Fixed bug #13630: inst_proposal reinitialized after selecting
  "No" in final installation confirmation (inst_doit)
* Fri Mar  1 2002 kkaempf@suse.de
- Fixed YaST2.firstboot to handle pcmcia network correctly (#13993).
* Thu Feb 28 2002 tom@suse.de
- (#14076) Now marking the monitor as "configured" and "needed".
* Thu Feb 28 2002 tom@suse.de
- (#13888) Libhd now delivers a fake monitor when no monitor can be probed.
  So inst_choose_desktop now checks for the unique_key of this fake monitor.
  Also improved logging for diagnosing purposes.
* Thu Feb 28 2002 sh@suse.de
- Fixed bug #13555: HW proposal error handling - added err logging
* Thu Feb 28 2002 sh@suse.de
- Fixed bug #13556: Installation proposal screen not re-translated
* Thu Feb 28 2002 gs@suse.de
- missing description for set "images" added (#1406)
- only one default button (#14067)
- correct installation of software packages in hardware configuration
  dialog (#14026)
* Thu Feb 28 2002 schubi@suse.de
- Installing 3d packages after rebooting #13659
* Thu Feb 28 2002 gs@suse.de
- improvements in popups used for software installation
* Thu Feb 28 2002 fehr@suse.de
- fixes the wrong default when selecting a swap partition in the
  custom partitioner and formatting is turned on.
* Wed Feb 27 2002 tom@suse.de
- (#13906) Invented a new function TimedOKCancelPopup() in
  common_popups.ycp. Using this function during X11-configuration.
* Wed Feb 27 2002 kkaempf@suse.de
- Allow splitted dirs (.../CD1, .../CD2, ...) for all network
  installs (#14009).
- Sort partitions combo box in bootloader dialogue (#14124).
* Wed Feb 27 2002 gs@suse.de
- proposal dialog: show a warning message, if the software selection is reset
  (bug #13942)
- set default button "Select/Deselect" in dialog Package Selection
* Wed Feb 27 2002 tom@suse.de
- (#13944) Now reading sysconfig with default value.
  This applies to language, keyboard, mouse and timezone.
  Moved SysconfigRead() to Misc-module.
* Wed Feb 27 2002 schubi@suse.de
- target.insmod to target.modprobe changed #13928
  ( update )
- LANG might not be in install.inf, get it from descr/info then.
  (#13959).
* Wed Feb 27 2002 kkaempf@suse.de
- fix checking VNC on startup.
* Wed Feb 27 2002 schubi@suse.de
- bugfix in starting update #13909
* Wed Feb 27 2002 schubi@suse.de
- setting keyboard while update #13610
* Tue Feb 26 2002 kkaempf@suse.de
- Fix "please wait" popup, wrap string in `Label().
* Tue Feb 26 2002 tom@suse.de
- (#13944) Now reading sysconfig with default value.
  This applies to language, keyboard, mouse and timezone.
* Tue Feb 26 2002 schubi@suse.de
- setting timezone moved to inst_rootpart ( update )
* Tue Feb 26 2002 arvin@suse.de
- fixed emergency unmounting of installation system
* Tue Feb 26 2002 kkaempf@suse.de
- add "sv_SV" for "swedish" to language list.
* Tue Feb 26 2002 fehr@suse.de
- fix syntax error in functions used during update
- add call to .lvm.init before rereading Lvm infos
* Tue Feb 26 2002 sh@suse.de
- Added help text for installation and hardware proposals
* Tue Feb 26 2002 sh@suse.de
- Removed leftover debugging condition from last checkin
* Tue Feb 26 2002 sh@suse.de
- "Only new installation" popup msg back from proof reading
* Tue Feb 26 2002 schubi@suse.de
- setting timezone after update #13651
* Tue Feb 26 2002 fehr@suse.de
- fix typo ia86 -> ia64 in do_propocal.ycp
* Tue Feb 26 2002 gs@suse.de
- software installation: show the package version in the
  description popup (bug #13750)
* Tue Feb 26 2002 schubi@suse.de
- initialize package agent correctly for update #13838
  ( grep and locate has not been updated )
* Tue Feb 26 2002 sh@suse.de
- Added notify popup when user wants to change installation mode
  and no Linux partitions were found
* Tue Feb 26 2002 kkaempf@suse.de
- Fix vnc password setting.
* Tue Feb 26 2002 kkaempf@suse.de
- fix VNC check and startup.
* Tue Feb 26 2002 kkaempf@suse.de
- remove "runme_on_start" early during first boot in order to
  prevent endless re-start (#13907).
- re-create "media" convenience symlinks (e.g. /cdrom->/media/cdrom)
  after update (#13756).
* Mon Feb 25 2002 tom@suse.de
- Corrected handling of wheel mice in Mouse.ycp.
- Extended mouse_raw.ycp with "wheels"-field.
* Mon Feb 25 2002 kkaempf@suse.de
- re-probe floppy and cdroms in installed system (#13828).
* Mon Feb 25 2002 kkaempf@suse.de
- Support installation via VNC.
* Mon Feb 25 2002 fehr@suse.de
- enable support for xfs, issue warning when it is used
- fix reading of fstab in installed system (#13457, #13455)
- fix wrong workflow in partitioner in installed system (#13456)
* Mon Feb 25 2002 sh@suse.de
- Changed order of initial installation proposals to match
  agreement with marketing and software ergonimists
* Mon Feb 25 2002 kkaempf@suse.de
- Enable "lo" interface when running in installed system.
- mout installation media read-only (#13846).
* Mon Feb 25 2002 sh@suse.de
- Fixed bug #13612: Call to obsolete Wizard::SetStage()
* Mon Feb 25 2002 sh@suse.de
- Fixed bug #13666: (Apparent) bad spelling
* Mon Feb 25 2002 kkaempf@suse.de
- write hardware status for all storage related devices (#13657).
* Mon Feb 25 2002 fehr@suse.de
- Fixed bug #11300, #13742 removal of a PV forgot partition marked
  for deletion
- handle active swap partition during installation
* Fri Feb 22 2002 gs@suse.de
- Fixed bug #13640: consider change of partitioning for software
  selection
* Fri Feb 22 2002 sh@suse.de
- Fixed bug #13341: Hardware Proposal must suppress missing configs
* Fri Feb 22 2002 lnussel@suse.de
- workaround to make textdomain call work
- Added some commandline switches to /sbin/yast2, like --list
  (Bug #13738)
* Thu Feb 21 2002 sh@suse.de
- Reimported monitor DB - fixed bug #13530: IBM monitor not detected
* Thu Feb 21 2002 kkaempf@suse.de
- Unmount installation medium in target system (#13706).
- Install "apmd" if pcmcia detected (#13713).
- Load "mousedev" if USB (wheel) mouse (#13654).
- Check for either IO or memory resource when checking for
  active storage controllers (#13567).
- Copy hardware status to target system (#13762).
* Wed Feb 20 2002 fehr@suse.de
- do not destroy proposal in `inst_mode when `installation is
  selected (#13644)
- reorder LVM changes in inst_predisk to make removal of PVs from
  VGs easier and make it succeed in more cases than before (#13415)
* Wed Feb 20 2002 sh@suse.de
- Fixed bug #13513: Double abort confirmation
* Wed Feb 20 2002 sh@suse.de
- Fixed bug #13594: Fallback for slide show "en" only, no longer
  "en_US", "en_GB", "en" (in this order)
* Wed Feb 20 2002 kkaempf@suse.de
- add agent for /etc/sysconfig/windowmanager.
- fix writing of hwstatus for disk controllers.
- fix symlink handling for cd-w and cd-rw (#13596).
- handle $(srcdir) correctly when installing .scr files.
- add "acpismp=force" to kernel command line for "ht" processors.
* Tue Feb 19 2002 kkaempf@suse.de
- Check for specific .S.u.S.E file, so multiple CDs can be copied
  into a single directory for network installation.
* Tue Feb 19 2002 tom@suse.de
- Now setting timezone info with hwclock_wrapper.
* Tue Feb 19 2002 kkaempf@suse.de
- Properly install "Vendor" module.
- Handle "Sourcemounted" from linuxrc and mount the medium if
  not done properly by linuxrc.
* Tue Feb 19 2002 fehr@suse.de
- fix missing "/data<n>" mount point in installed system (#13406)
* Tue Feb 19 2002 fehr@suse.de
- fix bug with windows resizing in old installation path
  (inst_target_selection.ycp, inst_target_part.ycp) (#13559)
* Tue Feb 19 2002 kkaempf@suse.de
- save 'configured' status of devices detected during installation
  in order to get hw-probing at boot time correct.
* Tue Feb 19 2002 kkaempf@suse.de
- Install SMP kernel if "ht" set in cpuinfo:flags (#13532).
- Keep old initrd, only add new modules.
* Mon Feb 18 2002 kkaempf@suse.de
- Handle update in Boot, merge old initrd modules with new (#13370).
* Mon Feb 18 2002 tom@suse.de
- Implemented reprobe functionality  for X11 config.
* Mon Feb 18 2002 sh@suse.de
- V 2.5.41
* Mon Feb 18 2002 fehr@suse.de
- Do not allow FAT partitions for system mountpoints (#13485)
- Do not allow some special characters in mountpoint (#13411)
- fix configuration of encrypted filesystems (#13268)
- fix inconsitencie in mount point suggestion (#13444)
* Mon Feb 18 2002 sh@suse.de
- Fixed bug #13383: Letters not mentioned as valid chars in help text
* Mon Feb 18 2002 kkaempf@suse.de
- Check pcmcia values in /etc/sysconfig/pcmcia instead of /etc/rc.config.
* Mon Feb 18 2002 sh@suse.de
- Fixed bug #10726: Installation log incomplete during slide show
* Mon Feb 18 2002 kkaempf@suse.de
- Move vendor driver update code to separate module.
* Mon Feb 18 2002 schubi@suse.de
- vim howto* and ttmkfdir added to force list #13195
- Removing release number while checking packages for force update #12187
* Fri Feb 15 2002 gs@suse.de
- Change source medium dialog: read the package information from
  the source medium (if mounting works)
* Fri Feb 15 2002 kkaempf@suse.de
- make symlinks for /sbin/yast, /sbin/YaST, /sbin/zast, and /sbin/ZaST (#13292)
* Thu Feb 14 2002 sh@suse.de
- inst_doit falls through back to proposal if inst_prepdisk etc. failed
- [Back] in update falls back to inst_mode
* Thu Feb 14 2002 kkaempf@suse.de
- recognize USB-Wheel mouse (imps2 protocol) (#13258).
* Thu Feb 14 2002 fehr@suse.de
- Fix ycp syntax error (#13214) when editing a dos partition
- Change second error dialog button in inst_prepdisk from
  "Cancel" to "Abort" (#13217)
* Thu Feb 14 2002 kkaempf@suse.de
- Make fstab entries for all /dev/fdX devices (#13235).
* Wed Feb 13 2002 sh@suse.de
- Changed default background color in installation start script
- Changed default geometry to 800x600 in start script
* Wed Feb 13 2002 sh@suse.de
- cut off one of the "easy installation" pics to get rid of tons
  of layout warnings (allow some pixels more space for buttons to
  grow)
* Wed Feb 13 2002 fehr@suse.de
- fix option handling for new version of mkreiserfs (#13205)
* Wed Feb 13 2002 gs@suse.de
- don't compare the release number of the installation source
  with the information saved on hard disk
* Wed Feb 13 2002 kkaempf@suse.de
- make remove button in physical volume dialog of PV work again
- remove correspondig create/remove pairs for LVM modify_targets
  (# 12083)
- add modify_targets to backup set of partition values
* Wed Feb 13 2002 kkaempf@suse.de
- Call BootLILO constructor for proper setting of lba_support.
* Wed Feb 13 2002 olh@suse.de
- default to GMT also on chrp and prep
* Wed Feb 13 2002 olh@suse.de
- dont call yast1 anymore on ppc
  dont write to non existant tty devices on iSeries
  handle p690 hvc console on startup
  update ask_for_TERM_variable
* Wed Feb 13 2002 olh@suse.de
- add support for p690 hvc console in postinstall
  activate all 41prep boot partitions on iSeries
* Wed Feb 13 2002 olh@suse.de
- add fixes for console font. whitespaces
- add ja_JP.sjis entry to consolefonts.ycp
* Wed Feb 13 2002 olh@suse.de
- add ppc64 keymaps
* Tue Feb 12 2002 fehr@suse.de
- fix bug in doing a valid proposal when using only primary
  partitions and /boot is needed (#13184)
- V 2.5.39
* Tue Feb 12 2002 kkaempf@suse.de
- remove superfluous calls to inst_ask_hardware.
* Tue Feb 12 2002 sh@suse.de
- V 2.5.37
- Initial call to submod Write() func in proposal (for HW config)
* Tue Feb 12 2002 kkaempf@suse.de
- setup "lo" during network install.
* Tue Feb 12 2002 sh@suse.de
- V 2.5.35
* Tue Feb 12 2002 sh@suse.de
- Added images for new "easy installation" layout
* Tue Feb 12 2002 msvec@suse.cz
- added network proposals
- 2.5.34
* Tue Feb 12 2002 kkaempf@suse.de
- hwclock runs only GMT on sparc and iseries.
- dont write FQHOSTNAME.
* Tue Feb 12 2002 kkaempf@suse.de
- write keyboard data to /etc/sysconfig/keyboard instead of sysconfig/console.
* Mon Feb 11 2002 kkaempf@suse.de
- re-config network device even on 'warm' boot.
* Mon Feb 11 2002 fehr@suse.de
- following changes in partition proposal:
  try not to create an extended partition when enough primaries are
    available
  split swap from root slots large enough if at all possible
* Thu Feb  7 2002 pblahos@suse.cz
- proposal_printers changed to proposal_printers
* Thu Feb  7 2002 kkaempf@suse.de
- save infoMap and installMap for re-use after reboot.
* Wed Feb  6 2002 sh@suse.de
- Provides/obsoletes yast
* Tue Feb  5 2002 sh@suse.de
- Timeout upon msg "now booting your system"
  unless a hard reboot is required
* Tue Feb  5 2002 kkaempf@suse.de
- Properly reboot when adding ide-scsi to cmdline.
- Re-config ethX for all network installation modes.
- Restart portmapper for "nfs" installation mode.
* Tue Feb  5 2002 kukuk@suse.de
- Try to clear terminal before we ask for TERM variable [Bug #12848]
* Tue Feb  5 2002 sh@suse.de
- Fixed bug #13040: yast2 should not require saxtools
* Tue Feb  5 2002 kkaempf@suse.de
- Make "custom" boot loader field an editable combo box (#11821).
* Mon Feb  4 2002 snwint@suse.de
- added 'change-rules reset' to lilo.conf to prevent lilo from rewriting
  the partition table (#11875)
* Fri Feb  1 2002 gs@suse.de
- Single Package Selection: optimize checks when selecting a package
* Thu Jan 31 2002 sh@suse.de
- Made proposal aware of language changes
- Reintroduced inst_mode unless absolutely clear if update possible
* Thu Jan 31 2002 kkaempf@suse.de
- recognize "imps2" mice.
* Thu Jan 31 2002 kkaempf@suse.de
- Fix writing of yast.inf
* Wed Jan 30 2002 kkaempf@suse.de
- force /dev/cdrom symlink to point to boot cdrom.
- work around linuxrc "InstMode" bug.
* Wed Jan 30 2002 kkaempf@suse.de
- drop ag_yast agent, do yast.inf writing in Misc module.
* Wed Jan 30 2002 kkaempf@suse.de
- make cd-links prior to re-mounting.
* Wed Jan 30 2002 gs@suse.de
- bugfix concerning software installation workflow:
  read local package description instead of information from mounted medium
* Wed Jan 30 2002 kkaempf@suse.de
- make device symlinks earlier.
* Tue Jan 29 2002 kkaempf@suse.de
- write lilo to /dev/md if /boot is on raid1.
- adapting update to new agents.
* Tue Jan 29 2002 arvin@suse.de
- always use ini-agent instead of rcconfig-agent;
  bugfix syntax error in Bootloader module
* Mon Jan 28 2002 kkaempf@suse.de
- Simplify bootloader proposal.
- Adapt to changed install.inf syntax.
* Mon Jan 28 2002 gs@suse.de
- internal changes concerning the initialization of the package agent
* Thu Jan 24 2002 gs@suse.de
- bugfixes package installation workflow (already installed system)
* Wed Jan 23 2002 schubi@suse.de
- include/packages added in specfile
* Tue Jan 22 2002 schubi@suse.de
- Saving user package selections
* Mon Jan 21 2002 nashif@suse.de
- Skip confirmation(inst_doit)  in autoinst mode
  if requested in control file
* Mon Jan 21 2002 schubi@suse.de
- bufixes in installing packages after reboot
* Fri Jan 18 2002 kkaempf@suse.de
- more agents moved here.
- Fixed initrd creation, corrected module order.
- Final installation workflow (3 clicks !) and button labels.
* Tue Jan 15 2002 kkaempf@suse.de
- move bootloader do* scripts to bootloader sub-directories.
- fix bootloader proposal and texts.
* Mon Jan 14 2002 kkaempf@suse.de
- add dasddev.scr etc_cryptotab.scr etc_fstab.scr parted_check.scr
  parted_print.scr pdisk.scr proc_meminfo.scr proc_swaps.scr
  run_swapon_s.scr to ycp/partitioning/agents
- remove conf directory
* Mon Jan 14 2002 kkaempf@suse.de
- Integrate bootloader proposal.
* Thu Jan 10 2002 kkaempf@suse.de
- fix filelist.
* Thu Jan 10 2002 sh@suse.de
- Added proposal files to spec file file list
* Wed Jan  9 2002 kkaempf@suse.de
- pass filesystem module needed for "/" to Boot module.
* Tue Jan  8 2002 kkaempf@suse.de
- integrated software and partition proposal.
* Fri Jan  4 2002 arvin@suse.de
- adapted the new SCROpen syntax
* Fri Jan  4 2002 kkaempf@suse.de
- Complete modularization, drop user_settings.
- Implement new workflow, based on proposals, requiring
  a minimum amount of mouse clicks.
- Add support for auto installation.
* Mon Dec 10 2001 kkaempf@suse.de
- Greek locale fix (el_GR@ISO8859-7 instead of el_GR@euro, #12587)
* Wed Nov 21 2001 sh@suse.de
- Fixed bug #12381: YaST2 ignores ENABLE_SUSECONFIG in rc.config
* Thu Nov 15 2001 sh@suse.de
- V 2.5.8
- Fixed lots of missing lookup() default values
- Migrated inst_startup to new ProgressBar wizard
* Fri Oct 19 2001 ms@suse.de
- include BusID statement if r128 driver is used. This is needed
  for the r128 driver on PPC and does not influence the i386 setup
  negatively [y2xr40.pl] Bug: 11689
* Thu Oct 18 2001 tom@suse.de
- (#11689) Necessary changes to provide the BusID on PPC/r128.
* Thu Oct 18 2001 tom@suse.de
- (#11876) Corrected Symbols for Japanese. nec/jp --> jp.
* Tue Oct 16 2001 tom@suse.de
- (#11847) X11-config. Now using new y2xr40 parameter "-o <option-csl>".
* Tue Oct 16 2001 sh@suse.de
- V 2.5.4
- Migration to yast2-devtools
* Mon Oct 15 2001 ms@suse.de
- include a general parameter called --option which
  requires a comma separated list of options. This is the better
  solution if we need special options for calling y2xr40.pl
* Mon Oct 15 2001 sh@suse.de
- Fixed bug #11812: patch_lilo_conf produces double initrd entry
* Fri Oct 12 2001 tom@suse.de
- (#11672) Extended some YCP files with special cases for PPC.
* Fri Oct  5 2001 kkaempf@suse.de
- present button "format floppy" if mount fails (#1220).
* Thu Oct  4 2001 lnussel@suse.de
- do not overwrite softwaresel in usersettings if it's already set
* Wed Oct  3 2001 olh@suse.de
- first part of bootconfiguration for ppc (#5440) ..............
* Wed Oct  3 2001 olh@suse.de
- do not create floppy link on new Macs and iSeries
  write fstab correctly, not type auto for known filesystems
  whitespaces..
* Wed Oct  3 2001 olh@suse.de
- do not force xf3 on ppc. the whole Xsetup is still broken...
* Wed Oct  3 2001 olh@suse.de
- add mol and sudo to package list on pmac
  small whitespace fixes
* Wed Oct  3 2001 olh@suse.de
- do not call mk_initrd on ppc in inst_finish_update
* Wed Oct  3 2001 olh@suse.de
- fix handling of chrp kernels, compare lowercase strings
  use name_of_kernel_image for usersettings,
  s390 and axp must be verified (#9713)
* Tue Oct  2 2001 olh@suse.de
- add keymap2mac.ycp to filelist (#11336)
  fix english-us and uk list
* Fri Sep 28 2001 fehr@suse.de
- add dasd-parameter to S390 boot configuration
* Thu Sep 27 2001 fehr@suse.de
- remove entry bus -> "SCSI" for LVM VGs
* Thu Sep 27 2001 olh@suse.de
- install pmud on pmac and remove some obsolete packages on pmac
* Thu Sep 27 2001 kkaempf@suse.de
- drop 3-button emulation since it might interfere with X11
  button events (#11204).
* Wed Sep 26 2001 tom@suse.de
- (#11315 addendum) Now also updating the path section.
* Wed Sep 26 2001 kendy@suse.cz
- update_unique_keys.pl: call hwinfo with --all instead of --reallyall
  (#11340).
* Wed Sep 26 2001 sh@suse.de
- Reimported monitor DB (bug #11252: Iiyama monitors missing)
* Wed Sep 26 2001 kkaempf@suse.de
- add /sbin:/usr/sbin to runtime PATH.
- vendor.ycp: message is string, not locale.
* Tue Sep 25 2001 tom@suse.de
- (#11315) X11 reconfig: Now also updating the card section.
* Tue Sep 25 2001 kkaempf@suse.de
- re-probe for mountable media (floppies) after loading
  of usb-storage (#11299).
* Tue Sep 25 2001 kkaempf@suse.de
- make proper re-use of messages in inst_finish_update to get
  correct translations.
- prepare a mtab for mk_initrd after update.
- if first bios drive isn't hda, lilo probably wants to know about this.
* Mon Sep 24 2001 snwint@suse.de
- do not try to install lilo into a raid partition (#10329)
* Mon Sep 24 2001 sh@suse.de
- Added final "all the rest" step for SuSEconfig
* Mon Sep 24 2001 lnussel@suse.de
- do not mount ntfs partitions automatically during installation (#11222)
* Mon Sep 24 2001 kkaempf@suse.de
- If the mouse was choosen manually, going back must present
  mouse selection again (#11235).
- No need to make a backup of /etc/fstab in inst-sys, there's none anyway.
  Then inst_finish_update gets the correct fstab (#11215).
* Mon Sep 24 2001 kkaempf@suse.de
- update NVIDIA kernel modules regardless of version (#11091).
* Mon Sep 24 2001 kkaempf@suse.de
- set console keyboard even when called standalone (#11223).
* Mon Sep 24 2001 kkaempf@suse.de
- split language and encoding to prevent gettext from applying
  it's own recoding.
* Mon Sep 24 2001 sh@suse.de
- Correctly init slide show in installed system so YOU and single
  package installation works OK
* Mon Sep 24 2001 kkaempf@suse.de
- Load usb-storage last in order to not interfere with other storage
  module (9490).
* Sun Sep 23 2001 mike@suse.de
- (#11188) Press back at the "suggested partitioning" screen followed by
  "next" and YaST2 says "You have rejected the proposal.
  RAID: bugfix: user are not allowed to remove RAID Devices in UI
  which are already exist.
* Sun Sep 23 2001 kukuk@suse.de
- Check for color depth, not # of colors for slide show to avoid
  problems with overflow (#11178)
* Sat Sep 22 2001 kukuk@suse.de
- Sync X11 font path with SaX2
- Enable jfs and ext3 on PPC (#11194)
* Sat Sep 22 2001 fehr@suse.de
- add "ori_nr" entries for lvm and md devices
- add empty argument to SCR call
* Sat Sep 22 2001 tom@suse.de
- (#10421) Fixed the focus switch.
* Fri Sep 21 2001 mike@suse.de
- md: detect number of raid partitions per RAID only for new created RAIDs
- md: do not let the user edit or delete already existing RAIDs
- swap: activate per default all swap partitions automatically
-modules: switch on automatical load of modules when Y2 is mounting
    filesystems, so that undetectebal and not formated fs are mounted
    properly
* Fri Sep 21 2001 sh@suse.de
- Fixed bug #10303: Must press 'back' twice in 'choose part. to boot'
* Fri Sep 21 2001 fehr@suse.de
- allow adding of mount points to LVs in lvm runtime config
- prevent formatting of edited LV in lvm runtime config
- allow handling of ataraid devices (e.g. /dev/ataraid/d0p0)
- prevent partitions with id 0x8E from being written to fstab (#10390)
* Fri Sep 21 2001 sh@suse.de, gs@suse.de
- Only ONE SlideShow::OpenSlideShowDialog() in all modes -
  avoid confusion, much more reliable in all the different modes
* Fri Sep 21 2001 lnussel@suse.de
- no longer mark partitions with id 130 automatically as swap
- do not change flags for swap devices in fstab if more than one
  such entry exists
- properly hande fstab entries for moved logical partitions (#11074)
- change fstab entry for first occurence of a device, instead of
  creating a new one
- do not create directories for swap partitions
* Fri Sep 21 2001 mike@suse.de
- lvm_config now works in ncurses
* Fri Sep 21 2001 gs@suse.de
- installation startup always (not only in manual mode) checks whether a
  kernel module is already loaded
  (workaround for bug #10983)
* Fri Sep 21 2001 sh@suse.de
- Fixed bug #9977: Abort button doesn't work during slide show
* Fri Sep 21 2001 ms@suse.de
- fixed access control bug during X11 reconfiguration
  with YaST2. For further details see Bug: [10921]
* Fri Sep 21 2001 fehr@suse.de
- fix impossible 0 as stripe size in LV dialog
- make lvm configuration in system work again (#10291)
* Fri Sep 21 2001 kendy@suse.cz
- Update /var/lib/YaST/unique.inf during update (bug 10931, 10941)
* Fri Sep 21 2001 kkaempf@suse.de
- default medianame to "CD" (11106).
* Thu Sep 20 2001 fehr@suse.de
- Fixed bug #10963: Now an update on systems using encrypted fs is
  possible
* Thu Sep 20 2001 sh@suse.de
- Fixed bug #10325: Save settings to floppy doesn't work
- Reading log file of mkinitrd and lilo correctly #11030
  (inst_finish_update.ycp)
- Correct cancel popup added #10951( inst_kernel.ycp )
* Thu Sep 20 2001 kkaempf@suse.de
- "break" is not allowed inside "foreach" (11015).
- properly extract module arguments (11015).
- umount medium before ejecting (11053).
- offer "save & exit" in media selection (11086).
* Thu Sep 20 2001 lnussel@suse.de
- do not create symlink for mountpoint if it would point to itself
* Thu Sep 20 2001 lnussel@suse.de
- fstab entries for mount flags, passno etc are no longer changed
  for existing entries
* Thu Sep 20 2001 mike@suse.de
- bug 11063: YaST2 trys to change fsids of pdisk-label partitions, and
  popups therefore irritating popups
* Thu Sep 20 2001 fehr@suse.de
- fix problem when root fs is md of personality raid5 (#10747)
* Thu Sep 20 2001 tom@suse.de
- (#10920) Now the presence of the dummy packages is checked at first.
* Thu Sep 20 2001 kkaempf@suse.de
- Remove old release number file before installing new one (#10992).
* Thu Sep 20 2001 sh@suse.de
- Fixed bug #10684: Monitor DB outdated
* Thu Sep 20 2001 fehr@suse.de
- Do not delete modify_targets in inst_sw_select.ycp except when
  using a while disk for installation
* Thu Sep 20 2001 lnussel@suse.de
- Fixed root filesystem on raid leads to corrupted fstab (#10418)
* Wed Sep 19 2001 mike@suse.de
- Bugfix: if zero partition table: resync /proc/partitions
  Added warning, if "/" is /dev/md and there is no /boot
- Downgrade versions correctly #10906 ( inst_sw_update.ycp )
* Wed Sep 19 2001 snwint@suse.de
- YaST2.start: mtab might be missing, avoid error message
- unmounting proc filesystem in inst_finish_update.ycp
- start X-Server for testing with "-ac", needed when starting
  from inside YCC.
* Wed Sep 19 2001 fehr@suse.de
- force a hard reboot when root filesystem is on a md device
- Logging reduced in inst_rpmupdate.ycp
* Wed Sep 19 2001 sh@suse.de
- Fixed bug #10909: Complaint about slide show init in log file
- Added more packages for version 6.2 in forceUpdate.ycp
- No error, if the versions of updated packages differs from common.pkd
* Wed Sep 19 2001 kkaempf@suse.de
- Fix installing package information to updated target.
- Eject CDs on PPC only when unmounting.
* Wed Sep 19 2001 kkaempf@suse.de
- Fix "Lithuanian" with native translation in language list.
- Properly label progress bar during swap formatting.
- Use predefined button labels for continue/cancel/retry if partitioning
  or formatting fails.
- preselect first partition #10840 (inst_rootpart.ycp)
- /sbin/yast2: add "-f" to 'rm'.
* Tue Sep 18 2001 schubi@suse.de
- Silly testpopup in inst_finish_update removed.
- packages for 7.2 added #10874" (forceUpdate.ycp)
* Tue Sep 18 2001 schubi@suse.de
- Recognize update mode after reboot ( installation.ycp )
- /mnt to Installation::destdir changed ; checking modus improved in
  inst_sw_backup.ycp
* Tue Sep 18 2001 sh@suse.de
- V 2.4.84
- Fixed bug #10859: Inconsistent "needed from CD" values
* Tue Sep 18 2001 tom@suse.de
- (#10762) Popups displayed in Richtext now (with scroll bars).
* Tue Sep 18 2001 sh@suse.de
- Fixed bug #10411: Show difference between pkg deleting and inst.
- Fixed bug #10793: Unmounting /mnt after update.
* Tue Sep 18 2001 tom@suse.de
- Added script call when switching 3D <--> 2D mode. (#10761)
- Module inst_config_x11.ycp
* Tue Sep 18 2001 kkaempf@suse.de
- only use "switch2mesasoft" for non-3d x11 setups.
* Tue Sep 18 2001 lnussel@suse.de
- do not try to create or change /etc/raidtab if raid is active
  while the user has changed nothing
* Tue Sep 18 2001 mike@suse.de
- bug 10673: need /boot if no ext2 on /
- bug 10686: swap <= 1GB
- show raid size correct: existing raid and raid in LVM
- ignore automatic inserted mountpoints
- pdisk: size of partition for inst_doit fixed
* Tue Sep 18 2001 fehr@suse.de
- shut down LVM VGs and umount /etc/lvmtab.d in inst_finish.ycp
* Tue Sep 18 2001 lnussel@suse.de
- workaround for '&'-character not displayed in ncurses menu
* Tue Sep 18 2001 lnussel@suse.de
- removed the texdomain switching from menu.ycp (Bug #10819)
- only create fstab entry for partitions if user explicitly
  entererd a mountpoint, instead of inventing one
* Tue Sep 18 2001 kkaempf@suse.de
- properly pass encoding ("UTF-8", "ISO-8859-X", ...) via SetLanguage() (#10807).
- drop unsupported "korean" from language list.
- properly detect that X11 couldn't be started and present
  and appropriate error message.
- just skip unknown options.
- stop SCR and all agents on target before umounting filesystems
  from WFM.
- remove faked /etc/mtab from target.
- Installation::normal_mode = true if running in installed system.
  (neither initila_mode, nor continue_mode).
- fix parport zip module loading.
* Mon Sep 17 2001 kkaempf@suse.de
- write language back to /etc/yast.inf (#9790).
- umount all filesystems in target, except "/". Umount this
  from WFM after stopping SCR (#10685).
- Reading language from user_settings while selection kernel
- Showing correct counter of updated packages
- Button -Old Version- changed #10559
- ChangeCD --> ChangeMedium
- include package_utils removed #10763
* Mon Sep 17 2001 kkaempf@suse.de
- use "lt-brim-8x14" font and "iso-8859-13" encoding for 'Lithuanian'.
* Sun Sep 16 2001 kkaempf@suse.de
- only symlink /dev/cdrom once (#10370).
* Fri Sep 14 2001 kukuk@suse.de
- On SPARC print error message about SILO, not LILO
* Fri Sep 14 2001 kkaempf@suse.de
- adapt language list accoring to doc department.
* Fri Sep 14 2001 tom@suse.de
- Bugfix #9986: Reduced suggestion refresh to 75 Hz.
* Fri Sep 14 2001 mike@suse.de
- bug 10200: check the proposal for failures
  make a boot partition if possible
  bug 10347: set whole_diskflag
  bug 10044: set a message when proposal is discarded
* Fri Sep 14 2001 kkaempf@suse.de
- fix inst_environment for standalone mode (#10413).
- respect user choice to NOT install a module (#10665).
* Fri Sep 14 2001 tom@suse.de
- Fixed Bug #10651: Autoadjusting refresh/resolution/color-depth now correct.
* Fri Sep 14 2001 kkaempf@suse.de
- set correct Installation::encoding in continue_mode (#10611).
* Fri Sep 14 2001 mike@suse.de
- dont reread partition data always at start of inst_custom
  activate lvm if at least one vg exist
- check if textmode due to memory restrictions or x11 failure (#10134).
- use Arch and Installation modules in inst_environment (#10413).
- pkginfo release common.pkd before releasing CD 1 #10555
* Fri Sep 14 2001 kkaempf@suse.de
- correct handling of 'splitted' media (#10532)
- touch/remove /var/run/yast.pid
* Thu Sep 13 2001 snwint@suse.de
- dolilo: new mk_initrd needs fb resolution for splash screen config
- Taking long language for kernel description #10556 #1552
- No penguin progress bar in kernel selection module #10311
- Button -Old Version- changed #10559
* Thu Sep 13 2001 kkaempf@suse.de
- dont probe mouse on serial console.
- dont probe mouse outside of initial_mode.
- sort languages by ascii equivalent.
* Thu Sep 13 2001 kkaempf@suse.de
- enable software selection on S/390 (froh@suse.de).
- show proper boot-loader partition even if we don't have lilo (froh@suse.de).
- load input, hid, and mousedev if USB-mouse detected (#9228).
- default medium is CD (#10374)
- re-enable WFM::SetLanguage(), regexp bug in glibc identified,
  workaround in liby2 applied. (#10496)
- use /boot/zilo-kernel/image instead of /boot/vmlinuz on S/390 (froh@suse.de).
- sort language list alphabetically (#10516).
* Wed Sep 12 2001 kkaempf@suse.de
- drop all WFM::SetLanguage()
- Unmounting partitions correctly while going back #10125
- REQUIRES are ordered; qt, qt-japanese.... in the selection box
- Warning popup for single selection removed while going backward
  in the software selection #10339
* Wed Sep 12 2001 snwint@suse.de
- revert latest vmware changes to YaST2.start
* Wed Sep 12 2001 kkaempf@suse.de
- drop initial WFM::SetLanguage()
* Tue Sep 11 2001 kkaempf@suse.de
- Initial zipl configuration for S/390.
* Tue Sep 11 2001 kkaempf@suse.de
- Unmount .probe and .disk agent before package installation.
* Tue Sep 11 2001 kkaempf@suse.de
- call SetLanguage in UI and WFM.
* Mon Sep 10 2001 snwint@suse.de
- create 'failsafe' instead of 'suse' entry in lilo.conf
- don't overwrite existing vmlinuz.suse
* Mon Sep 10 2001 snwint@suse.de
- make YaST2.start work with vmware
* Mon Sep 10 2001 sh@suse.de
- Fixed bug #10350: YaST2 doesn't look good with anti-aliasing
* Fri Sep  7 2001 sh@suse.de
- Fixed bug #10244: No slide show unless at least 800x600x256col
- center slide show image
* Fri Sep  7 2001 sh@suse.de
- V2.4.64
* Fri Sep  7 2001 pblahos@suse.cz
- hotplug is started instead of usbmgr during YaST2.firstboot
* Fri Sep  7 2001 sh@suse.de
- CD remaining times more pessimistic
* Fri Sep  7 2001 kkaempf@suse.de
- fix textmode recognition with help of GetDisplayInfo().
* Thu Sep  6 2001 kkaempf@suse.de
- fix X11 resolution dedection if 3D is selected.
* Thu Sep  6 2001 sh@suse.de
- V 2.4.62
- Correctly reinitialize packager in continue mode
  - > correct remaining times / progress bar display
* Thu Sep  6 2001 kkaempf@suse.de
- drop extraction of boot parameter from lilo setup, already
  done at startup. (#10223)
- fix reading of local package information.
- check if mount point is in use in InstMedia
* Wed Sep  5 2001 schubi@suse.de
- Do not upgrade a package which produces package conflicts.
* Wed Sep  5 2001 sh@suse.de
- Fixed bug #10063: bad display of hd partitions in inst_doit
  Re-used existing function from partitioning
* Wed Sep  5 2001 sh@suse.de
- Fixed bug #10084: zero size for k_deflt
* Wed Sep  5 2001 kkaempf@suse.de
- add belgian keyboard to keyboard list (#9577)
* Wed Sep  5 2001 kkaempf@suse.de
- fix runtime installation and configuration of X11.
* Wed Sep  5 2001 kkaempf@suse.de
- dont unmount installation medium if wrong product id detected,
  honor user request to ignore this fact.
* Tue Sep  4 2001 kkaempf@suse.de
- use plain ascii language names if running in text mode (#10026).
- correct parameter for setEnvironment
* Tue Sep  4 2001 fehr@suse.de
- add dummy parameter to SCR::Write(.lvm.deactivate)
- deactivate lvm only when running in inst-sys
* Tue Sep  4 2001 mike@suse.de
- partproposal always creates /boot
  bugfix inst_do_resize: resize always when a "resize" is in targetmap
  software installation in installed system fixed
* Tue Sep  4 2001 sh@suse.de
- Reimported monitor db
* Tue Sep  4 2001 kkaempf@suse.de
- get {install,delete}_list in inst_rpmcopy from user_settings if
  not passed otherwise.
* Tue Sep  4 2001 snwint@suse.de
- YaST start script: use vmware server module, not vga16
* Tue Sep  4 2001 kukuk@suse.de
- inst_silo_expert.ycp: Initialize PROM/boot-device variablen
- inst_disk.ycp: Fix allowed filesystems on sparc [Bug #9678]
* Mon Sep  3 2001 kkaempf@suse.de
- recognize IDE CD-R(W) drives and set up ide-scsi automatically.
- Hard reboot after update, if the installed kernel differs from
  the kernel which has been booted #10103
- Checking dependencies in -only update modus- too #10043
* Mon Sep  3 2001 kendy@suse.cz
- keyboard_raw.ycp: group(shift_toggle) is not needed for the
  Czech and Slovak keyboards any more...
  (In fact, it breaks them.)
* Mon Sep  3 2001 kkaempf@suse.de
- sort keyboards alphabetically.
- Error popup for dolilo #9729
* Sat Sep  1 2001 kukuk@suse.de
- Show warning about PROMs with 1GB bug only on sparc32
- If /boot is selected for the boot manager, this is Ok on SPARC.
  Remove extra warning on SPARC since it is wrong here.
- Disable gpm if we install over serial console
* Fri Aug 31 2001 kkaempf@suse.de
- fix installation path handling and mounting
  should now work for CD, DVD, Harddisk, Nfs, and Smb
* Thu Aug 30 2001 kkaempf@suse.de
- modularized SlideShow.
- New help text in upgrade frame
- properly recode output of commands to utf-8
- allow change of installation medium on server (Nfs/Ftp/Smb)
- Short language description in inst_sw_select removed.
- fixed some parse errors <msvec@suse.cz>
- added abuild parse check <msvec@suse.cz>
* Wed Aug 29 2001 kkaempf@suse.de
- unmount wrong medium.
* Wed Aug 29 2001 kkaempf@suse.de
- always give all alternatives in ChangeCDPopup.
- always do a hard reboot after installation from first medium.
* Wed Aug 29 2001 kkaempf@suse.de
- properly handle media release and product codes.
- initialize PKGINFO to installed data in continue_mode.
* Wed Aug 29 2001 kkaempf@suse.de
- re-read installation data in continue_mode.
* Tue Aug 28 2001 kkaempf@suse.de
- properly switch SCR during update.
- write YaST information after re-mounting installation medium.
- fix re-mounting of source medium in continue_mode
- re-init PKGINFO environment in continue_mode
- Packagelist added which have to be updated without checking version.
* Tue Aug 28 2001 kkaempf@suse.de
- use "Installation" module in update.
* Tue Aug 28 2001 kukuk@suse.de
- Fix dosilo script for new /proc behaviour with kernel 2.4.x
  print a message about SuSE Linux version before loading the
  kernel
* Tue Aug 28 2001 sh@suse.de
- Fixed bug #9900: No ISDN for SPARC
- inst_rpmcopy now displays remaining times for each CD
- slide show
* Tue Aug 28 2001 kendy@suse.cz
- inst_hw_config.ycp: maps describing the devices to configure can
  have a list "force_reread". It is useful for modules which
  call another one to configure something (e.g. TV may call Sound)
* Tue Aug 28 2001 mike@suse.de
- fix: part_proposal only for arch == i386
* Mon Aug 27 2001 kkaempf@suse.de
- Clean up SCR/WFM handling. WFM is always local, SCR is always the target.
- Introduce modules for Installation, InstMedia, PackageIO, and MediaUI.
- Prepare for multiple DVD installation.
- Prepare for Ftp, Harddisk, and SMB installation.
- Finally clean up installMap handling.
* Thu Aug 23 2001 kukuk@suse.de
- Don't reboot if we use k_deflt on UltraSPARC
* Thu Aug 23 2001 pblahos@suse.cz
- Fixed: there were 2 arrows in progressbar shown during hw probe.
* Wed Aug 22 2001 kkaempf@suse.de
- fixed X11 setup
* Mon Aug 20 2001 mike@suse.de
- partition proposal creates swap partitions
* Mon Aug 20 2001 kkaempf@suse.de
- dont write "swap" to yast.inf, but "RebootMsg 0" instead
* Sat Aug 18 2001 tom@suse.de
- Finished new X11 configuration dialog incl. control center ability.
* Fri Aug 17 2001 kkaempf@suse.de
- implement and use "Arch" module.
- provide modules directory in specfile.
- reduce number of timezones.
- Patch runlevel in /etc/inittab while updating the system.
* Fri Aug 17 2001 schubi@suse.de
- .targetroot to .root changed
* Tue Aug 14 2001 kendy@suse.cz
- keyboard_raw.ycp: cs, cs_qwerty -> cz, cz_qwerty
- Added slovak keyboard.
* Fri Aug 10 2001 tom@suse.de
- X11 configuration:
- Completely redesigned the xf86config module for use with the new
- agent-isax.
- Outsourced functions for X11 keyboard manipulation.
- Outsourced functions for X11 mouse manipulation.
- Outsourced functions for X11 card manipulation.
- Outsourced functions for X11 desktop manipulation.
- Outsourced functions for X11 path manipulation.
- Added batch mode for use with autoinst in xf86config.ycp.
* Fri Aug 10 2001 jbuch@suse.de
- added SW-RAID support for installation Workflow
- added sequencer
* Fri Aug 10 2001 kkaempf@suse.de
- extract kernel parameters from /proc/cmdline and pass them to LILO
* Fri Aug 10 2001 kukuk@suse.de
- Only ask for TERM variable if we use serial console and not if
  we are in text mode (#9701)
* Fri Aug 10 2001 kkaempf@suse.de
- partitioning enhancements for automatic and runtime usage
- copy info and update.in_ after CD1 installation, not before
* Thu Aug  9 2001 kkaempf@suse.de
- check /proc/modules before asking for module load (#9698)
* Thu Aug  9 2001 snwint@suse.de
- yast2 text mode starts on /dev/console, not tty3
- /mnt is a link on LiveEval: don't umount it
* Wed Aug  8 2001 kkaempf@suse.de
- mount and mk*fs are .local not .target actions
* Wed Aug  8 2001 kkaempf@suse.de
- adapt driver loading to new .probe format
- replace .target.inject calls
* Tue Aug  7 2001 kkaempf@suse.de
- replace use of targetroot in favour of system agent.
* Tue Aug  7 2001 kkaempf@suse.de
- skip "whole disk" partitions on BSD disks. (#7904)
- Activate button in lilo now reads "Activate LILO partition". (#7884)
* Mon Aug  6 2001 kukuk@suse.de
- Add script to ask for TERM variable to yast2-instsys, too.
* Fri Aug  3 2001 arvin@suse.de
- don't start vga x11 server on ppc (bug #9622)
* Fri Aug  3 2001 arvin@suse.de
- added inst_part_proposal.ycp to inst-sys
* Fri Aug  3 2001 kukuk@suse.de
- If installed over serial console ask the user for the TERM
  variable and write it to /etc/install.inf
* Thu Aug  2 2001 mike@suse.de
- taged version for 7.3 - preview 3
* Tue Jul 31 2001 mike@suse.de
- first Version for RAID and partition proposal
  (only for translation, dosn't work properly)
* Fri Jul 27 2001 kkaempf@suse.de
- initial slide show code for package installation
* Fri Jul 27 2001 kkaempf@suse.de
- ask for confirmation before loading module in manual mode
* Fri Jul 27 2001 kkaempf@suse.de
- fix initrd module handling
  properly pass options to modules.conf
  use agent-modules in inst_finish
* Thu Jul 26 2001 kkaempf@suse.de
- minor text changes
* Tue Jul 24 2001 fehr@suse.de
- add detection of md devices to function GetLvmMdSystemInfo
* Wed Jul 18 2001 fehr@suse.de
- fix a bug in LVM configuration for devices /dev/ida/, /dev/rd/
  and /dev/cciss/
* Mon Jul 16 2001 kkaempf@suse.de
- fix keyboard data for swedish
* Thu Jul 12 2001 sh@suse.de
- Improved inst_startup UI: More feedback
* Tue Jul 10 2001 sh@suse.de
- Improved inst_suseconfig UI: Give feedback for individual steps
* Fri Jul  6 2001 kkaempf@suse.de
- merge SLES fixes
- add JFS as filesystem
* Thu Jul  5 2001 schubi@suse.de
- New handle of package selection groups.
* Thu Jul  5 2001 sh@suse.de
- Fixed bug #9277: Bad initial focus in menu.ycp
* Wed Jul  4 2001 sh@suse.de
- Redesigned inst_doit: Now using RichText widget
* Mon Jul  2 2001 kkaempf@suse.de
- merge with 7.1-axp fixes:
  fix user information for vfat /boot
  format /boot as fat on milo and ia64
  changed 'doaboot' to get a useable /etc/aboot.conf
  force "-t vfat" for mount of /boot on MILO machines
  check cylinder boundaries on "aboot" only, not "axp" in general
  format /boot on "milo" machines with mkdosfs
  boot_mode "milo" on Alpha has FAT disklabel
  use smp flag from install.inf instead of probing on Alpha
  select correct cpml package for cpu model on Alpha
  auto-select aboot or milo on Alpha
  use data from milo package for installation
  write correct /etc/aboot.conf
  fix kernel image names for depmod
  for /boot to be FAT16 for MILO machines
  implemented boot loader installation on Alpha
  fix handling of XkbModel on pmac
  remove arch_ppc check in inst_lilo_expert.ycp #6684
  add missing pdisk partition type #6688
  allow update on a drive with pdisk label #6689
* Mon Jun 25 2001 kkaempf@suse.de
- tell about reboot after first round of installation (#7994)
- modprobe "hid" and "mousedev" if "usb mouse" choosen from list (#8215)
- close CD tray before executing mount (#8492)
* Fri Jun 22 2001 kkaempf@suse.de
- dont mention LILO on ia64 (#9003)
* Wed Jun 20 2001 fehr@suse.de
- add necessary changes to handle LVs in fstab in running system
* Tue Jun 19 2001 fehr@suse.de
- add changes for lvm configuration in installed system to
  handle /etc/fstab reasonable.
- Enable "next" button in selection ftp-server (#8641)
* Tue Jun 12 2001 sh@suse.de
- V 2.4.1
  Fixed bug #8726: SuSEconfig fails on SPARC with serial console
- Fixed bug #8641: Allow "next" button in choosing ftp server
* Tue Jun 12 2001 sh@suse.de
- V 2.4.0 for 7.3
  Honor new BarGraph / PartitionSplitter format: "%%1"
* Thu Jun  7 2001 kkaempf@suse.de
- remove @euro for en_GB and da_DK
* Thu Jun  7 2001 kukuk@suse.de
- inst_silo_info.ycp: Fix info text: Don't speak about whole
  computer but only about selected harddisk.
* Wed Jun  6 2001 kukuk@suse.de
- inst_environment.ycp: Don't set keyboard if serial console was
  detected.
* Tue Jun  5 2001 kukuk@suse.de
- Remove inst_sunfb.ycp from instsys
- keyboard_raw.ycp: Replace default us keymap with new cz keymap
  on SPARC.
- inst_choose_desktop: Switch to own workflow for Sun Framebuffers
* Fri Jun  1 2001 kukuk@suse.de
- inst_finish.ycp: Set correct boot device for hard reboot,
    modify boot-device and set linux alias
* Fri Jun  1 2001 kkaempf@suse.de
- install correct kernel for different ia64 cpu steppings
- allow vfat as root during update
- define "string architecture" in vendor.ycp
-#8425 update does a hard reboot
  [#8081] too negative message after update ..
  [#8356] vfat will not be mounted while updating the system
  [#8185] Installation/Update: sformat wanted
  [#8567] YaST2 does not mount /boot
  [#6063] Update: Don't see ok button
  [#7097] YaST2 info during update
  [#4953] "Configurate boot-mode" should be renamed to "Configure boot-mode"
  [#5051] typo in yast2 installation popup
* Fri Jun  1 2001 kkaempf@suse.de
- adapt and enter inst_lilo_info for ia64
* Mon May 28 2001 schwab@suse.de
- Also mount vfat filesystems during update.
* Wed May 23 2001 gs@suse.de
- package_utils: samba mount implemented
  inst_smbmount: new module
* Tue May 22 2001 schwab@suse.de
- doelilo: Adjust elilo config file for gnu-efi 2.5.
* Mon May 21 2001 mike@suse.de
- XFS support in custom partitioner and LVM configuration
* Mon May 21 2001 kukuk@suse.de
- inst_silo_info/inst_silo_expert: Tell the user that we change
  PROM aliases and let him change this.
* Fri May 18 2001 kkaempf@suse.de
- add xfs to inst_prepdisk
* Fri May 18 2001 kkaempf@suse.de
- setab 0 -> setab 9 to make output more pleasing on splash screen (#8551)
* Thu May 17 2001 tom@suse.de
-  X configuration:
  Bugfix 8454: Besides the passing of the currently selected refresh rate
    in the resolution string (e.g. 600x800@70) to isax for XFree 3
    the selected refresh now also terminates the vsync range to
    prevent isax from generating modelines up to this value.
  Bugfix 8524: The 3D acceleration button is now disabled if the graphics
    adapter doesn't support 3D-acceleration.
  Bugfix 8540: Now the vendor and model strings are converted to upper case
    on module entry.
  Bugfix 8541: Now the probed data are deleted if the user selects another
    monitor.
* Thu May 17 2001 kkaempf@suse.de
- dont pretend that no other os has been found if we can't
  write LILO to floppy disk.
* Wed May 16 2001 sh@suse.de
- V 2.3.90
  added patch_lilo_conf to file list
* Wed May 16 2001 sh@suse.de
- Fixed patch_lilo_conf: optional as well as initrd
* Wed May 16 2001 kkaempf@suse.de
- prevent duplicate entry in initrdmodules during update
- activate only primary devices (#8458)
* Wed May 16 2001 kkaempf@suse.de
- give proper default for "lilo_device" if "mbr_disk" is unknown (#8501)
* Wed May 16 2001 sh@suse.de
- Fixed bug #8494: initrd not added to lilo.conf
  patch_lilo_conf adds "initrd" entries if corresponding
  initrd is present in /boot (for SuSE standard kernels only!)
* Wed May 16 2001 kkaempf@suse.de
- add reiserfs to initrd if root is on reiserfs (#8494)
* Wed May 16 2001 sh@suse.de
- Fix for bug #7465: "Abort Installation" always default button
  Added more SetFocus() calls for good measure
* Wed May 16 2001 kkaempf@suse.de
- use gdm as displaymanager if minimal(+x11) and gnome (#6175)
- dont write MODEM in rc.config (#7895)
- copy complete y2log to installed system.
- fix declaration in lilo_info, string->boolean
* Tue May 15 2001 tom@suse.de
- Bugfix 8423: probed monitor data now used.
* Tue May 15 2001 gs@suse.de
- bugfix in Change Source Media (include file added) bug # 8406
* Tue May 15 2001 mike@suse.de
- due to last information: to crypt /usr is
  not allowed. Added a popup
* Tue May 15 2001 kkaempf@suse.de
- revert change in y2xr40.pl, support tft panel layouts
  in favour of higher resolutions (#8348)
- remove "breton" from languages, add "danish"
- patching XF86config for wheel mouse (#8251)
* Tue May 15 2001 mike@suse.de
- bugfix cryptofs: now works with already existing
  and edited partitions
* Tue May 15 2001 ms@suse.de
- disable use of DDC resolutions in y2xr40.pl (bug #8329)
  ( YaST2 used its own resolution list )
* Tue May 15 2001 gs@suse.de
- don't show /dev/shm in single package selection (bug #8318)
* Mon May 14 2001 sh@suse.de
- V2.2.79
  Fixed bug #8255: Wrong mouse cursor during SuSEconfig
  Removed obsolete UI(`NormalCursor()) calls
* Mon May 14 2001 kkaempf@suse.de
- create lower case symlinks for /windows and /dos mount points
  (installation and update) to get around case mapping bug
  in star office (#8310)
* Mon May 14 2001 kkaempf@suse.de
- properly initiale UI wizard for vendor cd modules (#8268)
- de-activate pt_PT, translations are incomplete (afaber@suse.de)
* Mon May 14 2001 kkaempf@suse.de
- fix variable name in inst_finish (install_inf -> installMap) (#8247)
* Mon May 14 2001 kkaempf@suse.de
- dont look at "Language" in install.inf, it's not in ISO-format
  if "Locale" in install.inf doesn't give a value, look at descr/info
* Mon May 14 2001 kkaempf@suse.de
- read Locale, Language (from install.inf), and LANG (from desc/info)
  and use first set value.
* Mon May 14 2001 kkaempf@suse.de
- restart network after staring system in NFS install (#8274)
* Mon May 14 2001 kkaempf@suse.de
- check if "/" is reiser and force "reisefs" to INITRD_MODULES
* Mon May 14 2001 kkaempf@suse.de
- drop question for kernel 2.2 on pcmcia, only very rare systems
  still fail with kernel 2.4
* Mon May 14 2001 fehr@suse.de
- make removal of LVM volume groups work
* Sun May 13 2001 kkaempf@suse.de
- fix blocker bug 8216
* Sat May 12 2001 kkaempf@suse.de
- ask for kernel 2.2 on PCMCIA systems
* Sat May 12 2001 kkaempf@suse.de
- unset MODPATH at initial start (#8143)
- install kernel 2.2 on PCMCIA systems
* Fri May 11 2001 schubi@suse.de
- Not required reread of target map fixed.
* Fri May 11 2001 pblahos@suse.cz
- #8064: fixed: if there is print spooled installed and configuration
  tool is not, there is no status in final YaST2 inst. screen.
- Correct popup message while backup #7584
* Fri May 11 2001 kkaempf@suse.de
- provide extra start script for KDE which suppresses geometry hint
  to window manager.
* Thu May 10 2001 kkaempf@suse.de
- Require translation packages
- dont translate empty string
- force LILO on MBR if initrd won't make it on floppy (#7864)
- calling patch_lilo_conf while update #7556
- bugfix in renamed packages while update #8057
- mounting swapfile correctly while update #8040
* Thu May 10 2001 kkaempf@suse.de
- fix initrd modules order after update (#7948)
* Thu May 10 2001 mike@suse.de
- fix for LVM configuration at runtime
* Thu May 10 2001 sh@suse.de
- Fixed bug #7388: unnecessary OK-buttons
  (confirmation for writing LILO, confirmation for reboot)
  only one popup that contains both messages
* Thu May 10 2001 kkaempf@suse.de
- dont write /boot/message any more (#8062)
* Thu May 10 2001 fehr@suse.de
- add lvm initialisation when doing an update (#7974)
- allow update when root fs is LV (#7801)
- fixed:YaST updated old updatelist after reboot #8066
- #8025 not starting update, if there is nothing for update
* Thu May 10 2001 sh@suse.de
- Fixed bug #8049: "boot installed system" "back" button boots
* Thu May 10 2001 kkaempf@suse.de
- set "ulimit -s unlimited" before calling "rpm --rebuilddb"
* Thu May 10 2001 kendy@suse.cz
- added console fonts for Brezhoneg and Lithuania
- Russian -> Russkij in cyrilics
- adaption of SelectConsoleFont() to new language.ycp
* Thu May 10 2001 gs@suse.de
- make the popup Additional package needed larger (bug # 7900)
- Software Source Media dialog: label for button is "Next" (bug # 8038)
* Thu May 10 2001 sh@suse.de
- Fixed bug #7199: Printer config before network
  Changed order to "professional" mode when network card detected
- bugfix in eavaluate diskspace in boot partition #8047
* Thu May 10 2001 sh@suse.de
- (partial) fix for bug #7888: obsolete lilo.conf entries after update
  added patch_lilo_conf script that deletes vmlinuz_22 / vmlinuz_24
  if the respective boot images are not present and adds "optional"
  for other boot images that are not present
* Thu May 10 2001 kkaempf@suse.de
- use RC_LANG when starting yast2 to get correct language (#8013)
* Thu May 10 2001 tom@suse.de
- bugfix 7823:
  Now even in the special cases LCD and VESA an xserver query is made
  to get information regarding the possible color depths.
* Thu May 10 2001 tom@suse.de
- bugfix #8000:
  Now the modified monitor db is preserved by storing it to disk.
* Thu May 10 2001 sh@suse.de
- Re-imported SaX2 monitor DB
* Thu May 10 2001 kendy@suse.cz
- lat9w font for EU states (#7776)
* Thu May 10 2001 kkaempf@suse.de
- keep LANG codes and modifiers in single list (#7957)
* Wed May  9 2001 kkaempf@suse.de
- fix order of initrd modules (#7948)
* Wed May  9 2001 gs@suse.de
- text changed for popup package conflicts (bug # 7887)
  and popup "Release number differs ...."
* Wed May  9 2001 jbuch@suse.de
- forbid crypt_fs with mountpoints like / /boot swap
  added cryt_fs to ExistingPartitionDlg
* Tue May  8 2001 kkaempf@suse.de
- set "Greenwich" as default timezone for en_GB (#7837)
- unset MODPATH before calling depmod
- Update: selecting default to UPGRADE #7804
* Tue May  8 2001 kkaempf@suse.de
- skip drives which are not ready (#6547)
* Tue May  8 2001 tom@suse.de
- X11 configuration: removed integer <---> float inconsistency
* Tue May  8 2001 kkaempf@suse.de
- reset have_x11 after switching to "minimal"
- allow "activate" switch for partitions
* Tue May  8 2001 gs@suse.de
- package_utils: CheckLocalDescription added
* Tue May  8 2001 mike@suse.de
- for security reasons: use now losetup agent instead of standalone binary
* Tue May  8 2001 fehr@suse.de
- add shortcut key to crypt checkbox
* Tue May  8 2001 sh@suse.de
- Fixed bug #7547: "Boot installed system" not active
  Implemented reboot from installed system
* Tue May  8 2001 jbuch@suse.de
- fixed english
* Tue May  8 2001 jbuch@suse.de
- removed not used variable last_format from inst_custompart.ycp
  forbid using fat file system with mountpoints / /home /opt /usr /var
* Tue May  8 2001 schubi@suse.de
- showing progress bars again #7774
- rename /cdrom to /media/cdrom in /etc/fstab #7732
* Tue May  8 2001 snwint@suse.de
- floppy device for mk_lilo_conf via $floppy environment var
- mk_boot_floppy completely rewritten to use lilo instead of syslinux
* Tue May  8 2001 schwab@suse.de
- Fix typo targeroot -> targetroot.
* Tue May  8 2001 jbuch@suse.de
- added define to change fsid from 5 to 15
  only for new extended partitions
  added DisplayMessage if a fat file system is greater than 2 GB
- showing progress bars again #7774
* Tue May  8 2001 kkaempf@suse.de
- set hwclock before starting to change the target (#7833)
* Mon May  7 2001 gs@suse.de
- Single Package Selection: improve popup Severe package conflict
- mk_lilo_conf removed #7569
* Mon May  7 2001 kkaempf@suse.de
- FHS: /floppy -> /media/floppy also in inst-sys (#7827)
* Mon May  7 2001 fehr@suse.de
- Add possibility to encrypt lvm logical volumes
* Mon May  7 2001 sh@suse.de
- Fixed bug #7628: textmode info shown after booting
  Add flag to user_settings when text mode warning is shown
* Mon May  7 2001 kendy@suse.cz
- Do not use CONSOLE_UNIMAP in consolefonts.ycp (#7767)
* Mon May  7 2001 kkaempf@suse.de
- drop hard coded /dev/fd0, use value from hw-probing (#7789)
* Mon May  7 2001 mike@suse.de
- Bugfix LVM: mount more than one crypted partition
* Mon May  7 2001 tom@suse.de
- X-configuration
  Bugfix 7641: X-configuration for XFree86 3.x now functional (didn't work).
  Removed integer|float syntax warning.
  Added support for mice with wheels.
  checked default values for some lookups.
* Mon May  7 2001 arvin@suse.de
- added output of memory information to YaST2 start script
* Mon May  7 2001 sh@suse.de
- Use new UI builtin GetLanguage() parameter "strip_encoding"
* Mon May  7 2001 kendy@suse.cz
- Use non-UTF-8 locale in the y2xfinetune40 (not reported bug)
* Mon May  7 2001 arvin@suse.de
- start qt frontend with >= 64MB and adjusted corresponding text
- mounting /usr as reiserfs #7585
- initialize server, if another root has been selected #7495
* Mon May  7 2001 kkaempf@suse.de
- change controlling terminal after switching virtual console (#7626)
- dont check mouse with serial console (#7716)
- dont ask keyboard with serial console (#7717)
- dont ask hwclock setting on sparc (#7717)
* Fri May  4 2001 mike@suse.de
- fixed Bug 7528: YaST2->Partitioning: wrong info in popup
- Bug:          LVM:
    it at the moment not possible to delete a "activated"
    lvm partition (physical volume) and do afterwards
    mk*fs ...
  - changed: read lvm as late as possible
  - after deleting a  physical volume:
    immediately do partitioning and reboot
  - if the target_partitioner delets volume group: reboot
- Bug:          Setting up an LVM an than switching via back to custom
    partitioner:
  - drop target_modifications in inst_sw_select
- Bug:          wrong error message appears:
    quick hack: delete message: inst_target_selection.ycp
- Bug:          no warning if /boot is to small
  - added warning
- Bug:          missing textdomains is lvm includes
* Fri May  4 2001 gs@suse.de
- helptext for Mininum graphical system added (bug 7483) in
  dialog Software Selection
- check the software selection again when going next (bug reported by mike)
* Wed May  2 2001 kkaempf@suse.de
- allow calling inst_enviroment and inst_language from outside
* Wed May  2 2001 sh@suse.de
- Fixed bug #7463: next/abort/back not translated in installed system
  Moved msg re-translation code out to separate function
  added call to this function when starting in "continue mode"
- no more: RPM returned an error (#7424)
* Wed May  2 2001 fehr@suse.de
- umount lvm agent after re-partitioning harddisk
* Wed May  2 2001 sh@suse.de
- Fixed bug #7467: Help text not translated in inst_finish.ycp
  Added missing translation markers
* Wed May  2 2001 sh@suse.de
- updated monitor DB from devel server
* Wed May  2 2001 kkaempf@suse.de
- handle all sync values as floats in x11
* Wed May  2 2001 kkaempf@suse.de
- use gdm as display manager if gnome is selected
* Mon Apr 30 2001 kkaempf@suse.de
- drop obsolete file from filelist
* Mon Apr 30 2001 fehr@suse.de
- bugfix for lvm configuration
* Mon Apr 30 2001 kkaempf@suse.de
- Evaluate "buttons" and "wheels" values from probing
  dont emulate 3 buttons if not needed
* Mon Apr 30 2001 sh@suse.de
- Fix for bug #7004: Penguin image too small
  New penguin image at startup: colored margins right and bottom,
  can adapt to different screen geometries
* Mon Apr 30 2001 snwint@suse.de
- removed mk_lilo_message
- vga parameter correctly interpreted in mk_lilo_conf (#7197)
- new graphical boot screen handling
* Mon Apr 30 2001 kkaempf@suse.de
- first try on DVORAK keyboard (incomplete)
- showing package description while installing rpm via ftp update (#6573)
- install "yast2-ui-qt" if "xf86" is installed.
* Mon Apr 30 2001 mike@suse.de
- bugfix creating two volume groups
* Mon Apr 30 2001 kkaempf@suse.de
- fix lilo device message (show disk instead of partition)
* Mon Apr 30 2001 sh@suse.de
- (partial) fix for bug #7004: Penguin image too small at Y2 start
  Allow more flexible scaling of image, top left aligned, zero
  size by default
* Mon Apr 30 2001 tom@suse.de
- X11 configuration:
  Fixed bug 7437:
  Corrected typo in sorting algorithm for sorting resolutions in the GUI.
* Mon Apr 30 2001 kkaempf@suse.de
- mount "/boot" with "defaults", even if its vfat formatted (#7413)
* Fri Apr 27 2001 tom@suse.de
- X11 configuration:
  Improved display with erroneous probing of monitor vendor and/or model.
* Fri Apr 27 2001 fehr@suse.de
- bug fixes in lvm configuration
* Fri Apr 27 2001 gs@suse.de
- inst_sw_details: internal changes because of new package dependencies
- package_utils: improve function ChangeCD
- Single Package Selection: translation of group tags
- evaluate splitted packages correctly ( e.g finger ) #7271
* Fri Apr 27 2001 mike@suse.de
- Bugfixes:
    read cryptotab at firstboot failed
  7238  crypto dialog has no frame
  5967  unnecessary logline
    crypto dialog appears twice
  4693  deleting of extended partition 8 and 9
  2309  popup when deleteing partitions
  5422  display an error if we mount a ro filesystem for update
* Thu Apr 26 2001 kkaempf@suse.de
- extrace x11 3d packages correctly (#7231)
* Thu Apr 26 2001 tom@suse.de
- X11 configuration:
  Fixed Bug 4558: Now the model string (if VESA or LCD) is parsed and the
    resolution and refresh rate are used for configuration.
  Improved setting of refresh rate with XFree86 4.
  (now reality will suit the users demand better)
  Consequently changed suggestion value from 90 Hz to 80 Hz.
* Thu Apr 26 2001 kendy@suse.cz
- inst_hw_config: ReallyAbortPopup()->UI(`ReallyAbortPopup())
* Thu Apr 26 2001 kkaempf@suse.de
- evaluate return from NIS question (#7269)
* Thu Apr 26 2001 kkaempf@suse.de
- dont start inetd by default.
* Thu Apr 26 2001 kkaempf@suse.de
- re-compute timezone if language was changed (#7008)
* Thu Apr 26 2001 kkaempf@suse.de
- added "ash" to requires for dolilo (#7254)
- Checking boot partitionsize while updating the system (#6445)
* Thu Apr 26 2001 kkaempf@suse.de
- look for "update.tar.gz" first, fallback to "update.tgz" else
* Thu Apr 26 2001 kkaempf@suse.de
- load usb modules and mount usbdevfs (#7037)
* Thu Apr 26 2001 kkaempf@suse.de
- set hwclock option to "--localtime" instead of empty (#3907)
* Thu Apr 26 2001 kkaempf@suse.de
- correctly check for have_smp and pae flag for k_psmp kernel (#7093)
- add requires for yast2-instsys (#7189)
* Wed Apr 25 2001 fehr@suse.de
- removal of LVM volume group should now work
- Bugfix showing logging after installation (#7034)
- Deleting old kernel will be handled by rpm ( update )
- Setting textdomain for logging installation
* Wed Apr 25 2001 tom@suse.de
- X11 configuration
  fixed bug 7193: now empty vendor results in "".
  set default refresh to 90 Hz due to XFree86 4 variations.
  removed test code and test logging.
* Wed Apr 25 2001 schwab@suse.de
- Add doelilo for ia64.
* Wed Apr 25 2001 kkaempf@suse.de
- disable kernel include copies
* Wed Apr 25 2001 kkaempf@suse.de
- /boot on ia64 is `fat32, not `fat (#6599)
* Wed Apr 25 2001 mike@suse.de
- new lvm helptexts
* Wed Apr 25 2001 sh@suse.de
- Fixed bug #6947: Long time empty screen
  Added feedback what's happening to inst_finish.ycp
* Wed Apr 25 2001 sh@suse.de
- Fixed X11 config: Add correct user_settings key to
  inst_choose_desktop.ycp
* Wed Apr 25 2001 gs@suse.de
- use of common popups in update modules
* Wed Apr 25 2001 kkaempf@suse.de
- read euro.ycp from proper dir
- remove duplicate popup
* Wed Apr 25 2001 kkaempf@suse.de
- moved menu.ycp here (from yast2-menu)
* Tue Apr 24 2001 tom@suse.de
- X11 configuration fixed
  restriction logic complete in first version
  merged suggestion logic with restriction logic
* Tue Apr 24 2001 kkaempf@suse.de
- mount in lexical order
- updating k_deflt_24 to k_deflt
* Tue Apr 24 2001 gs@suse.de
- Single Package Selction: popup to show the Obsolete dependencies has changed
* Tue Apr 24 2001 tom@suse.de
- interim checkin for beta 2
- texts now final for translaters
- restriction logic partly implemented
* Tue Apr 24 2001 kkaempf@suse.de
- fix COMPOSETABLE entry according to latest kdb package (#7023)
* Tue Apr 24 2001 fehr@suse.de
- change layout of vuloume group dialog
- add help texts for lvm dialog
* Tue Apr 24 2001 kkaempf@suse.de
- new list of language codes which allow "@euro" appended
- error popup in inst_rpmupdate removed BUG 6243
* Mon Apr 23 2001 fehr@suse.de
- fixes and extensions for lvm configuration
* Mon Apr 23 2001 kkaempf@suse.de
- append "@euro" instead of ".ISO8859-15" to RC_LANG
* Mon Apr 23 2001 sh@suse.de
- Fix for bug #7013: Abort should be disabled
  Disable "Abort" button in inst_suseconfig.ycp
* Mon Apr 23 2001 sh@suse.de
- Always use "Abort Installation" for button label, even on the
  first dialogs (before lang switch)
- Fix screen shot mode hint in inst_startup: Use correct popup
* Mon Apr 23 2001 sh@suse.de
- Fixed check_ycp complaints in installation.ycp:
  Obsolete WFM functions
- Assume presence of floppy in test_mode so "write settings to
  floppy" button appears consistently (screen shots!)
* Mon Apr 23 2001 sh@suse.de
- Used correct include path for custom_part_helptexts.ycp
  in custom_part_dialogs.ycp
* Mon Apr 23 2001 sh@suse.de
- declared "hwclock" in inst_environment.ycp
* Mon Apr 23 2001 kkaempf@suse.de
- set COMPOSETABLE in rc.config (#7023)
* Mon Apr 23 2001 kkaempf@suse.de
- fix isnil check in installation.ycp
- inst_sw_update: Changes for new dependencies
- add requirements for yast2-instsys package
- remove /var/lib/YaST2/run_suseconfig after SuSEconfig
- replace all isnil() calls
* Fri Apr 20 2001 tom@suse.de
  X11 configuration:
- added nvidia warning
- added change warning popup
- cleaned sequence of dialogs
- streamlined code
- fixed bug 7028: now text login when X11 configuration is skipped
- restriction logic when selecting resolution, color depth, or refresh
  is still missing
* Fri Apr 20 2001 kkaempf@suse.de
- prepare standalone handling of keyboard and timezone selection
* Fri Apr 20 2001 kkaempf@suse.de
- show username only if given (#7082)
* Fri Apr 20 2001 kkaempf@suse.de
- switch "START_PORTMAP" back to "yes", must be fixed in kernel 2.4 by linus
- Update: Deleting old packages removed.
* Fri Apr 20 2001 kkaempf@suse.de
- write bios ids to lilo.conf only on an ide/scsi mix system
* Fri Apr 20 2001 gs@suse.de
- show set pay in dialog Pay Selection and groups tags in Single Selection
- popup displaying obsolete package dependencies added
* Fri Apr 20 2001 fehr@suse.de
- fix some problems with lvm configuration
* Fri Apr 20 2001 kkaempf@suse.de
- drop SEARCHLIST from rc.config (#7063)
* Thu Apr 19 2001 kkaempf@suse.de
- X11 configuration fixes
  module loading fix
* Wed Apr 18 2001 kkaempf@suse.de
- re-create tmpdir in continue_mode
* Wed Apr 18 2001 kkaempf@suse.de
- add ".ISO8859-15" to RC_LANG where appropriate
* Wed Apr 18 2001 kkaempf@suse.de
- provide correct "vga" entry to lilo.conf
* Wed Apr 18 2001 kkaempf@suse.de
- use WarningPopup in installation.ycp
* Wed Apr 18 2001 kkaempf@suse.de
- fixed x11 fontpathes
* Wed Apr 18 2001 kkaempf@suse.de
- fix filelist for yast2-instsys
* Wed Apr 18 2001 kkaempf@suse.de
- define "current_video" for x11 setting
* Wed Apr 18 2001 kkaempf@suse.de
- set "YAST_ASK" values in rc.config (#6261)
* Tue Apr 17 2001 kkaempf@suse.de
- check for serial console when configuring x11
* Tue Apr 17 2001 fehr@suse.de
- allow formatting of lvm logical volumes
* Tue Apr 17 2001 kkaempf@suse.de
- fix "have_x11" handling
* Tue Apr 17 2001 gs@suse.de
- show package groups when entering the dialog
* Tue Apr 17 2001 kkaempf@suse.de
- "START_PORTMAP" in rc.config defaults to "no" now (#6270)
* Tue Apr 17 2001 kkaempf@suse.de
- dont ask for mouse on serial console (#6030)
* Tue Apr 17 2001 kkaempf@suse.de
- dont ask for keyboard on serial console (#5939)
* Tue Apr 17 2001 kkaempf@suse.de
- set linuxrc override language code from CD (#5249)
* Tue Apr 17 2001 mike@suse.de
- new FEATURE: LVM setup is now possible
* Fri Apr 13 2001 kendy@suse.cz
- inst_hw_config rewritten to use ui/summary.ycp include and
  to ask modules about the configured devices (or about the
  devices to configure) using calls of <module>_summary.ycp.
* Thu Apr 12 2001 tom@suse.de
- X11 configuration
  Complete redesign involving heavy changes (mostly new code).
  o Split up functionality into modules and functions.
  o Providing testsuites for functions (nearly all of them still to be done)
  o Ask user if he wants to skip X11 configuration if "No X11" is selected
  in monitor selection dialog.
  o Now reading X11 font pathes dynamically (hardcoded up to now).
  o Better logic presenting resolution-colordepth-frequency dependencies.
  o Better logic providing the settings suggestion that user may accept.
  o New decision workflow in GUI (one more dialog).
  o Better handling of monitor refresh rate (user can choose one).
  o DPMS now supported in the XF86Config file to be created.
  o Now it is possible to go back to the original YaST2 monitor data base after
  having read a Microsoft compatible drivers disk.
  o Now a monitor that could be probed but is not known in the YaST2 monitor
  data base is automatically added to this data base (volatile, not in the
  data base file) if the monitor selection dialog is entered.
* Thu Apr 12 2001 gs@suse.de
- respect new package dependencies for Single Package Selection
* Thu Apr 12 2001 kkaempf@suse.de
- provide menuentry for vendor.ycp
* Thu Apr 12 2001 sh@suse.de
- Migration to yast2-lib-wizard: Get rid of duplicate code,
  replace old style popups with new ones from common_popups.ycp
- Fixed lots of check_ycp complaints
* Thu Apr 12 2001 kkaempf@suse.de
- adapt to FHS, /floppy, /cdrom, and /zip are below /media now
  provide compatibility symlinks
* Thu Apr 12 2001 kkaempf@suse.de
- dont pass user_settings to SelectConsoleFont
* Tue Apr 10 2001 kkaempf@suse.de
- do swap calculation based on detected main memory
* Fri Apr  6 2001 kkaempf@suse.de
- ensure proper libGL link in YaST2.firstboot (# 6916)
* Thu Apr  5 2001 kkaempf@suse.de
- kernel rpm rename, drop "_24" suffix
* Wed Apr  4 2001 kkaempf@suse.de
- revert "switch_kernel" check, 2.4 is default now
* Wed Apr  4 2001 kkaempf@suse.de
- separate show log defines from inst_suseconfig.ycp
* Tue Apr  3 2001 kkaempf@suse.de
- add "yast2-agent-rcconfig" to Requires
* Tue Apr  3 2001 kkaempf@suse.de
- remove need for global variables in installation.ycp
* Tue Apr  3 2001 arvin@suse.de
- adapt calls to makefs-agent to new syntax
* Fri Mar 30 2001 arvin@suse.de
- filelist correction for "yast2-instsys"
* Tue Mar 27 2001 kkaempf@suse.de
- recode passwd comment to local encoding (#3798)
* Tue Mar 27 2001 kkaempf@suse.de
- filelist correction for "yast2-instsys"
* Mon Mar 26 2001 kkaempf@suse.de
- mark global defines as such
- require "yast2-core-pkginfo"
* Thu Mar 22 2001 kkaempf@suse.de
- first round of check_ycp adaptions
* Thu Mar 22 2001 kkaempf@suse.de
- merge 7.1 branch with CVS head
* Wed Mar 21 2001 kkaempf@suse.de
- remove all "...|any" declarations
* Wed Mar 21 2001 kkaempf@suse.de
- sub-package "yast2-instsys" for easier instsys creation.
* Thu Mar 15 2001 mfabian@suse.de
- change ja_JP : "english" to ja_JP : "japanese" in lang2yast1.ycp
  YaST1 doesn't know "japanese" but this entry is also used for
  the package selection in YaST2.
* Fri Mar  9 2001 kkaempf@suse.de
- recognize firewall cd
* Thu Mar  8 2001 kkaempf@suse.de
- clean up neededforbuild
  add yast2-base, -core, and -agents to Requires
* Thu Mar  8 2001 kkaempf@suse.de
- dont show "save to floppy" if no floppy present (#6634)
* Tue Mar  6 2001 kkaempf@suse.de
- check for partition table overflow on BSD disks (#6614)
* Mon Mar  5 2001 kkaempf@suse.de
- recognize arch_alpha during kernel selection (#6581)
- no kernel selection on IA64 (#6597)
* Mon Mar  5 2001 kkaempf@suse.de
- compute last used partition for BSD partitions (# 6580)
* Tue Feb 27 2001 gs@suse.de
- ppc_fix: eject CD works also if there are several CD devices
    (module package_utils.ycp)
* Fri Feb 23 2001 mike@suse.de
- ppc_fix: more than 9 pdisk partitions, format hfs partition
* Fri Feb 23 2001 mfabian@suse.de
- gs@suse.de fixed the syntax error I introduced in
  inst_finish.ycp. Sorry.
- powerpc kernel selection by gs@suse.de
* Fri Feb 23 2001 kukuk@suse.de
- Reset kernel_is list for sparc64 and PPC [Bug #6489]
* Thu Feb 22 2001 mfabian@suse.de
- fix from ms@suse.de:
  update fine tune scripts to work with the new
  saxtools package ( start xbound as background process )
* Thu Feb 22 2001 mfabian@suse.de
- add entries for Korean and Japanese to lang2yast1.ycp
- workaround for Japanese: set RC_LANG. See also bug 5712.
* Wed Feb 21 2001 snwint@suse.de
- remove /var/X11R6/bin/X link in YaST2.start
* Wed Feb 21 2001 snwint@suse.de
- remove /var/X11R6/bin/X link in YaST2.start
* Wed Feb 21 2001 snwint@suse.de
- accidentally removed x11 detection in YaST2.start (ppc only); fixed
* Wed Feb 21 2001 kkaempf@suse.de
- only check lba_support on i386 (bug #6341)
* Tue Feb 20 2001 snwint@suse.de
- accidentally removed x11 detection in YaST2.start (ppc only); fixed
* Mon Feb 19 2001 kkaempf@suse.de
- dont refer to exact kernel version (bug #6403)
- treat primary partitions in BSD and FAT alike (bug #6394)
* Sat Feb 17 2001 kukuk@suse.de
- Switch for all Sun Framebuffer driver from XFree86 4.0.2 into
  the sunfb module.
- dosilo: Rename label "linux.suse" into "suse"
* Wed Feb 14 2001 snwint@suse.de
- no braille detection on ppc
* Fri Feb  9 2001 sh@suse.de
- Re-imported monitor DB - now includes some more Sun monitors
* Wed Feb  7 2001 sh@suse.de
- Fix for bug #6263: Language selection box loses keyboard focus
  Set focus to the selbox, now simply hitting "Return" doesn't
  proceed to the next dialog any more.
* Wed Feb  7 2001 kkaempf@suse.de
- honor answer for "show logging"
* Wed Feb  7 2001 kkaempf@suse.de
- remove USE_KERNEL_NFSD from rc.config (bug #6262)
* Tue Feb  6 2001 kkaempf@suse.de
- fix partition check for BSD partitions (bug #6249)
* Tue Feb  6 2001 kkaempf@suse.de
- fix kernel installation (2.2 and 2.4) for Sparc64 and PPC
* Sun Feb  4 2001 kukuk@suse.de
- custom_part_check_generated.ycp: Fix second check for broken
  PROM version (1GB limit), too
* Sun Feb  4 2001 kukuk@suse.de
- dosilo: add workaround for new mk_initrd return codes
* Fri Feb  2 2001 kkaempf@suse.de
- added "lt_LT" : "Lithuania" to language selection
* Tue Jan 30 2001 kkaempf@suse.de
- support live_eval_mode for LiveCD
* Mon Jan 29 2001 kkaempf@suse.de
- fix /dev/NULL -> /dev/null (bug 6182)
- update sparc-kernel (schubi)
- call silo (schubi)
* Mon Jan 29 2001 kkaempf@suse.de
- drop "id" (indonesia) from language list
* Mon Jan 29 2001 kukuk@suse.de
- keyboard_raw.ycp: Fix dutch type5 keyboard description
* Sat Jan 27 2001 kukuk@suse.de
- dosilo: Make it useable after installation
* Fri Jan 26 2001 kkaempf@suse.de
- removed unneeded unimap settings for ISO-2 console fonts
- added ca_ES and gl_ES to consolefonts
* Thu Jan 25 2001 mike@suse.de
- menulogo.png deleted, not needed anymore
* Wed Jan 24 2001 kkaempf@suse.de
- enabled "ca_ES" (catalan) in language selection
* Tue Jan 23 2001 kkaempf@suse.de
- dont check for graphics or mouse if serial console is active
* Tue Jan 23 2001 kkaempf@suse.de
- write swap partition to global data
* Tue Jan 23 2001 kkaempf@suse.de
- write proper data to /etc/yast.inf so linuxrc can swapoff
  and set language correctly
* Tue Jan 23 2001 kkaempf@suse.de
- rename of update.tgz to update.tar.gz
* Mon Jan 22 2001 kkaempf@suse.de
- fix for initial console message in YaST2.firstboot
* Mon Jan 22 2001 kkaempf@suse.de
- pass root device to mk_initrd in chroot environment
* Mon Jan 22 2001 mike@suse.de
- dumpe2fs with option -h to avoid enormous logging
* Mon Jan 22 2001 sh@suse.de
- Re-imported monitor DB:
  10%% higher sync range for LCDs to compensate for -10%%
  safety decrease during X11 config
  + some new monitors
* Mon Jan 22 2001 sh@suse.de
- V2.1.148
- New title graphics from <wimer@suse.de> that no longer are
  cut off to the right
* Sun Jan 21 2001 schubi@suse.de
- update from 6.2 works
* Sun Jan 21 2001 schubi@suse.de
- logging of dumpe2fs reduced, is important for update <6.3
* Sun Jan 21 2001 schubi@suse.de
- new menu position (new logo) in lilo
* Sun Jan 21 2001 schubi@suse.de
- Update although there are packages which need a manual selection
* Sat Jan 20 2001 schubi@suse.de
- Warning to update manuell packages
- Made softboot while update
* Fri Jan 19 2001 tom@suse.de
- Fixed bug #6012: Now restoring original partition state on `back
* Fri Jan 19 2001 kukuk@suse.de
- Don't set defaultdepth in the moment for Sun Framebuffer
* Fri Jan 19 2001 sh@suse.de
- V2.1.141
  updated monitor DB (fix for bug #5177: display DB outdated)
* Fri Jan 19 2001 mike@suse.de
- bug fix 5016: custom partitioner sees a other OS
* Fri Jan 19 2001 kkaempf@suse.de
- after update:
  properly merge initrd modules from linuxrc and hwinfo
  properly merge modules.conf settings
  properly set USB
  Changing installed kernels which are no longer supported.
  Writing Lilo on floppy while update and retry if an error
  has been occured
* Fri Jan 19 2001 kkaempf@suse.de
- re-construct INITRD_MODULES after update to match current hardware
  and kernel.
* Fri Jan 19 2001 kkaempf@suse.de
- write all data needed for re-start at end of first update
- properly initialize initrd modules at startup
- Bugfix 5880: shrinkable in table-widget removed ( inst_sw_single)
* Fri Jan 19 2001 mike@suse.de
- bugfix 5857: Layout logging of installation
  bugfix 5933: Save and exit-button changed
    message in changeCD changed
* Thu Jan 18 2001 kkaempf@suse.de
- dont configure X11 with serial console (bug 5951)
* Thu Jan 18 2001 kkaempf@suse.de
- enable "korean"
- create extended part as "Win Ext LBA" if it starts above cyl 1024
* Thu Jan 18 2001 tom@suse.de
- added functionality for emulate 3 buttons (Bug #5802)
* Thu Jan 18 2001 sh@suse.de
- V2.1.131
- Added new column for encoding (ISO-8859-1 etc.) in consolefonts
  and changed the call to SetConsole() accordingly
* Thu Jan 18 2001 kkaempf@suse.de
- alternative bugfix 5579 to write correct /var/lib/YaST/install.inf
- pass installMap correctly to inst_rpmcopy
* Thu Jan 18 2001 kkaempf@suse.de
- read correct image to determine kernel version
* Wed Jan 17 2001 kkaempf@suse.de
- fully implemented driver update feature
- fully implemented vendor driver CD feature with
  fallback to floppy
* Wed Jan 17 2001 kkaempf@suse.de
- fix chroot call for driver update script (bug #5810)
* Wed Jan 17 2001 schubi@suse.de
- not mounting partitions with the option noauto while update
* Tue Jan 16 2001 kkaempf@suse.de
- correctly detect driver update (bug 5799)
* Tue Jan 16 2001 kkaempf@suse.de
- replace "/mnt" to "/" instead of "" (bug 5512)
- fix syntax error in keymap2yast1 (bug 5782)
* Tue Jan 16 2001 kkaempf@suse.de
- start/stop usbmgr before probing for printers
* Tue Jan 16 2001 schubi@suse.de
- Checking dependencies and disk space while UPGRADE
* Mon Jan 15 2001 schubi@suse.de
- calling GetInstSource at the beginning of the update
* Mon Jan 15 2001 snwint@suse.de
- add memtest86 to lilo.conf
* Mon Jan 15 2001 kkaempf@suse.de
- leave RC_LANG alone (bug 5712)
* Mon Jan 15 2001 snwint@suse.de
- fixed Screen[vga] bug
* Mon Jan 15 2001 sh@suse.de
- Fixed bug #5114: Title graphics too small
  Changed title graphics to much wider images (2000 pixels wide)
* Sun Jan 14 2001 tom@suse.de
- Added comment as suggested by ke in bug #5484.
* Sun Jan 14 2001 tom@suse.de
- Fixed Bug 5638: NVIDIA Warning now appears when enabling 3D acceleration.
* Sun Jan 14 2001 kkaempf@suse.de
- show partitions being created or formatted (bug #5649)
* Sat Jan 13 2001 kkaempf@suse.de
- write mtab to target (bug 5512)
- add comment for translators to log popups
* Sat Jan 13 2001 kkaempf@suse.de
- correctly re-read installMap in continue_mode
* Sat Jan 13 2001 kkaempf@suse.de
- disable kernel modprobe (bug #5639)
* Sat Jan 13 2001 schubi@suse.de
- Calling SuSEConfig
- Writing installMap to user_settings
* Fri Jan 12 2001 mike@suse.de
-  maximum of hda and sda devices changed
  changed message of error popup
* Fri Jan 12 2001 sh@suse.de
- display only the first device of any kind (printer, sound card,
  modem/isdn card/net card) in inst_ask_config
* Fri Jan 12 2001 kkaempf@suse.de
- dont leave LILO screen empty (bug 4942)
- user popup "not enough disk space " changed ( schubi )
* Fri Jan 12 2001 kkaempf@suse.de
- pass full path to vendor install script
* Fri Jan 12 2001 kkaempf@suse.de
- dont load modules in "manual" mode (bug #5575)
* Fri Jan 12 2001 kukuk@suse.de
- inst_sunfb.ycp: Write glx modules into filelist for 3D fb cards
- Aborting installation after disk-space exhausted (schubi)
* Fri Jan 12 2001 smueller@suse.de
- removed debug logging in autoinst modules
* Fri Jan 12 2001 kkaempf@suse.de
- check for existance of kernels before access
* Fri Jan 12 2001 kkaempf@suse.de
- provide check.boot in filelist
* Fri Jan 12 2001 kkaempf@suse.de
- fix write of /var/lib/YaST/install.inf
* Thu Jan 11 2001 kkaempf@suse.de
- implemented full functionality for vendor.ycp (vendor driver CD)
* Thu Jan 11 2001 tom@suse.de
- Corrected wrong sync values in X configuration (#5539)
* Thu Jan 11 2001 kkaempf@suse.de
- add vendor.ycp to filelist
- Installation from partition fixed Bugfix 5480
* Thu Jan 11 2001 smueller@suse.de
- remember settings during autoinstall process
- user-logging added for non installed packages ( BUG ID 5417)
* Thu Jan 11 2001 kukuk@suse.de
- YaST2.start: Sync mouse protocoll with template, change keyboard
    section to autoprobed results, too.
* Thu Jan 11 2001 kkaempf@suse.de
- dont always copy kernel headers in inst_suseconfig (bug #5503)
* Thu Jan 11 2001 kkaempf@suse.de
- use yast2's copy of install.inf in package_utils
* Thu Jan 11 2001 kkaempf@suse.de
- write install.inf to installed system (for later use)
* Wed Jan 10 2001 tom@suse.de
- Fixed bug #5461
  Fixed bug #5411 (schubi)
* Wed Jan 10 2001 kkaempf@suse.de
- bugfix #5453
- bugfixes in ChangeCD ( schubi )
* Wed Jan 10 2001 schubi@suse.de
- bugfix in spec-file
* Wed Jan 10 2001 kukuk@suse.de
- inst_sunfb.ycp: Add XFree86 4.0 support for SPARC framebuffer
* Wed Jan 10 2001 tom@suse.de
- switch off 32 bpp for XFree 4 config.
  correct partition handling in the "delete Windows" case
* Wed Jan 10 2001 schubi@suse.de
- Booting from floppy with grafical-lilo works after update the
  system.
* Wed Jan 10 2001 kukuk@suse.de
- dosilo: Use /proc/mounts instead of mount
- inst_config_x11.ycp: Add more Sun framebuffer cards for inst_sunfb
* Wed Jan 10 2001 smueller@suse.de
- implemented disabling of SCR with dummyagent during config_mode
* Wed Jan 10 2001 kkaempf@suse.de
- pass lba capability to lilo (bug #5418)
* Tue Jan  9 2001 kkaempf@suse.de
- dont force usbcore on sparc (bug #5368)
* Tue Jan  9 2001 kkaempf@suse.de
- write dummy install.inf before calling PKGINFO (bug 5361)
* Tue Jan  9 2001 kkaempf@suse.de
- add usb mouse to manual selection list (bug #5355)
* Tue Jan  9 2001 kkaempf@suse.de
- honor xkblayout if present (bug #5341)
* Tue Jan  9 2001 kkaempf@suse.de
- do a hard reboot if user de-selects kernel 2.2 (bug #5344)
* Tue Jan  9 2001 tom@suse.de
- replaced dosfsck with parted, added scandisk hint in resizer module
* Mon Jan  8 2001 snwint@suse.de
- fixed (hopefully) quoting while reading install.inf
* Mon Jan  8 2001 kkaempf@suse.de
- remove X11 link before init, yast2.firstboot will do this
* Mon Jan  8 2001 snwint@suse.de
- set lilo timeout to 8s
* Mon Jan  8 2001 kkaempf@suse.de
- dont use xfree86 3.x vga16 or fbdev server any more (bug 5214)
* Sun Jan  7 2001 schubi@suse.de
- update from NFS with CD1,CD2...directories
* Sun Jan  7 2001 tom@suse.de
- added nvidia warning in inst_config_x11.ycp
* Sun Jan  7 2001 schubi@suse.de
- Rebooting after CD1 while updating the system
* Sat Jan  6 2001 kkaempf@suse.de
- fill vendor CD update module with life
* Sat Jan  6 2001 kkaempf@suse.de
- add missing "/boot" to path (bug 5268)
* Sat Jan  6 2001 kkaempf@suse.de
- patch y2xr40 for FireGL 2/3
* Sat Jan  6 2001 kkaempf@suse.de
- start X with PseudoColor if VGA(16) (bug #5243)
* Fri Jan  5 2001 kkaempf@suse.de
- recognize request for 3DLabs server at startup
* Fri Jan  5 2001 tom@suse.de
- resizer now handles extended partitions
* Thu Jan  4 2001 kkaempf@suse.de
- treat part 3 on BSD as extended (e.g. spanning multiple partitions)
* Thu Jan  4 2001 kkaempf@suse.de
- implement driver update functionality
* Thu Jan  4 2001 schubi@suse.de
- Bugfix in installPackageInformation ( rm -F )
* Wed Jan  3 2001 mike@suse.de
- bugfix Bug 2503 4390 detect used_fs
* Wed Jan  3 2001 kkaempf@suse.de
- fix architecture variable handling
* Wed Jan  3 2001 kkaempf@suse.de
- dont call xhost or su in /sbin/yast2, let susewm handle this
* Wed Jan  3 2001 kkaempf@suse.de
- dont explain "default+office" on non-i386
* Tue Jan  2 2001 tom@suse.de
- fixed bugs #4376 and #4849
* Tue Jan  2 2001 schubi@suse.de
- call RPM-rebuild with Shell
* Tue Jan  2 2001 kkaempf@suse.de
- fix lba support check
* Fri Dec 22 2000 schubi@suse.de
- Bug fixes in kernel-installation
* Wed Dec 20 2000 tom@suse.de
- corrected X11-3D setup
* Wed Dec 20 2000 sh@suse.de
- Moved hw_setup_launcher.ycp from include to include/ui
- V2.1.58
* Wed Dec 20 2000 kkaempf@suse.de
- add include/ui to filelist
* Tue Dec 19 2000 schubi@suse.de
- kill pkginfo-server removed
* Tue Dec 19 2000 kkaempf@suse.de
- dont resize Win2000 partitions, let M$ get their act together first
* Mon Dec 18 2000 kkaempf@suse.de
- better determine version of installed kernel image
* Mon Dec 18 2000 mike@suse.de
- Fixed Bug 4769
  reiserfs on /boot -> no warning
  check if bios supports lba -> no warning if boot-partition is >1024 cyl
* Sat Dec 16 2000 schubi@suse.de
-  killing pkginfo while installation
  saving package-description into system
  bugixes in ChangeCD
  installation-logging for user improved
* Fri Dec 15 2000 kkaempf@suse.de
- prepare for loading vendor-specific driver CDs
* Fri Dec 15 2000 kkaempf@suse.de
- tell the partitioner about ia64
* Fri Dec 15 2000 kkaempf@suse.de
- dont put usbdevs in /etc/fstab, usbmgr handles this now
* Thu Dec 14 2000 kkaempf@suse.de
- usbdevfs is available for ppc now (bug #4694)
* Thu Dec 14 2000 sh@suse.de
- Fixed bug #4633: Set keyboard focus in text field for package search
- Fixed bug #4632: Added popup for empty results for package search
- V2.1.48
* Thu Dec 14 2000 kkaempf@suse.de
- activate /boot only if LILO is in MBR
* Wed Dec 13 2000 schubi@suse.de
- runlevel switching removed, SuSEconfig handles this
* Wed Dec 13 2000 kkaempf@suse.de
- correct path for kernel includes
* Wed Dec 13 2000 kkaempf@suse.de
- mount ntfs partitions with umask=022
* Wed Dec 13 2000 mike@suse.de
- yast2 now starts y2controlcenter
* Wed Dec 13 2000 schubi@suse.de
- rpm-rebuild added
* Wed Dec 13 2000 kkaempf@suse.de
- automatically use free space on disk only if it's enough
  for a default installation (w/o office)
* Wed Dec 13 2000 kkaempf@suse.de
- create version correct include and depmods for all installed kernels
* Wed Dec 13 2000 kkaempf@suse.de
- flush rc.config agent at end of x11 configuration
* Wed Dec 13 2000 kkaempf@suse.de
- convert /sbin/init.d -> /etc/init.d in start scripts
* Tue Dec 12 2000 kkaempf@suse.de
- enable VESA framebuffer in lilo if needed and system is capable
* Mon Dec 11 2000 kkaempf@suse.de
- support Sun Type5/UK keyboard properly
* Mon Dec 11 2000 mike@suse.de
- bugfix 4524 reiserfs partition now possible
* Mon Dec 11 2000 kkaempf@suse.de
- force install usbcore to get usbdevfs
  run depmod for all installed kernels
  rm /etc/install.inf at end of continue_mode only
* Mon Dec 11 2000 kkaempf@suse.de
- install kernel source configs for all installed kernels
* Sun Dec 10 2000 schubi@suse.de
- update-mode in installation.ycp added
* Sun Dec 10 2000 kkaempf@suse.de
- modprobe usbcore to mount usbdevfs
* Sun Dec 10 2000 kkaempf@suse.de
- make appropriate mountpoints for cdrecorder, dvd, cdrom
  tell mk_lilo_conf about kernel 2.4 and initrd_24
* Sat Dec  9 2000 kkaempf@suse.de
- adapt mk_lilo_conf to multiple kernels
* Sat Dec  9 2000 kkaempf@suse.de
- activate kernel 2.4 installation
* Sat Dec  9 2000 dan@suse.cz
- remove '/etc/install.inf' after inst_ask_config
* Fri Dec  8 2000 mike@suse.de
- fixed bug in inst_custom test mode
* Fri Dec  8 2000 arvin@suse.de
- fixed variable name in inst_ask_config.ycp
* Thu Dec  7 2000 kkaempf@suse.de
- use () for each double-quote
  add "--enable-testsuite" to configure to do just this
  fix update mounts in respect to targetroot
* Thu Dec  7 2000 kkaempf@suse.de
- fix typo in filename
* Thu Dec  7 2000 kkaempf@suse.de
- fix mount calls in update
* Thu Dec  7 2000 kkaempf@suse.de
- dont use double qouted symbols or term, use expressions
* Thu Dec  7 2000 kkaempf@suse.de
- fix monitor selection
* Tue Dec  5 2000 kkaempf@suse.de
- do graceful exit on resize errors
* Tue Dec  5 2000 kkaempf@suse.de
- windows resizing enabled
* Mon Dec  4 2000 kkaempf@suse.de
- gcc not needed, just gpp
  re-read settings in continue mode
  correct text for curses fallback
  adapt to splitted translation packages
* Mon Dec  4 2000 kkaempf@suse.de
- strip auto_part_create to match requirements
* Sat Dec  2 2000 kkaempf@suse.de
- move all UI related code for auto partitioner to auto_part_ui.ycp
* Sat Dec  2 2000 kkaempf@suse.de
- split up inst_target_part to support testing and
  re-use code for partition resizer
* Fri Dec  1 2000 arvin@suse.de
- If either the x server could not be started or the computer
  has to less memory, ncurses interface is started and a message
  is displayed to inform the user. (Fix for bug #4272)
* Thu Nov 30 2000 arvin@suse.de
- unmount agent instsource after use
* Wed Nov 29 2000 kkaempf@suse.de
- force flush of rc.config agent
* Wed Nov 29 2000 kkaempf@suse.de
- respect data from setup/descr/info
* Tue Nov 28 2000 kkaempf@suse.de
- adopt to fixed Y2_TARGET_ROOT handling of target agent
* Tue Nov 21 2000 kkaempf@suse.de
- dont refer to k_laptop any more
* Mon Nov 20 2000 kkaempf@suse.de
- make use of target agent
* Fri Nov 17 2000 kkaempf@suse.de
- use proper agents
* Fri Nov 17 2000 kkaempf@suse.de
- drop y2t_inst from requires
* Thu Nov  9 2000 kkaempf@suse.de
- update workflow integrated
  general code cleanup
  workflow for product cd integrated
* Fri Nov  3 2000 kkaempf@suse.de
- merge with ppc and s390 branch
* Mon Oct 23 2000 kkaempf@suse.de
- disable .dumpto calls in inst_finish
  version 2.0.71
* Thu Oct 19 2000 mike@suse.de
- s390 fixes
  version 2.0.77
* Wed Oct 18 2000 choeger@suse.de
- added product cd detection
* Wed Oct 18 2000 choeger@suse.de
- changed the color of the lilo menu to green
* Wed Oct 18 2000 kkaempf@suse.de
- allow back from imap to lan at end of installation
  version 2.0.70
* Fri Oct 13 2000 kkaempf@suse.de
- also recognize /dev/cciss/... as raid device
  same in mk_lilo_conf
  version 2.0.69
* Thu Oct  5 2000 mike@suse.de
- fixed Makefile
  version 2.0.76
* Thu Oct  5 2000 mike@suse.de
- s390 support
  version 2.0.75
* Thu Sep 28 2000 choeger@suse.de
- workflow for imap server cd implemented
  version 2.0.68
* Tue Sep 26 2000 kkaempf@suse.de
- add '-p' to all mkdir calls
- fix alpha custom partition
- probe floppies for ZIP (IDE Zips report as floppy, not disk)
  version 2.0.74
* Fri Sep 22 2000 mike@suse.de
- ppc: limit boot region to 4MB if possible
  version 2.0.73
* Fri Sep  8 2000 mike@suse.de
- ppc fixes (no msdos floppy needed, warning if on prep/chrp /boot
  is missing, first root login string beautified)
  version 2.0.72
* Mon Aug 28 2000 kkaempf@suse.de
- create mountpoints for installation with mkdir -p
  usbdevfs is available for ppc now
  version 2.0.71
* Wed Aug 23 2000 kkaempf@suse.de
- new keyboard defines for ppc
  special yast1 keyboard handling for ppc/macs
  version 2.0.70
* Tue Aug 22 2000 kkaempf@suse.de
- ignore more Apple partition names
  version 2.0.69
* Thu Aug 17 2000 mike@suse.de
- check for a corrupt partition table (partition magic 5.0 can corrupt the
  partition tabe)
  version 2.0.67
* Tue Aug  8 2000 mike@suse.de
- enhancement fpr SPARC AXP and PPC
  version 2.0.68
* Mon Aug  7 2000 kkaempf@suse.de
- set GMT to "-u" on sparc
  check for dos/windows/nt partitions on i386 architectures only
  version 2.0.67
* Wed Aug  2 2000 kkaempf@suse.de
- remove /etc/install.inf at end of installation
  version 2.0.66
* Fri Jul 28 2000 kkaempf@suse.de
- default to 640x480 if DDC string does not contain frequency values
  dont select highest monitor resol, most monitors lie about this
  version 2.0.65
* Wed Jul 26 2000 kkaempf@suse.de
- fix x11 keyboard handling for sparc
  fix YaST2 startup for XFree86 4.0
  require y2t_inst in specfile
  clean up /tmp
  version 2.0.64
* Tue Jul 25 2000 kkaempf@suse.de
- call package module in live_eval_mode to get x11 server data
  set have_x11=true in live_eval_mode
  version 2.0.63
* Mon Jul 24 2000 kkaempf@suse.de
- bumped to 2.0.62 due to checkin clash
* Mon Jul 24 2000 kkaempf@suse.de
- always allow 640x480 as selectable resolution
  use unicode font at runtime
  pass module name to "su -c"
  better -probeonly parsing from x11 server
  version 2.0.61
* Mon Jul 24 2000 kkaempf@suse.de
- always close each opened dialog (bug 3611)
  version 2.0.60
* Fri Jul 21 2000 gs@suse.de
- added portuguese, delete brasil
  version 2.0.59
* Thu Jul 20 2000 kkaempf@suse.de
- enter all supported video modes to xf86config
  reboot if VGA16 is selected (clash with fbdev)
  check for x server alias existance befor using
  version 2.0.58
* Wed Jul 19 2000 gs@suse.de
- condition of warnig popup in package post install mode changed
  version 2.0.57
* Tue Jul 18 2000 kkaempf@suse.de
- take VGA16 as default X11 server for unknown graphic cards
  version 2.0.56
* Tue Jul 18 2000 kkaempf@suse.de
- fix x11 server selection bug (3d/non-3d)
  version 2.0.55
* Mon Jul 17 2000 kkaempf@suse.de
- restrict vsync to 100khz
  correctly construct video data
  version 2.0.54
* Mon Jul 17 2000 kkaempf@suse.de
- sparc port: SILO workflow added
  version 2.0.53
* Mon Jul 17 2000 kkaempf@suse.de
- only mount floppy if present (bug #3410)
  version 2.0.52
* Mon Jul 17 2000 kkaempf@suse.de
- always install vga16 and fbdev
  force reboot if laptop kernel was installed
  version 2.0.51
* Sun Jul 16 2000 kkaempf@suse.de
- pass x11 options to isax
  fix czech keyboard
  allow X4 fbdev if the user asked for it
  version 2.0.50
* Sat Jul 15 2000 kkaempf@suse.de
- remove bogus help, fix typos
  version 2.0.49
* Sat Jul 15 2000 kkaempf@suse.de
- never use nv/nvidia
  never use 4.0 fbdev
  version 2.0.48
* Fri Jul 14 2000 kkaempf@suse.de
- fixed custom installer
  decrease space safety threshold
  version 2.0.47
* Fri Jul 14 2000 kkaempf@suse.de
- fixed linear lilo bug
  fixed passing bios drivecodes to lilo
  version 2.0.46
* Fri Jul 14 2000 tom@suse.de
- added y2merge.pl
  version 2.0.45
* Fri Jul 14 2000 kkaempf@suse.de
- added client component password (bug #3403)
  version 2.0.44
* Thu Jul 13 2000 kkaempf@suse.de
- fix voodoo handling
  fix nfs install
  version 2.0.43
* Thu Jul 13 2000 kkaempf@suse.de
- remove mk_initrd, now in aaa_base
  version 2.0.42
* Wed Jul 12 2000 kkaempf@suse.de
- remove cmdline copy (libhd kludge)
* Wed Jul 12 2000 kkaempf@suse.de
- fix for free space immediately before empty extended part.
  version 2.0.41
* Wed Jul 12 2000 kkaempf@suse.de
- special handling for voodoo1/2 add-on cards
  version 2.0.40
* Wed Jul 12 2000 kkaempf@suse.de
- sparc patches
  version 2.0.39
* Tue Jul 11 2000 kkaempf@suse.de
- fix space requirements calculation (new du.dir)
  remember if hard-boot is needed (smp, pcmcia)
  version 2.0.38
* Tue Jul 11 2000 kkaempf@suse.de
- fix X11 start bug
  version 2.0.37
* Tue Jul 11 2000 kkaempf@suse.de
- restart network after hard reboot
  version 2.0.36
* Tue Jul 11 2000 kkaempf@suse.de
- dont offer zip drives for installation
  add /zip mountpoint to fstab
  version 2.0.35
* Tue Jul 11 2000 kkaempf@suse.de
- re-read partitions after custom partitioning
  version 2.0.34
* Tue Jul 11 2000 kkaempf@suse.de
- fix x11 start
  eject cdroms on ppc
  version 2.0.33
* Mon Jul 10 2000 kkaempf@suse.de
- fix raid support
  version 2.0.32
* Fri Jul  7 2000 @suse.de
- fix pdisk read for ppc
  fix parport ZIP init
  version 2.0.31
* Fri Jul  7 2000 kkaempf@suse.de
- fix system probing for PPC
  version 2.0.29
* Fri Jul  7 2000 kkaempf@suse.de
- fix NFS install from sub-dirs per CD
  version 2.0.28
* Tue Jul  4 2000 kkaempf@suse.de
- fix dolilo activate partition (snwint@suse.de)
  version 2.0.27
* Tue Jul  4 2000 kkaempf@suse.de
- support new dolilo options
  version 2.0.26
* Tue Jul  4 2000 kkaempf@suse.de
- allow module as argument to "yast2" script
  activate /boot partition in mk_lilo_conf
  version 2.0.25
* Tue Jul  4 2000 kkaempf@suse.de
- handle systems without mouse correctly
  version 2.0.24
* Mon Jul  3 2000 kkaempf@suse.de
- dont Include() translatable strings
  version 2.0.23
* Thu Jun 29 2000 kkaempf@suse.de
- remove noarch
  fixed copying of XF86Config
  version 2.0.22
* Wed Jun 28 2000 kkaempf@suse.de
- correct monitor database to reflect documentation
  version 2.0.21
* Wed Jun 28 2000 kkaempf@suse.de
- remove FROM_HEADER from sendmail.rc.config
* Wed Jun 28 2000 kkaempf@suse.de
- fix sync range handling, decrease max values by 10%%
  version 2.0.19
* Wed Jun 28 2000 kkaempf@suse.de
- added comments and sparc support to keyboard_raw.ycp
  version 2.0.18
* Wed Jun 28 2000 kkaempf@suse.de
- fixed wrong handling of xkbdprotocol
* Wed Jun 28 2000 kkaempf@suse.de
- add x11 config setup tools for XFree86 4.0
  version 2.0.17
* Wed Jun 28 2000 kkaempf@suse.de
- dont change consolefont for blinux
  version 2.0.16
* Wed Jun 28 2000 kkaempf@suse.de
- fix monitor probing
* Wed Jun 28 2000 kkaempf@suse.de
- add blinux support
  version 2.0.15
* Wed Jun 28 2000 kkaempf@suse.de
- select and install correct kernel for sun4u architecture
* Wed Jun 28 2000 kkaempf@suse.de
- fixed XFree86 4.0 startup to prevent sig11
  version 2.0.14
* Wed Jun 28 2000 kkaempf@suse.de
- new XFree86 4.0, re-enable SetLanguage and SetKeyboard
  version 2.0.13
* Mon Jun 26 2000 kkaempf@suse.de
- new title graphics
  version 2.0.12
* Mon Jun 19 2000 kkaempf@suse.de
- correct xf86config
  use binaries from saxtools package
  version 2.0.11
* Fri Jun 16 2000 kkaempf@suse.de
- make symlink for /usr/X11R6/bin/X (not in xf86 package any more)
  version 2.0.10
* Fri Jun 16 2000 kkaempf@suse.de
- back out workarounds for aaa_base bugs
  version 2.0.9
* Fri Jun  9 2000 kkaempf@suse.de
- start using ag_shell and Include()
  version 2.0.8
* Fri Jun  9 2000 kkaempf@suse.de
- .probe adaptions, no more "byclass" probing
  corrected inst_ask_config
  version 2.0.7
* Thu Jun  8 2000 kkaempf@suse.de
- scripts fixed for XFree86 4.0
  SetLanguage disabled for continue_mode
  version 2.0.6
* Thu Jun  8 2000 kkaempf@suse.de
- set LD_LIBRARY_PATH
  version 2.0.5
* Thu Jun  8 2000 kkaempf@suse.de
- fixed driver lookup
  added initrd scripts
  version 2.0.4
* Thu Jun  8 2000 kkaempf@suse.de
- added dolilo
  version 2.0.3
* Wed Jun  7 2000 kkaempf@suse.de
- .ycp are not executable
  use XFree86 3.3.x on startup
* Tue Jun  6 2000 kkaempf@suse.de
- syntax change for makefs/makereiserfs/packager clients
* Wed May 31 2000 kkaempf@suse.de
- allow for optional translation of timezone list
* Tue May 30 2000 kkaempf@suse.de
- allow for optional translation of keyboard and mouse list
* Wed May 24 2000 kkaempf@suse.de
- merge ppc changes
  new abort dialogue
  adapt to new .probe paths
* Tue May 23 2000 kkaempf@suse.de
- backport sparc changes from old yast2
* Fri May 19 2000 kkaempf@suse.de
- add data files for x11 configuration
* Fri May 19 2000 kkaempf@suse.de
- add start scripts for yast2
* Wed May 17 2000 kkaempf@suse.de
- Initial version based on SuSE 6.4 (i386)
