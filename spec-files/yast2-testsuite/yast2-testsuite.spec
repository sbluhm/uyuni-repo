#
# spec file for package yast2-testsuite
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           yast2-testsuite
Version:        4.1.0
Release:        1.5

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  yast2-devtools >= 3.1.10
Requires:       dejagnu
Requires:       expect
# y2base -I includepath -M modulepath
Requires:       yast2-core >= 2.19.0

Summary:        YaST2 - Testsuite
License:        GPL-2.0-or-later
Group:          System/YaST

BuildArch:      noarch

%description
This is a package for the YaST2 modules testsuite preparation and
execution.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

%files
%defattr(-,root,root)
%{yast_moduledir}
%{yast_ydatadir}
%{yast_yncludedir}
%doc %{yast_docdir}
%license COPYING

%changelog
* Tue Feb 26 2019 José Iván López González <jlopez@suse.com>
- Version bump (bsc#1124009)
- 4.1.0
* Tue Oct 16 2018 schubi@suse.de
- Added license file to spec.
* Wed Aug 22 2018 schubi@suse.de
- Switched license in spec file from SPDX2 to SPDX3 format.
* Fri Apr  6 2018 mfilka@suse.com
- bnc#1087957 - version bump
- 4.0.0
* Fri Sep 16 2016 jreidinger@suse.com
- reduce build dependencies to speed up build (bnc#999203)
- 3.1.6
* Mon Jun  6 2016 igonzalezsosa@suse.com
- Stop generating autodocs (fate#320356)
- 3.1.5
* Tue May 17 2016 mvidner@suse.com
- Prevent failures with dejagnu-1.6 (bsc#979519).
- 3.1.4
* Mon Mar  7 2016 mvidner@suse.com
- Default Y2DIR to ../src to enable 'make check'
  before 'make install' (mchandras)
- 3.1.3
* Thu Jan 23 2014 mvidner@suse.com
- Save raw y2base logs in raw.tmp.err.TESTCASE
  The stupid harness design only lets some error messages through
  but this saves all of them for post mortem debugging.
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
* Mon Jul  1 2013 lslezak@suse.cz
- Removed useless BuildRequires: openslp-devel, popt-devel and
  perl-XML-Writer
- 2.24.4
* Sun Jun 23 2013 lslezak@suse.cz
- support .yh files converted to .rb in testedfiles
- 2.24.3
* Thu Jun 13 2013 lslezak@suse.cz
- skip files which do not have the corresponding stderr and stdout
  files, these are likely just include files, not real tests
* Thu May 16 2013 mvidner@suse.com
- correctly pass the logging produced by Testsuite.rb (bnc#819137).
- 2.24.2
* Tue May 14 2013 mvidner@suse.com
- Make "testedfiles" work on Ruby files (bnc#819137).
- 2.24.1
* Thu May  9 2013 mvidner@suse.cz
- Run Ruby test cases as well as YCP test cases (bnc#819137).
- 2.24.0
* Fri Sep 23 2011 lslezak@suse.cz
- removed obsoleted functions from Pkg.ycp
- 2.21.0
* Mon Dec 21 2009 aschnell@suse.de
- don't override Makefile.am
- extended runtest.sh
- 2.19.0
* Fri Dec 11 2009 aschnell@suse.de
- run all tests even if some fail
* Mon Jun 29 2009 mvidner@suse.cz
- Moved Summary and Description from PDB to spec.
* Tue Jun 16 2009 mvidner@suse.cz
- Using autodocs-ycp.ami, which contains a fix for automake 1.11.
* Tue Apr  8 2008 mvidner@suse.cz
- Enable make check before make install, by telling y2base to search
  first in ../src (fate#2306).
- 2.16.2
* Fri Feb 29 2008 coolo@suse.de
- fix buildrequires after yast2-core split
- 2.16.1
* Mon Nov  5 2007 mvidner@suse.cz
- Use ./test.ycp instead of test.ycp when building (#330965).
- 2.16.0
* Fri Aug 10 2007 mvidner@suse.cz
- Finished integrating Feature #120292, UI as a namespace callable
  from yast2-*-bindings.
- 2.15.1
* Wed Aug  8 2007 mvidner@suse.cz
- Adapted to changes in yast2-core needed for making UI callable from
  yast2-*-bindings.
  (The testsuite component is no longer usable because it does not
  provide the UI namespace)
- 2.15.0.1
* Thu Jul 12 2007 locilka@suse.cz
- 2.15.0
* Mon Nov 13 2006 jsrain@suse.cz
- 2.14.0
* Wed Sep 13 2006 mvidner@suse.cz
- Using yast2-devtools.pc instead of yast2-core.pc is fine.
  Now using --print-errors too.
- 2.13.3
* Tue Sep 12 2006 ro@suse.de
- temporary fix to run testsuite without yast2-core-devel
* Tue Sep 12 2006 mvidner@suse.cz
- Require only yast2-core, not yast2-core-devel.
- 2.13.2
* Tue Mar 21 2006 mvidner@suse.cz
- converted neededforbuild to BuildRequires,
  removed yast2-packagemanager
- 2.13.1
* Tue Jan 10 2006 mvidner@suse.cz
- Just bumped to 2.13
- 2.13.0
* Wed Jul 20 2005 mvidner@suse.cz
- Added libxml2[-devel] to NFB because of yast2-packagemanager.
- 2.12.3
* Fri Jul  8 2005 visnov@suse.cz
- Adapt build requirements for blocxx
- 2.12.2
* Tue May  3 2005 mvidner@suse.cz
- Do not use "default" as an identifier.
- 2.12.1
* Tue Dec 14 2004 mvidner@suse.cz
- Log y2errors from Perl the same way as from YCP (#41448).
- 2.11.2
* Fri Oct 29 2004 mvidner@suse.cz
- Added pkgconfig support.
- Prepared for passing options to y2base during testsuite run.
- 2.11.1
* Mon Oct 18 2004 visnov@suse.de
- Removed Pkg testing
- 2.11.0
* Mon Jun 14 2004 msvec@suse.cz
- added Testsuite module
- 2.10.0
* Sat Apr  3 2004 kkaempf@suse.de
- filter [Y2PMrc] messages from logfile (#38235)
- 2.9.9
* Fri Apr  2 2004 msvec@suse.cz
- changed license to GPL
- 2.9.8
* Sat Feb 28 2004 kkaempf@suse.de
- add openslp, openslp-devel to neededforbuild
- 2.9.7
* Wed Feb 25 2004 msvec@suse.cz
- fixed files filtering (support files with path)
- 2.9.6
* Thu Feb  5 2004 msvec@suse.cz
- possibility to limit testsuite output only to some files
- 2.9.5
* Fri Jan 30 2004 msvec@suse.cz
- log also the empty lines (and files) in DUMP and DUMPFILE
- 2.9.4
* Fri Jan 23 2004 msvec@suse.cz
- take advantage of a custom log.conf
- the full logging (Y2DEBUG) is not required any more
- 2.9.3
* Fri Jan 23 2004 arvin@suse.de
- fixed for brand new interpreter
* Fri Jan 16 2004 msvec@suse.cz
- updates for NI
- 2.9.1
* Tue Dec  2 2003 msvec@suse.cz
- sync with current dummy agent
- simplified log handling
- 2.9.0
* Mon Sep  8 2003 msvec@suse.cz
- makefiles updates by arvin and schwab
- 2.8.3
* Fri Jul 11 2003 mvidner@suse.cz
- mentioned wdiff in the docs.
* Thu Jun 12 2003 arvin@suse.de
- fixed file list
* Wed Feb  5 2003 lslezak@suse.cz
- added TargetInit and TargetProducts into Pkg.ycp
- version 2.7.7
* Mon Jan 27 2003 arvin@suse.de
- added popt to neededforbuild
* Mon Jan 20 2003 msvec@suse.de
- better (non-conflicting) local name variable
- 2.7.5
* Mon Dec  9 2002 msvec@suse.cz
- added another Pkg:: function
- fixed for new log component names
- 2.7.4
* Thu Dec  5 2002 mvidner@suse.cz
- Fixed a typo to make it really work.
- 2.7.3
* Thu Dec  5 2002 mvidner@suse.cz
- Faked a bunch of Pkg:: functions that are used in the PackageCallbacks
  constructor.
  This should prevent the testsuite failures of yast2-mail etc.
- 2.7.2
* Tue Dec  3 2002 ro@suse.de
- added curl and openssl to neededforbuild
* Tue Oct 22 2002 ro@suse.de
- added perl-XML-Writer to neededforbuild
* Thu Aug 29 2002 msvec@suse.cz
- provide Pkg::SourceProductData for modules using Installation.ycp
- 2.6.9
* Fri Aug 23 2002 mvidner@suse.cz
- Added a dummy Pkg module for faking Pkg::Is{Provided,Available}
  (needed for the new packagemanager).
- 2.6.8
* Mon Jul 15 2002 mvidner@suse.cz
- yast2 not needed for build nor at runtime.
- 2.6.7
* Fri Jul 12 2002 kkaempf@suse.de
- use "testsuite" server instead of "scr" server in order
  to get a wfm-based (instead of scr based) runtime environment.
- 2.6.6
* Thu Jul  4 2002 arvin@suse.de
- move non binary file from /usr/lib/YaST2 to /usr/share/YaST2
- updated documentation
- 2.6.5
* Mon Jul  1 2002 msvec@suse.cz
- new version for new yast2 scheme
- 2.6.4
* Wed Jun 26 2002 mvidner@suse.cz
- Fix build errors (automake version mismatch) by not overwriting Makefile.am
- Run tests in alphabetical order.
- 2.6.3
* Fri May 31 2002 msvec@suse.cz
- possibility to test constructors
- 2.6.2
* Fri May 10 2002 msvec@suse.cz
- accept the new broken Wizard constructor
- 2.6.1
* Wed Apr  3 2002 msvec@suse.cz
- use devtools create-spec and y2autoconf
- updated for the new system agent
- 2.6.0
* Thu Dec 13 2001 arvin@suse.de
- adapted to renaming of y2bignfat to y2base
- 2.5.3
* Fri Nov 30 2001 msvec@suse.cz
- make all ycp symbols global for testing local functions
- removed some duplicated code
- 2.5.2
* Thu Nov 29 2001 pblahos@suse.cz
- Added 3rd parameter to select to satisfy new libycp.
- 2.5.1
* Mon Nov 12 2001 msvec@suse.cz
- use yast2-devtools
- fixed lookup default parameter
- 2.5.0
* Wed Sep 26 2001 msvec@suse.cz
- fixed DUMP for non-string variables
- updated testsuite
- 2.4.6
* Wed Sep 26 2001 msvec@suse.cz
- minor makefiles fixes
- added some missing files
- fixed DUMPFILE (new system agent)
- fixed DUMP (multiple lines)
- testsuite update
- 2.4.5
* Tue Aug 28 2001 msvec@suse.cz
- parseycp during check
- return the retcode
- 2.4.4
* Tue Aug 21 2001 msvec@suse.cz
- unset all locale variables before testing
- use faster SCR::
- 2.4.3
* Thu Aug  9 2001 msvec@suse.cz
- report signal number if yast2 exit with failure
- accept new Dir behavior
- 2.4.2
* Tue Jul 17 2001 msvec@suse.cz
- don't ignore white-space in diffs
- changes due to again renamed target.scr
- don't accept declarations with '|'
- exchange err and out outputs
- minor fix of filtering
- 2.4.1
* Tue Jul 10 2001 ro@suse.de
- removed yast2-core-translator from neededforbuild
* Tue Jul  3 2001 msvec@suse.cz
- adapted to new system agent split of y2scr
- 2.4.0
* Tue Apr 17 2001 msvec@suse.cz
- major documentation rewrite
- removed isnils
- 2.3.7
* Fri Apr 13 2001 msvec@suse.cz
- run diff on the last failed test
- enabled abuild checking
- 2.3.6
* Tue Apr 10 2001 msvec@suse.cz
- enabled maps as arguments for TEST
- stop after the first failed test
- 2.3.5
* Wed Apr  4 2001 msvec@suse.cz
- minor documentation update
- documentation moved to $RPMNAME
- fixed new target agent output
- fixed logconf.ycp handling
- 2.3.4
* Tue Mar 27 2001 msvec@suse.cz
- new libycp adoptation
- output beautification (final)
- testsuite
- 2.3.3
* Mon Mar 19 2001 arvin@suse.de
- don't check for gperf in configure
- 2.3.2
* Fri Mar 16 2001 msvec@suse.cz
- autobuild checking changes
- 2.3.1
* Wed Mar  7 2001 msvec@suse.cz
- Initial version
- Incorporates y2scr/ag_target change: .target.tmpdir is now
  deleted when target agent is unmounetd. <pblahos>
- DUMP function <gs>
