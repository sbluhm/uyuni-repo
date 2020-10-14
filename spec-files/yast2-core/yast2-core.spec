#
# spec file for package yast2-core
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


# Optionally build with llvm-clang instead of gcc
# because we are interested in the warnings it gives.
%bcond_with clang

# Optionally treat C/C++ warnings as errors.
# It is off by default so that it will not block mass tests of new GCC
# but we want to enable it in a side repo
# to be able to fix newly detected problems relatively early.
%bcond_with werror

Name:           yast2-core
Version:        4.3.2
Release:        1.1
URL:            https://github.com/yast/yast-core

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2
Source1:	dummy.desktop

# obviously
BuildRequires:  boost-devel
%if %{with clang}
BuildRequires:  llvm-clang
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libtool
# we have a parser
BuildRequires:  bison
BuildRequires:  flex
# workaround for error when jemalloc is dlopened in ruby in old testsuite (bsc#1068883)
BuildRequires:  jemalloc-devel
# incompatible change, parser.h -> parser.hh
BuildRequires:  automake >= 1.12
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-Pod-Html
# needed for all yast packages
BuildRequires:  yast2-devtools >= 3.1.10
# testsuite
BuildRequires:  dejagnu
%if 0%{?rhel} >= 8
BuildRequires:  langpacks-cs
%endif

Summary:        YaST2 - Core Libraries
License:        GPL-2.0-or-later
Group:          System/YaST
Requires:       perl = %{perl_version}

%description
This package contains the scanner, parser, and interpreter runtime
library for the YCP scripting language used in YaST2.

%package devel
Requires:       yast2-core = %version

Summary:        YaST2 - Core Libraries
Group:          Development/Libraries
Provides:       liby2util-devel = 2.16.1
Obsoletes:      liby2util-devel < 2.16.1
Requires:       glibc-devel
Requires:       libstdc++-devel

%description devel
This package contains include and documentation files for developing
applications using the YaST2 YCP interpreter.

%prep
%setup -n %{name}-%{version}

%build
%ifarch %arm
%if 0%{?qemu_user_space_build}
# disable autodoc building on qemu-arm only
sed -i SUBDIRS -e 's/autodocs//'
%endif
%endif

export SUSE_ASNEEDED=0 # disable --as-needed until this package is fixed

%if %{with werror}
export   CFLAGS="${RPM_OPT_FLAGS} -Werror"
export CXXFLAGS="${RPM_OPT_FLAGS} -Werror"
%endif

%if %{with clang}
export CC=clang CXX=clang++

# warning/error: argument unused during compilation
CFLAGS="${CFLAGS/-grecord-gcc-switches/}"
CXXFLAGS="${CXXFLAGS/-grecord-gcc-switches/}"
%endif

%yast_build

%install
mkdir -p "$RPM_BUILD_ROOT"/usr/share/applications/YaST2
cp %{SOURCE1} "$RPM_BUILD_ROOT"/usr/share/applications/YaST2
%yast_install

mkdir -p "$RPM_BUILD_ROOT"%{yast_logdir}

%if 0%{?suse_version}
%perl_process_packlist
%else
mv "$RPM_BUILD_ROOT"/usr/share/doc/packages/yast2-core "$RPM_BUILD_ROOT"%{_docdir}
rm "$RPM_BUILD_ROOT"/usr/lib64/perl5/perllocal.pod
%endif

%post
/sbin/ldconfig
# bnc#485992, since oS 11.2
C=blacklist
if test -f /etc/modprobe.d/$C; then
     mv -f /etc/modprobe.d/$C /etc/modprobe.d/50-$C.conf
fi

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)

%dir %{_libdir}/YaST2
%if "%_lib" == "lib64"
%dir /usr/lib/YaST2
%endif
%dir /usr/share/YaST2

%dir %attr(0700,root,root) %{yast_logdir}
%dir %{yast_ybindir}
%dir %{yast_plugindir}
%dir %{yast_scrconfdir}
%dir %{yast_execcompdir}/servers_non_y2

/usr/bin/ycpc
%{_libdir}/lib*.so.*
%{yast_ybindir}/y2base
%{yast_ybindir}/startshell
%{yast_ybindir}/tty_wrapper
%{yast_ybindir}/md_autorun
%{yast_ybindir}/elf-arch
%{yast_plugindir}/lib*.so.*
%{yast_scrconfdir}/*.scr
%{yast_execcompdir}/servers_non_y2/ag_*
# perl part (stdio agents)
# *: regular build compresses them, debug does not
%{_mandir}/man3/ycp.3pm*
%{_mandir}/man3/YaST::SCRAgent.3pm*
%{perl_vendorlib}/ycp.pm
%dir %{perl_vendorlib}/YaST
%{perl_vendorlib}/YaST/SCRAgent.pm

%if 0%{?suse_version} == 0 || 0%{?suse_version} <= 1130
#  .packlist
%{perl_vendorarch}/auto/ycp
#/var/adm/perl-modules/%name
%endif

%files devel
%defattr(-,root,root)
%{yast_ybindir}/ybcdump
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{yast_plugindir}/lib*.so
%{yast_plugindir}/lib*.la
%{yast_includedir}
%{_libdir}/pkgconfig/yast2-core.pc
%doc %{yast_docdir}
%doc %{_datadir}/doc/yastdoc
%license COPYING
%{yast_ydatadir}/devtools/bin/generateYCPWrappers
/usr/share/applications/YaST2/dummy.desktop

%changelog
* Fri Sep 18 2020 Martin Vidner <mvidner@suse.com>
- Avoid 'Construct not supported' on UnmountAgent (bsc#1176594)
- 4.3.2
* Fri Jun 19 2020 Martin Vidner <mvidner@suse.com>
- Save memory by SCR.UnmountAgent telling other-process agents
  to terminate (bsc#1172139)
- 4.3.1
* Tue May 12 2020 Josef Reidinger <jreidinger@suse.com>
- Fixed building with new bison 3.6 (bsc#1171505)
- 4.3.0
* Fri Nov  2 2018 lslezak@suse.cz
- Fixed Clang warnings (unused variables)
* Tue Oct 16 2018 schubi@suse.de
- Added license file to spec.
* Wed Oct  3 2018 lslezak@suse.cz
- Use an exclusive lock when rotating the YaST logs to avoid race
  conditions when several YaST processes run in paralell
  (related to bsc#1094875)
- 4.1.0
* Fri Sep 28 2018 schubi@suse.de
- Reduced risk of race condition between getenv and setenv while
  logging (bsc#1103076)
- 4.0.4
* Wed Aug 22 2018 schubi@suse.de
- Switched license in spec file from SPDX2 to SPDX3 format.
* Thu Jul 19 2018 aschnell@suse.com
- fixed detection of aarch64 during update by recognizing aarch64
  in elf-arch (bsc#1099325)
- recognise RISC-V in elf-arch
- 4.0.3
* Tue Feb  6 2018 mvidner@suse.com
- glibc-2.27 compatibility: Removed an overly specific test case
  for certain localized numbers (bsc#1079630)
- 4.0.2
* Tue Nov 28 2017 jreidinger@suse.com
- add jemalloc dependency for y2base which is used only in old
  testsuite and that workarounds problem with dynamic dlopening
  of jemalloc in ruby (bsc#1068883)
- 4.0.1
* Tue Oct 10 2017 mvidner@suse.com
- Fixed newly uncovered warnings: Wterminate, Wint-in-bool-context,
  sys/sysmacros (bsc#982942, bsc#434048).
- 4.0.0
* Wed Jan  4 2017 jreidinger@suse.com
- Dropped the YCP debugger in yast2-core-debugger not to confuse
  people who want to use the Byebug based Ruby debugger
  (bsc#1018038)
- 3.2.2
* Tue Jan  3 2017 jreidinger@suse.com
- Allow more detailed error specification when loading namespace
  to component system failed (bsc#932331)
- 3.2.1
* Mon Nov  7 2016 jreidinger@suse.com
- ag_anyangent: Do not fail the parse when an Optional syntax meets
  EOF, e.g. for a fstab without a trailing newline (bsc#429326#c11)
- 3.2.0
* Tue Sep 20 2016 jreidinger@suse.com
- disable doc generation (FATE#320356)
- remove unnecessary build dependency to speed up build
  (bsc#999203)
- 3.1.24
* Thu Jun  2 2016 mvidner@suse.com
- Optionally build with Clang instead of GCC (via bcond_with clang)
- Fixed most of Clang warnings (bsc#982942)
- 3.1.23
* Thu Mar  3 2016 gs@suse.de
- Add missing newline to error messages (bsc#969236)
- 3.1.22
* Tue Feb  2 2016 mvidner@suse.com
- Treat C/C++ warnings as errors but only via bcond_with werror.
- 3.1.21
* Tue Feb  2 2016 mvidner@suse.com
- Treat C/C++ warnings as errors.
- 3.1.20
* Tue Jan 19 2016 jreidinger@suse.com
- ag_ini: when multifile list contain glob, evaluate it in correct
  root. (bnc#962566)
- 3.1.19
* Tue Oct  6 2015 mvidner@suse.com
- In the signal handler, log the sender PID, and if present,
  run /usr/lib/YaST2/bin/signal-postmortem (bsc#935686).
- 3.1.18
* Wed May 13 2015 besser82@fedoraproject.org
- Fix more compilation warnings.
* Mon May 11 2015 mvidner@suse.com
- Fixed compilation warnings.
* Mon Mar 30 2015 jreidinger@suse.com
- Fix YCP symbol comparison with GCC 5 (thanks schubi for
  performance measurement and mvidner for review) (boo#914255)
- 3.1.17
* Tue Mar  3 2015 mvidner@suse.com
- Fixed compilation (but not tests) with GCC 5 (boo#914255).
- 3.1.16
* Thu Jan 22 2015 lslezak@suse.cz
- skip empty environment variables when activating the locale
  settings, fixes inconsistent locale setting when started
  via "kdesu" with unchecked "Remember password" option
  (boo#914081)
- 3.1.15
* Tue Nov 25 2014 mvidner@suse.com
- ag_any: respect target root also when the file
  does not exist in the original root (boo#903747).
  If applied at installation time as a DUD, it fixes
  "Internal error... in SaveModulesToLoad" during
  an upgrade to oS 13.2.
- 3.1.14
* Fri Oct 24 2014 lslezak@suse.cz
- yast2-core-devel: removed obsolete dependencies (flex, sysfsutils
  and hwinfo-devel), "ycp/Scanner.h" include file made private
  (not installed anymore)
- 3.1.13
* Mon Oct 20 2014 lslezak@suse.cz
- Travis support: added .travis.yml, portability: added crypt vs
  xcrypt detection, fixed order at base/src/Makefile.am
* Wed Oct  8 2014 mvidner@suse.com
- Fixed searching for programs in Y2DIR
  (gh#yast/yast-ruby-bindings#107)
- 3.1.12
* Wed Oct  8 2014 mvidner@suse.com
- Allow SCR.Read(.target.yast2, ...) on chroots (bnc#891053).
* Mon Sep  8 2014 mvidner@suse.com
- Enable buffering for parsing agent output (bnc#854809).
- 3.1.11
* Tue Aug 26 2014 mvidner@suse.com
- Fixed another batch of compilation warnings.
- 3.1.10
* Mon Aug 11 2014 mvidner@suse.com
- agent-any: stub "df" for testing.
- 3.1.9
* Fri Aug  8 2014 mvidner@suse.com
- Pass SCR root path to stdio agents (bnc#879365).
- If aborting on a SCRAgent::targetPath assertion, log it
  (bnc#891053).
- Fixed obvious compilation warnings.
- 3.1.8
* Tue May  6 2014 mvidner@suse.com
- Do not mention YCP in signal handler (by tcech)
- 3.1.7
* Mon Mar 17 2014 jreidinger@suse.com
- do not prefer executable programs over builtin components
- 3.1.6
* Fri Dec 13 2013 guillaume@opensuse.org
- Fix ARM build:
  * disable autodoc on qemu-arm only instead of all ARM builds
  * Update file list to sed to disable autodoc
* Fri Nov  8 2013 jreidinger@suse.com
- removed obsolete .target.control.printer_reset, .target.smbmount,
  .target.kill ( use .process.kill )
- 3.1.5
* Mon Nov  4 2013 jreidinger@suse.com
- remove remote libraries support on installed system. It requires
  yast2-core on installed system which forbits goal for SLE12 to
  not have yast on target system. The last piece that use it was
  adapted since perl-Bootloader-0.800 .
- 3.1.4
* Wed Oct 23 2013 lslezak@suse.cz
- system-agent: handle chroot at more places
* Mon Oct 21 2013 lslezak@suse.cz
- generateYCPWrappers: check also for YCPNull to avoid segfault
  when a parameter is missing (bnc#846467)
* Fri Oct 18 2013 jreidinger@suse.com
- Do not delete agent outside of component in WFM otherwise
  installation segfault
* Thu Oct 17 2013 jreidinger@suse.com
- chdir("/") after chroot otherwise commands fail with unreachable
  location after `cd ~`
* Tue Oct 15 2013 jreidinger@suse.com
- Dropped documentation generated by makebuildindocs, not include
  in yast2-devtools. Parts of it are obsolete anyway (YCP, WFM),
  ag_process and ag_system will get new tools.
- 3.1.3
* Mon Oct 14 2013 jreidinger@suse.com
- minimal chroot: fixed System:: to actually chroot; hopefully
  fixes bootloader setup at installation
* Wed Oct  2 2013 jreidinger@suse.com
- Adapt to incompatible changes in bison 3.0
- 3.1.2
* Tue Oct  1 2013 jreidinger@suse.com
- port from opensuse 13.1: fixed a segfault at the end of 'scr'
  program used during the installation, leading to /core file
  (BNC#841623)
- 3.1.1
* Wed Sep 25 2013 jreidinger@suse.com
- respect target root in: ag_any(for processes), system_agent
* Wed Sep 18 2013 lslezak@suse.cz
- do not use *.spec.in template, use *.spec file with RPM macros
  instead
- 3.1.0
* Wed Sep 11 2013 jreidinger@suse.com
- respect target root in: ag_any, ag_ini, ag_modules, ag_resolver
* Wed Sep  4 2013 mvidner@suse.com
- Avoid automake warning:
  'INCLUDES' is the old name for 'AM_CPPFLAGS'
* Tue Sep  3 2013 jreidinger@suse.com
- libscr: added "root" attribute to SCRAgent (FATE#314695). Agents
  must be adapted to respect it instead of relying on chroot(2)
  having been run.
* Wed Aug  7 2013 dmajda@suse.cz
- Do not lose comments before negative numbers in YCP parser
  (gh#yast/ycp-killer#617).
- 3.0.1
* Tue Jul 30 2013 yast-devel@opensuse.org
- version 3.0.0
* Tue Jul 16 2013 mvidner@suse.com
- XML: distinguish <call result="unused" ...> so that calls
  involving parameters passed by reference have a less ugly Ruby
  translation.
- XML: added forgotten comment attributes to <locale>
  (gh#yast/yast-core#39)
- 2.24.12
* Sun Jul 14 2013 mvidner@suse.com
- Adapt to move of crypt_gensalt to libowcrypt (FATE#314945).
- 2.24.11
* Fri Jul 12 2013 mvidner@suse.com
- factored out some common code in DejaGnu tests
- 2.24.10
* Thu Jul 11 2013 jreidinger@suse.com
- Fix exporting comments in list elements (gh#yast/yast-core#36).
- Fix exporting comments for function calls.
- Fix printing paths containing UTF8 (gh#yast/yast-ruby-bindings#64).
- Temporary disable tests that fails non-detereminic.
- 2.24.9
* Thu Jul 11 2013 mvidner@suse.com
- Fixed tests that would always succeed on oS-12.3, with
  "WARNING: could not find 'runtest'".
- Ignore the language bindings in all tests.
* Tue Jul  9 2013 jreidinger@suse.com
- fix segfault during installation
- 2.24.8
* Tue Jul  9 2013 jreidinger@suse.com
- Fix missing import in exported xml (gh#yast/y2r#41)
- Fix exporting comments for methods without parameters
  (gh#yast/yast-core#29)
- 2.24.7
* Thu Jul  4 2013 jreidinger@suse.com
- Prevent invalid XML by filtering out vertical tab and form-feed in
  xml output gh#yast/yast-core#25
- Fixed "Non constant value in case statement" parse error for
  `case -1:` with enabled comments parsing
- 2.24.6
* Fri Jun 28 2013 mvidner@suse.com
- enabled ignoring language bindings (yast2-ruby-bindings,
  yast2-perl-bindings, yast2-python-bindings) by setting the
  environment variable Y2DISABLELANGUAGEPLUGINS
  (gh#yast/yast-core#20)
- 2.24.5
* Thu Jun 27 2013 jreidinger@suse.com
- Allow parsing and exporting comments and whitespaces to XML if
  Y2PARSECOMMENTS is set
- 2.24.4
* Wed Jun 26 2013 jreidinger@suse.com
- YCP parser: fixed an endless loop for EOF in a string
  (gh#yast/yast-core#21)
- 2.24.3
* Fri Jun 21 2013 lslezak@suse.cz
- y2base: handle interleaved -I and -M options, as used by
  Makefiles of rubified modules.
- 2.24.2
* Fri Jun 21 2013 mvidner@suse.com
- re-enabled tests of ag_background
* Fri Jun 21 2013 jreidinger@suse.com
- fixed the apparently harmless segfault when YaST finishing.
- 2.24.1
* Mon Jun 10 2013 lslezak@suse.cz
- fixed YCP debugger client to make it run
- 2.24.0
* Fri Jun  7 2013 jreidinger@suse.com
- made SymbolEntry::value, setValue virtual (ABI change)
- added Y2WFMComponent::SetArgs, needed for non-YCP clients
- various fixes in handling YCP System::* calls
- do not strictly check types of arguments for System remote calls
- fixed parser annnd all serializers to use C locale for float
- fixed some memory leaks
- various fixes to the XML serialization of YCP
- Fixed function type matching to be contravariant for arguments
  (BNC#825263) (return type has always been covariant, correctly)
  Interface expected to handle "any" argument will no longer accept
  implementations handling only a specific subtype. Conversely,
  interfaces expected to handle a "string" will also accept
  implementation handling "any".
  Affects the "is" builtin; breaks *-bindings relying on the bug.
* Mon Oct  8 2012 mvidner@suse.cz
- Clarified how to return lists and maps from Perl (bnc#783846).
- 2.23.6
* Wed Jul 11 2012 mvidner@suse.cz
- automake incompatibility: require 1.12, to produce parser.hh
- agent-ini: if we cannot format a string, fail loudly (bnc#763386#c10)
* Wed Jul 11 2012 fehr@suse.de
- 2.23.5
- added builtin list::reverse for YCP list
* Fri Jun 22 2012 aschnell@suse.de
- allow C++ log functions to be used in namespaces
- 2.23.4
* Tue Jun 19 2012 mfilka@suse.com
- increase version
- added testcases
- handling of escape sequences when quoting
- enable quoting only for sysconfig files
- 2.23.3
* Mon Jun 18 2012 mfilka@suse.com
- (un)quoting rewriten to C++ due to bnc#765519
- 2.23.2
* Mon Jun 18 2012 aschnell@suse.de
- fixed function name conflict in agent-ini (bnc#765519)
- 2.23.2
* Wed Jun 13 2012 aschnell@suse.de
- fixed UTF-8 handling of several string builtins (bnc#755414)
* Tue Jun 12 2012 aschnell@suse.de
- removed blocxx usage (fate #313242)
- improved efficiency of logging functions
- 2.23.1
* Fri May  4 2012 mfilka@suse.com
- added support for shell like (un)quoting and (un)escaping of values
- 2.23.0
* Mon Mar 19 2012 aschnell@suse.de
- fixed for gcc 4.7
* Fri Mar 16 2012 aschnell@suse.de
- do not use xcrypt (removes bigcrypt) (fate #312617)
- 2.22.5
* Wed Feb 22 2012 aschnell@suse.de
- added tointeger builtin with explicite base qualification
- 2.22.4
* Fri Feb  3 2012 mvidner@suse.cz
- ini-agent: only change permissions of new files (bnc#743355)
- 2.22.3
* Thu Jan  5 2012 mvidner@suse.cz
- Relicensed agent-process from GPL-2.0 to GPL-2.0+
  to match the rest of the package (bnc#728950).
- 2.22.2
* Thu Jan  5 2012 mvidner@suse.cz
- ini-agent: added Write(.section_private.SECTION, BOOLEAN)
  (bnc#713661, CVE-2011-3177)
- system agent: added  Write(.target.string, [filename, mode], content)
- 2.22.1
* Fri Dec  2 2011 lslezak@suse.cz
- process-agent - fixed testuite (removed potential race condition)
- 2.22.0
* Fri Nov 25 2011 mvidner@suse.cz
- ini-agent: Fixed a test failure "wrong stderr for nonex"
  (bnc#706705#c16)
- process-agent: a badly designed test is less likely to fail now
- 2.21.8
* Fri Nov 25 2011 coolo@suse.com
- add libtool as buildrequire to avoid implicit dependency
* Tue Oct  4 2011 mvidner@suse.cz
- build fix for ARM (bnc#721846).
- 2.21.7
* Thu Aug 18 2011 mvidner@suse.cz
- change blowfish id from 2a to 2y (bnc#700876 bnc#706705 CVE-2011-2483)
  (thanks to Ludwig Nussel)
- 2.21.6
* Fri Aug  5 2011 mvidner@suse.cz
- YCP Debugger added, by Stano Visnovsky.
- 2.21.5
* Fri Jun 17 2011 jsuchome@suse.cz
- when if-condition evaluates to nil, use false instead (bnc#687236)
- 2.21.4
* Thu Jun  2 2011 aschnell@suse.de
- added missing include statements
- 2.21.3
* Fri May 27 2011 mvidner@suse.cz
- Fixed a garbled unbreakable space used as a thousand separator (bnc#683881).
- 2.21.2
* Fri May 27 2011 mvidner@suse.cz
- Don't crash when adding to a nil list (bnc#694520).
- A nil (type cast failure) in a list literal will not make the whole
  list nil (bnc#694520).
- 2.21.1
* Thu Mar 31 2011 aschnell@suse.de
- added sha256 and sha516 password encryption (fate #309705)
- 2.21.0
* Tue Mar 15 2011 coolo@novell.com
- fix build with gcc 4.6
* Mon Jan  3 2011 lslezak@suse.cz
- fixed packaging in openSUSE-11.4 (perl files)
- 2.20.0
* Tue Aug 10 2010 mvidner@suse.cz
- Enable input buffering for YCP include files (bnc#629882).
- 2.19.3
* Thu Mar 11 2010 mvidner@suse.cz
- Fixed the regexpsub algorithm not to loop endlessly
  if the source string contains \1 (bnc#552914).
- 2.19.2
* Tue Mar  9 2010 mvidner@suse.cz
- Fixed an ia64 crash in test_thread_log (a test case for bnc#565918).
* Mon Feb  1 2010 mvidner@suse.cz
- Fixed a crash in LogTail by adding a mutex to the shared variable
  (bnc#565918).
- Re-enabled parts of liby2util-r testsuite.
- 2.19.1
* Fri Dec 18 2009 aschnell@suse.de
- allow Y2DIR to be a list of paths separated by ":"
- 2.19.0
* Fri Aug 14 2009 lslezak@suse.cz
- don't generate autodocs on ARM (doesn't work in qemu-arm)
  (by jansimon.moeller@opensuse.org)
- 2.18.19
* Tue Aug 11 2009 mvidner@suse.cz
- ycp.pm: convert wide strings to byte strings,
  to silence a warning when handling parsed XML (bnc#512536).
- /var/log/YaST2/signal: do not make it executable
- 2.18.18
* Mon Aug  3 2009 lslezak@suse.cz
- the DBus code has been moved to separate packages
  (yast2-dbus-client and yast2-dbus-server) (bnc#431208)
- 2.18.17
* Fri Jul 10 2009 mvidner@suse.cz
- Return DBus errors in most cases that used to y2error only (bnc#520616).
- In BSV types, "" again means "string" (broken in previous version).
- Log also the user when reporting a PolKit check result.
- o.o.Y.modules.ModuleManager.Import fixed to return false on failure.
- 2.18.16
* Thu Jul  2 2009 mvidner@suse.cz
- Enhanced DBus -> YCP value conversion by considering
  also the expected YCP type.
  Otherwise it is impossible to tell whether an empty array
  should become an empty map or an empty list (bnc#516492).
- Removed the dependency on dbus-1-x11
  by calling dbus-daemon directly without dbus-launch.
- 2.18.15
* Fri Jun 26 2009 mvidner@suse.cz
- yast_modules_dbus_server: return org.freedesktop.DBus.Error.UnknownMethod
  for unknown methods
- Disable --as-needed until this package is fixed.
* Fri Jun 19 2009 mvidner@suse.cz
- float::tolstring fixed to use the fixed notation
- 2.18.14
* Thu Jun 18 2009 lslezak@suse.cz
- DBus service - fixed returning "any" values (bnc#513503),
  return correct signatures in DBus introspection data, return the
  values according to it (bnc#513571), added basic testuite
* Wed Jun 17 2009 mvidner@suse.cz
- DBusServerBase: exit properly if the connection got closed
* Mon Jun 15 2009 lslezak@suse.cz
- DBus service - fixed returning of nested values (e.g. list<map>),
  removed extra check for map (bnc#512569)
- 2.18.13
* Tue Jun  9 2009 mvidner@suse.cz
- Added 'string float::tolstring(float f, integer precision)' using the
  current locale decimal separator (bnc#460094).
- Fixed makefiles to work with "install" calls changed via
  automake-1.11.
- Fixed tons of warnings by explicitly initializing all members of
  declaration_t.
- 2.18.12
* Mon Jun  1 2009 mvidner@suse.cz
- Fixed char* constness for glibc-2.10.
- 2.18.11
* Thu May 14 2009 lslezak@suse.cz
- DBus service - fixed DBus object to Yast name space conversion
  in autoimport code ('/' -> '::'), replace all occurrences
* Thu May  7 2009 mvidner@suse.cz
- Y2ProgramComponent: close fds>2 before exec
  to make external agents more robust (bnc#501758).
* Mon May  4 2009 lslezak@suse.cz
- SCR DBus service - fixed DBus object registration, fixed creating
  the PolicyKit action ID
- 2.18.10
* Mon Apr 27 2009 mvidner@suse.cz
- Resurrected logging in the signal handler, into
  /var/log/YaST2/signal (or ./y2signal.log) (bnc#493152#c33).
- Y2StdioComponent: exit only at EOF, not on parse error (bnc#498407).
- 2.18.9
* Fri Apr 24 2009 mvidner@suse.cz
- agent-ini: do not truncate strings longer than 2048
  while writing (bnc#492859)
- 2.18.8
* Fri Apr 24 2009 lslezak@suse.cz
- DBus service - better handle "::" separators in name space
  string - replace it by "/" in DBus object path and "." in
  PolicyKit action ID string
- 2.18.7
* Tue Apr 21 2009 coolo@suse.de
- avoid y2log in both signal handler and forked children (bnc#493152)
* Tue Apr 21 2009 coolo@suse.de
- another hot fix
* Mon Apr 20 2009 coolo@suse.de
- trying hot fix for bnc#493152
* Mon Apr 20 2009 jreidinger@suse.cz
- add builtin list::swap for list
* Fri Apr 17 2009 juhliarik@suse.cz
- added fix for problem with adding nil to list (bnc#216177)
* Wed Apr 15 2009 mvidner@suse.cz
- DBus service:
  * handle variants in replies
  * don't crash on unsupported types
  * fixed ModuleManager action IDs
  * more examples
* Fri Apr 10 2009 lslezak@suse.cz
- Merged the Yast DBus service from /tmp/lslezak/core branch, the
  service exports Yast name spaces on DBus. The SCR service has
  been refactored - the common parts have been moved to liby2dbus.
- Removed oboleted YCPMapIterators
- 2.18.6
* Mon Apr  6 2009 mvidner@suse.cz
- Use /etc/modprobe.d/50-yast.conf instead of /etc/modprobe.conf
  (bnc#485992).
- Move /etc/modprobe.d/blacklist on update (bnc#485992).
- Dropped ag_xauth (.xauth.key), superseded since 2005 by
  $XAUTHLOCALHOSTNAME (bnc#482223).
- 2.18.5
* Thu Mar 26 2009 lslezak@suse.cz
- .modprobe_blacklist agent: use /etc/modprobe.d/50-blacklist.conf
  file instead of deprecated /etc/modprobe.d/blacklist (bnc#485992)
* Fri Mar  6 2009 mvidner@suse.cz
- ag_background: re-disabled the testsuite, silly me.
- 2.18.4
* Fri Mar  6 2009 lslezak@suse.cz
- put backtrace begin and end markers to y2log when e.g.
  y2error(-1, ...) is called
* Fri Mar  6 2009 mvidner@suse.cz
- ag_background: re-enabled the testsuite (bnc#470645#c11),
  with some expect magic (~bnc#475551)
* Wed Feb 25 2009 mvidner@suse.cz
- Fixed tty_wrapper losing output: stdio was interrupted by SIGCHLD (bnc#470645).
* Sun Feb  1 2009 mvidner@suse.cz
- dbus: fixed timeout handling to reduce latency (kkaempf)
  http://lists.opensuse.org/yast-devel/2009-02/msg00004.html
- dbus: code cleanup (kkaempf)
- dbus: fixed resource leaks (aschnell, lslezak)
* Thu Jan 29 2009 aschnell@suse.de
- added dbus client agent (required for bnc #464453)
- 2.18.3
* Mon Jan 26 2009 mvidner@suse.cz
- Fixed the D-Bus access policy (bnc#468390, CVE-2008-4311).
- 2.18.2
* Thu Jan  8 2009 aschnell@suse.de
- added namespace multiset with 1. some list function, 2. some new
  functions and 3. extended testsuite
- 2.18.1
* Wed Jan  7 2009 aschnell@suse.de
- improved YCPList and YCPMap iterators
* Mon Jan  5 2009 visnov@suse.cz
- match WFM component name and component creator instance
- improve main page for doxygen
* Mon Dec 22 2008 mvidner@suse.cz
- Reverted r50800 which, in an attempt to fix another bug, encoded to
  UTF-8 once too many, breaking i18n going thru Perl agents (bnc#448217).
* Sat Dec 20 2008 aschnell@suse.de
- added tosymbol builtin (bnc #192389)
- added isempty builtin for string, list and map
- 2.18.0
* Thu Dec 11 2008 lslezak@suse.cz
- tty_wrapper - fixed a deadlock in tty setting (set the terminal
  properties _before_ starting the subprocess) (bnc#458025)
- 2.17.25
* Tue Dec  9 2008 lslezak@suse.cz
- SCR DBus service - check for the global permissions at first
  (all method parameters are allowed) then for specific ones,
  added .policy file with the default values (bnc#449794)
- 2.17.24
* Thu Nov 27 2008 lslezak@suse.cz
- tty_wrapper - disable LF to CRLF translation on the stdout stream
  (bnc#444228)
- 2.17.23
* Wed Nov 26 2008 visnov@suse.cz
- added lsubstring builtin (bnc#446996)
- 2.17.22
* Sun Nov  9 2008 lslezak@suse.cz
- added 'tty_wrapper' binary to start a yast module in commandline
  mode without a tty device (bnc#444228)
- 2.17.21
* Mon Nov  3 2008 lslezak@suse.cz
- fixed testing of the result of polkit_caller_new_from_dbus_name()
  call which sometime sets the error object even when there is no
  real error (bnc#439150)
- 2.17.20
* Fri Oct 24 2008 visnov@suse.cz
- Also print diff when agent-process testsuite fails
- 2.17.19
* Tue Oct 14 2008 mvidner@suse.cz
- Avoid YCPNull reaching SCR agents to prevent crashes (bnc#406138).
- Allow make check before make install again, after libycpvalues API
  changed in 2.17.15.
- 2.17.18
* Tue Oct 14 2008 lslezak@suse.cz
- use atomic type sig_atomic_t in signal handlers (bnc#434509)
* Sat Oct 11 2008 mvidner@suse.cz
- Handle EINTR in YCP scanner. Makes possible to toggle
  debugging via SIGUSR1 to 'y2base stdio scr' (bnc#434253).
- 2.17.17
* Tue Oct  7 2008 visnov@suse.cz
- change remove builtin behavior to saner one (bnc #396697)
- more documentation updates
- 2.17.16
* Mon Sep 29 2008 visnov@suse.cz
- YCP values overview page added to docs
* Fri Sep 26 2008 visnov@suse.cz
- new builtins: list::difference, list::symmetric_difference,
  list::intersection, list::union (aschnell, bnc #58844)
- 2.17.15
* Fri Sep 26 2008 visnov@suse.cz
- allow clients to return exit code (bnc #350740)
- clean up documentation in liby2
- 2.17.14
* Thu Sep 25 2008 visnov@suse.cz
- support SCR::RegisterAgent and SCR::UnregisterAgent in chroot
  (bnc #425472)
- 2.17.13
* Wed Sep 17 2008 visnov@suse.cz
- Warn to log if using non-standard place for loading modules
- 2.17.12
* Tue Sep  9 2008 visnov@suse.cz
- Added y2useritem and y2usernote builtins for user-level
  action log (Fate #100386)
* Tue Sep  9 2008 locilka@suse.cz
- Adjusted STDOUT in ycp.pm to use 'utf8'.
* Fri Sep  5 2008 locilka@suse.cz
- Added WFM::ClientExists function (needed for installation).
- 2.17.10
* Wed Aug 27 2008 locilka@suse.cz
- Enabled getenv builtin.
- 2.17.9
* Wed Aug 13 2008 aschnell@suse.de
- added tohexstring builtin with width parameter
- 2.17.8
* Fri Aug  8 2008 locilka@suse.cz
- Re-added support to build libycp documentation in separate files
  additionally to combined.xml (needed for overall documentation).
* Wed Jul 30 2008 mvidner@suse.cz
- Moved documentation around and adjusted it to conform with
  http://en.opensuse.org/YaST/yastdoc
- 2.17.7
* Fri Jul 25 2008 aschnell@suse.de
- fixed requires for yast2-core-devel
- 2.17.6
* Thu Jul 24 2008 mvidner@suse.cz
- Better error message when an agent dies with errors (bnc#401706).
* Tue Jul 22 2008 lslezak@suse.cz
- added PolicyKit-devel and dbus-1-devel packages to
  yast2-core-devel dependencies
- fixed crash: prevent from multiple delete in SCR destructor
- 2.17.5
* Mon Jul 21 2008 lslezak@suse.cz
- integrated DBus/PolicyKit support to SCR level (SCR can run
  as a DBus service, set Y2DBUS=1 for using the DBus service from
  a yast client, requires setting PolicyKit priviledges for users)
  (fate#301960)
- 2.17.4
* Fri Jul 18 2008 mvidner@suse.cz
- Use -std=gnu++0x instead of c++0x so that we do not lose gnu
  extensions like typeof (fixes yast2-pkg-bindings build).
- 2.17.3
* Thu Jul 17 2008 mvidner@suse.cz
- Check GCC version and use <unordered_map> to get rid of
  <ext/hash_map> warnings. It needs yast2-devtools-2.17.2 but fails
  gracefully.
- 2.17.2
* Fri Jun 20 2008 aschnell@suse.de
- Added list::reduce builtin.
- 2.17.1
* Fri Jun 13 2008 aschnell@suse.de
- Added float::abs, float::ceil, float::floor, float::trunc and
  float::pow.
- 2.17.0
* Thu May 15 2008 mvidner@suse.cz
- Set YAST_IS_RUNNING to "instsys" also for the live-installer (bnc#389099).
- 2.16.51
* Mon May  5 2008 mvidner@suse.cz
- Show search path when client is not found (bnc#342213).
- 2.16.50
* Mon May  5 2008 mvidner@suse.cz
- Allow literal strings as arguments (bnc#382883):
  Before:   y2base foo    '("\\t")' '("\"")' UI
  Now also: y2base foo -S '(\t)'    '(")'    UI
- 2.16.49
* Mon Apr 14 2008 mvidner@suse.cz
- If Y2DEBUGONCRASH is set, the crash handler will also print the
  last few debugging log messages, even if Y2DEBUG is not set
  (fate#302166).
- 2.16.48
* Thu Apr 10 2008 mvidner@suse.cz
- New builtin: dpgettext ("animals", "/mnt/share/locale", "Giraffe")
  (fate#2826, by juhliarik).
- 2.16.47
* Wed Apr  9 2008 aschnell@suse.de
- added new builtin sublist
- 2.16.46
* Tue Apr  8 2008 mvidner@suse.cz
- Compress (gzip) the rotated y2logs, in the background (fate#300637).
- y2base: Added -I and -M options to add search paths for includes and
  modules (fate#2306).
- 2.16.45
* Sun Apr  6 2008 aschnell@suse.de
- added float builtins trunc and pow
- 2.16.44
* Sun Apr  6 2008 coolo@suse.de
- compile with xcrypt 3
- 2.16.43
* Thu Apr  3 2008 aschnell@suse.de
- extended toterm builtin
- 2.16.42
* Fri Mar 28 2008 mvidner@suse.cz
- Lazy SCR: to better suit the current naming scheme, to get .foo.bar
  look for foo_bar.scr instead of foo.bar.scr
- Lazy SCR: when sweeping, warn in the log
- 2.16.41
* Wed Mar  5 2008 locilka@suse.cz
- Extended .process agent with 'buffer_empty' function that returns
  whether the stdout buffer is empty (needed for backup).
- Adjusted and fixed process agent testsuite.
- 2.16.40
* Tue Mar  4 2008 mvidner@suse.cz
- Do not stop registering agents after UnregisterAgent (bnc#365116).
- 2.16.39
* Mon Feb 25 2008 sh@suse.de
- Package split: libyui and ycp-ui-bindings are now separate pkgs
- V 2.16.38
* Thu Feb 21 2008 coolo@suse.de
- support gtk
- V 2.16.37
* Wed Feb 20 2008 coolo@suse.de
- fix dummy UIs for test cases in yast modules
* Wed Feb 20 2008 lslezak@suse.cz
- .process agent - fixed reading large stdout/stderr output (added
  a testsuite), removed .buffer path (output reading is now part
  of .running)
* Wed Feb 20 2008 sh@suse.de
- Accept `opt(`immediate) for tree widget
- V 2.16.36
* Wed Feb 20 2008 mvidner@suse.cz
- If the log directory does not exist, create it.
* Wed Feb 20 2008 mvidner@suse.cz
- Fixed linking of libpy2UI.
* Mon Feb 18 2008 sh@suse.de
- Load plug-ins for "UI", "qt", "ncurses" from one single plug-in
- Made core UI independent of YCP and liby2 (Y2Component...)
- V 2.16.35
* Fri Feb 15 2008 lslezak@suse.cz
- added new .process (agent-process) agent (obsoletes old
  .background agent) - handles multiple subprocess, complete I/O
  communication, tty support
* Wed Feb 13 2008 sh@suse.de
- Made new UI logging thread-safe
* Tue Feb 12 2008 sh@suse.de
- New utility class YCommandLine in libyui to retrieve
  argc and argv from /proc/<pid>/cmdline
- V 2.16.34
* Mon Feb 11 2008 sh@suse.de
- Preliminary UI split: moved ycp-ui out of libyui
- V 2.16.33
* Fri Feb  8 2008 sh@suse.de
- Moved last YCPValue out of YUI
- V 2.16.32
* Fri Feb  8 2008 mvidner@suse.cz
- Endless recursion: not only log it, but also break it by returning
  nil after 1001 call frames (setenv Y2RECURSIONLIMIT to change that).
- 2.16.31
* Thu Feb  7 2008 sh@suse.de
- Moved UI built-ins out to separate class YCP_UI
- V 2.16.30
* Thu Feb  7 2008 mvidner@suse.cz
- Make SCR registration lazy: to find .foo, open only foo.scr.
  If that fails, only then scan all *.scr. (fate#302975)
- Test ports using bash's /dev/tcp instead of netcat (bnc#264309).
* Wed Feb  6 2008 sh@suse.de
- Moved macro recording and playing out of YUI class into new
  YMacro class with static functions
- V 2.16.29
* Fri Feb  1 2008 sh@suse.de
- Moved UI event handling from YUI to YDialog
- V 2.16.26
* Thu Jan 31 2008 sh@suse.de
- Simplified and unified internal UI dialog handling
- V 2.16.25
* Tue Jan 29 2008 sh@suse.de
- YCP-less event handling in libyui core
- V 2.16.24
* Fri Jan 25 2008 sh@suse.de
- Improved UI syntax error handling: Open dialogs to inform the user
* Wed Jan 23 2008 sh@suse.de
- V 2.16.23
* Tue Jan 22 2008 lslezak@suse.cz
- ag_background - added .signal path for sending a specified signal
  e.g. SCR::Execute(.background.signal, 10), posted by Kevin James
* Tue Jan 22 2008 sh@suse.de
- Improved back trace legibility: Demangling C++ symbols
* Wed Jan 16 2008 tgoettlicher@suse.de
- updated docu for BusyIndicator widget
* Wed Jan 16 2008 tgoettlicher@suse.de
- fixed BusyIndicator example
* Wed Jan 16 2008 sh@suse.de
- Infrastructure for new stream-based UI logging
* Tue Jan 15 2008 mvidner@suse.cz
- Log the C backtrace when receiving a signal (FATE 302167).
- reverted libpy2UI.so.3 to .so.2 as the plugin loader expects
- 2.16.22
* Mon Jan 14 2008 tgoettlicher@suse.de
- minor changes in BusyIndicator widget
- V 2.16.21
* Thu Jan 10 2008 tgoettlicher@suse.de
- added BusyIndicator widget (fate #302559)
- V 2.16.20
* Thu Jan 10 2008 lslezak@suse.cz
- added .modprobe_blacklist agent for parsing
  /etc/modprobe.d/blacklist file (#330109)
- V 2.16.19
* Wed Jan  9 2008 sh@suse.de
- Fixed segfault upon shutting down UI
  (observed mostly on single-CPU non-hyperthreading machines)
- V 2.16.18
* Fri Dec 21 2007 coolo@suse.de
- support `CurrentItem to the timezone selector
- V 2.16.17
* Tue Dec 18 2007 coolo@suse.de
- adding another optional widget: timezone selector
- V 2.16.16
* Tue Dec 11 2007 sh@suse.de
- Fixed bug #347634: Cannot pass empty string to editable ComboBox
* Tue Dec 11 2007 sh@suse.de
- Fixed byproduct of fix for bug #346158 and bug #346165:
  All YSimpleEvents returned strings now, even predefined IDs
  `cancel, `timeout, `debugConsole; now returning correct IDs again
* Mon Dec 10 2007 sh@suse.de
- Moved file and directory dialogs from YUI to YApplication:
  - askForExistingDirectory(),
  - askForExistingFile()
  - askForSaveFile()
- V 2.16.15
* Thu Dec  6 2007 sh@suse.de
- Fixed bug #345819 (input fields too small):
  Introduced bug compatibility mode for TextEntry widget;
  when used with the old name `TextEntry(), `opt(`hstretch)
  is automatically assumed; with the new name `InputField() it
  behaves like specified.
- V 2.16.14
* Wed Dec  5 2007 sh@suse.de
- Fixed YMenuEvent( string ) handling:
  => Fixed bug #346158: Hyperlinks don't work
  => Fixed bug #346165: Wizard tree selection doesn't work
- V 2.16.13
* Wed Dec  5 2007 sh@suse.de
- Fixed bug #346139: CheckBoxFrame is inverted
* Mon Dec  3 2007 coolo@suse.de
- continue supporting `Value for RadioButtonGroup (#345490) for now
* Fri Nov 30 2007 sh@suse.de
- Removed YContainerWidget for good
- Removed legacy YWidget::queryWidget() and YWidget::changeWidget()
  methods
- Dropped support for outdated property handling with old
  YWidget::queryWidget() and YWidget::changeWidget() methods
- Dropped support for outdated YWidget( YWidgetOpt ) constructors
- Unified Y*WidgetFactory::create*Dialog() methods:
  - Added pure virtual YWidgetFactory::createDialog( type, colorMode)
  - Made YWidgetFactory::createMainDialog() and
    YWidgetFactory::createPopupDialog() non-virtual
- Moved special YInputField macro handling for passwords
  to YMacroRecorder (don't record passwords in macros)
- Removed unneeded YWidgetOpt fields
- Catch exceptions in evaluateReplaceWidget
  (more graceful error handling)
- Added basic default button handling to YDialog, YPushButton
- V 2.16.11
* Thu Nov 29 2007 locilka@suse.cz
- Added some examples to UI::GetDisplayInfo() documentation.
- Fixed examples for Image widget.
* Tue Nov 27 2007 sh@suse.de
- Moved UI::WizardCommand() parsing to separate class
- Added stubs to YWizard to make YCP-free derived classes possible
- YWizard's internal YReplacePoint now has a string ID "contents",
  no longer YCPSymbol `contents
- V 2.16.10
* Mon Nov 26 2007 mvidner@suse.cz
- Visibly report the failure to create the temporary directory (#343258).
- 2.16.9
* Mon Nov 26 2007 mvidner@suse.cz
- ElectricFence is not required since 2 years ago
- 2.16.8
* Fri Nov 23 2007 sh@suse.de
- Fixed bug #52673 : Deselect all items in SelectionBox
- Fixed bug #230496: Exchange MenuButton items
* Fri Nov 23 2007 sh@suse.de
- Allow selecting nothing in SelectionWidgets
  - SelectionBox
  - ComboBox
  - MultiSelectionBox
  - Tree
  - Table
  Use   UI::ChangeWidget(`myWidget, `CurrentItem, nil )
* Fri Nov 23 2007 mvidner@suse.cz
- Dependencies: liby2util absorbed, blocxx renamed, cleaned up
  ancient cruft.
* Thu Nov 22 2007 sh@suse.de
- Moved UI setLanguage from YUI to YApplication
* Thu Nov 22 2007 locilka@suse.cz
- Fixed XML documentation not to point to non-existent widgets.
* Tue Nov 20 2007 sh@suse.de
- V 2.16.7
- More graceful error handling in
  - UI::ChangeWidget()
  - UI::QueryWidget()
- InputField widgets now use reasonable default width,
  no longer grow to eat up as much width as available
* Fri Nov 16 2007 sh@suse.de
- V 2.16.6
- Merged mod-ui branch to trunk:
  - Moved YCP code out of widget code
    (still to be done for some non-widget classes)
  - Clearer and consistent widget (C++) interfaces
  - Reasonable support for creating YWidgets from C++
  - Now using widget factories for better abstraction and handling
  - Moved misc. YCP parsers out of widget classes to separate classes
  - Item parsers (YSelectionBox, YComboBox, YTree, YTable, ...)
    now more forgiving
  - Individual table cells can now queried and set in YTable
  - More informative error messages
  - Error messages in log now report the YCP code location
  - Renamed YTextEdit to YInputField (old name still valid)
  - Renamed YTime     to YTimeField  (old name still valid)
  - Renamed YDate     to YDateField  (old name still valid)
  - Dropped YColoredLabel widget     (nowhere in use any more anyway)
  - Dropped UI::CollectUserInput()   (nowhere in use)
  - Dropped YImage from YCPByteBlock (nowhere in use any more)
  - All YSelectionWidgets (YSelectionBox, YComboBox, YTree, YTable,
    YMultiSelectionBox, YMenu) now support
    UI::QueryWidget(`myWidget, `Items )   (returning an item list)
  - Consistent icon support for YSelectionWidgets
    (YSelectionBox, YComboBox, YTree, YTable, YMultiSelectionBox, YMenu)
  Background and more details at
  http://www.suse.de/~sh/y2-mod-ui.pdf
  http://www.suse.de/~sh/y2-ui-arch-old.pdf
  http://www.suse.de/~sh/y2-ui-arch-modular.pdf
* Wed Nov 14 2007 mvidner@suse.cz
- Added missing parts of liby2util.rpm.
- 2.16.5
* Tue Nov 13 2007 mvidner@suse.cz
- Integrated the surviving parts of liby2util.rpm (F120312).
- 2.16.4
* Fri Nov  9 2007 mvidner@suse.cz
- Allow nil in UI::ChangeWidget again (#340523). Improved error
  reporting for cases where it is rightly disallowed.
- 2.16.3
* Fri Nov  2 2007 mvidner@suse.cz
- Do not look for YCP scripts under the current working
  directory, unless explicitly requested (#330965).
- 2.16.2
* Thu Oct  4 2007 mvidner@suse.cz
- Distinguish "foo.ycp contains an error" from "foo.ycp not found"
  (#330656).
- 2.16.1
* Tue Oct  2 2007 mvidner@suse.cz
- Close unneeded file descriptors before execing another
  program (#223602).
- Fixed compilation errors with GCC 4.3 by adding missing includes.
- 2.16.0
* Thu Sep 13 2007 mvidner@suse.cz
- UI::CollectUserInput: fixed crash introduced when namespacifying,
  restricting to a subtree of a dialog works now (#307056).
- 2.15.12
* Thu Sep  6 2007 mvidner@suse.cz
- Enabled iterating over all functions of a Y2Namespace, for
  a more natural call syntax in yast2-python-bindings (#308213).
- Do not log return value from clients (#248300).
- 2.15.11
* Wed Sep  5 2007 mvidner@suse.cz
- Fixed missing return value in YSymbolEntry::toXml
* Mon Sep  3 2007 juhliarik@suse.cz
- Added new function getenv(), #305163
- 2.15.10
* Tue Aug 21 2007 mvidner@suse.cz
- Fixed changing the value of table cells (#302042).
- 2.15.9
* Mon Aug 13 2007 coolo@suse.de
- really fix the crash
* Mon Aug 13 2007 coolo@suse.de
- Fix endless recursion (#299826)
* Mon Aug 13 2007 mvidner@suse.cz
- Fixed the capitalization of UI::MakeScreenShot.
- 2.15.8
* Fri Aug 10 2007 mvidner@suse.cz
- Finished integrating Feature #120292, UI as a namespace callable
  from yast2-*-bindings.
- 2.15.7
* Thu Aug  9 2007 mvidner@suse.cz
- The dummy Y2 component is instantiable but YUI is not, fixed the
  namespace accordingly.
- 2.15.6.4
* Wed Aug  8 2007 mvidner@suse.cz
- Make the dummy UI instantiable for testsuite purposes.
- 2.15.6.3
* Mon Aug  6 2007 mvidner@suse.cz
- Increased the ag_background test suite timeout to prevent random
  failures due to scheduling.
- Disabled it.
* Mon Aug  6 2007 mvidner@suse.cz
- Converted the UI functions from YCP builtins to a YCP namespace, so
  that they can be called from other language bindings.
- 2.15.6.2
* Wed Jul 18 2007 kkaempf@suse.de
- ycpc can now output an XML representation of the parse tree
  http://kkaempf.blogspot.com/2007/07/hackweek-aftermath.html
* Thu Jul 12 2007 locilka@suse.cz
- Fixed ag_background to always read the process exit status before
  returning it (#285920).
* Mon Jun 25 2007 mvidner@suse.cz
- ag_background: added a test suite.
- Recommend, not require, netcat (#264309).
* Thu Jun 21 2007 adrian@suse.de
- fix changelog entry order
* Thu May 24 2007 stbinner@suse.de
- add missing %%run_ldconfig calls
* Fri Apr 13 2007 sh@suse.de
- Merged mod-ui branch changes (r37142:37462) back to trunk:
  - Added infrastructure for UI plugins
- V 2.15.6
* Fri Mar 30 2007 mvidner@suse.cz
- BuildRequire flex and bison explicitly.
- yast2-core-devel: Require flex because of FlexLexer.h
- 2.15.5
* Wed Mar 21 2007 kmachalkova@suse.cz
- YWidget: warning instead of error in setKeyboardFocus (#255785)
* Fri Mar 16 2007 mvidner@suse.cz
- Files referenced from /usr/share/doc/packages/yast2-core/libycp/index.html
  were not installed due to a typo (#235111).
* Mon Feb 26 2007 mvidner@suse.cz
- Fixed format string bugs in log messages (#246807).
* Fri Feb 23 2007 mvidner@suse.cz
- Added SCR::RegisterNewAgents, for agents defined in add-ons (#245508).
- 2.15.4
* Fri Feb 23 2007 mvidner@suse.cz
- ag_ini: Log errors if the syntax description term contains invalid data,
  for example if "params" is not a list or its items are not maps..
* Fri Feb 23 2007 mvidner@suse.cz
- Signals: in addition to SEGV, catch also HUP, INT, QUIT, ILL, ABRT,
  FPE, TERM, and log the fact (#238172).
* Tue Feb 13 2007 kmachalkova@suse.cz
- Replaced '[x]' placeholder glyph (CheckMark) with 'x' to make it
  distinct from ncurses checkbox (#244061)
* Thu Feb  8 2007 mvidner@suse.cz
- SCR::RegisterAgent: fixed a bug in the declaration of this call.
* Thu Feb  1 2007 mvidner@suse.cz
- libycp: clarified docs for iterator builtins ("in a new block"
  instead of "in a new context", #236730)
* Mon Jan 29 2007 mvidner@suse.cz
- ag_system: do not make yast exit when PID has 7 or more digits (#237481).
* Mon Jan 22 2007 mvidner@suse.cz
- ag_modinfo: do not return numbers instead of strings. Fixes a crash
  in "yast2 tv" when accessing 80211.ko (#224742).
- 2.15.3
* Mon Jan 22 2007 mvidner@suse.cz
- autodocs: reenabled liby2util.tag
* Fri Jan  5 2007 sh@suse.de
- Added CheckBoxFrame widget for feature #5673
- 2.15.2
* Tue Dec  5 2006 mvidner@suse.cz
- ini-agent with repeat_names: do not merge sections with same name
  when parsing. They can be accessed using .all. (#224414)
* Tue Dec  5 2006 kmachalkova@suse.cz
- Added RunInTerminal UI builtin for running external programs from
  ncurses UI (#148683, #221254, #222547)
- 2.15.1
* Tue Dec  5 2006 mvidner@suse.cz
- Do not abort if a nonterm is passed to `ReplacePoint or `*Squash
  (#225815).
- 2.15.0
* Tue Oct 31 2006 mvidner@suse.cz
- ini-agent: use C locale when building regular expressions so that
  A-Z works for Estonian (#177560).
- 2.14.4
* Mon Oct 23 2006 mvidner@suse.cz
- Worked around building with doxygen 1.5.0 by not including
  liby2util.tag.
- 2.14.3
* Sun Oct  1 2006 mvidner@suse.cz
- Adapted for upcoming blocxx 2.x changes (by Michael Calmer).
- 2.14.2
* Mon Sep 25 2006 mvidner@suse.cz
- Removed unneeded BuildRequires.
- Call xsltproc with --nonet, via $(XSLTPROC_FLAGS).
- Adjusted testsuite for the Missing import change.
- 2.14.1
* Wed Sep 20 2006 mvidner@suse.cz
- libycp: Improved an error message to say "Missing import?".
* Tue Sep 19 2006 mvidner@suse.cz
- Reduced YCPValue from two pointers to one by removing the
  superfluous "virtual" qualifiers. Heap reduced by 10%%.
- 2.14.0
* Tue Sep 19 2006 lslezak@suse.cz
- ag_background - added missing .open_output_err path handler
* Wed Sep 13 2006 sh@suse.de
- Applied patch from Ricardo Cruz <rpmcruz@clix.pt>
  for new UI::Beep() built-in
* Fri Sep  8 2006 mvidner@suse.de
- ini-agent: let Dir(.) return ["section", "value"] for non-flat files.
- Added some Doxygen comments.
* Tue Aug 22 2006 lslezak@suse.cz
- generateYCPWrappers - fixed crash when nil is passed as
  an argument to YCP binding (#194435)
- 2.13.30
* Mon Aug 21 2006 mvidner@suse.cz
- ycp.pm: added PathComponents to normalize nontrivial paths
- 2.13.29
* Wed Aug  9 2006 mvidner@suse.cz
- agent-ini: fixed value_type and section_type with repeat_names (#191495).
- libycp: added YCPValue::valuetype_str() for better debug messages.
- 2.13.28
* Tue Aug  8 2006 mvidner@suse.cz
- Added ybcdump, a tool for understaning the *.ybc "bytecode".
- 2.13.27
* Mon Aug  7 2006 mvidner@suse.cz
- ini-agent: use a space separator for join_multiline (#195914).
- Fixed a crash when modifying a `Tree property on a non-existing
  item (Ricardo Cruz).
- 2.13.26
* Fri Aug  4 2006 mvidner@suse.cz
- Memory reduction: removed YCode members m_valid and m_kind to save
  5%% of heap.
* Wed Aug  2 2006 mvidner@suse.cz
- Include more variables in yast2-core.pc
- 2.13.25
* Tue Aug  1 2006 visnov@suse.cz
- Fix POSIX make
- 2.13.24
* Thu May 25 2006 mvidner@suse.cz
- Use [:alpha:] instead of A-Za-z to catch all ASCII letters even in
  Estonian (#177560).
- 2.13.23
* Tue May  2 2006 lslezak@suse.cz
- ag_background - use unlimited buffer size as default, do not
  block the subprocess (#169648), update of the example
- 2.13.22
* Tue Apr 25 2006 mvidner@suse.cz
- Print also the y2base arguments on the first log line (#169257).
- 2.13.21
* Mon Apr  3 2006 mvidner@suse.cz
- Do not use a random path if an invalid one is given in Dir(.modinfo)
  (#154171).
- 2.13.20
* Thu Mar 23 2006 sh@suse.de
- V 2.13.19
- Enable starting up pkg selector in inst sources view: Use
  `opt(`instSourcesMode)
* Fri Feb 24 2006 mvidner@suse.cz
- ini agent docs: emphasized that writes are cached.
* Wed Feb 22 2006 sh@suse.de
- V 2.13.18
- Support for registration during installation:
  Dump complete contents of a dialog with one single call
  (new builtin UI::CollectUserInput() )
* Mon Jan 30 2006 sh@suse.de
- V 2.13.17
- Implemented (optional) PatternSelector widget (feature #129)
* Tue Jan 10 2006 visnov@suse.cz
- display file name on failing import (#141566)
* Fri Jan  6 2006 mvidner@suse.cz
- Ini agent: allow deleting files via .all, needed by slp-server.
- V 2.13.16
* Wed Jan  4 2006 sh@suse.de
- Add-on for feature #3476: left-handed mouse during installation
  enable querying if user changed mouse to left-handed from the UI
- V 2.13.15
* Tue Jan  3 2006 mvidner@suse.cz
- UI: made `Value an alias for `CurrentButton (`RadioButtonGroup)
  and `CurrentItem (`Table, `SelectionBox, `Tree). #23605.
- V 2.13.14
* Mon Dec 19 2005 visnov@suse.cz
- workaround ppc64 problems, don't like against ElectricFence
- V 2.13.13
* Fri Dec 16 2005 visnov@suse.cz
- remove obsolete code
- join libraries
- V 2.13.12
* Tue Dec 13 2005 mvidner@suse.cz
- Added yast2-core.pc.in (new devtools don't provide a generic one).
- Do not require hwinfo now that .probe is in yast2-hardware-detection.
- V 2.13.11
* Mon Dec  5 2005 visnov@suse.cz
- include <langinfo.h> for nl_langinfo()
- V 2.13.10
* Thu Dec  1 2005 kkaempf@suse.de
- include <libintl.h> for dngettext()
* Wed Nov 30 2005 kkaempf@suse.de
- disallow references to 'any' (#97956)
* Tue Nov 29 2005 kkaempf@suse.de
- make preference rule explicit in scanner.ll (for flex-2.5.31)
- evaluate rhs before lhs in bracket assignment (#135858)
- V 2.13.9
* Tue Nov 29 2005 visnov@suse.cz
- implemented search () for string lookup, marked find ()
  for strings as deprecated.
- fix scanner for newer flex
- don't crash on 'nil' as return value from filter/find (#120298)
- in bracket assignment, allow to change the lhv in rh expression (#135858)
- V 2.13.8
* Fri Nov 25 2005 kkaempf@suse.de
- remove scanner.cc and parser.cc from .tar.bz2 in order to force
  their re-generation during build.
* Thu Nov 24 2005 kkaempf@suse.de
- fix 'tointeger' to match documentation. It now returns nil
  instead of 0 on illegal (non-convertible) string values (#115560)
* Tue Nov 22 2005 kkaempf@suse.de
- fix 'type-punned pointer' warnings in parser.yy
- V 2.13.5
* Thu Oct 20 2005 visnov@suse.cz
- added missing import for Agent skeleton
- V 2.13.4
* Wed Oct 12 2005 visnov@suse.cz
- really fix the system agent testsuite
- V 2.13.3
* Mon Oct 10 2005 visnov@suse.cz
- install also string helpers
- disable failing testsuite in system agent
- V 2.13.2
* Wed Oct  5 2005 visnov@suse.cz
- fix build
- V 2.13.1
* Thu Sep 29 2005 visnov@suse.cz
- Split .probe agent to another package
- V 2.13.0
* Wed Sep 28 2005 sh@suse.de
- Added UI::QueryWidget(..., CurrentBranch ) for YTree
* Mon Sep 19 2005 mvidner@suse.cz
- For deprecated builtins, document what to use instead.
* Mon Sep 12 2005 kkaempf@suse.de
- ensure string reference does not go out of scope too early
  (#116432)
- V 2.12.27
* Fri Sep  9 2005 sh@suse.de
- (visnov) Fixed bug #115298: Install on x86_64 horribly slow
  due to excessive memory requirements
  Removed string hash in YCPString
- V 2.12.26
* Tue Sep  6 2005 kkaempf@suse.de
- configure with AC_SYS_LARGEFILE (#115394)
- put config.h in include chain of SystemAgent.cc
* Fri Aug 19 2005 sh@suse.de
- Added macro player support for the other event-releated UI builtins:
  WaitForEvent(), WaitForEvent( timeout ), TimeoutUserInput()
  to fix bug #98265: Macro player doesn't work
- V 2.12.23
* Fri Aug 19 2005 sh@suse.de
- Reintroduced the UI layout engine's change reverted on 2005-08-04
  by jsrain below now that the true cause of the problem is
  established
- V 2.12.22
* Tue Aug  9 2005 kkaempf@suse.de
- pass the UDI value in probing results. [#102575].
* Mon Aug  8 2005 kkaempf@suse.de
- hd_change_status() -> hd_change_config_status() to get the
  unique_key <-> UDI mapping right in libhd [#102575].
- 2.12.21
* Sat Aug  6 2005 aj@suse.de
- Add libxml2-devel to neededforbuild.
* Thu Aug  4 2005 jsrain@suse.cz
- reverted changes in layout engine in order to display stretches
  properly
- 2.12.20
* Thu Jul 21 2005 sh@suse.de
- Restored correct HStretch() and VStretch() behaviour
- V 2.12.19
* Thu Jul 21 2005 mvidner@suse.cz
- System agent: Check for fork failure (#97566).
- 2.12.18
* Thu Jul 21 2005 sh@suse.de
- Added support `opt(`hvstretch) for alignment widgets for
  backward compatibility with (buggy) old layout behaviour:
  propagate child stretchability to alignment parent
- V 2.12.17
* Mon Jul 11 2005 sh@suse.de
- Fixed bug #95722: No items in NCurses MultiSelectionBox
- V 2.12.16
* Fri Jul  8 2005 visnov@suse.cz
- Log blocxx messages to YaST2 log
- Fix Requires
- V 2.12.15
* Wed Jul  6 2005 kkaempf@suse.de
- V 2.12.14
- Allow multi string constants in _() locales
* Tue Jul  5 2005 sh@suse.de
- V 2.12.13
- Support for background pixmaps in alignment widgets
* Tue Jul  5 2005 sh@suse.de
- New UI layout helper widgets: MinWidth, MinHeight, MinSize
- Added klibc, klibc-devel, udev to neededforbuild (for hwinfo)
- V 2.12.12
* Tue Jul  5 2005 kkaempf@suse.de
- hwinfo/libhd need hal and dbus for building
* Fri Jul  1 2005 sh@suse.de
- V 2.12.10
- New layout helper widget: MarginBox
- Improved geometry management for insufficient screen space
- Fixed bug in Alignment widget - now no longer requiring a Squash
  widget inside for proper alignment
* Tue Jun 21 2005 visnov@suse.cz
- use redirected System:: prefix also after the redirection
- 2.12.9
* Tue Jun 14 2005 visnov@suse.cz
- libpy2wfm: fix missing dependency on libpy2program (schwab)
- 2.12.8
* Tue Jun 14 2005 visnov@suse.cz
- added sysfsutils to NFB
- 2.12.7
* Wed Jun  1 2005 mlazar@suse.cz
- libycp: added YCPExternal type for storing external data types
* Mon May 30 2005 visnov@suse.cz
- implemented chroot redirect of namespaces
* Mon May 23 2005 visnov@suse.cz
- 2.12.6
* Sun May 22 2005 aj@suse.de
- Fix for GCC4 friends conformance.
* Tue May  3 2005 visnov@suse.cz
- don't crash if include file does not enclose
  the code in a block (#65486)
* Mon May  2 2005 visnov@suse.cz
- fix function parameter type check (#64627)
- evaluate the code returned if not constant (#65815)
- report unreachable code at the end of file (#66152)
- don't assume there are always parameters (#72810)
* Mon May  2 2005 visnov@suse.cz
- 2.12.5
* Wed Apr 27 2005 sh@suse.de
- Added support for icons in YSelectionWidgets
* Thu Apr 21 2005 sh@suse.de
- Merged selection_widget_cleanups branch to trunk:
  selection widgets can now replace list items
  (SelectionBox, ComboBox, MultiSelectionBox, Tree)
* Tue Apr 19 2005 visnov@suse.cz
- implemented 'switch' statement
* Wed Apr 13 2005 visnov@suse.cz
- added libpthread for all YaST binaries (#76401)
- 2.12.4
* Wed Apr  6 2005 visnov@suse.cz
- added virtual destructors to keep gcc4 happy
* Tue Apr  5 2005 visnov@suse.cz
- enable ElectricFence again without checking for 0 size allocs
- fix support for perl-bindings
- 2.12.3
* Mon Apr  4 2005 visnov@suse.cz
- temporarily disable ElectricFence to workaround glibc problem
- another gcc4 fix (logged incorrect function name)
* Fri Apr  1 2005 visnov@suse.cz
- merged 9.3 branch
- another gcc4 fix
* Thu Mar 31 2005 coolo@suse.de
- build better with gcc4
* Wed Mar 30 2005 mvidner@suse.cz
- ini agent: do not indent comments (#74698)
- 2.12.1
* Wed Mar 16 2005 visnov@suse.cz
- reduced UI logging
- added YCP testsuites for is() also for build
- 2.11.26
* Tue Mar 15 2005 locilka@suse.cz
- Checked, fixed and added YCP builtins description and examples
- Mark tolist() as deprecated
* Tue Mar  8 2005 locilka@suse.cz
- Checked, fixed and added YCP builtins description and examples
* Fri Mar  4 2005 visnov@suse.cz
- Fixed yast2-crash on parsing lan probe results
- 2.11.25
* Thu Feb 24 2005 visnov@suse.cz
- revert  YCP module import reporting change
- 2.11.24
* Tue Feb 22 2005 mvidner@suse.cz
- Added wireles card features to agent-probe (#65391).
- When renumbering file descriptors, check whether we already have
  the desired number (#64797).
- 2.11.23
* Mon Feb 21 2005 ro@suse.de
- added wireless-tools to nfb (for libhd)
* Mon Feb 21 2005 visnov@suse.cz
- report YCP module import only when reading the bytecode
* Tue Feb 15 2005 arvin@suse.de
- adapted agent-probe to new hwinfo
* Tue Feb 15 2005 sh@suse.de
- PackageSelector now supports `opt(`summaryMode) to get installation
  summary right away (-> Anas)
- V 2.11.21
* Mon Feb  7 2005 lslezak@suse.cz
- modules agent - use .YaST2save suffix for backup files (#50517)
- 2.11.20
* Mon Jan 31 2005 sh@suse.de
- V 2.11.19
- Suppressing plain text passwords in recorded macros
* Tue Jan 11 2005 mvidner@suse.cz
- Added .probe.dsl
- 2.11.18
* Tue Jan 11 2005 visnov@suse.cz
- remove fprintf calls, use logs instead
- 2.11.17
* Tue Jan  4 2005 arvin@suse.de
- fixed architecture detection (s390/s390x) during update (bug
  [#49313])
* Thu Dec  2 2004 mvidner@suse.cz
- ini agent: do not merge external changes when repeat_names is
  enabled (#42297)
- ini agent: include file name in parse errors (#48777)
* Thu Nov 18 2004 kkaempf@suse.de
- increase bison stack limit (#45509)
- evaluate bracket default expression only if required (#48337)
* Wed Nov 17 2004 nashif@suse.de
- Fixed nfb for docbook
* Fri Nov 12 2004 sh@suse.de
- New debugging tools in UI:
  - Widget property WidgetClass (all widgets)
  - Widget property DebugLabel  (all widgets)
* Tue Nov  9 2004 visnov@suse.cz
- don't allow variable declaration for functions and terms (#40441)
- issue proper error when unable to create intermediate structures
  on map/list/term assignment (#39236)
- don't escape strings (#44461)
- recoded testcases to UTF8
- show warning on too many call frames (#40426)
* Mon Nov  8 2004 visnov@suse.cz
- reintroduced YCP backtraces (#41841)
- 2.11.13
* Mon Nov  8 2004 visnov@suse.cz
- Don't crash on wrong nested import (#47357)
- Cleanup parse error handling (return NULL always)
- 2.11.12
* Fri Nov  5 2004 visnov@suse.cz
- Show parameters for all function symbol entries (#47078)
- Allow to set symbol entry global
* Thu Nov  4 2004 visnov@suse.cz
- report file and line number for builtins (#43830)
- report correct line number of wrong function calls (#47077)
- don't crash on builtins without parameters when they require one
- 2.11.11
* Wed Nov  3 2004 visnov@suse.cz
- create libycpvalues library
* Wed Nov  3 2004 kkaempf@suse.de
- warn about using uninitialized variables (#42648)
* Wed Nov  3 2004 visnov@suse.cz
- Recognize wrong octal and hexa constants and report them (#47883)
* Wed Nov  3 2004 visnov@suse.cz
- Always create a symbol table for modules (#42007)
* Tue Nov  2 2004 kkaempf@suse.de
- Fix type ordering in detailedtype() further, 'any' has more
  type information than '<unspec>' (#47853)
* Tue Nov  2 2004 kkaempf@suse.de
- recognize select() in parser.
- use identical type checking for bracket operator and select()
  (#43612)
- mark select() as deprecated.
* Tue Nov  2 2004 nashif@suse.de
- Added new widgets: YDate / YTime
* Tue Nov  2 2004 kkaempf@suse.de
- check for proper return statement in definition of non-void
  functions (#40687)
* Tue Nov  2 2004 kkaempf@suse.de
- use identical type checking for bracket operator and lookup()
  (#44221)
- mark lookup() as deprecated.
* Tue Nov  2 2004 visnov@suse.cz
- Use shared representation for booleans and nils
- consider only single digit arguments
- 2.11.9
* Mon Nov  1 2004 mvidner@suse.cz
- UI: added Date and Time widgets, qt only (nashif)
- 2.11.8
* Fri Oct 29 2004 mvidner@suse.cz
- Added pkgconfig support.
- 2.11.7
* Thu Oct 28 2004 kkaempf@suse.de
- 'any' has more type information than 'void' (#47659)
- dont propagate any->any (regression found with above fix)
* Wed Oct 27 2004 arvin@suse.de
- removed has_apm from probe agent
* Wed Oct 27 2004 lslezak@suse.cz
- ag_modinfo: modinfo output was incorrectly parsed when it
  contained more `:' chars
* Thu Oct 21 2004 kkaempf@suse.de
- improve type checking to always use the most detailed type
  information available (#38375).
* Tue Oct 19 2004 kkaempf@suse.de
- is() now checks against the actual value, not the declared
  type (#37146)
* Tue Oct 19 2004 visnov@suse.de
- Y2ScriptComponent removed
* Fri Oct 15 2004 visnov@suse.de
- Add back WFM headers
- fix testsuite
- 2.11.3
* Fri Oct 15 2004 kkaempf@suse.de
- add .probe.bluetooth (#47297)
* Fri Oct 15 2004 visnov@suse.de
- Move Pkg namespace to the pkg-bindings package
- 2.11.1
* Thu Oct 14 2004 kkaempf@suse.de
- check format string (in sformat() or y2milestone()) against
  number of actual arguments (#35822)
* Mon Oct 11 2004 visnov@suse.cz
- Make recursion lighter on memory (allocate stack
  only when needed)
* Fri Oct  8 2004 visnov@suse.cz
- Split Pkg as a standalone component, don't link against it.
* Wed Oct  6 2004 sh@suse.de
- UI: Dropped support for hardcoded images "suseheader" and "yast2"
  Use path names and/or the wizard instead!
* Wed Oct  6 2004 visnov@suse.cz
- Read whole u32 at once from bytecode to speed it up
* Tue Oct  5 2004 visnov@suse.cz
- Allow namespaces to be located in libraries, so we don't
  need to link them (using Y2PluginComponent)
* Thu Sep 30 2004 visnov@suse.cz
- log non-existent directory in .target.dir as a milestone only (bug #45573)
* Thu Sep 23 2004 arvin@suse.de
- added Pkg::RpmChecksig function (bug #45647)
* Mon Sep 20 2004 schwab@suse.de
- Fix C++ syntax and format strings.
* Mon Sep 13 2004 arvin@suse.de
- don't use hd_base after freeing (bug #44855)
* Mon Sep 13 2004 arvin@suse.de
- fixed TargetInitDU for missing readonly key
- 2.10.14
* Fri Sep 10 2004 sh@suse.de
- Implemented enhancement #44799: Log error for leftover dialogs
- V 2.10.13
* Fri Sep 10 2004 sh@suse.de
- Improved `opt(`debugLayout) UI logging
* Fri Sep 10 2004 ma@suse.de
- Pass information about readonly mounted partitions in Pkg::TargetGetDU.
* Wed Sep  8 2004 visnov@suse.cz
- reverted the flex patch for now
* Tue Sep  7 2004 visnov@suse.cz
- support newer flex (patch by tcrhak)
- 2.10.12
* Mon Sep  6 2004 jsrain@suse.cz
- Added Pkg::PkgMarkLicenseConfirmed() (#44145)
- Changed  Pkg::PkgGetLicenseToConfirm() and
  Pkg::PkgGetLicensesToConfirm() to return only unconfirmed
  licenses (#44145)
- 2.10.11
* Thu Sep  2 2004 sh@suse.de
- Added Pkg::PkgMediaCount()
- V 2.10.10
* Wed Sep  1 2004 sh@suse.de
- Fixed bug #44579: YMultiProgressBar integer overflow
- V 2.10.9
* Mon Aug 30 2004 mvidner@suse.cz
- substring: fixed an unlikely bug with offset signedness
- bytecode: fixed m_release comparison in isVersionAtMost
- updated builtin docs
- 2.10.8
* Mon Aug 30 2004 jsrain@suse.cz
- added Pkg::PkgTaboo builtin (#43499)
* Wed Aug 18 2004 visnov@suse.cz
- support also bytecode from SLES9/9.1 (#43881)
- 2.10.7
* Wed Aug 18 2004 mvidner@suse.cz
- ag_probe: parse carrier detection information from libhd (res_link)
* Mon Aug 16 2004 visnov@suse.cz
- return 'nil' if function pointer cannot be used instead of NULL (#42330)
* Mon Aug 16 2004 visnov@suse.cz
- fix is() for function pointers (#43848)
* Mon Aug 16 2004 visnov@suse.cz
- fix function pointers from perl-bindings (#43606)
- 2.10.5
* Thu Aug 12 2004 jsrain@suse.cz
- added libpng to neededforbuild
- 2.10.4
* Tue Aug  3 2004 visnov@suse.cz
- fix handling of 'import "Summary"' testcase in symbol tables
- 2.10.3
* Mon Aug  2 2004 visnov@suse.cz
- better split of YCP interpreter and rest of YaST (use Y2Function only)
- type of builtin parameters are checked at the end of all parameters
- YCode::type () is cleaned up - now it always returns the type of the
  code after its evaluation, determined as good as possible
- split of function call and function call via function pointer (Bytecode change)
- 2.10.2
* Fri Jul 16 2004 sh@suse.de
- YTree widget can now return `Item property
- YTree widget can now return new `OpenItems property
* Wed Jun 23 2004 visnov@suse.cz
- allow YCP code to call overloaded functions in other namespaces
- parser should not use ExecutionEnvironment for logging (#42088)
- removed obsolete stuff (callbacks)
* Wed Jun 16 2004 arvin@suse.de
- set current directory to / for chrooted programs
* Thu May 27 2004 visnov@suse.cz
- do not reregister scrconf files on startup (#40833)
- 2.9.94
* Tue May 25 2004 arvin@suse.de
- include data about requires, conflicts, provides and obsoletes
  in Pkg::SelectionData (bug #37133)
* Fri May 21 2004 mvidner@suse.cz
- Host finder (ag_hostnames): ping longer to get more hosts (#40582)
- 2.9.92
* Wed May 19 2004 ma@suse.de
- Adapt PKG interface to changes in packagemanger.
- 2.9.91
* Thu May 13 2004 arvin@suse.de
- removed seg. fault when chrooted scr can't be created
* Mon May 10 2004 visnov@suse.cz
- fix number formattting (#39645)
- 2.9.89
* Wed May  5 2004 arvin@suse.de
- added bus_hwcfg entry in probe-agent (bug #39456)
* Fri Apr 30 2004 sh@suse.de
- Added new widget DumbTab
- V 2.9.87
* Fri Apr 30 2004 mvidner@suse.cz
- allowed to read YCPPathSearch search lists, so that Perl
  can synchronize @INC (#39512)
- 2.9.86
* Thu Apr 29 2004 mvidner@suse.cz
- publish some WFM headers so that Perl can know
  when to destroy us (#39519)
- 2.9.85
* Thu Apr 29 2004 mvidner@suse.cz
- added /y2update to YCPPathSearch::initialize (#38677)
- 2.9.84
* Wed Apr 28 2004 cschum@suse.de
- Pkg::TargetProducts(): include base architecture for you_server.
* Tue Apr 27 2004 visnov@suse.cz
- 2.9.83
* Fri Apr 23 2004 ma@suse.de
- PKG: Avoid logging of YCP arguments on conversion to C++ datatypes.
  YCPStrings may deote urls with cleartext passord inside. They should
  not show up in the logfile.(#38897)
* Mon Apr 19 2004 visnov@suse.cz
- revert fix for #38568, it breaks yast2-backup
- 2.9.82
* Fri Apr 16 2004 visnov@suse.cz
- 2.9.81
* Thu Apr 15 2004 visnov@suse.cz
- implemented QueryWidget ( `Items ) for `Table (#38909)
* Thu Apr 15 2004 visnov@suse.cz
- log also arguments when doing WFM::call (#39002)
* Thu Apr 15 2004 mvidner@suse.cz
- ensure that there's only one WFM (#37338)
- 2.9.80
* Thu Apr 15 2004 kkaempf@suse.de
- improve error message for "... type>>" typos (#38967)
* Thu Apr 15 2004 visnov@suse.cz
- show nil warning even for builtins (#38568)
- handle incorrect function redefinition gracefully (#37366)
- use the common type for if/then/else unless it's void
- accept block as a parameter for functions
* Wed Apr 14 2004 visnov@suse.cz
- fix recursion (#38596)
* Tue Apr 13 2004 visnov@suse.cz
- Document localization builtins (#38171)
* Tue Apr 13 2004 mvidner@suse.cz
- initialize stub UI when invoked from Perl (#37338)
- 2.9.79
* Tue Apr  6 2004 kkaempf@suse.de
- check strings from hwinfo properly (#36080)
- 2.9.78
* Tue Apr  6 2004 visnov@suse.cz
- Don't print superflous characters to stdout (#38327)
* Mon Apr  5 2004 ma@suse.de
- Send correct size of source packages to install
  in callbacks.
* Mon Apr  5 2004 ma@suse.de
- Include source packages to install in disk usage
  calculation. (#38257)
- 2.9.76
* Fri Apr  2 2004 msvec@suse.cz
- fixed agent-probe to report correct requires (#37335)
- 2.9.75
* Fri Apr  2 2004 visnov@suse.cz
- YaST is now GPL
- 2.9.76
* Thu Apr  1 2004 visnov@suse.cz
- restore textdomain at the end of included file (#36989)
* Wed Mar 31 2004 sh@suse.de
- implemented UI::QueryWidget() for wizard
* Tue Mar 30 2004 arvin@suse.de
- fixed setting of YAST_IS_RUNNING (bug #37536)
* Tue Mar 30 2004 sh@suse.de
- Fixed bug #37534: MultiSelectionBox returns [nil] without item
  IDs
* Tue Mar 30 2004 sh@suse.de
- added `opt(`treeEnabled) for wizard widget
* Tue Mar 30 2004 kkaempf@suse.de
- sync agent-probe with current hwinfo, add wlan, block, and tape
  probing flags.
* Mon Mar 29 2004 kkaempf@suse.de
- improve checking if default of bracket operator is void (#36922)
* Mon Mar 29 2004 arvin@suse.de
- fixed uml detection
* Mon Mar 29 2004 visnov@suse.cz
- 2.9.70
* Mon Mar 29 2004 visnov@suse.cz
- properly initialize domain (#36711)
* Mon Mar 29 2004 kkaempf@suse.de
- improve checking if rhs in assignment is void (#36922)
* Fri Mar 26 2004 arvin@suse.de
- added uml detection
* Fri Mar 26 2004 kkaempf@suse.de
- enhance type information for 'is()' (#37146)
* Fri Mar 26 2004 visnov@suse.cz
- 2.9.68
* Fri Mar 26 2004 visnov@suse.cz
- handle closing of default SCR gracefully (#37050)
- do not allow to pass 'nil' to Pkg (#37052)
- show full function name for parameter mismatch (#36924)
* Thu Mar 25 2004 kkaempf@suse.de
- warn if rhs of assignment is a void function (#36922)
* Thu Mar 25 2004 kkaempf@suse.de
- treat empty block after 'if' properly (#36902)
* Wed Mar 24 2004 kkaempf@suse.de
- treat _("") as "", don't call dgettext() (#36850)
* Wed Mar 24 2004 sh@suse.de
- Fixed bug #36802: Combo box returns nil instead of ""
* Wed Mar 24 2004 visnov@suse.cz
- empty void function produces just warning (#35536)
* Tue Mar 23 2004 visnov@suse.cz
- allow repeated use of Pkg in ycpc (#35533)
- close include files (#36747)
* Tue Mar 23 2004 sh@suse.de
- Fixed blocker bug #36779: Segfault on UI::QueryWidget(ComboBox)
* Tue Mar 23 2004 kkaempf@suse.de
- don't complain about bad cast if the to-be-casted expression
  is already wrong (#36751)
* Tue Mar 23 2004 mvidner@suse.cz
- check that external agents returned the correct type (#35363)
- 2.9.66
* Tue Mar 23 2004 kkaempf@suse.de
- check for function type in "<name> (...)" properly (#36246)
* Mon Mar 22 2004 cschum@suse.de
- Repackage tarball
- 2.9.65
* Mon Mar 22 2004 cschum@suse.de
- Adapt to changes of PMYouServer in packagemanager.
- 2.9.64
* Mon Mar 22 2004 visnov@suse.cz
- 2.9.63
* Fri Mar 19 2004 kkaempf@suse.de
- add "dgettext" and "dngettext" builtins to support easy
  re-translation after language change.
* Fri Mar 19 2004 mvidner@suse.cz
- added AGENT_LIBADD so that agents work from standalone Perl
* Thu Mar 18 2004 ma@suse.de
- Let Pkg::CommitProvide Callback report progress, if package is
  downloaded via ftp/http.
- 2.9.62
* Wed Mar 17 2004 mvidner@suse.cz
- include MemUsage.h unconditionally, let *it* (un)define D_MEMUSAGE
* Wed Mar 17 2004 visnov@suse.cz
- don't pass YCPNull to UI builtins
* Tue Mar 16 2004 ma@suse.de
- Added Pkg::CallbackStartDownload, Pkg::CallbackProgressDownload
  and Pkg::CallbackDoneDownload. Triggered from y2pm when downloading
  files via ftp/http.
- 2.9.61
* Mon Mar 15 2004 visnov@suse.cz
- 2.9.60
* Sun Mar 14 2004 kkaempf@suse.de
- use Ustring for all strings
- drop last pointer from linked lists
- drop unused Type::setNocheck
- delete m_parameterblock from YEBuiltin if not used
* Fri Mar 12 2004 sh@suse.de
- Fixed non-const reference to const ref for all widget constructors
* Fri Mar 12 2004 kkaempf@suse.de
- add <string> + <symbol> builtin (#35830)
* Fri Mar 12 2004 visnov@suse.cz
- drop unneeded type info
- 2.9.58
* Thu Mar 11 2004 ma@suse.de
- Added: Pkg::PkgSolveCheckTargetOnly and Pkg::PkgGetFilelist
* Thu Mar 11 2004 visnov@suse.cz
- don't load libpy2remote for "remote" component (#35536)
* Thu Mar 11 2004 kkaempf@suse.de
- improve type determination of list and map constants (#35567)
* Wed Mar 10 2004 jsrain@suse.de
- probe agent returns additional info for ccw devices
- moved additional info for scsi devices to "detail" submap
* Wed Mar 10 2004 kkaempf@suse.de
- fix whitespace handling in agent-resolver (#34888)
- fix parameter check for Pkg::SetAdditionalLocales (#35609)
* Wed Mar 10 2004 sh@suse.de
- V 2.9.57
- Suppressed UI::WizardCommand() complaints if no wizard present
* Tue Mar  9 2004 visnov@suse.cz
- save/restore argument list in WFM:Call (in doActualWork actually)
* Mon Mar  8 2004 kkaempf@suse.de
- haskey() should accept any key (#35465)
- 2.9.55
* Mon Mar  8 2004 jsrain@suse.de
- probe agent returns additional info for SCSI discs
- 2.9.54
* Sun Mar  7 2004 kkaempf@suse.de
- use propagation information from Type::match in Type::canCast
* Sun Mar  7 2004 kkaempf@suse.de
- add UI::WizardCommand (sh@suse.de)
* Fri Mar  5 2004 mvidner@suse.cz
- enabled nested::namespaces in the scanner
* Thu Mar  4 2004 ma@suse.de
- WFM: Added Pkg::PkgGetLicenseToConfirm and Pkg::PkgGetLicensesToConfirm
- 2.9.52
* Wed Mar  3 2004 kkaempf@suse.de
- implement stricter type checking for builtin functions and
  bracket assignment
- 2.9.51
* Wed Mar  3 2004 kkaempf@suse.de
- support new hwinfo fields "sysfs_bus_id" and "hwaddr"
- 2.9.50
* Tue Mar  2 2004 msvec@suse.cz
- disabled part of the agents-perl testsute (byteblock)
- 2.9.49
* Mon Mar  1 2004 sh@suse.de
- Enable saving of screen shot name if recording macro
* Mon Mar  1 2004 mvidner@suse.cz
- ycp.pm: implemented byteblocks
- 2.9.47
* Mon Mar  1 2004 cschum@suse.de
  WFM: - Added Pkg::CallbackYouMessage, Pkg::CallbackYouError and
    Pkg::CallbackYouLog.
  - Renamed Pkg::YouGetPatches to Pkg::YouRetrievePatchInfo.
  - Renamed Pkg::YouGetPackages to Pkg::YouRetrievePatches.
  - Removed obsolete functions Pkg::YouAttachSource,
    Pkg::YouDisconnect, Pkg::YouFinish, Pkg::YouFirstPatch,
    Pkg::YouGetCurrentPatch, Pkg::YouInstallCurrentPatch and
    Pkg::YouNextPatch.
- 2.9.46
* Mon Mar  1 2004 kkaempf@suse.de
- properly add all device resources to output list (#35190)
* Sat Feb 28 2004 kkaempf@suse.de
- use 'new' to allocate char buffer for SymbolEntry, so it can
  be safely 'delete'd
- share type pointers instead of creating new ones.
* Sat Feb 28 2004 kkaempf@suse.de
- improve usage of existing type information for builtin
  functions
- fix bytecode input to be upward compatible with previous
  version
- properly release unneeded memory
- 2.9.44
* Fri Feb 27 2004 visnov@suse.cz
- added openslp to neededforbuild
* Fri Feb 27 2004 visnov@suse.cz
- ycodeptr branch merge:
  - counted pointers for YCode and SymbolEntry
  - allow to start bytecode clients
  - initialization of namespaces now in Y2Namespace
  - improved flex type matching
* Wed Feb 25 2004 ma@suse.de
- Adapt to new Y2PM locale setting interface.
- 2.9.43
* Mon Feb 23 2004 visnov@suse.cz
- reinitialize preloaded namespaces before new parsing, not after the
  last one
* Sun Feb 22 2004 kkaempf@suse.de
- restore filename at end of parser, adapt testcases
- 2.9.41
* Sun Feb 22 2004 kkaempf@suse.de
- don't delete YConst code
- 2.9.40
* Sat Feb 21 2004 ma@suse.de
- Reimplemented counted pointer classes
- 2.9.39
* Fri Feb 20 2004 visnov@suse.cz
- correctly free code in YEBinary and YETriple
- don't create a table entry for filename in block
- free the code after optimizing it out
* Fri Feb 20 2004 arvin@suse.de
- fix Pkg::SourceEditGet, Pkg::SourceEditSet and Pkg::SourceScan
- fixed seg. fault with unresolved xref's
* Fri Feb 20 2004 visnov@suse.cz
- more memory fixes:
  allow YCPCode to free the code (used in system agent)
  share textdomain (helps in reading bytecode)
  delete parameter block for builtins
- 2.9.37
* Thu Feb 19 2004 visnov@suse.cz
- memory fixes:
  lazy initialization of a symbol table
  free function declarations/definitions in client calls
* Thu Feb 19 2004 mvidner@suse.cz
- sort (`a, `b, l, ``( a<b ) )
  now uses std::sort instead of bubblesort:
  the comparison must be irreflexive (no "<=")
- 2.9.36
* Wed Feb 18 2004 mvidner@suse.cz
- added SCR::Error
- 2.9.35
* Wed Feb 18 2004 visnov@suse.cz
- drop unused md5 implementation
- fix memory leak in reading bytecode header
* Tue Feb 17 2004 mvidner@suse.cz
- fixed leaks:
  parsed code in Y2WFMComponent::CallFunction and SCRAgent::readconf
- reduced memory consumption a bit:
  reduced SymbolTable size from 211 to 31
  TableEntry::m_inner removed
- count objects using MemUsage (liby2util).
- 2.9.34
* Mon Feb 16 2004 kkaempf@suse.de
- properly support indirect function calls via pointers (#34579)
* Mon Feb 16 2004 mvidner@suse.cz
- don't segfault when agent output cannot be parsed (#34581)
* Mon Feb 16 2004 mvidner@suse.cz
- ini agent: ignore_case is incompatible with multiple files
- ycpc: re-add trailing newlines (should fix yast2-nis-client)
- 2.9.32
* Fri Feb 13 2004 kkaempf@suse.de
- replace module timestamps with import lists checking the
  actually used signatures with the provided ones.
- enhance parsetime and runtime error information with better
  file/line tracking
- enhance 'ycpc' with a dependency checker
* Fri Feb 13 2004 sh@suse.de
- Late creation of UI: UI is only created when the first UI
  builtin is actually used, so for command line YCP scripts
  no UI is needed any longer and thus no X connection (for Qt)
  or controlling tty (for NCurses)
* Thu Feb 12 2004 arvin@suse.de
- moved program ycpc to main package
* Thu Feb 12 2004 arvin@suse.de
- added some udev and sysfs info in probe agent (bug #34355)
* Tue Feb 10 2004 arvin@suse.de
- include YWizard.h in yast2-core-devel
* Tue Feb 10 2004 visnov@suse.cz
- fixed crash when trying to apply bracket operator to nil.
* Mon Feb  9 2004 visnov@suse.cz
- Revert y2error -> y2warning for UI builtin without an instance.
- ycpc now prints errors and warnings to stderr by default
* Mon Feb  9 2004 arvin@suse.de
- fixed building on s390
* Fri Feb  6 2004 sh@suse.de
- Re-enabled macro player with new interpreter
* Fri Feb  6 2004 visnov@suse.cz
- Fix UI::changeWidget for terms in `Table
* Thu Feb  5 2004 msvec@suse.cz
- log YCP file and line in dummy agent to limit testsuites output
- 2.9.25
* Tue Feb  3 2004 visnov@suse.cz
- Fix memory corruption on duplicate function parameters.
- 2.9.24
* Tue Feb  3 2004 visnov@suse.cz
- Fix UI::queryWidget for terms in `Table
* Tue Feb  3 2004 visnov@suse.cz
- Fix some Pkg builtins
* Tue Feb  3 2004 visnov@suse.cz
- Don't do fancy testsuite presentation
* Tue Feb  3 2004 gs@suse.de
- make language change known in Y2WFMComponent::SetLanguage
* Tue Feb  3 2004 kkaempf@suse.de
- Fix type for YEBuiltin (#34249)
* Tue Feb  3 2004 visnov@suse.cz
- ycpc puts a new line at the end for -E (msvec@suse.cz)
* Mon Feb  2 2004 msvec@suse.cz
- fixed resolver agent creation
* Fri Jan 30 2004 visnov@suse.cz
- for lookup use the same code as for bracket
- bytecode version change!
* Fri Jan 30 2004 visnov@suse.cz
- implemented constant evaluation of terms (#34167)
- bytecode change
* Thu Jan 29 2004 msvec@suse.cz
- 2.9.23
* Thu Jan 29 2004 visnov@suse.cz
- temporary fix bytecode testsuite for nonroot build
- UI emits only warning not error if no handler is available
* Thu Jan 29 2004 mvidner@suse.cz
- ini agent: make parent directories when writing files
  (useful eg. for CA management)
- fixed bugs revealed by -Woverloaded-virtual
* Thu Jan 29 2004 visnov@suse.cz
- don't distribute bison-generated code
* Thu Jan 29 2004 mvidner@suse.cz
- fixed YError::toString signature
- libycp/testsuite runs again (added xfail)
* Wed Jan 28 2004 arvin@suse.de
- fixed testsuite
* Wed Jan 28 2004 nashif@suse.de
- Added builtin Pkg::PkgProperties to retrieve more data about
  package location and source
* Tue Jan 27 2004 mvidner@suse.cz
- moved agent-ypserv to yast2-nis-client
  and agent-losetup to yast2-storage
* Tue Jan 27 2004 sh@suse.de
- V 2.9.21
- Consistent naming scheme in UI
* Tue Jan 27 2004 visnov@suse.cz
- remove url parameter from Pkg::YouGetPatches
* Tue Jan 27 2004 kkaempf@suse.de
- fix cast vs. bracket precedence (#34156)
* Tue Jan 27 2004 visnov@suse.cz
- always bind textdomain (even in bytecode)
- set textdomain codeset to UTF-8
* Mon Jan 26 2004 visnov@suse.cz
- fix "return nil;" endless loop
- 2.9.19
* Mon Jan 26 2004 mvidner@suse.cz
- ycpc: progress to stderr, can parse stdin (ycpc -E -)
* Fri Jan 23 2004 msvec@suse.cz
- added possibility to use a custom log.conf
- 2.9.18
* Fri Jan 23 2004 visnov@suse.cz
- this is "The New Interpreter" release
* Fri Jan 16 2004 arvin@suse.de
- implemented stack for each ycp callback of packagemanager
* Thu Jan 15 2004 mvidner@suse.cz
- agents-perl: added YaST::SCRAgent
- agent-probe: return also SMBIOS info for .bios subpath (lslezak)
- dropped WFM::GetClientName (arvin)
- 2.9.17
* Thu Jan  8 2004 mvidner@suse.cz
- ini agent: Read/Write (.all)
- fixes for a nonstandard prefix
- 2.9.16
* Thu Jan  8 2004 arvin@suse.de
- adapted to bison 1.875
* Mon Jan  5 2004 visnov@suse.cz
- ignore quotes in scr also for testsuites
- 2.9.14
* Tue Dec 16 2003 mvidner@suse.cz
- ini agent: allow multiple values for the same key
- 2.9.13
* Mon Dec 15 2003 ma@suse.de
- Removed outdated Pkg::SelectionsUpdateAll
- 2.9.11
* Fri Dec 12 2003 msvec@suse.cz
- adapted for the logging changes in liby2util
- 2.9.12
* Fri Dec  5 2003 mvidner@suse.cz
- ycp.pm: accept `Command(...) as well as Command(...)
* Thu Dec  4 2003 ma@suse.de
- Added Pkg::SourceEdit/GetSourceEditSet for instsource editor.
- 2.9.9
* Tue Dec  2 2003 visnov@suse.cz
- fix function prototypes
* Tue Dec  2 2003 msvec@suse.cz
- better logging in the dummy agent (needs newer testsuite)
- migrated modules agent to use modprobe.conf (2.6 kernel)
- 2.9.8
* Thu Nov 27 2003 visnov@suse.cz
- ignore function prototypes
- ignore variable references from NI
* Mon Nov 24 2003 ma@suse.de
- Overworked Pkg::Source... functions. Removed internal InstSrc cache
  and install order list (we've got an InstSrcManager for this).
- 2.9.7
* Fri Nov 14 2003 visnov@suse.cz
- allow map to specify its types like map<string,integer>
- 2.9.6
* Thu Nov 13 2003 gs@suse.de
- libyui: KeyEvent added
* Mon Nov 10 2003 visnov@suse.cz
- allow block also specify a return type (ignored)
- WFM::call () is now the same as WFM::CallFunction ()
- fix mapmap () and maplist () if returning a map
- 2.9.5
* Thu Nov  6 2003 mvidner@suse.cz
- Using doxygen instead of kdoc.
- 2.9.4
* Wed Oct 22 2003 visnov@suse.cz
- implemented mapmap and listmap accepting also $[] as a result
  of the block.
* Wed Oct 22 2003 visnov@suse.cz
- workaround to allow quotes in scrfiles
- 2.9.3
* Thu Oct 16 2003 visnov@suse.cz
- added support for typecast syntax and list<type> syntax
  of typed lists.
- 2.9.2
* Thu Oct  2 2003 arvin@suse.de
- fixed compiling of losetup agent
* Sun Sep 21 2003 arvin@suse.de
- extended MediaChange callback to support double sided media
* Fri Sep 19 2003 ma@suse.de
- If SourceStartCache(enabled==true) is requested, check InstSrcManager
  to see whether sources are realy enabled. 'Change source of installation'
  for example starts the InstSrcManager without autoenabling the sources.
  (#29324)
- 2.8.34
* Thu Sep 18 2003 kkaempf@suse.de
- pass "family" and "model" for .probe.cpu also on x86_64 (#31305)
* Wed Sep 17 2003 arvin@suse.de
- better return value of PkgUpdateAll
* Tue Sep 16 2003 jsuchome@suse.cz
- adapted ag_hostnames to return list of IP's (#30996)
- 2.8.31
* Sun Sep 14 2003 arvin@suse.de
- implemented PkgReset function (bug #27970)
* Wed Sep 10 2003 arvin@suse.de
- fixed setting of YAST_IS_RUNNING (bug #30409)
* Wed Sep 10 2003 ma@suse.de
- Share PkgModule between multiple WFM interpreter instance.
  (#29324)
- 2.8.28
* Tue Sep  9 2003 ma@suse.de
- Fixed DoneProvide callback to send package name as third arg
  on error (#29922)
- 2.8.27
* Sun Sep  7 2003 ma@suse.de
- Fixed TargetInit and TargetFinish calls.
  (#29679 as far as PKG module is affected)
- 2.8.26
* Fri Sep  5 2003 sh@suse.de
- V 2.8.25
- Fixed bug #30151: Enable starting pkg mgr in search mode
  by default in the installed system
* Fri Sep  5 2003 gs@suse.de
- testsuite adapted (language.err)
- 2.8.24
* Thu Sep  4 2003 gs@suse.de
- WFMInterpreter: get correct encoding in SetLanguage()
- 2.8.23
* Thu Aug 28 2003 ma@suse.de
- Adapted PKG module to new packagemanager callbacks.
- Introduced CallbackStartConvertDb, CallbackProgressConvertDb,
  CallbackNotifyConvertDb, CallbackStopConvertDb. (#29484 as far as
  PKG module is affected).
- 2.8.22
* Mon Aug 25 2003 kkeil@suse.de
- new ISDN interface for agent-probe, data is now based on CDB
* Wed Aug 20 2003 mjancar@suse.cz
- require the perl version we build with
* Mon Aug 18 2003 arvin@suse.de
- added ycp builtin findlastnotof
* Mon Aug 18 2003 lslezak@suse.cz
- fixes in ag_background (result command check, buffer size check,
  log errors)
- enhancements in libyui examples (gs@suse.de)
- version 2.8.18
* Tue Aug 12 2003 arvin@suse.de
- added warnings about to libyui about wrong widget tree structure
- fixed parsing of class tag in make_widget_doc
- also handle release notes url here
* Wed Aug  6 2003 gs@suse.de
- V 2.8.16
- WFM setLanguage() returns proposed encoding
  (revert changes)
* Wed Aug  6 2003 fehr@suse.de
- added new ycp builtin regexppos
- version 2.8.15
* Tue Aug  5 2003 arvin@suse.de
- fixed testsuite
* Tue Aug  5 2003 gs@suse.de
- V 2.8.13
- libyui: YUI builtin SetKeyboard added
* Thu Jul 31 2003 arvin@suse.de
- support special plugins with several agents
* Wed Jul 30 2003 arvin@suse.de
- fixed build
* Tue Jul 29 2003 sh@suse.de
- V 2.8.11
- Added support for embedded Perl interpreter as plugin
  (requires new additional package yast2-perl-bindings)
* Tue Jul 29 2003 arvin@suse.de
- extended meaning of YAST_IS_RUNNING
* Tue Jul 29 2003 cschum@suse.de
- WFM: Added Pkg::YouDisconnect().
* Mon Jul 21 2003 arvin@suse.de
- handle new hwinfo-field unix_dev_name2 (bug #26121)
* Tue Jul 15 2003 arvin@suse.de
- fixed testsuite of wfm
* Tue Jul 15 2003 sh@suse.de
- V 2.8.7
  UI changes:
- Lots of internal reworking
- Completely reworked event handling
- No more self-generated events during widget creation / ChangeWidget
- Basic support for right-to-left languages like Arabic / Hebrew
  (not perfect yet)
- `id() now optional for UI builtins if ID type is symbol
* Tue Jul 15 2003 gs@suse.de
- 2.8.6
- advanced event handling in libyui
* Tue Jul 15 2003 mvidner@suse.cz
- Moved ycp.pm to %%perl_vendorlib.
* Thu Jul 10 2003 mvidner@suse.cz
- perl library:
  * parse paths with quoted components
  * consider also negative integers in ycp::Return
* Wed Jul  9 2003 cschum@suse.de
- WFM: Added Pkg::YouSetServer().
* Mon Jul  7 2003 gs@suse.de
- WFMInterpreter: call setlocale(LC_ALL, "") in constructor;
  remove it in setLanguage() and changeToModuleLanguage()
* Fri Jul  4 2003 msvec@suse.de
- keep the include modules.conf.local at the end (#27681)
- dropped unused modules paths
- updated testsuite
- 2.8.5
* Wed Jul  2 2003 visnov@suse.de
- return boolean value from client as exit code
* Fri Jun 27 2003 msvec@suse.de
- different fix for regexp*
- 2.8.4
* Thu Jun 26 2003 msvec@suse.de
- fixed regexpsub behavior
- 2.8.3
* Wed Jun 25 2003 cschum@suse.de
- Removed WFM builtin CallFile as it isn't needed anymore by YOU.
* Wed Jun 25 2003 arvin@suse.de
- correct C++ syntax in HwProbe.cc
* Tue Jun 24 2003 cschum@suse.de
- Removed classes ExternalProgram and ExternalDataSource from
  liby2 as they duplicated the classes from liby2util.
* Tue Jun 24 2003 cschum@suse.de
- Added progress callback for execution of scripts by YOU.
* Tue Jun 10 2003 arvin@suse.de
- fixed file list for rpm v4
* Fri Jun  6 2003 mvidner@suse.cz
- libycp scanner: don't mistake an invalid token for EOF.
* Wed May 28 2003 cschum@suse.de
- Added WFM builtin CallFile needed by YOU.
* Tue Apr 22 2003 arvin@suse.de
- added ycp function lsort to sort lists of strings with
  respect to the current locale (bug #23850)
* Fri Mar 28 2003 mvidner@suse.de
- ag_hostnames: added scanning for RPC servers
* Fri Mar 28 2003 lslezak@suse.de
- ag_background: limited input buffer size, added .buffer_size
  subpath, updated documentation
- 2.8.0
* Thu Mar 13 2003 kkaempf@suse.de
- handle installation of source packages (#25318).
- 2.7.34
* Tue Mar 11 2003 kkaempf@suse.de
- fix parseycp syntax checker to detect trailing errors
  after a successful parse. Also fixes detection and
  handling of EOF in parser. (#24994)
* Sat Mar  8 2003 arvin@suse.de
- handle wlan flag from hwinfo (bug #23491)
* Fri Mar  7 2003 arvin@suse.de
- make string compare function locale unaware again as it leads
  to strange results after changing the locale
* Fri Mar  7 2003 kkaempf@suse.de
- close target logfile at shutdown (#24756)
- 2.7.30
* Wed Mar  5 2003 kkaempf@suse.de
- enhance provideDone and packageDone callbacks to return a
  string in order to control retry/abort/ignore on package
  errors (#23780)
- 2.7.29
* Tue Mar  4 2003 arvin@suse.de
- handle InstSrcDescr::content_flags (bug #21561)
* Tue Mar  4 2003 kkaempf@suse.de
- use general state functions from packagemanager, not just
  the package specific ones (part of #23616)
* Mon Mar  3 2003 kkaempf@suse.de
- use packagemanager stati when handling selection, so upgrade
  properly gets required and recommended selections too (#24371).
* Mon Mar  3 2003 cschum@suse.de
- Allow installation sources for different products from same URL
  (#24492).
* Fri Feb 28 2003 kkaempf@suse.de
- make MediaChangeCallback global for all sources (part of #24201)
* Fri Feb 28 2003 sh@suse.de
- Added optional "floppyDevice" parameter to YPackageSelector widget
* Fri Feb 28 2003 kkaempf@suse.de
- don't treat nl_langinfo() as godsend, they're all lying anyway.
  We return nl_langinfo as a propsed encoding only and set UTF-8
  (#24383)
* Tue Feb 25 2003 arvin@suse.de
- use locale dependent string compare (bug #23850)
* Tue Feb 25 2003 gs@suse.de
- #include <assert.h> in YUIInterpreter_special_widgets.cc
* Mon Feb 24 2003 gs@suse.de
- setLanguage: call nl_langinfo (bug #23348)
* Mon Feb 24 2003 kkaempf@suse.de
- finally fix Pkg:: functions to act upon tag string
  instead of package names.
  This will make "yast2 -i <name-of-.so>" possible.
* Mon Feb 24 2003 arvin@suse.de
- added command .bash_input to system agent
* Fri Feb 21 2003 kkaempf@suse.de
- add Pkg::SelectionContent() function (#23589)
  adpated testsuite accordingly.
* Thu Feb 20 2003 arvin@suse.de
- resolver agent doesn't complain about empty lists (bug #23797)
* Thu Feb 20 2003 arvin@suse.de
- added dsl modem (pppoe) detection to probe-agent (bug #23662)
* Wed Feb 19 2003 sh@suse.de
- Fixed bug #23781: YCPthread problems during SuSEconfig
* Mon Feb 17 2003 gs@suse.de
- don't call nl_langinfo in WMFInterpreter setLanguage
  (encoding is not set correctly, bug #23348)
* Mon Feb 17 2003 sh@suse.de
- Fixed bug #23599: Recode: unexpected small output buffer
* Thu Feb 13 2003 sh@suse.de
- Reduced log severity for UI shortcut conflicts
* Wed Feb 12 2003 kkaempf@suse.de
- add Pkg::TargetFileHasOwner() (#23555)
* Tue Feb 11 2003 sh@suse.de
- New generic way to find widgets belonging to a dialog, excluding
  sub-dialogs: YDialog::widgets()
* Fri Feb  7 2003 kkaempf@suse.de
- call nl_langinfo() if no explicit encoding given (#23348)
- V 2.7.12
* Mon Feb  3 2003 sh@suse.de
- V 2.7.11
- New UI builtin: SetFunctionKeys()
* Mon Jan 27 2003 arvin@suse.de
- added rpm-devel, popt and popt-devel to neededforbuild
* Thu Jan 23 2003 mvidner@suse.de
- Activate the debugger on receiving SIGUSR2.
- 2.7.9
* Tue Jan 21 2003 arvin@suse.de
- make it build with latest yast2-packagemanager
* Tue Jan 14 2003 arvin@suse.de
- probe agent handles capability flags of libhd (bug #20068)
* Fri Dec 20 2002 arvin@suse.de
- merged from 8.1 branch:
  - set umask to 0022 in genericfronted.cc
* Thu Dec 19 2002 cschum@suse.de
- Pkg:: interface
  - Added ErrorDetails() function.
  - Added YouFinish() function.
  - Added callback handling for YOU progress.
- 2.7.6
* Wed Dec 18 2002 mvidner@suse.de
- perl library:
  * Fixed parsing compounds containing a number starting with 0.
  * Use the script base name as the log component instead of "perl".
* Mon Dec  2 2002 arvin@suse.de
- consider all four environment variables `LANGUAGE', `LC_ALL',
  `LC_MESSAGES' and `LANG' to get the language during startup
  (bug #22008)
* Mon Dec  2 2002 arvin@suse.de
- fixed linking (after drop of dumpto agent)
* Fri Nov 29 2002 sh@suse.de
- Fixed bug/wish #13866: Delayed keyboard shortcut checking
  New UI builtins PostponeShortcutCheck(), CheckShortcuts()
* Fri Nov 22 2002 msvec@suse.cz
- system agent:
  * background logging
  * nice mode for written ycp values
  * updated testsuite
- modules agent:
  * use paths for the modules specs
- dumpto agent:
  * drop (obsoleted by system agent)
- runtime agent:
  * drop (obsoleted by system agent)
* Wed Nov 20 2002 sh@suse.de
- UI::MakeScreenShot() now takes a string argument
* Mon Nov 11 2002 sh@suse.de
- New widget: IconButton
* Thu Nov  7 2002 arvin@suse.de
- adaption of libycp for bison version 1.75
* Thu Nov  7 2002 sh@suse.de
- Fixed bug #19389: Frame widget shows keyboard shortcuts, but
  can't handle any
* Wed Nov  6 2002 sh@suse.de
- New UI builtins:
  - AskForExistingDirectory()
  - AskForExistingFile()
  - AskForSaveFileName()
* Wed Nov  6 2002 mvidner@suse.cz
- Fixed recursive Dir in ini-agent flat mode (used for .sysconfig)
  [#21574]
* Tue Oct 15 2002 kkaempf@suse.de
- fix 'sort' testcase
- 2.6.53
* Mon Oct 14 2002 kkaempf@suse.de
- reduce debug log (#20854, mvidner@suse.cz)
- 2.6.52
* Mon Oct 14 2002 kkaempf@suse.de
- when switching base selection, reset selections
  and packages
- RemoteComponent: check for null to avoid segfault (#20087, arvin)
* Wed Oct  9 2002 kkaempf@suse.de
- install product data in installation order.
- 2.6.51
* Tue Oct  8 2002 kkaempf@suse.de
- add functions to display install time splitted across
  multiple sources and multiple media within each source
- 2.6.50
* Tue Oct  8 2002 arvin@suse.de
- use own version as suse version since suse version is not
  present on united linux
* Mon Oct  7 2002 kkaempf@suse.de
- add Pkg:: function to set installation order (#20609)
- add Pkg:: function to disable ram caching of source meta-data
- 2.6.48
* Fri Sep 20 2002 kkaempf@suse.de
- provide full product data including base and dist product
- 2.6.47
* Fri Sep 20 2002 kkaempf@suse.de
- add SourceChange callback
- write selections conflicts to /var/log/YaST2/badselections
- 2.6.46
* Thu Sep 19 2002 kkaempf@suse.de
- return partition size after package installation in DU check.
- disable source (release media) before delete.
- 2.6.45
* Wed Sep 18 2002 kkaempf@suse.de
- add Pkg:: functions for multiple source installation
- 2.6.44
* Thu Sep 12 2002 kkaempf@suse.de
- drop "-" in product string
- 2.6.43
* Wed Sep 11 2002 kkaempf@suse.de
- implement "PkgNeutral" to neutralize the status of
  a package (#19475)
- implement status save/restore (#19328)
- fix abort during install (#18954)
- 2.6.42
* Wed Sep 11 2002 kkaempf@suse.de
- copy product and selection data to target (#19324)
- 2.6.41
* Wed Sep 11 2002 kkaempf@suse.de
- allow rewrite of url if cdrom device changed due
  to ide-scsi (#19185)
- 2.6.40
* Tue Sep 10 2002 kkaempf@suse.de
- correctly release sources
- pass flag to solver to prefer installed packages in
  case of conflict during update
- products don't have a release, just a version
- 2.6.39
* Tue Sep 10 2002 arvin@suse.de
- provide/obsolete yast2-lib64-compat (bug #19325)
* Mon Sep  9 2002 kkaempf@suse.de
- display all CDs, even those with no packages to install
- handle uninstalled source packages
- 2.6.37
* Mon Sep  9 2002 arvin@suse.de
- explicit set permissions of /etc/resolv.conf to 0644 (bug #19188)
* Mon Sep  9 2002 kkaempf@suse.de
- reduce logging
- fix space calculation
- 2.6.35
* Sun Sep  8 2002 kkaempf@suse.de
- add function to retrieve space calculation
- 2.6.34
* Sun Sep  8 2002 kkaempf@suse.de
- add function to pass directories to space calculation in
  package manager
- 2.6.33
* Sat Sep  7 2002 mvidner@suse.cz
- agent-ini: section names  for multifile data were not translated
  properly upon second Write (#19066).
- 2.6.32
* Sat Sep  7 2002 kkaempf@suse.de
- add Pkg::PkgGroup to get group tag of a package
* Sat Sep  7 2002 kkaempf@suse.de
- include url to media change callback
- report translated selection label
- 2.6.31
* Fri Sep  6 2002 arvin@suse.de
- provide/obsolete more old packages
* Fri Sep  6 2002 kkaempf@suse.de
- fix update api, allow for deletion of old packages
  return number of unknown packages
- fix packager UI to show unknown packages
- 2.6.29
* Thu Sep  5 2002 kkaempf@suse.de
- add Pkg:: functions for package backup
  and rebuilddb progress
- 2.6.28
* Wed Sep  4 2002 kkaempf@suse.de
- check for loops in selection requirements.
- authorization checks for YOU.
- 2.6.27
* Tue Sep  3 2002 kkaempf@suse.de
- enhanced callback handling for Pkg::
- product data access functions
- 2.6.26
* Tue Sep  3 2002 mvidner@suse.cz
- kdoc cleanup: better cross references and fixed some parsing issues.
* Fri Aug 30 2002 mvidner@suse.cz
- ag_hostnames: fixed ip to host name translation (#18638).
- 2.6.25
* Thu Aug 29 2002 sh@suse.de
- New widget options for YPushButton: key_F1 .. key_F12
- New widget option for YSelectionBox: immediate
- New widget options for YPackageSelector: youMode, updateMode
* Thu Aug 29 2002 arvin@suse.de
- more fixes for initialization of logging
* Wed Aug 28 2002 kkaempf@suse.de
- more Pkg:: functions for media change via packagemanager
  callbacks
- 2.6.23
* Tue Aug 27 2002 arvin@suse.de
- added support for firewire controllers in probe agent
  (bug #18379)
- fixed initialization of logging
* Wed Aug 21 2002 kkaempf@suse.de
- furter connections to packagemanager
- V 2.6.21
* Mon Aug 19 2002 sh@suse.de
- V 2.6.20
- New package management in UI
* Fri Aug 16 2002 arvin@suse.de
- adaptions for libhd version 5.12
* Thu Aug 15 2002 arvin@suse.de
- added handling of hotplug entry to probe agent (bug #13571)
* Tue Aug 13 2002 arvin@suse.de
- fixed return value of regexpsub for case of no match
* Mon Aug 12 2002 kkaempf@suse.de
- add "vendor" and "name" keys to .probe.cpu map
* Fri Aug  9 2002 arvin@suse.de
- added support for dvb cards to probe agent
* Thu Aug  8 2002 arvin@suse.de
- fixed error logging for .string command of system agent and
  added testsuite for that
- redirect stdout and stderr to /dev/null for .bash_background
  command of system agent (bug #17223)
* Wed Aug  7 2002 arvin@suse.de
- adaption for libhd changes
* Mon Aug  5 2002 arvin@suse.de
- fixed cpu and boot detection on S390
* Thu Aug  1 2002 arvin@suse.de
- fixes for VNC installation
* Mon Jul 29 2002 arvin@suse.de
- disable Qt/KDE's own malloc implementation (it's too late to
  activated them from dlopen)
* Wed Jul 24 2002 kkaempf@suse.de
- Allow empty nameserver list in agent-resolver (#17178)
* Wed Jul 24 2002 arvin@suse.de
- Execute (.target.remove, ...) is now quiet (bug #17177)
* Wed Jul 24 2002 arvin@suse.de
- fixed error messages for Read (.target.yast2, ...) (bug #17170)
- fixed model entry in Read (.probe.cpu) (bug #17166)
* Mon Jul 22 2002 arvin@suse.de
- implemented stat and lstat functions in agent-system
* Mon Jul 22 2002 arvin@suse.de
- agent-probe recognizes boot mechanism grub from hwinfo
* Wed Jul 17 2002 arvin@suse.de
- provide full directory structure
- removed obsolete getyast2dir function from libycp
* Fri Jul 12 2002 kkeil@suse.de
- agent-probe: Additional fields for the ISDN database to
  identify DSL support and supported protocols and architectures
  of the driver.
* Mon Jul  8 2002 mvidner@suse.cz
- completed the Provides/Obsoletes list for the devel subpackage
* Thu Jul  4 2002 arvin@suse.de
- move non binary file from /usr/lib/YaST2 to /usr/share/YaST2
* Tue Jul  2 2002 msvec@suse.cz
- y2log dir is /var/log/YaST2 (#16712)
* Tue Jul  2 2002 arvin@suse.de
- only complain once if recode fails (bug #16773)
* Thu Jun 27 2002 arvin@suse.de
- the Read (.yast2, ...) of the system agent appends "data/" the
  the filename
- removed function Write (.yast2, ...) from system agent
* Tue Jun 25 2002 kkaempf@suse.de
- Evaluate keys in map constants (#16701).
* Fri Jun 21 2002 arvin@suse.de
- merged libycp, liby2, libyui, libscr, yast2-core-scr,
  yast2-core-wfm, yast2-agent-any, yast2-agent-probe,
  yast2-agent-ini, yast2-agent-modules, yast2-agent-system
  and yast2-base into new package yast2-core