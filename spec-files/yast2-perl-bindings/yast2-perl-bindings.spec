#
# spec file for package yast2-perl-bindings
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


Name:           yast2-perl-bindings
Version:        4.3.0
Release:        1.3

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  yast2-ruby-bindings >= 1.0.0
BuildRequires:  yast2-ycp-ui-bindings-devel

# ErrorNamespace
Requires:       yast2-core >= 3.2.1
BuildRequires:  yast2-ycp-ui-bindings-devel >= 2.16.37
Requires:       perl = %{perl_version}
Requires:       yast2-ycp-ui-bindings       >= 2.16.37
%if 0%{?suse_version} < 1220
BuildRequires:  libxcrypt-devel
%endif
# for YaPI.pm
Requires:       perl(Locale::gettext)

Summary:        YaST2 - Perl Bindings
License:        GPL-2.0-or-later
Group:          System/YaST

%description
This adds an embedded Perl interpreter to YaST2 as a plug-in (in other
words it will be loaded only if required). This is a very efficient way
of calling Perl from within YaST2 YCP scripts.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

rm $RPM_BUILD_ROOT/%{yast_plugindir}/libpy2lang_perl.la
rm $RPM_BUILD_ROOT/%{perl_vendorarch}/auto/YaST/YCP/libYCP.la
%if 0%{?rhel}
mv "$RPM_BUILD_ROOT"/usr/share/doc/packages/%{name} "$RPM_BUILD_ROOT"%{_docdir}
%endif

%files
%defattr (-, root, root)
%{yast_plugindir}/libpy2lang_perl.so.*
%{yast_plugindir}/libpy2lang_perl.so
# libYCP goes elsewhere
%dir %{perl_vendorarch}/YaST
%{perl_vendorarch}/YaST/YCP.pm
%dir %{perl_vendorarch}/auto/YaST
%dir %{perl_vendorarch}/auto/YaST/YCP
%{perl_vendorarch}/auto/YaST/YCP/libYCP.so*
%dir %{yast_moduledir}
%{yast_moduledir}/YaPI.pm
%doc %{yast_docdir}
%license COPYING

%changelog
* Wed May 27 2020 David Diaz <dgonzalez@suse.com>
- Dropped legacy testsuite (related to bsc#1138668).
- Dropped obsolete pluglib-bindings.
- 4.3.0
* Tue Feb 26 2019 José Iván López González <jlopez@suse.com>
- Version bump (bsc#1124009)
- 4.1.0
* Tue Oct 16 2018 schubi@suse.de
- Added license file to spec.
* Wed Aug 22 2018 schubi@suse.de
- Switched license in spec file from SPDX2 to SPDX3 format.
* Tue Feb 27 2018 gsouza@suse.com
- Added warning to inform user that YAPI is deprecated and should
  not be used by any external program (fate#323734).
- 4.0.1
* Thu Nov 30 2017 lslezak@suse.cz
- Fixed build failure caused by a jemalloc warning printed on
  the STDERR (bsc#1068883)
- 4.0.0
* Thu Jan  5 2017 jreidinger@suse.com
- Initial adaptation to new ErrorNamespace for failed imports
  which is already used by ruby-bindings (bsc#932331)
- 3.2.0
* Wed Jun  4 2014 mls@suse.de
- Adapt to perl-5.20.0, where an integer can get encoded as an
  NV without the PV flag being set
- 3.1.2
* Thu Oct 17 2013 mvidner@suse.com
- Fix untranslated texts in yast2-users: call bindtextdomain
  with YaST locale directory to find mo-files (bnc#845600).
- 3.1.1
* Thu Sep 19 2013 lslezak@suse.cz
- do not use *.spec.in template, use *.spec file with RPM macros
  instead
- 3.1.0
* Wed Jul 31 2013 yast-devel@opensuse.org
- converted from YCP to Ruby by YCP Killer
  (https://github.com/yast/ycp-killer)
- version 3.0.0
* Wed Jul 17 2013 mvidner@suse.cz
- Fix type conversion for parameters passed by reference
  (gh#yast/ycp-killer#486)
- 2.24.6
* Wed Jul 10 2013 mvidner@suse.cz
- testsuite: ignore line numbers, properly (gh#yast/ycp-killer#554)
- 2.24.5
* Mon Jul  1 2013 lslezak@suse.cz
- Removed useless BuildRequires: curl-devel and rpm-devel
- 2.24.4
* Fri Jun 28 2013 lslezak@suse.cz
- testsuite: filter out yast2-core messages from tests, make the
  tests less sensitive to changes in yast2-core
- 2.24.3
* Mon Jun 24 2013 lslezak@suse.cz
- testsuite: forward compatibility with YCP to Ruby conversion,
  all modules have to start with an uppercase letter (Ruby
  convention for module names)
- 2.24.2
* Tue Jun 18 2013 lslezak@suse.cz
- set the source location when calling YaST functions outside Perl,
  fixes wrong location in y2log
- 2.24.1
* Fri Jun 14 2013 mvidner@suse.com
- Removed BloCXX support (FATE#313242).
- 2.24.0
* Tue Jun 26 2012 aschnell@suse.de
- adapted to namespace changes in yast2-core
- 2.19.2
* Fri Nov 25 2011 coolo@suse.com
- add libtool as buildrequire to avoid implicit dependency
* Tue Mar  9 2010 juhliarik@suse.cz
- added check for "glob" (bnc#585757)
- 2.19.1
* Thu Nov 26 2009 lslezak@suse.cz
- added versioned perl dependency (require a specific perl version)
- 2.19.0
* Wed Feb  4 2009 mvidner@suse.cz
- Added logging functions YaST::YCP::y2useritem and y2usernote (FATE#100386).
- 2.18.0
* Mon Sep 29 2008 visnov@suse.cz
- Fixed testsuite
- 2.17.2
* Fri Jul 18 2008 mvidner@suse.cz
- Fixed a missing declaration uncovered by a change in yast2-core.
- 2.17.1
* Wed Jul 16 2008 mvidner@suse.cz
- Pluglib-bindings:
  - Fixed accessing deques as struct members (bnc#398815).
  - Improved tests.
- 2.17.0
* Tue Jul 15 2008 mvidner@suse.cz
- Allow string representation of large numbers in SWIG typemaps for
  "integer &" (bnc#408829).
* Mon Jul 14 2008 mvidner@suse.cz
- Respect prefix when installing pluglibs.
* Mon Apr 28 2008 mvidner@suse.cz
- Removed superfluous .la file (bnc#223733).
- 2.16.7
* Thu Apr 10 2008 mvidner@suse.cz
- No need to link with libzypp here (fate#302119).
- 2.16.6
* Mon Mar 31 2008 mvidner@suse.cz
- Trap Perl exceptions so that simple bugs don't kill the whole YaST
  (fate#412).
- 2.16.5
* Wed Mar 12 2008 mvidner@suse.cz
- adapt testsuite results to latest debug output again
- 2.16.4
* Thu Feb 21 2008 sh@suse.de
- Added new UI packages to Requires/BuildRequires in .spec file
- V 2.16.3
* Wed Feb 20 2008 coolo@suse.de
- adapt testsuite results to latest debug output
- 2.16.2
* Fri Feb 15 2008 coolo@suse.de
- fix build against newer yui
- 2.16.1
* Wed Oct  3 2007 mvidner@suse.cz
- Fixed compilation errors with GCC 4.3 by adding missing includes.
- 2.16.0
* Wed Aug 15 2007 mvidner@suse.cz
- UI from Perl: added examples and helper functions (F#120292).
- 2.15.3
* Fri Aug 10 2007 mvidner@suse.cz
- Finished integrating Feature #120292, UI as a namespace callable
  from yast2-*-bindings.
- 2.15.2
* Wed Aug  8 2007 mvidner@suse.cz
- Adapted to changes in yast2-core needed for making UI callable from
  yast2-*-bindings.
- 2.15.1.1
* Fri Jun  1 2007 mvidner@suse.cz
- pluglib-bindings: do not create nearly empty '.pm' for STL classes
- 2.15.1
* Tue Feb  6 2007 mvidner@suse.cz
- pluglib-bindings.ami: Detect if sablot fails.
  Prevents mysterious failure with LibStorage.pm.
- Enabled building in a non-/usr prefix.
- 2.15.0
* Mon Nov 13 2006 jsrain@suse.cz
- 2.14.0
* Mon Oct  2 2006 mvidner@suse.cz
- Fixed LDFLAGS for a fix in automake-1.9b.
- 2.13.11
* Thu Aug 31 2006 mvidner@suse.cz
- Fixed SWIG typemaps to really work with 1.3.27.
- 2.13.10
* Wed Aug  9 2006 mvidner@suse.cz
- Using YCPValue::valuetype_str() for better error messages.
* Wed Aug  9 2006 mvidner@suse.cz
- Use the Import class when calling a YCP function
  so that the log is not flooded with "import (Foo)" (#197845).
- 2.13.9
* Mon Aug  7 2006 mvidner@suse.cz
- Fixed the SWIG fix not to end a comment prematurely.
- 2.13.8
* Fri Aug  4 2006 mvidner@suse.cz
- Removed a search path that is added elsewhere already and here just
  breaks compilation is some cases (#197099).
- 2.13.7
* Wed Aug  2 2006 mvidner@suse.cz
- Fixed SWIG typemaps for swig-1.3.29, thanks mmarek.
- 2.13.6
* Tue Aug  1 2006 mvidner@suse.cz
- Documented how YaST::YCP::Import differs from YCP import.
* Tue Jul 18 2006 mvidner@suse.cz
- Documentation updates: doc/typeinfo replaced with doc/perl-bindings,
  doc/useperl.ycp, doc/modules/*.pm
* Fri Jun  9 2006 mvidner@suse.cz
- Reenabled testsuite, needs libzypp r3558 (#182672).
- 2.13.5
* Wed Jun  7 2006 ro@suse.de
- disable testsuite for the moment, hangs forever
* Tue Apr 25 2006 ro@suse.de
- hack to fix testsuite (change in yast2-core)
* Thu Feb  2 2006 mvidner@suse.cz
- Replaced yast2-packagemanager by libzypp.
- Require perl, do not package .la file (lint and build warnings).
- 2.13.4
* Wed Feb  1 2006 mvidner@suse.cz
- Fixed passing large integers between YCP and Perl (converting
  to/from strings if necessary), up to signed long long (#127896).
- Use BuildRequires.
- 2.13.3
* Wed Jan 25 2006 mvidner@suse.cz
- Return 1 as true value. 8 causes perl warnings if there are too
  many of them (#144296).
- pluglib-bindings.ami: clean the _wrap.* files too.
- 2.13.2
* Mon Dec 19 2005 mvidner@suse.cz
- Do not link libraries that were merged with liby2 in yast2-core.
- 2.13.1
* Tue Oct 11 2005 mvidner@suse.cz
- Functions without TYPEINFO are no longer made available as
  any Foo(...), because it is useless and only complicates error
  cases.
- 2.13.0
* Wed Jul 20 2005 arvin@suse.de
- added libxml2 and libxml2-devel to neededforbuild
* Fri Jul 15 2005 mlazar@suse.cz
- fixed "problem with corrupted memory when using C++/ycp interface..."
- 2.12.7
* Mon Jul 11 2005 visnov@suse.cz
- Fix packages needed for build
- 2.12.6
* Fri Jul  1 2005 mlazar@suse.cz
- quick workaround for "problems with corrupted memory when using
  C++/ycp interface of libstorage", see yast2-hacker
* Wed Jun 29 2005 mlazar@suse.cz
- pluglib-bindings: added --strip option to filter.pl
- YPerl.cc: better debug messages for perl_class_destructor
* Tue Jun 14 2005 mlazar@suse.cz
- Fixed enums in TYPEINFO (again and better).
* Tue Jun 14 2005 mlazar@suse.cz
- Fixed enums in TYPEINFO.
* Mon Jun  6 2005 mvidner@suse.cz
- Fixed build after introducing remote namespaces in yast2-core.
- 2.12.5
* Fri Jun  3 2005 mlazar@suse.cz
- pluglib-bindings: improved constructors in TYPEINFO
* Wed Jun  1 2005 mlazar@suse.cz
- removed limal_perlrun.swg (not needed sinc YCP support external data types)
* Wed Jun  1 2005 mlazar@suse.cz
- added support for perl objects (via YCPExternal type)
* Fri May 27 2005 mvidner@suse.cz
- In TYPEINFO, represent enums as integers, not any.
- Do not grow the generated pm's infinitely, remove them before
  apending to them.
- Added PLUGLIB_DEPEND (arvin)
* Wed May 25 2005 mlazar@suse.cz
- added support for reference to enum types
* Fri May 20 2005 mvidner@suse.cz
- Enhanced for sharing a single interpreter with pluglibs written in
  perl (perl2cpp).
- Fixed double deletion of the interpreter when invoked from perl.
* Wed May 18 2005 mvidner@suse.cz
- pluglib-bindings: Compile wrapper using libtool so that
  x86_64 gets -fPIC.
- 2.12.4
* Mon May 16 2005 mlazar@suse.cz
- pluglib-bindings: support for enum in YCP
* Mon May 16 2005 mlazar@suse.cz
- pluglib-bindigs: support for class constructor
* Tue May 10 2005 arvin@suse.de
- honour DESTDIR in pluglib-bindings.ami
- 2.12.3
* Tue May 10 2005 arvin@suse.de
- use CXX instead of CXXCOMPILE in pluglib-bindings.ami
- 2.12.2
* Fri May  6 2005 mlazar@suse.cz
- pluglib-bindings: support for list of hash and hash of list
* Thu May  5 2005 mlazar@suse.cz
- pluglib-bindings: support for packet data as input argument to
  functions expected reference/pointer
- pluglib-bindings: typemap for pointer/reference to str:string output
* Wed May  4 2005 mvidner@suse.cz
- Build fixes
- 2.12.1
* Mon May  2 2005 mlazar@suse.cz
- restructured pluglib-bindings/swig
- added support for lists and hashes of "black box" objects
* Thu Apr 28 2005 mvidner@suse.cz
- Added a generic makefile (automake include)
  for compiling and installing pluglibs for yast
* Tue Apr 26 2005 mlazar@suse.cz
- support for one level hashes/maps in pluglib-bindings
* Tue Apr 26 2005 mlazar@suse.cz
- support for two level lists in pluglib-bindings
* Mon Apr 25 2005 mvidner@suse.cz
- Imported pluglib-bindings-0.7
* Wed Apr 20 2005 mlazar@suse.cz
- Added support for reference.
- 2.12.0
* Mon Feb 14 2005 mvidner@suse.cz
- Do not redirect stderr to y2log (#42155, #37652).
- 2.11.3
* Thu Jan  6 2005 mvidner@suse.cz
- Added $TYPEINFO{ALL_METHODS} (true by default) so that
  YCP can call plain Perl subs, not only methods.
- 2.11.2
* Fri Nov  5 2004 visnov@suse.cz
- Set exported symbol entries global (#47078)
- 2.11.1
* Fri Oct 29 2004 mvidner@suse.cz
- Added pkgconfig support.
- 2.11.0
* Thu Aug 19 2004 mvidner@suse.cz
- Make YaPI.pm using configure to substitute the prefix in 'use lib'.
- 2.10.4
* Thu Aug 12 2004 mvidner@suse.cz
- Broke neededforbuild cycle by substituting
  for yast2-devel-packages (msvec).
- 2.10.3
* Tue Aug  3 2004 visnov@suse.cz
- return correct type for the next wanted parameter in function calls
- 2.10.2
* Tue Aug  3 2004 visnov@suse.cz
- Adapted for the new abstract function call interface
- 2.10.1
* Fri May  7 2004 mvidner@suse.cz
- Made _ a *working* alias for __ (#39954).
- 2.9.34
* Fri May  7 2004 mvidner@suse.cz
- YaST::YCP: Use the common log file so that there's context
  for Perl errors (#39959)
- YaPI::_ deprecated in favor of YaPI::__ (#39954)
- more documentation for YaPI.pm
- 2.9.33
* Mon May  3 2004 mvidner@suse.cz
- logging: fixed caller info, enabled multiple arguments (#39768)
- 2.9.32
* Fri Apr 30 2004 mvidner@suse.cz
- rewrote PrependModulePath to use exactly what YCPPathSearch uses
  (#39512)
- 2.9.31
* Thu Apr 29 2004 mvidner@suse.cz
- if we created WFM, do also the cleanup (#39519)
- 2.9.30
* Thu Apr 29 2004 mvidner@suse.cz
- YaPI->SetError: write description (if any) to the log
- 2.9.29
* Tue Apr 20 2004 mvidner@suse.cz
- if there is no UI, use ncurses (#39192)
- 2.9.28
* Mon Apr 19 2004 mvidner@suse.cz
- adapted testsuite for fix in yast2-core-2.9.80
- 2.9.27
* Tue Apr 13 2004 mvidner@suse.cz
- check that a single package does not use inconsistent textdomains
* Thu Apr  8 2004 mvidner@suse.cz
- YaPI.pm: Remember the text domain
  and use dgettext instead of gettext (#38613).
- 2.9.26
* Fri Apr  2 2004 mvidner@suse.cz
- changed license to GPL
- 2.9.25
* Wed Mar 31 2004 mvidner@suse.cz
- redirect stderr to prevent errors from garbling ncurses screen (#37652)
- docs: fixed :: to ->
- 2.9.24
* Mon Mar 29 2004 mvidner@suse.cz
- require perl(Locale::gettext) now that YaPI.pm uses it
- 2.9.23
* Thu Mar 25 2004 mvidner@suse.cz
- added i18n functions to YaPI.pm (mcalmer)
- 2.9.22
* Thu Mar 25 2004 mvidner@suse.cz
- fixed passing nested terms
- 2.9.21
* Mon Mar 22 2004 mvidner@suse.cz
- implemented passing symbols and terms to Perl
- 2.9.20
* Mon Mar 22 2004 mvidner@suse.cz
- fixed testsuite on lib64 architectures
- 2.9.19
* Wed Mar 17 2004 mvidner@suse.cz
- strip $self on the way from Perl to YCP,
  just as it is added in the reverse direction
- YaPI.inc -> YaPI.pm
- 2.9.18
* Wed Mar 17 2004 mvidner@suse.cz
- YCP now calls all perl functions as class methods
  (so adding $self = shift; etc. is needed)
- added tests
- 2.9.17
* Fri Mar 12 2004 mvidner@suse.cz
- added YaPI.inc
- 2.9.16
* Thu Mar 11 2004 mvidner@suse.cz
- YPerlNamespace: some stuff is now in Y2Namespace, removed (#34207)
- parseTypeinfo: allow argument names after whitespace
- 2.9.15
* Tue Mar  9 2004 mvidner@suse.cz
- disregard array context: a YCP list is always a reference to a Perl array
- added data type docs
- fixed explicit Byteblock if type known
- 2.9.14
* Mon Mar  1 2004 mvidner@suse.cz
- added YaST::YCP::Byteblock
* Mon Mar  1 2004 mvidner@suse.cz
- adapted to changes in yast2-core: Type::List
- 2.9.13
* Fri Feb 27 2004 mvidner@suse.cz
- added sformat
- adapted to changes in yast2-core:
  Y2Namespace::initialize, SymbolEntryPtr, YFunctionPtr
- 2.9.12
* Wed Feb 25 2004 mvidner@suse.cz
- added liby2util based logging
- use all libraries when starting from Perl (visnov)
- 2.9.11
* Mon Feb 23 2004 mvidner@suse.cz
- Prepend $Y2DIR/modules and $moduledir to PERL5LIB for the embedded Perl
- 2.9.10
* Fri Feb 20 2004 mvidner@suse.cz
- initialize imported namespaces (kkaempf)
- functions without TYPEINFO return "any" and do not produce warnings
- 2.9.8
* Sat Feb 14 2004 kkaempf@suse.de
- drop timestamp in Y2Namespace
- 2.9.7
* Tue Feb 10 2004 mvidner@suse.cz
- reduced logging to make yast2-inetd build
- 2.9.6
* Tue Feb 10 2004 mvidner@suse.cz
- revert the preference of numbers
  now strings are used unless the wanted type is known
  or an explicit data class is used (Integer, Float, String added)
- 2.9.5
* Mon Feb  9 2004 mvidner@suse.cz
- try harder to convert Perl data to integers/strings
  if the wanted YCP type is known
- prefer numbers to strings if the wanted YCP type is unknown
- enable passing maps/lists containing nil to Perl
- 2.9.4
* Fri Jan 30 2004 mvidner@suse.cz
- don't consume Perl arrays when passing them to YCP
- 2.9.3
* Fri Jan 30 2004 mvidner@suse.cz
- fixed parse errors and more
- enabled elementary tests
- 2.9.2
* Tue Jan 27 2004 mvidner@suse.cz
- initial version for autobuild
- 2.9.1
