#
# spec file for package yast2-devtools
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


Name:           yast2-devtools
Version:        4.2.6
Release:        1.2
Url:            https://github.com/yast/yast-devtools
Summary:        YaST2 - Development Tools
License:        GPL-2.0-or-later
Group:          System/YaST

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  perl-XML-Writer
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel

Requires:       yast2-buildtools

BuildArch:      noarch

%description
Scripts and templates for developing YaST2 modules and components.

%package -n yast2-buildtools
Summary:        Minimal set of tools needed to build yast module
Group:          System/YaST

Requires:       perl
Requires:       perl-XML-Writer
# we install our .pc under $prefix/share
Requires:       autoconf
Requires:       automake
Requires:       gettext-tools
Requires:       pkgconfig >= 0.16

%if 0%{?suse_version} <= 1230
# extra package for yard Markdown formatting in openSUSE <= 12.3
Requires:       rubygem(%{rb_default_ruby_abi}:redcarpet)
%endif

Recommends:     cmake
# /usr/lib/YaST2/bin/ydoxygen needs it
Recommends:     doxygen
# for svn builds of binary packages
Recommends:     libtool
# for extracting translatable strings from *.rb files using "make pot" command
# weak dependency, "make pot" is usually not needed
Suggests:       rubygem(gettext)

%description -n yast2-buildtools
Scripts and templates required for rebuilding the existing YaST2
modules and components (both ruby and C++).

%prep
%setup -q

%build
make -f Makefile.cvs all

./configure --prefix=%{_prefix} --libdir=%{_libdir}
make

%install
make install DESTDIR="%{buildroot}"
[ -e "%{_datadir}/YaST2/data/devtools/NO_MAKE_CHECK" ] || Y2DIR="%{buildroot}%{_datadir}/YaST2" make check DESTDIR="%{buildroot}"
for f in `find %{buildroot}%{_datadir}/applications/YaST2 -name "*.desktop"` ; do
    d=${f##*/}
    %suse_update_desktop_file -d ycc_${d%.desktop} ${d%.desktop}
done

%if 0%{?qemu_user_space_build}
# disable testsuite on QEMU builds, will fail
cat > "%{buildroot}%{_datadir}/YaST2/data/devtools/NO_MAKE_CHECK" <<EOF
Disabling testsuite on QEMU builds, as the userspace emulation
is not complete enough for yast2-core
EOF
%endif

# Change false to true in the following line when yast2 core is broken
false && cat > "%{buildroot}%{_datadir}/YaST2/data/devtools/NO_MAKE_CHECK" <<EOF
When yast2 core is broken and the interpreter does not work,
submitting yast2-devtools with the flag file existing will
prevent ycp developers being flooded by testsuite failures.
EOF

%fdupes %{buildroot}%{_prefix}

%files
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/*ycp-mode.el
%dir %{_datadir}/vim
%dir %{_datadir}/vim/site
%dir %{_datadir}/vim/site/syntax
%{_datadir}/vim/site/syntax/ycp.vim
%dir %{_datadir}/vim/site/ftdetect
%{_datadir}/vim/site/ftdetect/ycp_filetype.vim
%dir %{_prefix}/lib/YaST2
%{_datadir}/cmake
%dir %{_datadir}/YaST2
%doc %{_datadir}/doc/packages/%{name}
%dir %{_prefix}/lib/YaST2/bin
%{_prefix}/lib/YaST2/bin/scrdoc
%{_prefix}/lib/YaST2/bin/ycp_puttext
%{_prefix}/lib/YaST2/bin/ydoxygen
%dir %{_datadir}/YaST2/clients/
%{_datadir}/YaST2/clients/ycp2yml.rb
%{_datadir}/YaST2/data/devtools/bin/check-textdomain
%{_datadir}/YaST2/data/devtools/bin/check_icons
%{_datadir}/YaST2/data/devtools/bin/create_maintenance_branch
%{_datadir}/YaST2/data/devtools/bin/find-unused-published
%{_datadir}/YaST2/data/devtools/bin/get-lib
%{_datadir}/YaST2/data/devtools/bin/pot-spellcheck
%{_datadir}/YaST2/data/devtools/bin/rny2rnc
%{_datadir}/YaST2/data/devtools/bin/showy2log
%{_datadir}/YaST2/data/devtools/bin/tagversion
%{_datadir}/YaST2/data/devtools/bin/y2makepot
%{_datadir}/YaST2/data/devtools/bin/po_add_format_hints
%{_datadir}/YaST2/data/devtools/bin/gettextdomains
%{_datadir}/YaST2/data/devtools/bin/ycp_puttext
%{_datadir}/YaST2/data/devtools/data/rubocop_yast_style.yml
%{_datadir}/YaST2/data/devtools/data/rubocop-0.71.0_yast_style.yml
%dir %{_datadir}/YaST2/control/
%{_datadir}/YaST2/control/control_to_glade.xsl

%files -n yast2-buildtools
%{_sysconfdir}/rpm/macros.yast
%{_bindir}/y2tool
%{_datadir}/aclocal/*.m4
%{_datadir}/pkgconfig/yast2-devtools.pc
%{_datadir}/YaST2/data/docbook
%dir %{_datadir}/YaST2/data
%dir %{_datadir}/YaST2/data/devtools
%dir %{_datadir}/YaST2/data/devtools/bin
%{_datadir}/YaST2/data/devtools/admin
%{_datadir}/YaST2/data/devtools/Doxyfile
%if 0%{?qemu_user_space_build}
%{_datadir}/YaST2/data/devtools/NO_MAKE_CHECK
%endif
# needed for doxygen, not nice
%{_datadir}/YaST2/data/devtools/footer-notimestamp.html
%dir %{_datadir}/YaST2/data/devtools/data
%{_datadir}/YaST2/data/devtools/data/YaST2.dict.txt
%{_datadir}/YaST2/data/devtools/bin/y2autoconf
%{_datadir}/YaST2/data/devtools/bin/y2automake
%{_datadir}/YaST2/data/devtools/bin/y2metainfo
%license COPYING

%changelog
* Tue May  5 2020 Stefan Hundhammer <shundhammer@suse.com>
- New script to add format hints for translated messages:
  po_add_format_hints (bsc#954505, bsc#980329)
- 4.2.6
* Wed Jul 17 2019 Ladislav Slezák <lslezak@suse.cz>
- Fixed syntax error in the RPM macros causing
  "line 53: [: missing `]'" error during package build
- Related to the desktop file changes (boo#1084864)
- 4.2.5
* Tue Jun 25 2019 Josef Reidinger <jreidinger@suse.com>
- Allow smooth adaptation of newer rubocop by adding defaults for
  it (bsc#1139270)
- 4.2.4
* Sat Jun  1 2019 Stasiek Michalski <hellcp@mailbox.org>
- Adapt to desktop file changes (boo#1084864)
- 4.2.3
* Wed May 29 2019 Stasiek Michalski <hellcp@mailbox.org>
- Create a directory for metainfo files (fate#319035)
- 4.2.2
* Mon May 20 2019 Stasiek Michalski <hellcp@mailbox.org>
- Generate metainfo appstream for desktop files (fate#319035)
- 4.2.1
* Thu Apr 25 2019 Stasiek Michalski <hellcp@mailbox.org>
- Check if directory exists before updating desktop files (boo#1133433)
- 4.2.0
* Wed Nov 28 2018 lslezak@suse.cz
- Fix up for the icondir path expansion (boo#1109310)
- 4.1.2
* Tue Nov 27 2018 Stasiek Michalski <hellcp@mailbox.org>
- Provide icon with module (boo#1109310)
- 4.1.1
* Tue Oct 16 2018 schubi@suse.de
- Added license file to spec.
* Wed Aug 22 2018 schubi@suse.de
- Switched license in spec file from SPDX2 to SPDX3 format.
* Wed Jul 25 2018 lslezak@suse.cz
- Pass absolute paths to "yard", relative paths do not work anymore
  because of a security update (bsc#1070263, CVE-2017-17042)
- We do not auto generate the documentation anymore, but it might
  be used by some 3rd party packages...
- 4.1.0
* Thu Mar 22 2018 lslezak@suse.cz
- Allow extracting the translatable texts alsom from XSL files
  (bsc#1083720)
- 4.0.5
* Thu Mar  1 2018 lslezak@suse.cz
- Fixed generating translations from XML (*.glade) files
  (related to bsc#1083015)
- 4.0.4
* Tue Feb 27 2018 jreidinger@suse.com
- Prevent missing translatable string with missing textdomain by
  making it fatal error, so it can be catched in travis or jenkins
  (bsc#1083015)
- 4.0.3
* Tue Feb 27 2018 lslezak@suse.cz
- Fixed regular expression used for finding translatable messages
  in the source files (bsc#1082969)
- 4.0.2
* Wed Nov 29 2017 igonzalezsosa@suse.com
- Fix fillup-templates path (bsc#1070408)
- 4.0.1
* Tue Oct 10 2017 mvidner@suse.com
- Use -Wno-format-nonliteral (bsc#982942)
- 4.0.0
* Tue Sep 20 2016 jreidinger@suse.com
- run old yast testsuite in parallel to speed up build (bsc#999203)
* Wed Aug 24 2016 jreidinger@suse.com
- ignore in spellcheck 'vc' because used as 'osc vc' suggestion in
  CONTRIBUTING.md (needed to submit bnc#995333)
- 3.1.46
* Fri Aug  5 2016 mvidner@suse.com
- y2makepot, gettextdomains: ignore test/ directories.
* Tue Jul 19 2016 jreidinger@suse.com
- Generate simple page if yard is not available (follow-up of
  previous fix for building) (part of FATE#320356)
- 3.1.45
* Mon Jul 18 2016 jreidinger@suse.com
- prevent yard failure as it is no longer dependency, so skip
  ruby autodocs generation if not available (fix yast-rdp and
  yard-smt build) (part of FATE#320356)
- 3.1.44
* Thu Jul 14 2016 jreidinger@suse.com
- Update the Rubocop config to prefer method_alias over alias
  (bsc#988759)
- 3.1.43
* Wed Jul 13 2016 lslezak@suse.cz
- Update the Rubocop config so YaST can use a new Rubocop version
  (0.41.x) (bsc#988759)
- 3.1.42
* Fri Jun  3 2016 igonzalezsosa@suse.com
- Remove yard dependency as *-devel-doc packages are not being
  generated anymore.
* Mon Mar 14 2016 mvidner@suse.com
- y2makepot: copy also comments for translators from control.xml
  (FATE#317481)
- 3.1.41
* Wed Feb 24 2016 lslezak@suse.cz
- YaST RPM macros - fix for the previous change: some packages
  use configure.ac.in instead of the old configure.in.in (bsc#968002)
- 3.1.40
* Tue Feb  9 2016 lslezak@suse.cz
- YaST RPM macros - add support for Rake based packages, optionally
  run additional tests (used at Jenkins CI builds)
- 3.1.39
* Wed Aug  5 2015 shundhammer@suse.de
- reasonable defaults for method and class lengths in rubocop.yml
  (bnc#940671)
- 3.1.38
* Wed Aug  5 2015 lslezak@suse.cz
- integrate the common rubocop.yml file for the SUSE Ruby style
  (bsc#940571)
- 3.1.37
* Thu May 21 2015 lslezak@suse.cz
- y2makepot: do not create confusing _MISSING_TEXTDOMAIN_* files
  (they cause for example rubocop check to fail) (bnc#940203)
- 3.1.36
* Thu May 14 2015 jreidinger@suse.com
- revert incompatible change for vardir as it break yast2.rpm
  build
- 3.1.35
* Tue May 12 2015 besser82@fedoraproject.org
- show warnings about problems with Autotools-setup
- split generation of Autotools into %%yast_prep
- run configure with '--disable-silent-rules' and use %%make_build
- use fallback if %%make_build is not defined
- split './configure'-step into %%yast_configure
- add %%yast_libdir
- use macros instead of hardcoded paths
- use %%buildroot instead of $RPM_BUILD_ROOT
- use %%__make instead of plain 'make'
- make %%yast_desktop_files generic for other distris
- invoke %%yast_check during %%yast_install on SUSE only
- 3.1.34
* Mon May 11 2015 besser82@fedoraproject.org
- add configure-option '--disable-debug'
- use '--disable-debug' instead forcing $RPM_OPT_FLAGS into $ENV
  handling $RPM_OPT_FLAGS is done by %%configure-macro anyways
- 'gettextdomains' is DATA not SCRIPT
- use 'dist_'-prefix instead of 'EXTRA_DIST'
- 3.1.33
* Sat May  9 2015 besser82@fedoraproject.org
- replace obsolete `AC_PROG_LIBTOOL` with `LT_INIT()`
- use new `AC_INIT()`-syntax with args in square braces
- 3.1.32
* Wed May  6 2015 aschnell@suse.de
- require rubygems of default ruby version (bsc#929899)
- 3.1.31
* Thu Mar 26 2015 jreidinger@suse.com
- yast-jenkins-modify:
  - handle correctly modules that do not have github repo in
    yast-{mod} format
  - fix used sed to handle correctly oneliner xml
  - improve error reporting for quicker detection of problems
- 3.1.30
* Wed Jan 21 2015 jreidinger@suse.com
- find-unused-published: support new ruby hash syntax
- 3.1.29
* Fri Jan 16 2015 aschnell@suse.de
- split rpm macro %%yast_install into submacros for finer control
- 3.1.28
* Thu Jan  8 2015 jreidinger@suse.com
- Add shared rubocop yast style config
- 3.1.27
* Thu Nov 13 2014 jreidinger@suse.com
- fix building with new libtool which use variable in backticks
  causing double backticks and failure to build
- 3.1.26
* Tue Sep 23 2014 jreidinger@suse.com
- Do not read (and have ./configure evaluate) the MAINTAINER file.
- 3.1.25
* Fri Sep  5 2014 mvidner@suse.com
- Merged git and IBS
- 3.1.24
* Fri Sep  5 2014 jreidinger@suse.com
- create_maintenance_branch: fix build target for SLE-12 branch
- 3.1.23
* Thu Sep  4 2014 jreidinger@suse.com
- add tool for easy creation of maintenance branches to ytools
- 3.1.22
* Thu Sep  4 2014 mvidner@suse.com
- Use a more flexible rubygem requirement syntax (bnc#895069)
- 3.1.21
* Fri Jul 18 2014 mrueckert@suse.de
- switch to rubygem() based buildrequires so we can easily switch
  the ruby version.
* Fri Jun  6 2014 locilka@suse.com
- gettextdomains: added support for single quotes around
  textdomain (bnc#881277)
- 3.1.20
* Thu Jun  5 2014 lslezak@suse.cz
- y2makepot: transform control files into glade compatible format
  so they can be processed by xgettext (the latest xgettext does
  some format validation before processing) (bnc#881278)
- 3.1.19
* Tue Jun  3 2014 jreidinger@suse.com
- gettextdomains fix detection of files including somewhere "/*"
  bnc#880659
- 3.1.18
* Tue Mar 25 2014 lslezak@suse.cz
- y2makepot: added support for extracting translatable strings from
  ERB files (*.erb)
- 3.1.17
* Fri Feb 14 2014 jreidinger@suse.com
- return back gettextdomains to allow generating translations
- 3.1.16
* Wed Dec 18 2013 lslezak@suse.cz
- added @ylibdir@ and @controldir@ automake macros
- added %%yast_controldir RPM macro
- 3.1.15
* Tue Dec 17 2013 lslezak@suse.cz
- added %%yast_libdir RPM macro
- 3.1.14
* Mon Dec 16 2013 lslezak@suse.cz
- use the first "Version" tag from spec when looking for the
  package version, fixes problem when multiple tags are present
- 3.1.13
* Fri Dec 13 2013 guillaume@opensuse.org
- Fix QEMU-ARM build by adding
  %%{_datadir}/YaST2/data/devtools/NO_MAKE_CHECK file in file list
  when built in qemu since no make check are done in this case
* Wed Dec 11 2013 lslezak@suse.cz
- y2autoconf - in perl we need extra backslash escaping
- 3.1.12
* Wed Dec 11 2013 lslezak@suse.cz
- use grep/sed instead of rpm for parsing spec files (rpm prints
  the version for each subpackage, moreover it does some dependecy
  resolving which might fail)
- 3.1.11
* Mon Dec  9 2013 lslezak@suse.cz
- read the version directly from *.spec file (ignore the VERSION
  files so they can be removed)
- 3.1.10
* Tue Oct 15 2013 jreidinger@suse.com
- y2automake: properly install required COPYING file from top
  directory
- 3.1.9
* Mon Oct 14 2013 jreidinger@suse.com
- cmake module: Do not generate spec file from spec.in as it is
  obsolete with spec file including rpm macros
- 3.1.8
* Mon Oct 14 2013 jreidinger@suse.com
- big clean-up of dead tools
- new subpackage yast2-buildtools that contain minimal set of tools
  needed for modules as BuildRequire
- 3.1.7
* Wed Oct  9 2013 jreidinger@suse.com
- cmake module: read VERSION instead of VERSION.cmake to be
  consistent across all packages
- 3.1.6
* Tue Oct  8 2013 jreidinger@suse.com
- rpm macros: Use "%%configure" to properly configure also
  sysconfdir and sbindir
- 3.1.5
* Wed Oct  2 2013 mvidner@suse.com
- rpm macros: Use "make check VERBOSE=1"
  to debug failures directly from build logs
- 3.1.4
* Tue Oct  1 2013 jreidinger@suse.com
- fix Makefile.am.common to respect removed tools and killed ycp
- 3.1.3
* Mon Sep 30 2013 jreidinger@suse.com
- fix bunch of build service warnings
- add Rakefile to allow uniform access to all yast modules
- start using fdupes to reduce duplicities
- 3.1.2
* Wed Sep 25 2013 jreidinger@suse.com
- remove ycpdoc as ycp is no longer live
- clean a bit old unused tools
- 3.1.1
* Tue Sep 17 2013 lslezak@suse.cz
- added yast RPM macros (/etc/rpm/macros.yast)
- this package: use *.spec directly instead of expanding *.spec.in
- all packages: make *.spec.in files optional (do not fail if missing)
- 3.1.0
* Wed Sep 11 2013 lslezak@suse.cz
- y2makepot (used in "make pot" call) - added support for ruby
  gettext 3.0.0, check POT file compatibility with GNU gettext
- 3.0.5
* Tue Aug 13 2013 lslezak@suse.cz
- correctly handle yard documentation in Yast/ subdirectories
- 3.0.4
* Fri Aug  9 2013 lslezak@suse.cz
- Makefile.am.common - do not create empty ".dep" YCP dependency
  file when there is no YCP module file
- 3.0.3
* Wed Aug  7 2013 lslezak@suse.cz
- added ycp2yml client for converting static YCP data files into
  YAML format
- 3.0.2
* Fri Aug  2 2013 lslezak@suse.cz
- enhanced syntax check in 'make check-syntax':
  - check Ruby source files
  - check YCP data files (some are still present even after Ruby
    conversion)
- 3.0.1
* Tue Jul 30 2013 yast-devel@opensuse.org
- version 3.0.0
* Mon Jul 29 2013 lslezak@suse.cz
- autodocs fixes:
  - doxygen: install _all_ JS and CSS files (dynsections.js,
    jquery.js and tabs.css were missing, resulting in unusable
    documentation)
  - doxygen: updated the default doxygen config file - removed
    obsolete options which caused warnings during build
  - yard: use --title option with package name
- 2.24.7
* Fri Jul 26 2013 lslezak@suse.cz
- y2makepot (used in "make pot") - extract translatable strings
  from Ruby files using rxgettext (rubygem-gettext)
- 2.24.6
* Wed Jul 24 2013 lslezak@suse.cz
- require rubygem-redcarpet in openSUSE <= 12.3, needed for yard
  Markdown formatting
- 2.24.5
* Mon Jul 22 2013 lslezak@suse.cz
- autodocs - use markdown format in ruby documentation comments,
  added YARD_OPTIONS to allow overriding the defaults
- 2.24.4
* Thu Jul 18 2013 mvidner@suse.com
- fixed automake warnings about configure.in and INCLUDES
* Thu Jul 18 2013 lslezak@suse.cz
- autodocs - added support for generating documentation for ruby
  files using yard generator
- 2.24.3
* Tue Jul 16 2013 mvidner@suse.com
- autodocs-ycp.ami: only call ycpdoc if YCP files are found
- 2.24.2
* Thu Jun 27 2013 lslezak@suse.cz
- ycpdoc - improved generating index file, the same functions are
  additionaly sorted by source file to avoid random order in the
  output (fixes testsuite failure after upgrading to perl-5.18)
- 2.24.1
* Mon Apr  8 2013 jreidinger@suse.com
- fix tagversion to work with git
- fix package checks to work with git
- allow resubmit package to BS without changes entry
- 2.24.0
* Tue Dec 11 2012 jreidinger@suse.com
- fix cmake plugin search. In particular, look in lib64, and find
  them in /usr when our prefix is /usr/local.
- 2.23.2
* Tue Oct 30 2012 jsuchome@suse.cz
- removed references to SuSEconfig (fate#100011)
- 2.23.1
* Mon Aug  6 2012 dmueller@suse.com
- fix disablement of make check on QEMU/ARM builds
* Mon Jun 18 2012 aschnell@suse.de
- link agents against y2util and ycpvalues to get proper rpm
  dependencies (zypper and buildservice need them)
- 2.23.0
* Thu May  3 2012 mfilka@suse.com
- updated Makefile.am.common - rebuilds ybc when make package-local
- 2.21.9
* Thu Jan 12 2012 coolo@suse.com
- yast's license is GPL-2.0 in doubt, not "GPL"
- 2.21.8
* Tue Jan  3 2012 ke@suse.de
- ydoc/po-tools/po-stats: filter file name (FILE.LL.po:) that 'msgfmt
  - -stats' now outputs.
* Fri Dec 16 2011 coolo@suse.com
- autoreconf and suse_config_update are doing the same thing, so leave
  out suse specifics
* Mon Nov 21 2011 coolo@suse.com
- add libtool as buildrequire to avoid implicit dependency
- remove clean section
* Tue Oct 25 2011 lslezak@suse.cz
- fixed oscsubmit to not submit *.rej and *.orig files left after
  failed merging
- 2.21.6
* Tue Oct  4 2011 visnov@suse.cz
- remove definition of Prefix in spec file (create-spec)
- use _prefix in .spec file
- 2.21.5
* Fri Sep 30 2011 visnov@suse.cz
- added 'y2tool obssync'
- 2.21.4
* Tue Sep 27 2011 visnov@suse.cz
- dropped all-packages and devel-packages lists
- 2.21.3
* Thu Sep 22 2011 mvidner@suse.cz
- create-spec: adjusted whitespace to comply with prepare_spec
- create-spec: use %%version to minimize diffs
- 2.21.2
* Mon Sep 19 2011 visnov@suse.cz
- Simplify config module skeleton
- Remove dependency on Wizard_hw
- Add setting window title and icon to config skeleton
- 2.21.1
* Wed Aug 24 2011 ke@suse.de
- Makefile.am.center: Ignore warnings when building po file statistics.
* Fri Aug  5 2011 tgoettlicher@suse.de
- fixed .desktop file (bnc #681249)
* Fri Jul 22 2011 locilka@suse.cz
- Obsoleted X-KDE-SubstituteUID replaced with xdg-su in Exec in
  desktop files (bnc#540627)
- 2.21.0
* Fri Jul  1 2011 locilka@suse.cz
- Added some more known words to the spellcheck whitelist.
* Thu Sep 24 2009 mvidner@suse.cz
- create-spec: recognize plain rpm subpackages.
- 2.18.11
* Fri Aug 14 2009 lslezak@suse.cz
- disable testsuite on ARM
- 2.18.10
* Thu Jul  2 2009 mzugec@suse.cz
- added yast2-isns module
* Fri Jun 26 2009 mvidner@suse.cz
- YastCommon.cmake: don't override License, Group
* Mon Jun 22 2009 mvidner@suse.cz
- create-spec: don't override License, Group, %%build
- 2.18.9
* Fri Jun 19 2009 mvidner@suse.cz
- autodocs-ycp.ami: fixes to work with subdirectories:
  introduced AUTODOCS_STRIP.
- 2.18.8
* Tue Jun 16 2009 mvidner@suse.cz
- autodocs-ycp.ami: Added AUTODOCS_SUBDIR, for yast2.rpm
- oscsubmit: Adjusted "osc sr" syntax to work with old and new (0.119) osc.
* Tue Jun 16 2009 coolo@novell.com
- fixed more makefiles
* Mon Jun 15 2009 mvidner@suse.cz
- Fixed makefile includes (*.ami) to work with "install" calls changed
  via automake-1.11.
- 2.18.7
* Thu Jun 11 2009 lslezak@suse.cz
- added float::tolstring builtin to the vim syntax file
  (added in yast2-core-2.18.12)
- rest-plugin skeleton - define and use 'id' member
* Tue Jun  9 2009 mvidner@suse.cz
- Take advantage of AM_SILENT_RULES and AUTOMAKE_JOBS if supported
  (in automake-1.11)
* Mon Jun  8 2009 lslezak@suse.cz
- 2.18.6
* Mon May 25 2009 lslezak@suse.cz
- added new skeleton 'rest-plugin' for webservice plugins,
  initial version
* Wed May 20 2009 lslezak@suse.cz
- create-new-package - fixed syntax error (missing semicolon)
* Wed May 20 2009 mvidner@suse.cz
- y2tool tagversion: fixed branch tagging for tmp/* branches such as
  tmp/SLE-11-SP1-Stash.
* Wed May  6 2009 jsrain@suse.cz
- updates of oscupdate
- 2.18.5
* Wed Apr 29 2009 lslezak@suse.cz
- updated vim YCP syntax file - added missing built-ins: lsort,
  lsubstring, ClientExists, GetEncoding, GetEnvironmentEncoding,
  dgettext, dngettext, dpgettext, float::abs, float::ceil,
  float::floor, float::pow, float::trunc, list::reduce, sublist,
  added type name: const, added UI option: Cell
* Mon Apr 27 2009 jsrain@suse.cz
- fixed y2tool oscsubmit when submitting package the first time
- make oscsubmit work correctly with cmake-based modules
* Mon Apr 27 2009 jsrain@suse.cz
- added y2tool oscsubmit (for Factory only)
- 2.18.4
* Thu Apr  9 2009 jreidinger@suse.cz
- ycp.vim : add switch condition and argsof builtin
* Thu Apr  2 2009 mvidner@suse.cz
- Makefile.am.toplevel: do not mkdir "`if" (bnc#490713).
- 2.18.3
* Thu Apr  2 2009 mvidner@suse.cz
- FindYast.cmake: make it a bit more verbose on error (kkaempf)
- ycp.vim: added ButtonBox (jsuchome)
- ycp-mode.el: added notifyContextMenu (aschnell)
- y2autoconf: Fixed bootstrapping via Makefile.cvs
- y2makeall: merge back the one used on Hudson,
  with additional features like printing the base buildrequires (visnov)
- y2log_ana: remove hardcoded moc that broke with new qt (dmacvicar)
* Tue Mar  3 2009 ke@suse.de
- Call msgmerge with the --previous option.
* Tue Feb 10 2009 mvidner@suse.cz
- ydoxygen: omit timestamps in the output to avoid unnecessary
  rebuilds (bnc#474281).
- 2.18.2
* Wed Feb  4 2009 mvidner@suse.cz
- Added 'y2tool svnignore' to convert .cvsignore to svn:ignore (bnc#470981).
- Renamed .cvsignore to _cvsignore in the skeletons.
- remove .cvsignore files (coolo)
- 2.18.1
* Fri Jan 16 2009 aschnell@suse.de
- added some new YCP keywords to emacs mode
- 2.18.0
* Fri Nov 14 2008 ke@suse.de
- bin/create-spec: Remove sles version check from yast2-trans-spec
  files.
* Fri Aug  8 2008 locilka@suse.cz
- Fixed ydoc2 to generate builtin/widget description even if there
  is no empty line between description and the following  tag
  (adding newlines between all known tags before parsing).
* Mon Aug  4 2008 locilka@suse.cz
- Generating better XML (Authors section) to be easier-to-process
  by XSLT transformations (bnc #401680).
- Adapted testsuites.
- 2.17.6
* Wed Jul 30 2008 mvidner@suse.cz
- Added yastdoc (http://en.opensuse.org/YaST/yastdoc).
- Create a disambiguation chapter only if requested by a xslt
  parameter.
- 2.17.5
* Tue Jul 29 2008 mvidner@suse.cz
- Recommend libtool for svn builds of binary packages.
- YDoxygen:
  - Updated template Doxyfile to doxygen 1.5.5, enabled built in STL
    support.
  - Made it easier to troubleshoot by using a real config file instead
    of a pipe, pointed out the log (bnc#412465).
- Stylesheets for documentation of builtins (and WFM, Pkg):
  - Assist a straightforward mapping between source code
    usage and reference docs URLs: list::reduce should be
    .../ycp/list/reduce.html, not .../YCPListBuiltins_reduce.html.
  - Enabled processing multiple chapters at once to make overload
    disambiguation possible.
  - Minor Docbook validity fixes.
- 2.17.4
* Fri Jul 18 2008 mvidner@suse.cz
- The previous change broke the few packages that do not need
  yast2-core. Only use yast2-core.pc when it is present.
- 2.17.3
* Thu Jul 17 2008 mvidner@suse.cz
- Use Y2CORE_CFLAGS, so that we can get rid of <ext/hash_map>
  warnings.
- 2.17.2
* Tue Jul 15 2008 locilka@suse.cz
- Killed some ycpdoc lamentation (leaving the worthy complaints).
- Added some docu-bug tolerancy level (@tag:->@tag, @tags->@tag).
- Testsuites forced to accept my changes!
- 2.17.1
* Fri Jun 13 2008 locilka@suse.cz
- Script ycpdoc has been extended to understand new header-tag
  'Internal'. Internal modules are skipped while creating the YaST
  overall documentation (bnc #344926).
* Mon Jun  9 2008 mvidner@suse.cz
- ydoc.xsl: don't break on builtins in namespaces.
- Fixed some perl warnings in ydoc2.
* Wed Jun  4 2008 mvidner@suse.cz
- Make ycp_puttext reachable by y2tool (bnc#396315).
- 2.17.0
* Fri May 16 2008 jsrain@suse.cz
- added categories Settings and System into desktop file
  (bnc #382778)
* Wed Apr 16 2008 mvidner@suse.cz
- removed bash constructs from y2tool and y2automake which are marked
  with /bin/sh (bnc#379849)
- exposed warnings in ydoc2 (docs for YCP builtins)
- tagversion --remove: remove tag after adding it by mistake
* Mon Mar 31 2008 locilka@suse.cz
- Some more words added to the current YaST dictionary.
* Mon Mar 17 2008 jsrain@suse.cz
- added 'StartupNotify=true' to the desktop file (bnc #304964)
* Wed Mar 12 2008 mvidner@suse.cz
- Fixed file list.
- 2.16.8
* Wed Mar 12 2008 mvidner@suse.cz
- Moved VIM simtax highlighting here from vim-data (bnc#364509).
- prefixbuild: accounted for recent package splits
- 2.16.7
* Fri Feb 15 2008 coolo@suse.de
- several fixes in the cmake modules
- 2.16.6
* Fri Feb 15 2008 visnov@suse.de
- support 'y2tool -h' as well
* Fri Feb  8 2008 coolo@suse.de
- enhance cmake macros for tar generation
- 2.16.5
* Fri Feb  1 2008 mvidner@suse.cz
- Require autotools, gettext-tools, recommend cmake (bnc#356996).
- y2makepot: look for gettext() in addition to _() and __() (bnc#354678).
- prefixbuild: cmake fixes, small fixes for individual modules
- 2.16.4
* Thu Jan 24 2008 mzugec@suse.de
- replace deprecated NetworkDevices by NetworkInterfaces (from yast2)
* Thu Jan 24 2008 sh@suse.de
- In cmake-based projects, use @HEADERCOMMENT@ instead of
  @HEADER-COMMENT@ (the "-" seems to be an illegal character)
* Fri Jan 18 2008 locilka@suse.cz
- Recommends: doxygen (needed by ydoxygen).
* Thu Dec 20 2007 sh@suse.de
- Added support for cmake-based projects to y2makeall
  (Not just completely out of tree like libzypp, even subdirs
  in the normal yast2 SVN tree)
* Mon Dec  3 2007 coolo@suse.de
- include cmake directories
* Mon Nov 26 2007 dmacvicar@suse.de
- added basic cmake infrastructure
- 2.16.3
* Fri Nov  9 2007 dfiser@suse.cz
- Added script for generating graph of includes/imports from YCP
  called ycp_graph.
* Fri Nov  9 2007 locilka@suse.cz
- Added new check_deps script for basic checking of imported
  YCP or Perl (YaST) modules.
- Added new gen_logic_deps script for generating dependency graphs.
- Added new gen_logic_deps_nodes script for picking up just nodes
  we are interested in.
- 2.16.2
* Wed Oct 10 2007 mvidner@suse.cz
- Suppresed portability warnings from automake. We know that we use
  GNU Make extensions.
- 2.16.1
* Tue Oct  2 2007 mvidner@suse.cz
- One copy of the license is enough (COPYING), removed
  COPYRIGHT.english (#299144).
- 2.16.0
* Wed Sep 12 2007 dfiser@suse.cz
- Added support for reading from stdin to showy2log script.
- 2.15.9
* Wed Aug 29 2007 mvidner@suse.cz
- "make dist" will create only a tar.bz2, not a tar.gz (#289571).
- 2.15.8
* Thu Aug 23 2007 sh@suse.de
- y2makeall: Check for multiple installed verions of libzypp
* Wed Aug 22 2007 mvidner@suse.cz
- prefixbuild/recreate: Accomodate for libzypp
* Wed Aug 15 2007 mvidner@suse.cz
- Fixed spec creation for non-trans packages.
- 2.15.7
* Wed Aug 15 2007 mvidner@suse.cz
- prefixbuild: handle lib64, yast2-metapackage, and *-devel-doc
- 2.15.6
* Tue Aug 14 2007 ke@suse.de
- Better language handling on spec file level for *trans* packages;
  introduce @ISO639@ (#279869).
* Fri Aug 10 2007 mvidner@suse.cz
- Fixed make package for gtk.
* Wed Aug  8 2007 od@suse.de
- remove unused "use Encode" from showy2log
- 2.15.5
* Tue Aug  7 2007 od@suse.de
- changes for showylog:
  - fixed --version output: show revision, date, time but no extra
    line
  - print extra line / line finisher with color reset only when
    normal output was printed
- 2.15.4
* Tue Aug  7 2007 locilka@suse.cz
- Added yast2-kdump, yast2-python-bindings, yast2-squid,
  and yast2-ruby-bindings, into all-packages.
* Mon Aug  6 2007 od@suse.de
- ported showy2log to perl, average speedup for pretty-print is 20x
- using a "command" with options now needs a "--" in front of the
  command (Getopt::Long cannot handle this better)
- fixed matching the component
- fixed logic that decides when to call the "accept line" filter
- 2.15.3
* Mon Jul 30 2007 locilka@suse.cz
- Added yast2-sshd into all-packages.
* Wed Jul 25 2007 sh@suse.de
- Added YAST2-CHECKS-QT4 to y2autoconf for Qt-4.x support
- V 2.15.2
* Wed May 30 2007 mvidner@suse.cz
- check-textdomain: Fixed --help and issues with empty lines
  in POTFILES (#278784).
- 2.15.1
* Thu May 17 2007 locilka@suse.cz
- Added more words into the YaST dictionary.
* Tue Apr  3 2007 mvidner@suse.cz
- Added Get/SetModified to skeleton *_auto.ycp (#260263)
* Fri Mar 30 2007 mvidner@suse.cz
- Fixed filelist because of reduced default buildsystem.
- 2.15.0
* Thu Mar 22 2007 aschnell@suse.de
- y2makeall: fixed excluding of packages/directories;
  added obsolete ipsec to exclude_list
* Mon Feb 26 2007 mvidner@suse.cz
- y2autoconf: Changed -Wformat to -Wformat=2 to catch more bugs (#246807).
* Fri Feb 23 2007 od@suse.de
- showy2log: accept lines containing parentheses around the
  hostname as in '(none)' for pretty-printing
* Fri Feb 16 2007 locilka@suse.cz
- Added yast2-add-on into all-packages.
* Fri Jan 26 2007 shaas@suse.de
- y2log_ana is a Qt-Viewer for all logfiles in y2log-syntax
  (it needs Qt4 so it is not built by default)
* Fri Jan 12 2007 jsrain@suse.cz
- let ycp_puttext process header files (*.h)
* Mon Nov 13 2006 jsrain@suse.cz
- 2.14.0
* Fri Oct 27 2006 mvidner@suse.cz
- Made the yast2-testsuite check only a warning, otherwise too many
  packages would break.
- prefixbuild/pfx: Let also Perl search in the prefix (via PERL5LIB).
- 2.13.29
* Tue Oct 24 2006 mvidner@suse.cz
- Run pkg-config at configure time, not at make time (#208998).
- For YCP packages, check for yast2-testsuite at configure time (#208999).
- 2.13.28
* Wed Oct 11 2006 mvidner@suse.cz
- "make dist" will honor CHECK_SYNTAX=false
- 2.13.27
* Mon Sep 25 2006 mvidner@suse.cz
- Docbook configure check: fixed when no catalog found, and
  don't overwrite config.log.
- prefixbuild/recreate -t: run configure instead of config.status
- prefixbuild/yp: honor PREFIX
- 2.13.26
* Mon Sep 18 2006 mvidner@suse.cz
- With xgettext 0.15, "--keyword=_:1,2" alone did not trigger for
  single-form messages. Added "--keyword=_" to fix that.
- Added yast2-trans-et to all-packages.
- 2.13.25
* Mon Sep 11 2006 mvidner@suse.de
- Fixed the autodocs if there were no *.pm files.
- 2.13.24
* Fri Sep  8 2006 mvidner@suse.cz
- Check for docbook-xml-stylesheets if using docbook (#157629).
- autodocs-ycp.ami: Generate docs also from *.pm sources, by pod2html (F#415).
- ycpdoc: Ignore *.pm but write them to files.html (F#415).
- 2.13.23
* Tue Aug 29 2006 mvidner@suse.cz
- po makefiles: cope with both old and new suse-i18n directory layout (ke).
- yast2-devtools.pc: removed libdir because this is a noarch package.
- prefixbuild: Another fix to honor PREFIX in the environment.
- 2.13.22
* Wed Aug 23 2006 mvidner@suse.cz
- Added yast2-sudo to all-packages.
* Mon Aug  7 2006 mvidner@suse.cz
- Added yast2-trans-ca to all-packages (#190072).
* Mon Aug  7 2006 mvidner@suse.cz
- Better parsing of "listmap" and the like not to mistake it for
  a function declaration (#133662).
- Prevent false positives for check-textdomain in core and perl-bindings.
- 2.13.21
* Wed Aug  2 2006 mvidner@suse.cz
- Fixed makefiles for make 3.81
- 2.13.20
* Tue Jul 18 2006 mvidner@suse.cz
- all-packages: added yast2-trans-{el,sl,vi}; kept
  yast2-trans-{el_GR,sl_SI} for SLE 10 compatibility.
* Fri Jun 30 2006 locilka@suse.cz
- New tag alias 'Author' -> 'Authors' in ycpdoc (bug #188881).
* Thu Jun 29 2006 locilka@suse.cz
- Teaching scrdoc one-line tags, general description, tag-aliases,
  fixing mount-point identification, etc.
* Mon Jun 26 2006 mvidner@suse.cz
- tagversion: do not break the tag if run again.
* Tue May 16 2006 locilka@suse.cz
- Sort YCP builtins in generated doc alphabetically, ASC.
* Fri May 12 2006 sh@suse.de
- Added check_buildrequires and checkall_buildrequires utilities
  as substitutes for check_neededforbuild and checkall_neededforbuild
* Thu May 11 2006 mvidner@suse.cz
- Fixed filtering for files that contain translated messages
  while making pot files (#173826, etoulas).
- 2.13.19
* Wed Apr 26 2006 sh@suse.de
- V 2.13.17
- Changed feedback address to http://bugs.opensuse.org/
  upon lrupp's request
* Thu Apr 13 2006 mvidner@suse.cz
- Respect POTFILES in y2makepot and check-textdomain.
- y2autoconf: Write the devtools version to the output.
- top_srcdir/Makefile.am: Always call y2tool in the right prefix.
- yast2-deps: Process all BuildRequires lines, do not skip
  liby2util-devel.
- recreate: Added usage (-h), skip recently recreated (-s), non-YaST
  mode (-Y).
- 2.13.17
* Fri Mar 24 2006 mzugec@suse.cz
- add Confirm::MustBeRoot() to ReadDialog()
* Mon Mar 13 2006 od@suse.de
- moved yast2/showy2log to devtools/bin/showy2log
- fixed endless loop in showy2log pretty-print when encountering
  unexpected formats
- 2.13.16
* Mon Mar 13 2006 od@suse.de
- check-textdomain needs gettextdomains, *sigh*
- 2.13.15
* Mon Mar 13 2006 od@suse.de
- added pretty-printing showy2log: new options -v, -s, -i, -F (and
  - d)
- 2.13.14
* Thu Mar  9 2006 sh@suse.de
- V 2.13.13
- Install check-textdomain
* Thu Mar  2 2006 lslezak@suse.cz
- fixed the skeletons:
  - removed yast2-devel-packages macro
  - added missing file in .spec in config skeleton
- 2.13.12
* Thu Feb 23 2006 etoulas@suse.de
- Extend devtools to catch missing textdomain in C/C++/YCP/Perl code
  (enhancement 147611)
  'make package' fails if a textdomain is missing (and needed)
  'make pot'     warns if a textdomain is missing (and needed)
- 2.13.11
* Thu Feb 23 2006 mvidner@suse.cz
- create-spec: HEADER will include Provides: locale(yast2:$L)
  for yast2-trans-$L.
- 2.13.10
* Wed Feb 22 2006 sh@suse.de
- Updated UI builtins and widgets in Emacs mode (ycp-mode.el)
* Tue Feb 21 2006 mvidner@suse.cz
- Provide autodocs-cc-off.ami for leaf packages that only want
  autodocs on maintainers explicit request (#151370).
- 2.13.9
* Mon Feb 13 2006 locilka@suse.cz
- Added standardized file header into the skeletons.
- 2.13.8
* Thu Feb  9 2006 mvidner@suse.cz
- Do not fail on repeated make install from a SVN working copy.
* Wed Jan 25 2006 mvidner@suse.cz
- Config skeleton: create a symlink for local build, #145327.
- 2.13.7
* Fri Jan 13 2006 od@suse.de
- showy2log: moved switching back to normal to the end of lines --
  after CTRL-C and after leaving "showy2log | o -r" now the prompt
  appears in normal colors
- 2.13.6
* Tue Jan 10 2006 mvidner@suse.cz
- Check error codes in ydoxygen so that we know if doxygen fails (#141384).
- Bumped versions in skeletons.
- 2.13.5
* Tue Dec 13 2005 mvidner@suse.cz
- Removed generic.pc.in, because once used, it was impossible to check
  for updates. Now every package using CREATE_PKGCONFIG must have
  its own *.pc.in.
- Fixed the inclusion of po/Makefile in AC_CONFIG_FILES.
- recreate: can be used for yast2-trans-*
- 2.13.4
* Thu Dec  1 2005 mvidner@suse.cz
- ycpdoc: @-tags are only recognized at the start of a comment line.
  Improved error reporting for incomplete @param and @return.
- Devtools now work in a custom prefix
- Added autoconf variable YCPC
- Running pkg-config with --print-errors
- 2.13.3
* Thu Oct 27 2005 mvidner@suse.cz
- Added a stylesheet for converting the CLI XML help to docbook.
- 2.13.2
* Thu Oct 13 2005 mvidner@suse.cz
- y2autoconf: Do not clutter . with OUTPUT and OUTPUT2.
- ycp_puttext: Do not complain if $ycp_file.rejected does not exist.
- 2.13.1
* Wed Oct  5 2005 mvidner@suse.cz
- ycpdoc: interface stability markup (incomplete)
- 2.13.0
* Tue Aug 23 2005 jsuchome@suse.cz
- added yast2-trans-fi to all-packages
- 2.12.12
* Fri Aug 12 2005 lslezak@suse.cz
- added yast2-vm into list of all yast packages
- 2.12.11
* Fri Aug 12 2005 visnov@suse.cz
- don't check imports by default
- 2.12.10
* Thu Aug 11 2005 visnov@suse.cz
- don't mention parseycp in check_ycp
* Thu Aug  4 2005 arvin@suse.de
- allow setting Y2DIR for ycpc (needed to build storage)
- 2.12.9
* Tue Aug  2 2005 locilka@suse.cz
- Adding "UTF-8" default parameter for XML::Writer::xmlDecl to fix
  the changed default behavior in ycpdoc.
- 2.12.8
* Tue Jul 26 2005 mir@suse.de
- fixed my typo in all-packages
- 2.12.7
* Tue Jul 26 2005 mir@suse.de
- added packagemanager-test and online-update-test to all-packages
- 2.12.6
* Fri Jul 22 2005 sh@suse.de
- Relaxed y2makepot syntax checking: Allow "Textdomain:", too
- Overwrite existing .pot file by default
- Made -f option to y2makepot obsolete (throw warning, but continue)
* Wed Jun 29 2005 arvin@suse.de
- allow setting LD_LIBRARY_PATH for ycpc (needed in storage)
* Tue Jun 28 2005 mvidner@suse.cz
- ycpdoc: rewrote @tag parsing for clarity.
* Mon Jun 27 2005 locilka@suse.cz
- adding new option -f = output format, it supports xml and html
  output formats (scrdoc)
* Mon Jun 27 2005 locilka@suse.cz
- adding lost dependency on .pot creation before the spellcheck
* Mon Jun 20 2005 mvidner@suse.cz
- y2autoconf: Avoid infinite recursion if SUBDIRS contains ".".
- ycpdoc:
  Print the current line together with its parsing state (--state).
  Documented --xml-output, die if the file cannot be opened.
- 2.12.3
* Thu Jun 16 2005 mvidner@suse.cz
- Better finding of subdirs for configure.in: do not do "find" since
  that does not honor SUBDIRS in Makefiles.am and so for example tries
  to work with the skeletons.
- Makefile.am.toplevel:check-all-packages: separate by any whitespace,
  not only tabs.
- Added autodocs-cc.ami for doxygen.
  Used autodocs-*.ami in skeletons.
- Added fillupdir (as configure parameter --with-fillupdir)
- 2.12.2
* Mon Jun  6 2005 hmacht@suse.de
- added script y2makepot and removed potfile creation from
  Makefile.am's
* Thu Jun  2 2005 mvidner@suse.cz
- Restored pkgconfigdir to keep compatibility.
- Remove .dep at make distclean.
* Tue May 31 2005 visnov@suse.cz
- rename XXPkgXX.pm to XXPkgXX2.pm to make skeleton work out of box
* Mon May 30 2005 mvidner@suse.cz
- Rewrote ycpdoc HTML output to xhtml+css.
* Mon May 23 2005 hmacht@suse.de
- ycp_puttext: added handling of *.glade source files (#65591),
  handle comments in texts to translate and write
  the "suspicious" changes to a diff file
* Wed May 18 2005 visnov@suse.cz
- merge back proofread skeleton
* Tue May 17 2005 mvidner@suse.cz
- Install pkgconfig file under /usr/share so that we can
  stay noarch. (#83201)
  Other yast packages can choose to do so too by setting
  CREATE_PKGCONFIG=noarch in configure.in.in
- Added automakefile fragment for ycpdoc.
* Wed May 11 2005 mvidner@suse.cz
- The package is no longer noarch because it contains pkgconfig files
  and these are in /usr/{lib,lib64}. (#83201, sbrabec).
* Thu May  5 2005 locilka@suse.cz
- Rewritten spellcheck script to check all lines of messages
- Added YaST2-dictionary support
- Added YaST2-dictionary text-file
* Tue May  3 2005 mvidner@suse.cz
- Added YCP mode for Emacs.
- 2.12.1
* Thu Apr 28 2005 mvidner@suse.cz
- Added a script to spellcheck pot files (locilka):
  use "make spellcheck" in $(top_srcdir).
- Added aminclude, a directory for automakefile fragments
  to be copied to $(top_srcdir). Then they can be used by "include"
  in Makefile.am. First user: pluglib-bindings.
* Wed Apr  6 2005 visnov@suse.cz
- added gettext-devel to NFB
- 2.12.0
* Fri Feb 18 2005 ke@suse.de
- Fix translation related intallation target (reported by Stefan
  Schubert).
- Calculate percent of translated messages (proposed by Jiri Suchomel).
* Wed Feb  9 2005 ke@suse.de
- Generate and install .po file statistics.
* Tue Feb  8 2005 mvidner@suse.cz
- Added po-stats to sum up translation file statistics (ke).
* Fri Jan 21 2005 mlazar@suse.cz
- dual CVS/Subversion support
- 2.11.7
* Thu Jan 13 2005 mvidner@suse.cz
- Dependency fixes:
  * Create the dependency file outside "." to prevent endless loops.
  * Added line oriented /* */ comment handling.
  * Feed only ybc files to the pattern rule, preventing the warning
  "Target Foo.pm does not match the target pattern."
- 2.11.6
* Wed Jan 12 2005 nashif@suse.de
- Updated testsuite and fixed ycpdoc to not add <pre> in xml output
- 2.11.5
* Wed Jan 12 2005 mvidner@suse.cz
- Added ycpmakedep to replace makedep.sh (#42675).
  It considers includes (even with -I, -M options).
- Updated stylesheets and stuff (nashif).
* Fri Jan  7 2005 arvin@suse.de
- adding default entities names in desktop files for doc team
* Thu Dec  2 2004 mvidner@suse.cz
- ycpdoc: Do not warn if the types differ only in whitespace
- docbook stylesheets (nashif):
  removed deprecated style parameter
  removed some options which cause processing to run slow
  improvements to html output
  added ycpdoc stylesheet
- ydoc2 (nashif): fixed adding properties from class files
- y2makeall (sh): added unmaintained "certify" module to exclude
  list
- 2.11.4
* Wed Nov 10 2004 mvidner@suse.cz
- use VERSION instead of PACKAGE_VERSION, thus allow make package
  after bumping VERSION again (arvin)
- check_ycp: Removed check_alternate_declarations, they have long
  been syntax errors.
- i18n (ke)
    detect language code and assign it to LL
    Y2TEXTDOMAIN is gone; check for 'po' subdir
    drop make-pox from checkpo
- y2makeall (sh)
    added pkg-bindings
    filtered out "is newer" ycpc warning upon byte-compiling
- Improved STYLESHEET_* so that they are found in the devtools
  prefix, not the current prefix.
- 2.11.3
* Fri Oct 29 2004 mvidner@suse.cz
- Added pkgconfig support.
- 2.11.2
* Tue Oct 26 2004 nashif@suse.de
- Updated docu stylesheets
- 2.11.1
* Tue Oct 26 2004 mvidner@suse.cz
- Create acinclude.m4 in Makefile.cvs instead of having a redundant
  copy in cvs.
- 2.11.0
* Tue Oct 26 2004 locilka@suse.cz
- Changed config-skeleton to use Message module
* Mon Oct 25 2004 visnov@suse.cz
- Removed Requires: yast2
* Sat Oct 23 2004 nashif@suse.de
-  Removed dependency on sgmltoo, sp
-  Added nfb for sgml-skel
* Sat Oct 23 2004 nashif@suse.de
- Add check for xsltproc, XML catalogs
- Added AC macro for docbook
- adapted macros for stylesheets
* Thu Oct 14 2004 jsrain@suse.cz
- added missing AC_SUBST(ystartupdir) to y2autoconf
- updated neededforbuild due to changed dependencies of docbook
- 2.11.0
* Thu Oct 14 2004 visnov@suse.de
- Update skeleton version numbers
* Mon Sep 27 2004 sh@suse.de
- V 2.10.10
- (adrian) fixed "find" for *.desktop in create-spec
- (adrian) fixed "clean" in create-spec (obsolete check)
* Mon Sep 27 2004 arvin@suse.de
- recoded some files to UTF-8 (bug #46179)
* Fri Sep 24 2004 arvin@suse.de
- fixed for packages with uppercase characters in their name
* Tue Sep 21 2004 nashif@suse.de
- Use xsl locally, not using http
* Fri Sep 17 2004 mvidner@suse.cz
- Recognize parameters passed by& reference (AsciiFile).
* Tue Sep 14 2004 mvidner@suse.cz
- Convertor from Relax NG for YaST to Relax NG Compact
- 2.10.6
* Mon Sep 13 2004 arvin@suse.de
- use option tar-ustar to allow "long" filenames in tar-balls
* Mon Sep 13 2004 nashif@suse.de
- ycpdoc: parameters in xml output are lists, every parameter
  description appears as an item
- added ycpdoc.xsl for generating docbook refentries from ycpdoc
  xml output
- added docbook stylesheets and and admin/navigation images
* Mon Sep  6 2004 mvidner@suse.cz
- ycpdoc: Allow zero space between type and identifier
  (list<string>a).
* Tue Aug 31 2004 sh@suse.de
- Added yast2-firstboot to all-packages
* Tue Aug 31 2004 lnussel@suse.de
- ycp_puttext: save log in $HOME by default; also search *.pm and
  * .cc files
* Mon Aug 30 2004 nashif@suse.de
- removed norootforbuild from skeleton, it is added by create-spec
* Fri Aug 20 2004 nashif@suse.de
- added schemadir macro
- added norootforbuild in skeleton spec file
- 2.10.3
* Thu Aug 12 2004 mvidner@suse.cz
- ycpdoc:
  Fixed parsing compound types.
  "define" is optional, return type is mandatory.
  Make . the default output directory.
  Report all files that are being written.
  XML: do not output empty map items
* Thu Jul 22 2004 visnov@suse.cz
- Fixed dependencies for agent skeleton C++ autodocs
* Thu May 27 2004 ke@suse.de
- On SLES9 do not cleanup PO files (disable cleanuppo.awk).
* Wed May 19 2004 sh@suse.de
- Add correct license to .spec file
- V 2.9.20
* Tue May 11 2004 mvidner@suse.cz
- Let "make pot" find __ (#40160).
- Updated skeleton .pm (#40160).
- Sort file names according to C to have comparable pot files.
- 2.9.19
* Wed Apr 14 2004 msvec@suse.cz
- dropped removal of buildroot from %%install
* Fri Apr  2 2004 mvidner@suse.cz
- 2.9.18
* Fri Apr  2 2004 sh@suse.de
- Changed default license to GPL
  Packages with YaST license now need a file YAST_LICENSE
  in their package toplevel directory to indicate that
* Mon Mar 29 2004 sh@suse.de
- Added summary output for y2makeall
* Fri Mar 19 2004 mvidner@suse.cz
- added AGENT_LIBADD so that agents work from standalone Perl
- 2.9.16
* Thu Mar 18 2004 arvin@suse.de
- don't include .deps directories in package (bug #36379)
* Mon Mar 15 2004 mvidner@suse.cz
- ycpdoc: handle function declarations
- pmdoc: process typeinfo
- y2makeall: make clean
- fixed AbortFunction in skeleton
- 2.9.14
* Thu Mar 11 2004 mvidner@suse.cz
- ycpdoc: really fixed the omission of double backquotes
* Wed Mar 10 2004 mvidner@suse.cz
- ycpdoc: handle angle-bracketed types
- y2makeall:
    recognize command failure from SIGINT
  - n: no sudo
  - p: prefix
- 2.9.13
* Mon Mar  8 2004 mvidner@suse.cz
- fixed 'make pot' when POTFILES is empty
* Fri Mar  5 2004 lnussel@suse.de
- add package y2pmsh
* Thu Mar  4 2004 lnussel@suse.de
- add package yast2-ipsec
* Tue Mar  2 2004 sh@suse.de
- Added support for translatable text ("make pot") in XML files:
  <textdomain>..</textdomain>
* Mon Mar  1 2004 jsrain@suse.de
- fixed ycpdoc to process correctly function definitions without
  double backquites
* Fri Feb 27 2004 mvidner@suse.cz
- y2tool is prefix aware
- XXPkgXX.pm must return 1;
- removed -Woverloaded-virtual, cerqtain libraries don't like it
- 2.9.12
* Tue Feb 10 2004 msvec@suse.cz
- added check-syntax target dependence to make package-local
* Mon Feb  9 2004 msvec@suse.cz
- drop setting of Y2DIR in common Makefile.am
- drop configdir substitution
- better check-syntax target
- 2.9.11
* Thu Feb  5 2004 msvec@suse.cz
- extract translations also from the Perl files
- skeleton improvements
- 2.9.10
* Fri Jan 30 2004 visnov@suse.cz
- use "install -p" for installing files to preserve modification
  time (fixes perl modules timestamps)
- 2.9.9
* Thu Jan 29 2004 mvidner@suse.cz
- create-spec: set DESTDIR also for "make check",
  (used by yast2-perl-bindings)
- 2.9.8
* Thu Jan 29 2004 kkaempf@suse.de
- test for expect prior to runtest, complain about missing
  dejagnu if runtest not found.
* Tue Jan 27 2004 mvidner@suse.cz
- y2autoconf, CXXFLAGS:
  removed useless -Wmissing-prototypes, added -Woverloaded-virtual
- freshdoc: process also core/autodocs
- 2.9.7
* Mon Jan 26 2004 msvec@suse.cz
- leave only *ybc in CLEANFILES
- 2.9.6
* Mon Jan 26 2004 msvec@suse.cz
- enabled testsuites
- 2.9.5
* Fri Jan 16 2004 msvec@suse.cz
- updates for the NI
- 2.9.4
* Mon Dec 15 2003 msvec@suse.cz
- use prefix wher possible to simplify relocation
- 2.9.3
* Wed Dec  3 2003 msvec@suse.cz
- added placeholder for common Makefile.am
- 2.9.2
* Fri Nov 28 2003 ma@suse.de
- builtindoc: allow comment end to contain more than one '*';
  e.g. '**/'
* Tue Nov 18 2003 mvidner@suse.cz
- Fixed a problem with escaped newlines in ydoxygen, really.
* Thu Nov 13 2003 mvidner@suse.cz
- ycpdoc can now parse the angle-bracket syntax list<string>, block<string>.
- Fixed a problem with escaped newlines in ydoxygen (eg. yast2-core)
- Switched the agent skeleton autodocs to doxygen
- Updated the template Doxyfile to hush warnings about obsolete options
* Thu Nov  6 2003 mvidner@suse.cz
- Added a doxygen wrapper
- Turned on norootforbuild in spec files
- 2.9.1
* Mon Oct  6 2003 sh@suse.de
- V 2.9.0
- Removed generated HTML doc from dist tarball
* Fri Sep 19 2003 sh@suse.de
- V 2.8.9
- Support for GPL license
- Moved YaST license to separate subdir
- New subdir for GPL
* Thu Aug 28 2003 sh@suse.de
- V 2.8.8
- Changed feedback address to http://www.suse.de/feedback
* Tue Aug 26 2003 lnussel@suse.de
- add package yast2-wlanipsecclient
* Wed Aug 20 2003 jsuchome@suse.de
- removed redundant "initialization dialog" (#28779) from skeleton
- 2.8.7
* Tue Aug 12 2003 visnov@suse.de
- merged in proofread texts into the config skeleton
* Fri Aug  1 2003 arvin@suse.de
- added support for handling desktop files
* Fri Aug  1 2003 mvidner@suse.cz
- ycpdoc: don't expose perl-internal hash ordering (fixes build).
- 2.8.5
* Wed Jul 30 2003 visnov@suse.de
- added translator comments for all skeleton messages
* Tue Jul 22 2003 mvidner@suse.cz
- check_ycp: obsolete functions are not checked inside strings.
* Wed Jul 16 2003 kkaempf@suse.de
- fix COPYRIGHT.spanish
* Mon Jul 14 2003 mvidner@suse.cz
- ycpdoc: do not document items commented out by "//";
  added a simple header for comments without an item
* Fri Jul 11 2003 mvidner@suse.cz
- check_ycp (check_imports): it's not an error to use Foo::
  in a file called Foo.ycp.
* Tue Jul  1 2003 msvec@suse.de
- again include cvsignore in skeletons
- 2.8.4
* Thu Jun 19 2003 mvidner@suse.cz
- check_ycp: check_imports does not look inside strings,
    fixed backslash handling in strings
* Tue Jun 17 2003 mvidner@suse.cz
- enable YCP testsuites again
- check_ycp: detect symbols from modules that are not imported
  (applied to the skeleton too)
- simplified files for trans spec (ke)
- ycp-mode.el: added new UI builtins (sh)
- 2.8.3
* Thu Jun 12 2003 jsrain@suse.de
- added packages yast2-dhcp-server, yast2-dns-server,
  yast2-tftp-server, removed yast2-printerdb
* Thu Jun 12 2003 arvin@suse.de
- added missing directories to file list
- even better name creation (msvec)
- check_ycp: a hack not to complain about Popup::ContinueCancel (mvidner)
* Fri Jun  6 2003 mvidner@suse.cz
- Hack: while yast2-core is broken, don't run ycp testsuites.
- create-new-package: generate a better Module_Name (msvec).
- 2.8.1
* Fri May 30 2003 mvidner@suse.cz
- check-tagversion: use cvs status -v to prevent errorneous
  pass of the check
  (cvs server: VERSION is no longer in the repository)
* Fri May 23 2003 arvin@suse.de
- don't pack .cvsignore of skeleton
* Fri Mar  7 2003 arvin@suse.de
- updated date in copyright files
* Thu Mar  6 2003 arvin@suse.de
- added configure test for perl xml writer (bug #24429)
* Fri Feb 21 2003 mvidner@suse.de
- ycpdoc:
  Make separate indices for global and local functions/variables.
  Fixed the "skip" state removal (Nothing would be parsed after
  a long define).
  Added a @deprecated tag (thanks to Stano Visnovsky)
* Mon Feb  3 2003 msvec@suse.cz
- generate pot file during make package and include it in tar.bz2
- 2.7.3
* Fri Jan 17 2003 arvin@suse.de
- added sanity check for make package (bug #21578)
* Thu Dec  5 2002 mvidner@suse.cz
- ycpdoc:
  Eliminated a false warning about an undocumented function (msvec)
  Handle qualified function names (UI::, Pkg::)
  Removed the "skip" parsing state.
- ycp-mode.el: added new UI builtins (sh)
- skeletons/config: better Back handling (msvec)
- skeletons/trans: remove locale dirs on deinstall, #20846 (ke)
- freshdoc: updated for 8.1
- 2.7.1
* Tue Oct 22 2002 mvidner@suse.cz
- Added testsuite for ycpdoc.
* Tue Oct 22 2002 msvec@suse.cz
- removed %%ifarch from the generated spec files <arvin>
- 2.7.0
* Fri Oct 11 2002 arvin@suse.de
- enhance create-spec on account of SLES.
* Mon Sep 16 2002 arvin@suse.de
- updated to latest cleanuppo.awk from ke
* Thu Sep 12 2002 ke@suse.de
- Update to version 2.6.16.
- ydoc/po-tools/cleanuppo.awk: Respect word bounderies; ignore
  obsolete entries.
* Wed Sep 11 2002 ke@suse.de
- Update to version 2.6.15.
- Enhance create-spec on account of UnitedLinux.
* Wed Sep 11 2002 ke@suse.de
- Update to version 2.6.14.
- Add ydoc/po-tools/cleanuppo.awk.
* Wed Sep 11 2002 ke@suse.de
- Update to version 2.6.13.
- devtools/admin/all-packages: add yast2-trans-ko and
  yast2-trans-zh_TW.
* Thu Sep  5 2002 arvin@suse.de
- added themedir definition for theme-able images
* Thu Sep  5 2002 ke@suse.de
- Update to version 2.6.11.
* Thu Sep  5 2002 ke@suse.de
- devtools/devtools/admin/all-packages: add yast2-trans-da.
* Wed Aug 28 2002 jsuchome@suse.cz
- provide/obsolete old translation packages
* Wed Aug 21 2002 arvin@suse.de
- run parseycp already for "make package-local"
- list of all packages updated
* Tue Jul 30 2002 mvidner@suse.cz
- fixed a perl-5.8.0 warning about ycpdoc
- removed remnants of ydoc
* Fri Jul 26 2002 arvin@suse.de
- fixed generation of plural forms of message texts
- generated toplevel Makefile.am aborts on empty textdomains
* Fri Jul 19 2002 arvin@suse.de
- reduced ydoc to a wrapper for kdoc
* Tue Jul  9 2002 msvec@suse.cz
- reworked config skeleton
- install skeletons to the correct dir
- 2.6.7
* Tue Jul  9 2002 arvin@suse.de
- changed call of xgettext (bug #16832)
- run y2autoconf and y2automake during build (of created packages)
* Mon Jul  8 2002 mvidner@suse.cz
- Provide/Obsolete ycpdoc and ydoc.
* Mon Jul  8 2002 arvin@suse.de
- added checks for expect and dejagnu (bug #16835)
- warn about unknown macros
* Wed Jul  3 2002 msvec@suse.cz
- use /usr/share
- 2.6.4
* Wed Jul  3 2002 ke@suse.de
- For trans modules use @localedir@ instead of @YAST2DIR@/locale.
- Simplify .mo file installation target.
- y2autoconf: add po/Makefile to output for "trans" packages.
* Fri Jun 21 2002 kkaempf@suse.de
- package merge with scrdoc, ycpdoc, and ydoc.
  2.6.3
* Mon Jun 10 2002 sh@suse.de
- V 2.6.2
* Mon Jun 10 2002 ke@suse.de
- Makefile templates for po/y2t_LL/po rewritten for 8.1.
- Make location of compendium file configurable (@YAST2-INIT-PO@ in
  y2autoconf).
* Thu Jun  6 2002 ke@suse.de
- y2autoconf: replace recode_po_file_to_utf with msgconv
- start to drop obsolete skeleton files (Y2TEXTDOMAIN, po/POTFILES,
  po/LINGUAS) and related checks
* Wed May 15 2002 arvin@suse.de
- unified @XX-AGENT@, @XX-LIB@ and @XX-PROG@ macros and merged
  to @XX-PROGRAM@ macros
- added @XX-QT-PROGRAM@ macors
- new skeletons
- substitute new directory paths
- better all-packages checking
- fixes for new autoconf/automake
- fixed Y2LOG substitution (C++ sources)
- 2.6.1
* Wed Apr  3 2002 msvec@suse.cz
- generate License field instead of Copyright
- update @BUILD-AGENT@ and @INSTALL-AGENT@
- added @HEADER-DEVEL@ for -devel subpackage
- mandatory all-packages check
- allow 2.6.x checkins
- 2.6.0
* Wed Feb 13 2002 sh@suse.de
- V 2.5.21
- For 8.0 branch only: Prevent checkin-stable with VERSION 2.6*
* Fri Jan 25 2002 sh@suse.de
- V 2.5.20
- New check upon "make checkin-stable": Package in "all-packages"?
* Thu Jan 17 2002 ke@suse.de
- v 2.5.19
- Install textdomain files without language identifier; reported
  by Petr Blahos and Andreas Schwab.
* Wed Jan 16 2002 arvin@suse.de
- v 2.5.18
- ensure that DOCDIR exists
* Tue Dec 18 2001 mvidner@suse.cz
- v 2.5.17
- Exclude backup~ files~ from skeleton.
* Tue Dec 18 2001 mvidner@suse.cz
- v 2.5.16
- Skeleton: fixed _auto client to return an empty map if canceled.
* Fri Dec  7 2001 kendy@suse.cz
- v 2.5.15
- Changed the handling of COPY* and README files: It is not needed
  to have them in the toplevel directories any more, they are
  copied from devtools.
- Removed COPY* and README files from the skeleton
- Use DOCDIR instead of YAST2DOC
- Updated documentation (y2autoconf and create-spec)
* Fri Dec  7 2001 sh@suse.de
- V 2.5.14
- Rearranged generated spec file due to ro's wishes
* Thu Nov 22 2001 kendy@suse.cz
- v 2.5.13
- bin/create-spec: macros for agents, libs and po.
- bin/y2autoconf: hopefully functional
- config skeleton was changed to use y2autoconf
* Thu Nov 22 2001 pblahos@suse.cz
- v 2.5.12
- skeleton fix: ..._write.ycp honours new Write function prototype
* Wed Nov 21 2001 pblahos@suse.cz
- v 2.5.11
- changed progress bar processing in skeleton/config::Read/Write
* Mon Nov 19 2001 kendy@suse.cz
- v 2.5.10
- bin/create-spec: fix: @YAST2DOC@, @YAST2INC@
- autogenerated documentation is a part of the tarball
- bin/y2autoconf: alpha version
* Wed Nov 14 2001 kendy@suse.cz
- v 2.5.9
- bin/create-spec: A tool for better generating of .specs
- Makefile.am.toplevel adapted to use it
- make-new-package renamed to create-new-package
- Config skeleton improvements:
  - meaningful helps in the config skeleton
  - spec.in new uses BuildRoot for building
* Mon Nov 12 2001 kendy@suse.cz
- v 2.5.8
- doc/skeletons/config: Autodocs for the config skeleton
- Config skeleton improvements:
  - XXpkgXX_auto.ycp
  - XXpkgXX_write.ycp
  - use of modules
  - progress in the time of Read() and Write()
  - use of Wizard_hw::
* Mon Nov 12 2001 ke@suse.de
- V 2.5.7
- admin/po/Makefile.am.center: fix install target.
- admin/po/Makefile.am.center: remove 'dist-hook'.
- admin/Makefile.am.toplevel: enable 'checkpo', but don't call
  'update-po'.
- admin/po/Makefile.am.center: add 'checkin'.
* Tue Nov  6 2001 kendy@suse.cz
- v 2.5.6
- bin/make-new-package: a version of make_new_module adapted
  and generalized for skeletons in devtools
- skeletons/Makefile.am: prepared for skeletons
- skeletons/config: alpha version of the skeleton for configuration
  packages, which uses a module for storing the configuration data.
* Mon Nov  5 2001 ke@suse.de
- V 2.5.5
- admin/po/Makefile.am.center: add dist-hook to check .po files.
- admin/po/Makefile.am.*: Split $(MODULE).pot target.
* Wed Oct 31 2001 ke@suse.de
- V 2.5.4
- admin/po/Makefile.am.center: Provide YAST2DIR_xgettext.
- Start to move variable from admin/po/Makefile.am.center to
  admin/po/Makefile.am.top and admin/po/Makefile.am.bottom to make
  it possible to distinguish between y2t_* and y2d_* packages.
* Mon Oct 29 2001 mvidner@suse.cz
- V 2.5.3
- checkin-stable: fix for tabs in the specfile
* Fri Oct 26 2001 sh@suse.de
- V 2.5.2
- Auto-generate po/Makefile.am as well
- Move "checkin-stable" out to separate script
* Tue Oct 16 2001 sh@suse.de
- V 2.5.1
- Automatically derive SUBDIRS if not explicitly set
* Tue Oct 16 2001 sh@suse.de
- added "sgmltool" to "neededforbuild"
* Fri Oct 12 2001 sh@suse.de
- Initial version
