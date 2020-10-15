#
# spec file for package libxslt
#
# Copyright (c) 2019 SUSE LLC
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

%if 0%{?rhel}
%define ext_man .gz
%endif

%define libname %{name}1
%define exname  libexslt0
Name:           libxslt
Version:        1.1.34
Release:        1.5
Summary:        XSL Transformation Library
License:        MIT AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://xmlsoft.org/XSLT/
Source0:        ftp://xmlsoft.org/libxslt/libxslt-%{version}.tar.gz
Source1:        ftp://xmlsoft.org/libxslt/libxslt-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        xslt-config.1
Source99:       baselibs.conf
Patch0:         %{name}-1.1.24-no-net-autobuild.patch
Patch1:         libxslt-config-fixes.patch
Patch2:         0009-Make-generate-id-deterministic.patch
Patch3:         libxslt-random-seed.patch
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
Obsoletes:      libxslt-python

%description
This C library allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

It is based on libxml (version 2) for XML parsing, tree manipulation,
and XPath support. It is written in plain C, making as few assumptions
as possible and sticks closely to ANSI C/POSIX for easy embedding.
It includes support for the EXSLT set of extension functions as well
as some common extensions present in other XSLT engines.

%package -n %{libname}
Summary:        XSL Transformation Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{libname}
This C library allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

It is based on libxml (version 2) for XML parsing, tree manipulation,
and XPath support. It is written in plain C, making as few assumptions
as possible and sticks closely to ANSI C/POSIX for easy embedding.
It includes support for the EXSLT set of extension functions as well
as some common extensions present in other XSLT engines.

%package devel
Summary:        Development files for libxslt
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name}-tools = %{version}
Requires:       glibc-devel
Requires:       libgcrypt-devel
Requires:       libgpg-error-devel

%description devel
libxslt allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

This subpackage contains the header files for developing
applications that want to make use of the XSLT libraries.

%package tools
Summary:        Extended Stylesheet Language (XSL) Transformation utilities
License:        MIT AND GPL-2.0-or-later
Group:          Development/Tools/Other
Provides:       %{name} = %{version}
Provides:       xsltproc = %{version}

%description tools
This package contains xsltproc, a command line interface to the XSLT engine.
xtend the

%prep
%setup -q
%patch0
%patch1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fvi
%configure \
  --disable-static \
  --without-python \
  --disable-silent-rules
make %{?_smp_mflags}

%check
%if ! 0%{?qemu_user_space_build}
make %{?_smp_mflags} check
%endif

%install
%make_install

# Unwanted doc stuff
rm -fr %{buildroot}%{_datadir}/doc
# the manual page is required
install -D -m0644 %{SOURCE3} %{buildroot}%{_mandir}/man1/xslt-config.1
#kill all "la" files
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libxslt.so.*
%{_libdir}/libexslt.so.*

%files tools
%license COPYING*
%doc AUTHORS NEWS README Copyright TODO FEATURES
%{_bindir}/xsltproc
%{_mandir}/man1/xsltproc.1%{?ext_man}

%files devel
%{_libdir}/libxslt.so
%{_libdir}/libexslt.so
%{_libdir}/*.sh
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc
%{_includedir}/*
%{_datadir}/aclocal/*
%{_bindir}/xslt-config
%{_mandir}/man1/xslt-config.1%{?ext_man}
%{_mandir}/man3/*
%doc doc/*.html doc/html doc/tutorial doc/*.gif

%changelog
* Wed Nov 20 2019 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Update to 1.1.34: Oct 30 2019
  * Documentation:
  - Fix EXSLT web pages, Regenerate web pages
  - Fix Git link in news.html
  - Minor documentation fixes after recent changes
  - Regenerate symbols and API docs
  - Regenerate EXSLT website
  * Portability:
  - Remove stubs when compiling without debugger or profiler
  - configure.ac: Invoke PKG_CHECK_MODULES for building shared libraries
  - configure.ac: Conditionally determine whether xml2-config should pass
    shared libraries or static libraries
  - xslt-config.in: Fix broken --prefix=DIR support
  - libexslt.pc.in: Do not expose private library dependencies unless invoked
  - libxslt.pc.in: Do not expose private library dependencies unless invoked
  - Fix -Wformat-overflow warning (GCC 9)
  - Stop including ansidecl.h
  - Remove WIN32_EXTRA_* variables
  - Build without winsock
  * Bug Fixes:
  - xsl:template without name and match attributes should not be allowed
  - Make sure that Python tests exit with error code
  - Improve handling of invalid UTF-8 in format-number
  - Fix dangling pointer in xsltCopyText
  - Fix memory leak in pattern compilation error path
  - Fix uninitialized read with UTF-8 grouping chars
  - Fix integer overflow in FORMAT_GYEAR
  - Fix performance regression with xsl:number
  - Backup XPath context node in xsltInitCtxtKey
  - Fix unsigned integer overflow in date.c
  - Fix insertion of xsl:fallback content
  - Avoid quadratic behavior in xsltSaveResultTo
  - Fix numbering in non-Latin scripts
  - Fix uninitialized read of xsl:number token
  - Fix integer overflow in _exsltDateDayInWeek
  - Rework xsltAttrVT allocation
  - Fix check of xsltTestCompMatch return value
  - Fix security framework bypass
  - Use xmlNewTextChild in EXSLT dyn:map
  - Fix float casts in exsltDateDuration
  - Always set context node before calling XPath iterators
  - Fix attribute precedence with xsl:use-attribute-sets
  - Backup context node in exsltFuncFunctionFunction
  - Initialize ctxt->output before evaluating global vars
  - Fix memory leak in EXSLT functions error path
  * Improvements:
  - Fix -Wimplicit-fallthrough warnings
  - Adjust number of API index pages
  - Make xsltCompileRelativePathPattern non-recursive
  - Check that crypto:rc4_decrypt produces valid UTF-8
  - Avoid recursion in keys.c:skipPredicate
  - xslt-config.in: Simply handling of $all_flags
  - xslt-config.in: Add a --dynamic option to --libs
  - xslt-config.in: Simplify basic library handling
  - xslt-config.in: Remove unused variable
  - xslt-config: Simply handling of --cflags
  - Improve fuzzers
  - Always reuse XPath context
  - Compile with -Wextra
  - Make profiler support optional
  - Hide unused code when compiling without debugger
  - Reorganize fuzzing code
  - Optional operation limit
  - Improve seed corpus and dictionary
  - Reuse XPath context when compiling stylesheets
  - Reuse XPath context in dyn:map
  - Reuse XPath context in saxon:expression
  - Add libFuzzer targets
  - Adjust error message in expected test output
  - Change bug tracker URL
  - Change git repo URL
  - Regenerate NEWS
  - Fix misleading indentation in security.c
  * Cleanups:
  - Remove empty TODO file
  - Remove generated file libxsltclass.txt from version control
  - Rebuild docs
- Rebase patch libxslt-config-fixes.patch
- Remove patches fixed upstream:
  * libxslt-CVE-2019-11068.patch
  * libxslt-CVE-2019-13117.patch
  * libxslt-CVE-2019-13118.patch
  * libxslt-CVE-2019-18197.patch
* Mon Oct 21 2019 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Security fix [bsc#1154609, CVE-2019-18197]
  * Fix dangling pointer in xsltCopyText
  * Add libxslt-CVE-2019-18197.patch
* Tue Oct  1 2019 Tomáš Chvátal <tchvatal@suse.com>
- Drop out lilbxslt-python package as it is just py2 based and
  upstream yet didn't bother to port it to python3.
  When there is python3 compatible code it should be enabled as
  multibuild here
  * Drop now unused libxslt-1.1.24-linkflags.patch and
    libxslt-do_not_build_doc_nor_xsltproc.patch
* Tue Jul  2 2019 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Security fix: [bsc#1140101, CVE-2019-13118]
  * Fix uninitialized read with UTF-8 grouping chars. Read of
    uninitialized stack data due to too narrow xsl:number
    instruction and an invalid character
  * Added libxslt-CVE-2019-13118.patch
* Tue Jul  2 2019 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Security fix: [bsc#1140095, CVE-2019-13117]
  * Fix uninitialized read of xsl:number token. An xsl number with
    certain format strings could lead to a uninitialized read in
    xsltNumberFormatInsertNumbers
  * Added libxslt-CVE-2019-13117.patch
* Thu Apr 11 2019 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Security fix: [bsc#1132160, CVE-2019-11068]
  * Bypass of a protection mechanism because callers of xsltCheckRead
    and xsltCheckWrite permit access even upon receiving a -1 error
    code. xsltCheckRead can return -1 for a crafted URL that is not
    actually invalid and is subsequently loaded.
  * Added libxslt-CVE-2019-11068.patch
* Mon Mar  4 2019 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Update to version 1.1.33
  * Portability:
  - Variables need 'extern' in static lib on Cygwin
  - Really declare dllexport/dllimport for Cygwin
  - Fix callback signatures in Python bindings
  - Fix transform callback signatures
  - Fix extension callback signatures
  - Fix deallocator signatures
  - Fix XPath callback signatures
  - Fix hash callback signatures
  * Bug Fixes:
  - Don't cache direct evaluation of patterns with variables
  - Move function result RVTs to context variable
  - Fix EXSLT functions returning RVTs from outer scopes
  - Fix handling of RVTs returned from nested EXSLT functions
  - Fix typos
  * Improvements:
  - Run Travis ASan tests with "sudo: required"
  * Cleanups:
  - Remove doc/libxslt-decl.txt
  - Docs for 1.1.32 release
- Cleaned with spec-cleaner
* Wed Nov  8 2017 vcizek@suse.com
- Update to version 1.1.32
  * fixes xml-config detection regression (boo#1066525)
* Thu Oct 19 2017 pmonrealgonzalez@suse.com
- Update to version 1.1.30 [bsc#1063934]
  * Documentation:
  - Misc doc fixes
  * Portability:
  - Look for libxml2 via pkg-config first
  * Bug Fixes:
  - Also fix memory hazards in exsltFuncResultElem
  - Fix NULL deref in xsltDefaultSortFunction
  - Fix memory hazards in exsltFuncFunctionFunction
  - Fix memory leaks in EXSLT error paths
  - Fix memory leak in str:concat with empty node-set
  - Fix memory leaks in error paths
  - Switch to xmlUTF8Strsize in numbers.c
  - Fix NULL pointer deref in xsltFormatNumberFunction
  - Fix UTF-8 check in str:padding
  - Fix xmlStrPrintf argument
  - Check for overflow in _exsltDateParseGYear
  - Fix double to int conversion
  - Check for overflow in exsltDateParseDuration
  - Change version of xsltMaxVars back to 1.0.24
  - Disable xsltCopyTextString optimization for extensions
  - Create DOCTYPE for HTML version 5
  - Make xsl:decimal-format work with namespaces
  - Remove norm:localTime extension function
  - Check for integer overflow in xsltAddTextString
  - Detect infinite recursion when evaluating function arguments
  - Fix memory leak in xsltElementAvailableFunction
  - Fix for pattern predicates calling functions
  - Fix cmd.exe invocations in Makefile.mingw
  - Don't try to install index.sgml
  - Fix symbols.xml
  - Fix heap overread in xsltFormatNumberConversion
  - Fix <xsl:number level="any"/> for non-element nodes
  - Fix unreachable code in xsltAddChild
  - Change version number in xsl:version warning
  - Avoid infinite recursion after failed param evaluation
  - Stop if potential recursion is detected
  - Consider built-in templates in apply-imports
  - Fix precedence with multiple attribute sets
  - Rework attribute set resolution
  * Improvements:
  - Silence tests a little
  - Set LIBXML_SRC to absolute path
  - Add missing #include
  - Adjust expected error messages in tests
  - Make xsltDebug more quiet
  - New-line terminate error message that missed this convention
  - Use xmlBuffers in EXSLT string functions
  - Switch to xmlUTF8Strsize in EXSLT string functions
  - Check for return value of xmlUTF8Strlen
  - Avoid double/long round trip in FORMAT_ITEM
  - Separate date and duration structs
  - Check for overflow in _exsltDateDifference
  - Clamp seconds field of durations
  - Change _exsltDateAddDurCalc parameter types
  - Fix date:difference with time zones
  - Rework division/remainder arithmetic in date.c
  - Remove exsltDateCastDateToNumber
  - Change internal representation of years
  - Optimize IS_LEAP
  - Link libraries with libm
  - Rename xsltCopyTreeInternal to xsltCopyTree
  - Update linker version script
  - Add local wildcard to version script
  - Make some symbols static
  - Remove redundant NULL check in xsltNumberComp
  - Fix forwards compatibility for imported stylesheets
  - Reduce warnings in forwards-compatible mode
  - Precompute XSLT elements after preprocessing
  - Fix whitespace in xsltParseStylesheetTop
  - Consolidate recursion checks
  - Treat XSLT_STATE_STOPPED same as errors
  - Make sure that XSLT_STATE_STOPPED isn't overwritten
  - Add comment regarding built-in templates and params
  - Rewrite memory management of local RVTs
  - Validate QNames of attribute sets
  - Add xsl:attribute-set regression tests
  - Ignore imported stylesheets in xsltApplyAttributeSet
- Dropped patches fixed upstream
  * libxslt-CVE-2016-4738.patch
  * libxslt-1.1.28-CVE-2017-5029.patch
* Mon Sep 11 2017 jengelh@inai.de
- Fix RPM groups. Drop ineffective --with-pic.
  Trim conjecture from description.
* Fri Jul 28 2017 mpluskal@suse.com
- Add gpg signature
- Cleanup spec file with spec-cleaner
* Tue Apr 25 2017 pmonrealgonzalez@suse.com
- Fixed CVE-2017-5029 bcs#1035905
  * Limit buffer size in xsltAddTextString to INT_MAX
- Added patch libxslt-1.1.28-CVE-2017-5029.patch
* Wed Apr  5 2017 pgajdos@suse.com
- security update: initialize random generator, CVE-2015-9019
  [bsc#934119]
  + libxslt-random-seed.patch
* Mon Mar 13 2017 pmonrealgonzalez@suse.com
- Added patch libxslt-CVE-2016-4738.patch
  * Fix heap overread in xsltFormatNumberConversion: An empty
    decimal-separator could cause a heap overread. This can be
    exploited to leak a couple of bytes after the buffer that holds
    the pattern string.
  * bsc#1005591 CVE-2016-4738
* Sat Jun 11 2016 tchvatal@suse.com
- Update to 1.1.29:
  * new release after 4 years with few bugfies all around
- Refresh patch 0009-Make-generate-id-deterministic.patch to apply
- Remove cve patch that was integrated upstream:
  libxslt-1.1.28-type_confusion_preprocess_attr.patch
- Unpack the manpage as the compression is set by buildbot not always gz
* Fri May 20 2016 kstreitova@suse.com
- add libxslt-1.1.28-type_confusion_preprocess_attr.patch to fix
  type confusion in preprocessing attributes [bnc#952474],
  [CVE-2015-7995]
* Thu Apr  9 2015 suse@microstep-mis.com
- fix package with "soname" should obsolete libxslt package on suse < 12.2 (SLE11)
* Sun Feb  1 2015 coolo@suse.com
- add 0009-Make-generate-id-deterministic.patch from debian's
  reproducible builds project to avoid randomness in generated IDs
* Thu Dec  6 2012 pascal.bleser@opensuse.org
- update to 1.1.28:
  * fix generate-id() to avoid generating the same ID
  * fix crash with empty xsl:key/@match attribute
  * fix crash when passing an uninitialized variable to document()
  * fix regression: default namespace not correctly used
  * remove xsltTransStorageAdd and xsltTransStorageRemove from symbols.xml
- changes from 1.1.27:
  * link python module with python library (Frederic Crozat)
  * report errors on variable use in key
  * the XSLT namespace string is a constant one
  * fix handling of names in xsl:attribute
  * reserved namespaces in xsl:element and xsl:attribute
  * null-terminate result string of cry:rc4_decrypt
  * EXSLT date normalization fix
  * exit after compilation of invalid func:result
  * fix for EXSLT func:function
  * rewrite EXSLT string:replace to be conformant
  * avoid a heap use after free error
  * fix a dictionary string usage
  * output should not include extraneous newlines when indent is off
  * document('') fails to return stylesheets parsed from memory
  * xsltproc should return an error code if xinclude fails
  * forwards-compatible processing of unknown top level elements
  * fix system-property with unknown namespace
  * fix default template processing on namespace nodes
  * fix a bug in selecting XSLT elements
  * fix a memory leak with xsl:number
  * fix a problem with ESXLT date:add() with January
  * fix generate-id() to not expose object addresses
  * allow whitespace in xsl:variable with select
  * fix direct pattern matching bug
  * add the saxon:systemId extension
  * add an append mode to document output
  * fix portability to upcoming libxml2-2.9.0
  * precompile patterns in xsl:number
- change soname macro back to "1" and enforce it in the files list
- revert -tools subpackage for openSUSE < 12.2 as that has only
  become effective since 12.2 on the package that ships with the
  distribution, to avoid having a completely different package
  layout in this repository as compared to the stock distribution
  packages (added a Provides: libxslt-tools though)
* Wed Apr 25 2012 chris@computersalat.de
- add macro "soname" %%{name}1
- fix "self obsoletion"
* Sat Mar 17 2012 jengelh@medozas.de
- Make sure to follow shlib policy; put tools in a separate package
  like done in libxml2
* Wed Jan  4 2012 jengelh@medozas.de
- Remove redundant tags (License: field is inherited)
- Use exact EVR for Provides:
* Wed Jan  4 2012 cfarrell@suse.com
- Tutorial contains GPL-2.0+ code. Either split this off into a subpackage or
  add GPL-2.0+ as an aggregation to the main licence tag
* Sat Dec  3 2011 agraf@suse.com
- don't run make check in QEMU builds - breaks due to massive threading
* Mon Nov 21 2011 jengelh@medozas.de
- Remove redundant/unwanted tags/section (cf. specfile guidelines)
* Sun Nov 20 2011 coolo@suse.com
- add libtool as buildrequire to avoid implicit dependency
* Thu Sep  8 2011 dmueller@suse.de
- fix provides/obsoletes
* Tue Aug  2 2011 idonmez@novell.com
- Add dependency on libgcrypt-devel and libgpg-error-devel for
  the libxslt-devel package
* Mon Aug  1 2011 idonmez@novell.com
- Correctly obsolete libxslt package in the baselibs.conf too
* Fri Jul 29 2011 idonmez@novell.com
- Fix build on SLE
* Fri Jul 29 2011 crrodriguez@opensuse.org
- Fix broken requires,provides,Obsoletes causing "have choice.."
  build system errors
- Remove all "la" files since they are no longer needed
- Fix -devel pacakge requires and messed up -config scripts
  this may cause build fails of already broken dependant packages
  that do not link all the needed libraries in an explicit manner
  (This is not a bug here, it is expected to cause it)
* Wed Jul 27 2011 giecrilj@stegny.2a.pl
- package clean-up:
  - include library version number in the name of the binary package
  - add an alias for xsltproc (required by package xmlto)
* Wed Jul 21 2010 puzel@novell.com
- update to libxslt-1.1.26
  - Improvements:
  - Add xsltProcessOneNode to exported symbols for lxml
  - Features:
  - Add API versioning and various cleanups
  - xsl:sort lang support using the locale
  - Bug fixes
  - Portability, documentation fixes
- drop libxslt-1.1.24-rc4-overflow.patch (included upstream)
- drop libxslt-1.1.24-am.patch (included upstream)
* Sat Apr 24 2010 coolo@novell.com
- buildrequire pkg-config to fix provides
* Mon Dec 14 2009 jengelh@medozas.de
- add baselibs.conf as a source
* Sun Jun 21 2009 coolo@novell.com
- fix build with automake 1.11
* Fri Feb 13 2009 coolo@suse.de
- fix file list
* Wed Feb 11 2009 coolo@suse.de
- readd "la" files to fix libxslt-python build
* Mon Jan 26 2009 crrodriguez@suse.de
- remove useless "la" file
- remove static libraries, if something breaks, move libraries to /%%{_lib}
  instead of restoring them
* Wed Dec 10 2008 olh@suse.de
- use Obsoletes: -XXbit only for ppc64 to help solver during distupgrade
  (bnc#437293)
* Thu Oct 30 2008 olh@suse.de
- obsolete old -XXbit packages (bnc#437293)
* Fri Jul 18 2008 prusnak@suse.cz
- updated to 1.1.24:
  * documentation: man page fix
  * bug fixes: pattern bug fix, key initialization problems,
    exclusion of unknown namespaced element on top of stylesheets
    python generator syntactic cleanup
- dropped obsoleted CVE-2008-1767.patch (included in update)
- fixed overflow in RC4 code (rc4-overflow.patch) [bnc#410256]
* Mon May 19 2008 prusnak@suse.cz
- fixed CVE-2008-1767 (CVE-2008-1767.patch) [bnc#391920]
* Fri Apr 11 2008 prusnak@suse.cz
- updated to 1.1.23
  * Documentation
    fix links for Cygwin DocBook setup (Philippe Bourcier)
  - xsltParseStylesheetDoc doc fix (Jason Viers)
  - fix manpage default maxdepth value
  * Bug fixes:
  - python segfault (Daniel Gryniewicz)
  - week-in-year bug fix (Maurice van der Pot)
  - fix python iterator problem (William Brack)
  - avoid garbage collection problems on str:tokenize and str:split
    and function results (William Brack and Peter Pawlowski)
  - superfluous re-generation of keys (William Brack)
  - remove superfluous code in xsltExtInitTest (Tony Graham)
  - func:result segfault fix (William Brack)
  - timezone offset problem (Peter Pawlowski),
  * Portability fixes:
  - old gcrypt support fix (Brent Cowgill)
  - Python portability patch (Stephane Bidoul)
  - VS 2008 fix (Rob Richard)
* Thu Apr 10 2008 ro@suse.de
- added baselibs.conf file to build xxbit packages
  for multilib support
* Tue Jan 22 2008 prusnak@suse.cz
- build --without-python to allow compilation from src.rpm
* Tue Sep 18 2007 sbrabec@suse.cz
- Updated to version 1.1.22:
  * Bug fixes: RVT cleanup problems, exclude-result-prefix bug,
    stylesheet compilation error handling, out of memory allocation
    errors, namespace problem on compound predicates, python
    space/tab inconsistencies, hook xsl:message to per
    transformation error callbacks, cached RVT problem, XPath
    context maintainance on choose, memory leaks in the math
    module, exclude-result-prefix induced namespace problem
  * Portability fixes: improve build with VS2005, fixing build on
    AIX, fix the security file checks on Windows.
  * Improvement: add an --encoding option to xsltproc.
  * Build: configure setup for TRIO_REPLACE_STDIO
  * Documentation: updated after change from CVs to SVN
* Thu Jan 25 2007 prusnak@suse.cz
- update to 1.1.20
  * result Value Tree handling fix
  * function parameters fix
  * empty text node handling
  * plugin support and test fixes
  * fragment support fixes
  * python stylesheet compare and transform context access
  * EXSLT string replace support
  * xsltproc better low level error handling
- fixed crash on ENOMEM (null-retval.patch) [#215223]
- drop obsolete patches:
  * libxslt-aliasing.patch (included in update)
  * libxslt-transform.patch (included in update)
* Thu Dec 21 2006 ro@suse.de
- fix for crash with certain transformations (libxcb build crash)
* Tue Dec 12 2006 ke@suse.de
- 1.1.19; NEWS extract:
  * Bug fixes: entities within attributes; in-scope namespace bug, result
  value tree caching bug, a number of namespace related bugs, etc.
  * Improvements: refactoring of namespace handling, value-of
  impleemntation and template internal processing, new xsltproc flag to
  apply Xinclude to stylesheets.
  * Documentation.
* Fri Oct 27 2006 dmueller@suse.de
- update --nonet patch to work even when using rpmbuild directly
* Tue Oct 24 2006 dmueller@suse.de
- make --nonet default while building packages (#214338)
* Tue Oct 17 2006 ke@suse.de
- Move devel docs to the -devel subpackage; reported by Andreas Hanke [#
  212441].
* Fri Jun 16 2006 ke@suse.de
- 1.1.17:
  * Bug fixes: some regression tests, attribute/namespaces output,
    problem in mixed xsl:value-of and xsl:text uses.
  * Improvements: internal refactoring, use of the XPath object cache in
    libxml2-2.6.25.
- Require libxml2-2.2.25.
* Tue May 23 2006 ke@suse.de
- Update to version 1.1.16:
  * Bug fixes (pattern compilation, namespace prefixes, etc.).
  * Speed up sorting.
  * Documentation update.
- Adjust warn patch; drop libxslt-xpath-pattern.patch.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Oct 11 2005 ke@suse.de
- On account of pattern.c, add -fno-strict-aliasing again.
- Also require glibc-devel.
* Tue Oct  4 2005 ke@suse.de
- libxslt-xpath-pattern.patch:
  libxslt/pattern.c: fixed problem in internal XPath compilation
  of patterns including variables, fixes GNOME bug #316861
  (William Brack).  Reported by Andreas Jaeger/Uwe Gansert.
* Fri Sep 30 2005 aj@suse.de
- Fix compiler warnings.
- Add missing requires.
* Fri Sep 16 2005 ke@suse.de
- Update to version 1.1.15; NEWS from  http://xmlsoft.org/XSLT/ :
  * Bug fixes and improvements.
  * Documentation enhancement.
* Wed Jul  6 2005 meissner@suse.de
- fixed strict aliasing problem.
* Mon Apr  4 2005 ke@suse.de
- Update to version 1.1.14; some NEWS (extract since .13) from
  http://xmlsoft.org/XSLT/ :
  * Extensions: module support; dictionnary based speedups trying to get
    rid of xmlStrEqual as much as possible.
  * Bugfixes:
    exslt day-of-week-in-month, xsl:call-template should not change the
    current template rule, evaluation of global variables, RVT's in
    XPath predicates, namespace URI on template names, pattern
    expression fixes, out of memory detection misses, parserOptions
    propagation, exclude-result-prefixes fix, // patten fix,  text node
    on stylesheet document without a dictionary, more checking of XSLT
    syntax, calling xsltInit() multiple times, bug in pattern matching
    with ancestors, bug in pattern matching with cascading select,
    xinclude and document() problem.
- CFLAGS: Add -fno-strict-aliasing.
* Fri Dec 10 2004 ke@suse.de
- Do not list manpages twice; reported by Chris Lahey [Novell #472] and
  [# 49118].
* Tue Nov  2 2004 ke@suse.de
- Update to version 1.1.12; some NEWS from http://xmlsoft.org/XSLT/ :
  * Bug fixes: attribute document pointer fix, exslt date negative
    periods, generated tree structure fixes, namespace lookup fix, use
    reentrant gmtime_r, exslt:funtion namespace fix, potential NULL
    pointer reference, force string interning on generated documents.
  * Improve documentation.
* Fri Oct  8 2004 ke@suse.de
- Update to version 1.1.11; some NEWS from http://xmlsoft.org/XSLT/
  (since 1.1.9):
  * Bug fixes: xsl:include problems, UTF8 number pattern, date-time
    validation, namespace fix, various Exslt date fixes, error callback
    fixes, leak with namespaced global variable, attempt to fix a weird
    problem (Gnome Bugzilla #153137), key initialization problem.
  * Improvements: exslt:date-sum tests.
  * Documentation: Second tutorial by Panagiotis Lourida.
- Enable crypto support [#44119].
* Mon Aug 23 2004 ke@suse.de
- Update to version 1.1.9; some NEWS from http://xmlsoft.org/XSLT/
  * Various bug fixes (RVT key handling, Python bindings, key and XPath,
    64bit issue, etc.).
* Thu Aug 19 2004 schwab@suse.de
- Fix a broken cast.
* Wed Jul 14 2004 ke@suse.de
- Update to version 1.1.8; some NEWS from http://xmlsoft.org/XSLT/ :
  * Bug fixes.
* Fri May 21 2004 ke@suse.de
- Update to version 1.1.7; some NEWS from http://xmlsoft.org/XSLT/ :
  * Bugfixes: UTF-8 string tokenize, fix subtle memory corruption,
    linefeed after comment at document level, disable-output-escaping
    problem, pattern compilation in deep imported stylesheets,
    namespace extension prefix bug, namespace lookup for attribute,
    namespaced DOCTYPE name.
* Tue Apr 20 2004 ke@suse.de
- Update to version 1.1.6; some NEWS from
  http://xmlsoft.org/XSLT/ (since 1.1.2):
  * Performance improvements (e.g., dictionnary reuses for XSLT).
  * Various bugfixes (keys, thread troubles, tokenize fix for UTF-8,
  xpath, etc.).
  * Documentation cleanup.
- Drop obsolete patch (libxslt-m4.diff).
* Mon Mar 15 2004 ke@suse.de
- libxslt-m4.diff: Quote first argument of AC_DEFUN; reported by Dirk
  Mueller [# 35887].
* Mon Jan 12 2004 adrian@suse.de
- build as user
* Wed Jan  7 2004 ke@suse.de
- Update to version 1.1.2; NEWS from http://xmlsoft.org/XSLT/:
  * Documentation fixes; EXSLT documentation.
  * Bug fixes: exslt:date returning NULL strings, namespaces output,
    key and namespace definition problem, passing options down to
    the document() parser, xsl:number fixes.
* Fri Dec 12 2003 ke@suse.de
- Update to version 1.1.1; NEWS from http://xmlsoft.org/XSLT/:
  * bug fixes: number formatting, exslt:tokenize, key selector parsing
    with |, xsl:element with computed namespaces, xslt:import/include
    recursion detection, exslt:function used in keys, bug when
    CDATA_SECTION are found in the tree, entities handling when using
    XInclude.
* Wed Nov  5 2003 ke@suse.de
- Update to version 1.1.0; NEWS from http://xmlsoft.org/XSLT/:
  * Make use of the new libxml2 API.
  * Remove DocBook SGML broken support.
  * Remove the deprecated breakpoint library
  * Fixes: xsl:key to work with PIs, extension memory error fix, header
    path, some tortuous template problems when using predicates, a bug
    in default processing of attributes, detect invalid names on
    templates, exslt:document (and similar) base handling problem,
  * xsltproc option display fix,
  * Python: never use stdout for error.
* Tue Oct  7 2003 ke@suse.de
- Update to version 1.0.33; NEWS from http://xmlsoft.org/XSLT/:
  * mode not cascaded in template fallbacks.
  * catch redefinition of parameter/variables.
  * multiple keys with same namespace name.
  * cdata-section-elements handling of namespaced names.
  * apply-templates crash.
  * bug with imported templates.
  * imported attribute-sets merging bug (DocBook).
* Thu Sep 18 2003 sf@suse.de
- Do not free the hash keys during xmlHashScanFull,
  it will corrupt the hash table. The keys will be
  freed by xmlHashFree right afterwards anyway. #30506
* Fri Aug 15 2003 ke@suse.de
- Update to version 1.0.32; NEWS from http://xmlsoft.org/XSLT/:
  * Bugfixes: xsltSaveResultToFile() python binding, EXSLT fixes,
    speed of large text output, xsl:copy with attributes, strip-space and
    namespaces prefix, fix for --path xsltproc option, sort with multiple
    keys, checking of { and } for attribute value templates.
  * Python bindings for extension elements.
  * Doc cleanup.
* Wed Jul  9 2003 ke@suse.de
- Update to version 1.0.31; NEWS from http://xmlsoft.org/XSLT/:
  * Bugfixes: xsl:copy on namespace nodes, AVT for xsl:sort order, fix
    for the debugger, output filename limitation, trio.h and triodef.h
    added, EXSLT node-set, xsltChoose and whitespace, stylesheet
    compilation, NaN and sort.
  * Avoid generating &quot; (fix in libxml2-2.5.8)
* Tue Jun 17 2003 sbrabec@suse.cz
- Updated to version 1.0.30.
- Fixed linking of libxsltbreakpoint.
* Mon May 26 2003 ke@suse.de
- Remove unwanted files from $RPM_BUILD_ROOT.
* Wed Apr  2 2003 ke@suse.de
- Update to version 1.0.29; NEWS from http://xmlsoft.org/XSLT/:
  Significant speedup for large (flat) documents which also requires
  libxml2-2.5.6:
  * Bug fixes: Result Value Tree handling, XML IDs, keys(), extra namespace
    declarations with xsl:elements.
* Wed Mar 26 2003 ke@suse.de
- Update to version 1.0.28; NEWS from http://xmlsoft.org/XSLT/:
  * Fix node() in patterns semantic.
  * Fix a memory access problem in format-number()
  * Fix stack overflow in recursive global variable or params
  * Clean up Result Value Tree handling, and fix a couple of
  old bugs in the process.
* Tue Feb 11 2003 ke@suse.de
- Update to version 1.0.26; NEWS from http://xmlsoft.org/XSLT/:
  * Fixed 3 serious bugs in document() and stylesheet compilation which
    could lead to a crash.
* Thu Feb  6 2003 ke@suse.de
- Update to version 1.0.24; NEWS from http://xmlsoft.org/XSLT/:
  * Bug fixes: double-free for standalone stylesheets introduced in
    1.0.24, C syntax pbm, etc.
  * Some XPath and XInclude related problems were actually fixed in
    libxml2-2.5.2.
  * Documentation: emphasize that --docbook is not for XML docs.
* Wed Jan 15 2003 ke@suse.de
- Update to version 1.0.24; NEWS from http://xmlsoft.org/XSLT/:
  A lot of bug fixes and a few improvements:
  * Bug fixes: imported global varables, python bindings, EXSLT memory
    leak, namespace generation on xsl:attribute, space handling with
    imports, extension-element-prefixes, comments within xsl:text,
    superfluous xmlns generation, XInclude related bug for numbering,
    EXSLT strings, attribute-sets computation on imports, extension module
    init and shutdown callbacks not called.
  * Add xsltGetProfileInformation().
  * Fix API generation scripts.
  * API to provide the sorting routines.
  * Add XML description of the EXSLT API.
  * Add ESXLT URI (un)escaping.
  * Fix some memory leaks.
  * document() now supports fragment identifiers in URIs.
* Tue Nov 26 2002 ro@suse.de
- split libxslt-python to own specfile
  (libxslt is turning more and more into a base package
  and python requires a lot of other things to build)
- removed gtkdoc from neededforbuild (html is not rebuilt anyway)
* Mon Nov 18 2002 ke@suse.de
- Update to version 1.0.23; NEWS from http://xmlsoft.org/XSLT/:
  * Improvement of the python bindings: extension functions and
    activating EXSLT.
  * various bug fixes: number formatting, portability for bounded string
    functions, CData nodes, key(), @*[...] patterns.
  * Documentation improvements.
  * Add libxslt.m4.
- Require libxml2 2.4.27.
* Thu Oct 31 2002 ke@suse.de
- Update to version 1.0.22; NEWS from http://xmlsoft.org/XSLT/:
  * Add a security module, and a related set of new options to xsltproc.
  * Allow per transformation error handler.
  * Fix a few bugs: node() semantic, URI escaping, media-type, attribute
  lists.
* Wed Oct  9 2002 ke@suse.de
- Update to version 1.0.21; NEWS from http://xmlsoft.org/XSLT/:
  * Bug  fixes:  match="node()",  date:difference(), disable-output-escaping
  * Mem leak fix.
  * Python bindings: style.saveResultToString().
  * Documentation improvements.
  * try  to  handle  document('') as best as possible depending in the
  cases
  * Fix the DocBook stylesheets handling problem
  * Fix a few XSLT reported errors
- Drop namespace patch (already included).
* Tue Aug 20 2002 ke@suse.de
- Apply patch by Daniel Veillard to fix a namespace problem raised by
  recent DocBook stylesheets
  (cf. http://bugzilla.gnome.org/show_bug.cgi?id=87901).
  Reported by Stephan Kulow [# 18099].
* Wed Jul 31 2002 ke@suse.de
- Run %%run_ldconfig.
* Mon Jul  8 2002 ke@suse.de
- Update to version 1.0.19; NEWS from http://xmlsoft.org/XSLT/, not
  mentioned earlier:
  * Bug fixes: attributes, extra namespace declarations (DocBook),
    xsl:include crash, documentation, element-available.
  * xsltproc can now list registered extensions.
  * New API to save directly to a string xsltSaveResultToString().
  * Specific error registration function for the python API.
* Wed May 29 2002 ro@suse.de
- tweak python installation some more for lib64
* Tue May 28 2002 ke@suse.de
- Update to 1.0.18:
  - Add Pyhton bindings (libxslt-python).
  - Bug fixes.
  - New man page for libexslt.
* Tue Apr 30 2002 ke@suse.de
- Update to version 1.0.17; NEWS from http://xmlsoft.org/XSLT/ :
  o EXSLT date improvement and regression tests.
  o Attempt to fix a bug in xsltProcessUserParamInternal.
* Fri Apr 19 2002 ke@suse.de
- Update to version 1.0.16; NEWS from http://xmlsoft.org/XSLT/ :
  o Bug fixes: strip-space, URL in HTML output, error when xsltproc
    can't save.
  o Improve Python bindings.
* Tue Apr  9 2002 ke@suse.de
- Update to version 1.0.15; NEWS since 1.0.9 from http://xmlsoft.org/XSLT/ :
  * Change of Licence to the MIT Licence.
  * Bugfixes: XPath, python Makefile, recursive attribute sets,
    @foo[..] templates.
  * Fix a bug raised when using doctypes with HTML output.
  * More EXSLT functions.
  * Provide fixes and regression tests for exslt date functions.
  * Nasty bug fix related to exslt:node-set.
  * Fix bug "namespace node have no parents".
  * Obsoleted libxsltbreakpoint now deprecated and frozen to 1.0.8 API
  * xsltproc return codes are now significant, update documentation.
  * Debug of memory alocation with valgind.
  * Patch to allow as much as 40 steps in patterns.
  * Enhancements to interface with xsltdebugger.
  * Added a stringparam option to avoid escaping hell at the shell level.
  * serious profiling leading to significant improvement for DocBook
    processing.
  * Improvement in the XPath engine (libxml2-2.4.18).
  * Add Python bindings.
  * Documentation changes and updates.
* Wed Feb 20 2002 olh@suse.de
- fix prefix tag to build shared libs
* Tue Feb 12 2002 adrian@suse.de
- fix build for s390x
* Tue Dec 11 2001 ro@suse.de
- use less intrusive hack for libtool: export LIBRARY_PATH
* Thu Nov 29 2001 ro@suse.de
- install without buildroot first to work around libtool
  not being able to cope with dependant libraries and buildroot
* Tue Nov 27 2001 ke@suse.de
- Update to version 1.0.8; NEWS from http://xmlsoft.org/XSLT/ :
  - Previous header patch is superfluous.
  - Bug fixes.
* Tue Nov 20 2001 ke@suse.de
- Add missing define; cf.
  http://mail.gnome.org/archives/xslt/2001-November/msg00052.html .
- NEWS for 1.0.7 entries from http://xmlsoft.org/XSLT/ (not
  mentioned earlier):
  - Fix handling of indent="no" on HTML output.
* Sat Nov 10 2001 adrian@suse.de
- Update to version 1.0.7
- add fixes for automake 1.5
* Sat Nov  3 2001 ro@suse.de
- fix for automake 1.5
* Wed Oct 31 2001 ke@suse.de
- Update to version 1.0.6; NEWS from http://xmlsoft.org/XSLT/ :
  - Bug fixes on number formatting and date/time functions.
  - Fix DOCTYPE generation rules for HTML output.
* Thu Oct 11 2001 ke@suse.de
- Update to version 1.0.5; NEWS from http://xmlsoft.org/XSLT/ :
  - Portability fixes.
  - Fix a dozen bugs on XSLT and EXSLT.
  - Add support for Saxon's evaluate and expressions extensions.
  - Better handling of XPath evaluation errors.
* Mon Oct  1 2001 ke@suse.de
- Update to version 1.0.4; NEWS from http://xmlsoft.org/XSLT/ :
  - Documentation updates.
  - Bug fixes (DocBook FO generation should be fixed) and portability
    improvements.
  - Improve existing EXSLT support and add String, Time and Date core
    functions support.
* Fri Aug 24 2001 ke@suse.de
- Update to version 1.0.3; from the announcement (cf. libxml2):
  - Implement XML Catalog Specification from August 6:
    http://www.oasis-open.org/committees/entity/spec-2001-08-06.html
    http://xmlsoft.org/catalog.html
  - New NaN and Infinity code.
  - A number of small bugfixes.
* Fri Aug 17 2001 ke@suse.de
- Update to version 1.0.2.
- Call 'libtoolize' and friends.
* Wed Jul 11 2001 ke@suse.de
- New package: version 1.0.0.
