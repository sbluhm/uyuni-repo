#
# spec file for package libxml2
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

%if 0%{?rhel}
%define ext_man .gz
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Define "python" as a package in _multibuild file
%global flavor %{nil}
%if "%{flavor}" == "python"
%define psuffix -python
%define oldpython python
%bcond_without python
%bcond_without python2
%else
%define psuffix %{nil}
%bcond_with python
%endif
%define bname libxml2
%define lname libxml2-2
Name:           %{bname}%{psuffix}
Version:        2.9.10
Release:        5.1
Summary:        A Library to Manipulate XML Files
License:        MIT
URL:            http://xmlsoft.org
Source:         ftp://xmlsoft.org/libxml2/%{bname}-%{version}.tar.gz
Source1:        ftp://xmlsoft.org/libxml2/%{bname}-%{version}.tar.gz.asc
Source2:        baselibs.conf
Source3:        libxml2.keyring
Patch0:         fix-perl.diff
Patch1:         libxml2-python3-unicode-errors.patch
# PATCH-FIX-UPSTREAM libxml2-python3-string-null-check.patch bsc#1065270 mgorse@suse.com
# don't return a NULL string for an invalid UTF-8 conversion.
Patch2:         libxml2-python3-string-null-check.patch
# PATCH-FIX-SUSE bsc#1135123 Added a new configurable variable XPATH_DEFAULT_MAX_NODESET_LENGTH to avoid nodeset limit
Patch3:         libxml2-make-XPATH_MAX_NODESET_LENGTH-configurable.patch
# PATCH-FIX-UPSTREAM bsc#1157450 This commit breaks perl-XML-LibXSLT
Patch4:         libxml2-xmlFreeNodeList-recursive.patch
# PATCH-FIX-UPSTREAM bsc#1161517 CVE-2020-7595 Infinite loop in xmlStringLenDecodeEntities
Patch5:         libxml2-CVE-2020-7595.patch
# PATCH-FIX-UPSTREAM bsc#1159928 CVE-2019-19956 Revert usptream commit
Patch6:         libxml2-CVE-2019-19956.patch
# PATCH-FIX-UPSTREAM bsc#1176179 CVE-2020-24977 xmllint: global-buffer-overflow in xmlEncodeEntitiesInternal
Patch7:         libxml2-CVE-2020-24977.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
%if !%{with python}
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
%endif
%if %{with python}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module xml}
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       libxml2-2 = %{version}
%if "%{python_flavor}" == "python2"
Obsoletes:      %{bname}-python < %{version}
Provides:       %{bname}-python = %{version}
Obsoletes:      %{oldpython}-libxml2 < %{version}
Provides:       %{oldpython}-libxml2 = %{version}
%endif
%endif

%description
The XML C library was initially developed for the GNOME project. It is
now used by many programs to load and save extensible data structures
or manipulate any kind of XML files.

%package -n %{lname}
Summary:        A Library to Manipulate XML Files

%description -n %{lname}
The XML C library was initially developed for the GNOME project. It is
now used by many programs to load and save extensible data structures
or manipulate any kind of XML files.

This library implements a number of existing standards related to
markup languages, including the XML standard, name spaces in XML, XML
Base, RFC 2396, XPath, XPointer, HTML4, XInclude, SGML catalogs, and
XML catalogs. In most cases, libxml tries to implement the
specification in a rather strict way. To some extent, it provides
support for the following specifications, but does not claim to
implement them: DOM, FTP client, HTTP client, and SAX.

The library also supports RelaxNG. Support for W3C XML Schemas is in
progress.

%package tools
Summary:        Tools using libxml
Provides:       %{bname} = %{version}-%{release}
Obsoletes:      %{bname} < %{version}-%{release}

%description tools
This package contains xmllint, a very useful tool proving libxml's power.

%package devel
Summary:        Development files for libxml2, an XML manipulation library
Requires:       %{bname}-tools = %{version}
Requires:       %{lname} = %{version}
Requires:       glibc-devel
Requires:       readline-devel
Requires:       xz-devel
Requires:       zlib-devel
Requires:       pkgconfig(liblzma)
Requires:       pkgconfig(zlib)

%description devel
The XML C library can load and save extensible data structures
or manipulate any kind of XML files.

This subpackage contains header files for developing
applications that want to make use of libxml.

%package doc
Summary:        Documentation for libxml, an XML manipulation library
Requires:       %{lname} = %{version}
BuildArch:      noarch

%description doc
The XML C library was initially developed for the GNOME project. It is
now used by many programs to load and save extensible data structures
or manipulate any kind of XML files.

%package -n python2-libxml2
Summary:        Python 2 Bindings for libxml2
Obsoletes:      libxml2-python
Provides:       python2-libxml2-python
Obsoletes:      python2-libxml2-python

%description -n python2-libxml2
The python2-libxml2 package contains a module that permits
applications written in the Python programming language to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows manipulation of XML files. It includes support for
reading, modifying, and writing XML and HTML files. There is DTD
support that includes parsing and validation even with complex DTDs,
either at parse time or later once the document has been modified.

%package -n python3-libxml2
Summary:        Python 3 Bindings for libxml2
Obsoletes:      libxml2-python
Provides:       python3-libxml2-python
Obsoletes:      python3-libxml2-python

%description -n python3-libxml2
The python3-libxml2 package contains a module that permits
applications written in the Python programming language to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows manipulation of XML files. It includes support for
reading, modifying, and writing XML and HTML files. There is DTD
support that includes parsing and validation even with complex DTDs,
either at parse time or later once the document has been modified.

%prep
%setup -q -n libxml2-%{version}
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 -R
%patch5 -p1
%patch6 -p1 -R
%patch7 -p1

%build
%if !%{with python}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --disable-silent-rules \
    --disable-static \
    --docdir=%{_docdir}/%{bname} \
    --with-html-dir=%{_docdir}/%{bname}/html \
    --without-python \
    --with-fexceptions \
    --with-history \
    --enable-ipv6 \
    --with-sax1 \
    --with-regexps \
    --with-threads \
    --with-reader \
    --with-http

%make_build BASE_DIR="%{_docdir}" DOC_MODULE="%{bname}"
%else
pushd python
%python_build
popd
%endif

%install
%if !%{with python}
%make_install BASE_DIR="%{_docdir}" DOC_MODULE="%{bname}"
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p "%{buildroot}/%{_docdir}/%{bname}"
cp -a AUTHORS NEWS README TODO* %{buildroot}%{_docdir}/%{bname}/
ln -s libxml2/libxml %{buildroot}%{_includedir}/libxml
# Remove duplicated file Copyright as not found by fdupes
rm -fr %{buildroot}%{_docdir}/%{bname}/Copyright
%fdupes %{buildroot}%{_datadir}
%else
pushd python
%python_install
popd
chmod a-x python/tests/*.py
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
%if !%{with python}
# qemu-arm can't keep up atm, disabling check for arm
%ifnarch %{arm}
%make_build check
%endif
%endif

%if !%{with python}
%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/lib*.so.*
%license COPYING* Copyright
%doc %dir %{_docdir}/%{bname}
%doc %{_docdir}/%{bname}/[ANRCT]*

%files tools
%{_bindir}/xmllint
%{_bindir}/xmlcatalog
%{_mandir}/man1/xmllint.1%{?ext_man}
%{_mandir}/man1/xmlcatalog.1%{?ext_man}

%files devel
%{_bindir}/xml2-config
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/libxml.m4
%{_includedir}/libxml
%{_includedir}/libxml2
%{_libdir}/lib*.so
%{_libdir}/*.sh
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake
%{_mandir}/man1/xml2-config.1%{?ext_man}
%{_mandir}/man3/libxml.3%{?ext_man}

%files doc
%{_datadir}/gtk-doc/html/*
%doc %{_docdir}/%{bname}/examples
%doc %{_docdir}/%{bname}/html
# owning these directories prevents gtk-doc <-> libxml2 build loop:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html

%else
%files -n python3-libxml2
%doc python/TODO
%doc python/libxml2class.txt
%doc doc/*.py
%doc doc/python.html
%{python3_sitearch}/*

%if %{with python2}
%files -n python2-libxml2
%doc python/TODO
%doc python/libxml2class.txt
%doc doc/*.py
%doc doc/python.html
%{python_sitearch}/*
%endif
%endif

%changelog
* Mon Sep  7 2020 Pedro Monreal <pmonreal@suse.com>
- Security fix: [bsc#1176179, CVE-2020-24977]
  * xmllint: global-buffer-overflow in xmlEncodeEntitiesInternal
- Add patch libxml2-CVE-2020-24977.patch
* Wed May 27 2020 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Fix invalid xmlns references since the fix for CVE-2019-19956 [bsc#1172021]
- Revert upstream commit 5a02583c7e683896d84878bd90641d8d9b0d0549
  * Add patch libxml2-CVE-2019-19956.patch
* Mon Mar 16 2020 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Security fix: [bsc#1161517, CVE-2020-7595]
  * xmlStringLenDecodeEntities in parser.c has an infinite loop in
    a certain end-of-file situation
- Add libxml2-CVE-2020-7595.patch
* Mon Mar 16 2020 Tomáš Chvátal <tchvatal@suse.com>
- Do not pull in the non-python deps on the python build
* Sat Mar 14 2020 Tomáš Chvátal <tchvatal@suse.com>
- Revert the previous change and use multibuild to determine
  supported flavors.
  We need to be able to enable/disable pythons in prjconf and
  multibuild directly clashes with that.
* Sun Dec 15 2019 Stefan Brüns <stefan.bruens@rwth-aachen.de>
- Build python2 and python3 bindings in separate flavors. As
  python3-libxml2 is a dependency of e.g. itstools and thus many
  other packages these packages no longer have a build dependency
  on python2. Breaks a build loop for python2.
* Thu Nov 28 2019 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Since libxml2-2.9.10 perl-XML-LibXSLT fails to build: [bsc#1157450]
  * Revert upstream commit to make xmlFreeNodeList non-recursive
    https://github.com/GNOME/libxml2/commit/0762c9b69ba01628f72eada1c64ff3d361fb5716
- Add patch libxml2-xmlFreeNodeList-recursive.patch
* Fri Nov 15 2019 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Version update to 2.9.10:
  * Portability:
    + Fix exponent digits when running tests under old MSVC
    + Work around buggy ceil() function on AIX
    + Don't call printf with NULL string in runtest.c
    + Switched from unsigned long to ptrdiff_t in parser.c
    + timsort.h: support older GCCs
    + Make configure.ac work with older pkg-config
  * Bug Fixes:
    + Fix for conditional sections at end of document
    + Make sure that Python tests exit with error code
    + Audit memory error handling in xpath.c
    + Fix error code in xmlTextWriterStartDocument
    + Fix integer overflow when counting written bytes
    + Fix uninitialized memory access in HTML parser
    + Fix memory leak in xmlSchemaValAtomicType
    + Disallow conditional sections in internal subset
    + Fix use-after-free in xmlTextReaderFreeNodeList
    + Fix Regextests
    + Fix empty branch in regex
    + Fix integer overflow in entity recursion check
    + Don't read external entities or XIncludes from stdin
    + Fix Schema determinism check of ##other namespaces
    + Fix potential null deref in xmlSchemaIDCFillNodeTables
    + Fix potential memory leak in xmlBufBackToBuffer
    + Fix error message when processing XIncludes with fallbacks
    + Fix memory leak in xmlRegEpxFromParse
    + 14:00 is a valid timezone for xs:dateTime
    + Fix memory leak in xmlParseBalancedChunkMemoryRecover
    + Fix potential null deref in xmlRelaxNGParsePatterns
    + Misleading error message with xs:{min|max}Inclusive
    + Fix memory leak in xmlXIncludeLoadTxt
    + Partial fix for comparison of xs:durations
    + Fix null deref in xmlreader buffer
    + Fix unability to RelaxNG-validate grammar with choice-based name class
    + Fix unability to validate ambiguously constructed interleave for RelaxNG
    + Fix possible null dereference in xmlXPathIdFunction
    + fix memory leak in xmlAllocOutputBuffer
    + Fix unsigned int overflow
    + dict.h: gcc 2.95 doesn't allow multiple storage classes
    + Fix another code path in xmlParseQName
    + Make sure that xmlParseQName returns NULL in error case
    + Fix build without reader but with pattern
    + Fix memory leak in xmlAllocOutputBufferInternal error path
    + Fix unsigned integer overflow
    + Fix return value of xmlOutputBufferWrite
    + Fix parser termination from "Double hyphen within comment" error
    + Fix call stack overflow in xmlFreePattern
    + Fix null deref in previous commit
    + Fix memory leaks in xmlXPathParseNameComplex error paths
    + Check for integer overflow in xmlXPtrEvalChildSeq
    + Fix xmllint dump of XPath namespace nodes
    + Fix float casts in xmlXPathSubstringFunction
    + Fix null deref in xmlregexp error path
    + Fix null pointer dereference in xmlTextReaderReadOuterXml
    + Fix memory leaks in xmlParseStartTag2 error paths
    + Fix memory leak in xmlSAX2StartElement
    + Fix commit "Memory leak in xmlFreeID (xmlreader.c)"
    + Fix NULL pointer deref in xmlTextReaderValidateEntity
    + Memory leak in xmlFreeTextReader
    + Memory leak in xmlFreeID (xmlreader.c)
  * Improvements:
    + Propagate memory errors in valuePush
    + Propagate memory errors in xmlXPathCompExprAdd
    + Make xmlFreeDocElementContent non-recursive
    + Avoid ignored attribute warnings under GCC
    + Make xmlDumpElementContent non-recursive
    + Make apibuild.py ignore ATTRIBUTE_NO_SANITIZE
    + Mark xmlExp* symbols as removed
    + Make xmlParseConditionalSections non-recursive
    + Adjust expected error in Python tests
    + Make xmlTextReaderFreeNodeList non-recursive
    + Make xmlFreeNodeList non-recursive
    + Make xmlParseContent and xmlParseElement non-recursive
    + Remove executable bit from non-executable files
    + Fix expected output of test/schemas/any4
    + Optimize build instructions in README
    + xml2-config.in: Output CFLAGS and LIBS on the same line
    + xml2-config: Add a --dynamic switch to print only shared libraries
    + Annotate functions with __attribute__((no_sanitize))
    + Fix warnings when compiling without reader or push parser
    + Remove unused member `doc` in xmlSaveCtxt
    + Limit recursion depth in xmlXPathCompOpEvalPredicate
    + Remove -Wno-array-bounds
    + Remove unreachable code in xmlXPathCountFunction
    + Improve XPath predicate and filter evaluation
    + Limit recursion depth in xmlXPathOptimizeExpression
    + Disable hash randomization when fuzzing
    + Optional recursion limit when parsing XPath expressions
    + Optional recursion limit when evaluating XPath expressions
    + Use break statements in xmlXPathCompOpEval
    + Optional XPath operation limit
    + Fix compilation with --with-minimum
    + Check XPath stack after calling functions
    + Remove debug printf in xmlreader.c
    + Always define LIBXML_THREAD_ENABLED when enabled
    + Fix unused function warning in testapi.c
    + Remove unneeded function pointer casts
    + Fix -Wcast-function-type warnings (GCC 8)
    + Fix -Wformat-truncation warnings (GCC 8)
  * Cleanups:
    + Rebuild docs
    + Disable xmlExp regex code
    + Remove redundant code in xmlRelaxNGValidateState
    + Remove redundant code in xmlXPathCompRelationalExpr
- Rebase patch fix-perl.diff
* Mon Sep  9 2019 Tomáš Chvátal <tchvatal@suse.com>
- Do not depend on setuptools to keep the depgraph small and
  avoid build cycles
* Fri Aug  2 2019 Tomáš Chvátal <tchvatal@suse.com>
- Use python[23]-libmxl2 as python names not python-libxml2-python
  which is kinda confusing
* Thu Aug  1 2019 Tomáš Chvátal <tchvatal@suse.com>
- Do not ship libtool archive anymore
* Wed Jul 31 2019 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Enable tests also in the python subpackages
* Thu Jul  4 2019 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Added a new configurable variable XPATH_DEFAULT_MAX_NODESET_LENGTH
  to avoid nodeset limit when processing large XML files [bsc#1135123]
  * Added libxml2-make-XPATH_MAX_NODESET_LENGTH-configurable.patch
* Mon Feb 25 2019 Pedro Monreal Gonzalez <pmonrealgonzalez@suse.com>
- Merge python-libxml2-python spec and changes files into the
  libxml2 ones using _multibuild [bsc#1126499, bsc#1123919]
* Sat Jan 26 2019 mgorse@suse.com
- Version update to 2.9.9:
  * Security:
    + CVE-2018-9251 CVE-2018-14567 Fix infinite loop in LZMA
    decompression (boo#1088279 boo#1105166).
    + CVE-2018-14404 Fix nullptr deref with XPath logic ops
    (boo#1102046).
  * Bug fixes:
    + Fix building relative URIs
    + Problem with data in interleave in RelaxNG validation
    + Fix memory leak in xmlSwitchInputEncodingInt error path
    + Set doc on element obtained from freeElems
    + Fix HTML serialization with UTF-8 encoding
    + Use actual doc in xmlTextReaderRead*Xml
    + Unlink node before freeing it in xmlSAX2StartElement
    + Check return value of nodePush in xmlSAX2StartElement
    + Free input buffer in xmlHaltParser
    + Reset HTML parser input pointers on encoding failure
    + Fix xmlSchemaValidCtxtPtr reuse memory leak
    + Fix xmlTextReaderNext with preparsed document
    + HTML noscript should not close p
    + Don't change context node in xmlXPathRoot
  * Improvements:
    + Remove redefined starts and defines inside include elements
    + Allow choice within choice in nameClass in RELAX NG
    + Look inside divs for starts and defines inside include
    +  Add newlines to 'xmllint --xpath' output
    + Don't include SAX.h from globals.h
    + Support xmlTextReaderNextSibling w/o preparsed doc
    + Improve restoring of context size and position
    + Simplify and harden nodeset filtering
    + Avoid unnecessary backups of the context node
    + Fix inconsistency in xmlXPathIsInf
- Add libxml2-python3-string-null-check.patch: fix NULL pointer
    dereference when parsing invalid data (bsc#1065270
    glgo#libxml2!15).).
* Tue Mar 20 2018 kukuk@suse.de
- Use %%license instead of %%doc [bsc#1082318]
* Wed Mar 14 2018 tchvatal@suse.com
- Version update to 2.9.8:
  * Various -Werror fixes and compilation updates as travis is now
    used by upstream
  * Few additional tests added for ICU operations
- Drop patch python3.6-verify_fd.patch merged upstream
* Sat Nov 11 2017 aavindraa@gmail.com
- Version update to 2.9.7 release:
  * Bug Fixes:
    + xmlcatalog: restore ability to query system catalog easily
    + Fix comparison of nodesets to strings
  * Improvements:
    + Add Makefile rules to rebuild HTML man pages
    + Remove generated file python/setup.py from version control
    + Fix mixed decls and code in timsort.h
    + Rework handling of return values in thread tests
    + Fix unused variable warnings in testrecurse
    + Fix -Wimplicit-fallthrough warnings
    + Upgrade timsort.h to latest revision
    + Fix a couple of warnings in dict.c and threads.c
    + Fix unused variable warnings in nanohttp.c
    + Don't include winsock2.h in xmllint.c
    + Use __linux__ macro in generated code
  * Portability:
    + Add declaration for DllMain
    + Fix preprocessor conditional in threads.h
    + Fix macro redefinition warning
    + many Windows specific improvements
  * Documentation:
    + xmlcatalog: refresh man page wrt. quering system catalog easily
- Includes bug fixes from 2.9.6:
  * Fix XPath stack frame logic
  * Report undefined XPath variable error message
  * Fix regression with librsvg
  * Handle more invalid entity values in recovery mode
  * Fix structured validation errors
  * Fix memory leak in LZMA decompressor
  * Set memory limit for LZMA decompression
  * Handle illegal entity values in recovery mode
  * Fix debug dump of streaming XPath expressions
  * Fix memory leak in nanoftp
  * Fix memory leaks in SAX1 parser
- Drop libxml2-bug787941.patch
  * upstreamed in 3157cf4e53c03bc3da604472c015c63141907db8
* Sat Nov 11 2017 aavindraa@gmail.com
- clean with spec-cleaner
* Thu Oct 26 2017 jmatejek@suse.com
- libxml2-python3-unicode-errors.patch: work around an issue with
  libxml2 supplied error strings being undecodable UTF-8 (bsc#1065270)
* Mon Oct  2 2017 jmatejek@suse.com
- convert to singlespec, build a python 3 version
- change build instructions to use setup.py (and %%python_build macros)
  instead of makefile-based approach
- add python3.6-verify_fd.patch that fixes libxml2 on python 3.6
- rename to python-libxml2-python to conform to package naming policy
  (PyPI name is "libxml2-python")
* Thu Sep 21 2017 jengelh@inai.de
- Update package summaries and RPM groups. Trim descriptions for
  size on secondary subpackages. Replace install call by a
  commonly-used macro.
* Thu Sep 21 2017 tchvatal@suse.com
- Add patch to fix TW integration:
  * libxml2-bug787941.patch
* Sun Sep 10 2017 tchvatal@suse.com
- Version update to 2.9.5 release:
  * Merged all the previous cve fixes that were patched in
  * Few small tweaks
- Remove merged patches:
  * libxml2-CVE-2016-4658.patch
  * libxml2-CVE-2017-0663.patch
  * libxml2-CVE-2017-5969.patch
  * libxml2-CVE-2017-9047.patch
  * libxml2-CVE-2017-9048.patch
  * libxml2-CVE-2017-9049.patch
  * libxml2-2.9.4-fix_attribute_decoding.patch
* Thu Jun 15 2017 pmonrealgonzalez@suse.com
- Security fix:
  * libxml2-CVE-2017-0663.patch [bsc#1044337, CVE-2017-0663]
  * Fix Heap buffer overflow in xmlAddID
* Wed Jun 14 2017 pmonrealgonzalez@suse.com
- Security fix:
  * libxml2-CVE-2017-5969.patch [bsc#1024989, CVE-2017-5969]
  * Fix NULL pointer deref in xmlDumpElementContent
* Mon May 22 2017 pmonrealgonzalez@suse.com
- Security fixes:
  * libxml2-CVE-2017-9049.patch [bsc#1039066]
  * heap-based buffer overflow (xmlDictComputeFastKey func)
  * libxml2-CVE-2017-9048.patch [bsc#1039063]
  * stack overflow vulnerability (xmlSnprintfElementContent func)
  * libxml2-CVE-2017-9047.patch [bsc#1039064]
  * stack overflow vulnerability (xmlSnprintfElementContent func)
* Tue Mar  7 2017 pmonrealgonzalez@suse.com
- Added libxml2-CVE-2016-4658.patch: Disallow namespace nodes in
  XPointer ranges. Namespace nodes must be copied to avoid
  use-after-free errors. But they don't necessarily have a physical
  representation in a document, so simply disallow them in XPointer
  ranges [bsc#1005544] [CVE-2016-4658]
* Wed Jun  8 2016 kstreitova@suse.com
- add libxml2-2.9.4-fix_attribute_decoding.patch to fix attribute
  decoding during XML schema validation [bnc#983288]
* Fri May 27 2016 psimons@suse.com
- Update libxml2 to version libxml2-2.9.4. The new version is
  resistant against CVE-2016-3627, CVE-2016-1833, CVE-2016-1835,
  CVE-2016-1837, CVE-2016-1836, CVE-2016-1839, CVE-2016-1838,
  CVE-2016-1840, CVE-2016-4483, CVE-2016-1834, CVE-2016-3705, and
  CVE-2016-1762.
- Remove obsolete patches libxml2-2.9.1-CVE-2016-3627.patch,
  0001-Add-missing-increments-of-recursion-depth-counter-to.patch,
  and libxml2-2.9.3-bogus_UTF-8_encoding_error.patch.
* Fri May 20 2016 kstreitova@suse.com
- add libxml2-2.9.3-bogus_UTF-8_encoding_error.patch to fix XML
  push parser that fails with bogus UTF-8 encoding error when
  multi-byte character in large CDATA section is split across
  buffer [bnc#962796]
* Tue May  3 2016 sflees@suse.de
- Add libxml2-2.9.1-CVE-2016-3627.patch to fix stack exhaustion
  while parsing certain XML files in recovery mode (CVE-2016-3627,
  bnc#972335).
- Add 0001-Add-missing-increments-of-recursion-depth-counter-to.patch
  to improve protection against Billion Laughs Attack (bnc#975947).
* Tue Nov 24 2015 rpm@fthiessen.de
- Update to new upstream release 2.9.3 (bsc#954429):
  * Fixes for CVE-2015-8035, CVE-2015-7942, CVE-2015-7941,
    CVE-2015-1819, CVE-2015-7497, CVE-2015-7498, CVE-2015-5312,
    CVE-2015-7499, CVE-2015-7500 and CVE-2015-8242
  * And other bugfixes
- Removed upstream fixed patches:
  * libxml2-dont_initialize_catalog.patch
  * 0001-Fix-missing-entities-after-CVE-2014-3660-fix.patch
  * 0002-Adding-example-from-bugs-738805-to-regression-tests.patch
* Mon Nov  3 2014 vcizek@suse.com
- fix a missing entities after CVE-2014-3660 fix
  (https://bugzilla.gnome.org/show_bug.cgi?id=738805)
  * added patches:
    0001-Fix-missing-entities-after-CVE-2014-3660-fix.patch
    0002-Adding-example-from-bugs-738805-to-regression-tests.patch
* Mon Nov  3 2014 vcizek@suse.com
- fix a regression in libxml2 2.9.2
  * https://bugzilla.redhat.com/show_bug.cgi?id=1153753
- add libxml2-dont_initialize_catalog.patch
* Fri Oct 31 2014 vcizek@suse.com
- update to 2.9.2
  * drop libxml2-CVE-2014-3660.patch (upstream)
  * add keyring to verify tarball
  Security:
  Fix for CVE-2014-3660 billion laugh variant
  CVE-2014-0191 Do not fetch external parameter entities
  Improvements:
  win32/libxml2.def.src after rebuild in doc
  elfgcchack.h: more legacy needs xmlSAX2StartElement() and xmlSAX2EndElement()
  elfgcchack.h: add xmlXPathNodeEval and xmlXPathSetContextNode
  Provide cmake module
  Fix a couple of issues raised by make dist
  Fix and add const qualifiers
  Preparing for upcoming release of 2.9.2
  Fix zlib and lzma libraries check via command line
  wrong error column in structured error when parsing end tag
  doc/news.html: small update to avoid line join while generating NEWS.
  Add methods for python3 iterator
  Support element node traversal in document fragments
  xmlNodeSetName: Allow setting the name to a substring of the currently set name
  Added macros for argument casts
  adding init calls to xml and html Read parsing entry points
  Get rid of 'REPLACEMENT CHARACTER' Unicode chars in xmlschemas.c
  Implement choice for name classes on attributes
  Two small namespace tweaks
  xmllint --memory should fail on empty files
  Cast encoding name to char pointer to match arg type
* Fri Oct 17 2014 vcizek@suse.com
- fix for CVE-2014-3660 (bnc#901546)
  * denial of service via recursive entity expansion
    (related to billion laughs)
  * added libxml2-CVE-2014-3660.patch
* Mon Aug 18 2014 fcrozat@suse.com
- Add obsoletes/provides to baselibs.conf.
* Thu Jun  5 2014 vcizek@suse.com
- temporarily reverting libxml2-CVE-2014-0191.patch until there is a fix
  that doesn't break other applications
* Fri May 23 2014 vcizek@suse.com
- fix for CVE-2014-0191 (bnc#876652)
  * libxml2: external parameter entity loaded when entity
    substitution is disabled
  * added libxml2-CVE-2014-0191.patch
* Fri Aug  2 2013 vcizek@suse.com
- update to 2.9.1
  dropped patches (in upstream):
  * libxml2-2.9.0-CVE-2012-5134.patch
  * libxml2-CVE-2013-0338-Detect-excessive-entities-expansion-upon-replacement.patch
  * libxml2-CVE-2013-1969.patch
  New features:
  * Support for Python3
  * Add xmlXPathSetContextNode and xmlXPathNodeEval
* Sun Jul  7 2013 coolo@suse.com
- buildignore python to avoid build cycle
* Thu Apr 18 2013 vcizek@suse.com
- fix for CVE-2013-1969 (bnc#815665)
  * libxml2-CVE-2013-1969.patch
* Thu Mar  7 2013 vcizek@suse.com
- fix for CVE-2013-0338 (bnc#805233)
  libxml2-CVE-2013-0338-Detect-excessive-entities-expansion-upon-replacement.patch
* Sat Dec 15 2012 p.drouand@gmail.com
- update to 2.9.0 version:
  * please see the Changelog
- Updated patchs to get working with new version:
  * libxml2-2.9.0-CVE-2012-5134.patch ( libxml2-CVE-2012-5134.patch )
  * fix-perl.diff
* Fri Dec  7 2012 vcizek@suse.com
- Add libxml2-CVE-2012-5134.patch to fix CVE-2012-5134 (bnc#793334)
* Sun Sep 23 2012 dimstar@opensuse.org
- Add a comment next to libxml2.la to make sure that anybody
  removing it knows why it's there and reconsiders.
* Sun Sep 23 2012 coolo@suse.com
- readd .la file, python-libxml2 needs it
* Fri Sep 21 2012 jengelh@inai.de
- Remove .la files; make sure installation succeeds for
  Fedora_17 target
* Tue Jun 12 2012 chris@computersalat.de
- update to 2.8.0
  * please see ChangeLog for more info
- remove obsolete bigendian64 patch
- rebase fix-perl patch
* Sun Mar 11 2012 jengelh@medozas.de
- libxml2-2 should not require libxml2-tools. There is no trouble
  expected, since attempting to install libxml2 will already pull
  in libxml2-tools due to Provides tags.
* Mon Mar  5 2012 coolo@suse.com
- revert the two commits that broke perl-XML-LibXML's test case,
  I hope the two upstreams will figure it out
* Fri Mar  2 2012 coolo@suse.com
- update to git to fix some issues
  * Fix a logic error in Schemas Component ConstraintsHEADmaster
  * Fix a wrong enum type use in Schemas Types
* Thu Mar  1 2012 meissner@suse.de
- fixed a 64bit big endian bug in the file reader.
* Sat Feb 25 2012 coolo@suse.com
- the fallout of requiring libxml2-tools as explicit buildrequire
  is just too large, so avoid it for now and create a cycle between
  libxml2-2 and libxml2-tools
* Sat Feb 25 2012 coolo@suse.com
- fix version
* Sat Feb 25 2012 coolo@suse.com
- add provide for the old name to fix packages with explicit
  library dependency
* Thu Feb 23 2012 coolo@suse.com
- renamed to python-libxml2 to follow python naming expectations
- do not require python but let rpm figure it out
* Thu Feb 23 2012 coolo@suse.com
- update to today's GIT snapshot:
    include XZ support
- split libxml2-2 according to shared library policy
* Mon Dec 26 2011 jengelh@medozas.de
- Remove redundant tags/sections
* Wed Dec 21 2011 coolo@suse.com
- add autoconf as buildrequire to avoid implicit dependency
* Tue Dec 20 2011 coolo@suse.com
- own aclocal directory, there is no other reason to buildrequire
  automake
* Fri Jul  8 2011 saschpe@suse.de
- update to libxml-2.7.8+git20110708
  - several important bugfixes
- drop upstreamed patches:
  * libxml2-CVE-2010-4494.patch
  * libxml2-CVE-2011-1944.patch
  * noxref.patch
  * symbol-versioning.patch
* Wed Jun 29 2011 puzel@novell.com
- add libxml2-CVE-2011-1944.patch (bnc#697372)
* Sun Jun  5 2011 cshorler@googlemail.com
- add symbol-versioning.patch to restore 11.3 versioned symbols
* Mon Jan  3 2011 puzel@novell.com
- add libxml2-CVE-2010-4494.patch (bnc#661471)
* Mon Dec  6 2010 coolo@novell.com
- buildrequire python-xml to fix build
* Fri Dec  3 2010 puzel@novell.com
- update to libxml-2.7.8
  - number of bufixes, documentation and portability fixes
  - update language ID parser to RFC 5646
  - sort python generated stubs
  - add an HTML parser option to avoid a default doctype
  - see http://xmlsoft.org/news.html for exact details
- drop libxml2-xpath-ns-attr-axis.patch (in upstream)
- clean up specfile
* Mon Nov  1 2010 puzel@novell.com
- add libxml2-xpath-ns-attr-axis.patch (bnc#648277)
* Sat Oct 30 2010 cristian.rodriguez@opensuse.org
- Use --disable-static
* Mon Sep 20 2010 puzel@novell.com
- drop libxml2-largefile64.patch (revert last change)
  - the issue is fixed in zlib
* Fri Sep 17 2010 puzel@novell.com
- add libxml2-largefile64.patch (fixes build)
  - debian bug#439843
* Wed Jul 14 2010 jw@novell.com
- added noxref.patch,
  this implements a new --noxref option, which turns
  validation errors about missing xrefs into warnings.
  Upstreamed as https://bugzilla.gnome.org/show_bug.cgi?id=624386
* Sat Apr 24 2010 coolo@novell.com
- buildrequire pkg-config to fix provides
* Wed Apr  7 2010 coolo@novell.com
- fix build
* Tue Mar 23 2010 mrdocs@opensuse.org
- update to 2.7.7
- add extra options to ./configure for scribus features and avoid a crash
- updates from 2.7.3 > 2.7.7 include a number of portability, correctness
  memory leaks and build fixes including some CVE
- see http://xmlsoft.org/news.html for exact details
* Mon Feb 22 2010 mrdocs@opensuse.org
- add sax parser option compiled in
* Tue Dec 15 2009 jengelh@medozas.de
- enable parallel building
* Mon Dec 14 2009 jengelh@medozas.de
- add baselibs.conf as a source
- package documentation as noarch
* Sun Aug  2 2009 jansimon.moeller@opensuse.org
- Disable the check for ARM as qemu-arm can't keep up atm.
* Thu Mar 19 2009 prusnak@suse.cz
- updated to 2.7.2
  * Portability fix: fix solaris compilation problem,
    fix compilation if XPath is not configured in
  * Bug fixes: nasty entity bug introduced in 2.7.0, restore old
    behaviour when saving an HTML doc with an xml dump function,
    HTML UTF-8 parsing bug, fix reader custom error handlers
    (Riccardo Scussat)
  * Improvement: xmlSave options for more flexibility to save
    as XML/HTML/XHTML, handle leading BOM in HTML documents
- updated to 2.7.3
  * Build fix: fix build when HTML support is not included.
  * Bug fixes: avoid memory overflow in gigantic text nodes,
    indentation problem on the writed (Rob Richards),
    xmlAddChildList pointer problem (Rob Richards and Kevin Milburn),
    xmlAddChild problem with attribute (Rob Richards and Kris Breuker),
    avoid a memory leak in an edge case (Daniel Zimmermann),
    deallocate some pthread data (Alex Ott).
  * Improvements: configure option to avoid rebuilding docs
    (Adrian Bunk), limit text nodes to 10MB max by default,
    add element traversal APIs, add a parser option to enable
    pre 2.7 SAX behavior (Rob Richards),
    add gcc malloc checking (Marcus Meissner),
    add gcc printf like functions parameters checking (Marcus Meissner).
- dropped obsoleted patches:
  * alloc_size.patch (mainline)
  * CVE-2008-4225.patch (mainline)
  * CVE-2008-4226.patch (mainline)
  * CVE-2008-4409.patch (mainline)
  * oldsax.patch (mainline)
  * pritnf.patch (mainline)
  * xmlsave.patch (mainline)
* Mon Jan 12 2009 prusnak@suse.cz
- added oldsax.patch to enable pre 2.7.0 sax behaviour [bnc#457056]
* Wed Dec 10 2008 olh@suse.de
- use Obsoletes: -XXbit only for ppc64 to help solver during distupgrade
  (bnc#437293)
* Tue Nov 25 2008 prusnak@suse.cz
- fix broken xmlsave (xmlsave.patch) [bnc#437203]
* Tue Nov 18 2008 prusnak@suse.cz
- fixed CVE-2008-4225 [bnc#445677]
* Thu Nov  6 2008 prusnak@suse.cz
- fixed CVE-2008-4226 [bnc#441368]
* Thu Oct 30 2008 olh@suse.de
- obsolete old -XXbit packages (bnc#437293)
* Mon Oct  6 2008 prusnak@suse.cz
- fixed CVE-2008-4409 [bnc#432486]
* Tue Sep  9 2008 meissner@suse.de
- added GCC attribute alloc_size markup (alloc_size.patch)
* Wed Sep  3 2008 prusnak@suse.cz
- updated to 2.7.1
  * Portability fix: Borland C fix (Moritz Both)
  * Bug fixes: python serialization wrappers, XPath QName corner
    case handking and leaks (Martin)
  * Improvement: extend the xmlSave to handle HTML documents and trees
  * Cleanup: python serialization wrappers
* Wed Sep  3 2008 prusnak@suse.cz
- updated to 2.7.0
  * Documentation: switch ChangeLog to UTF-8, improve mutithreads and
    xmlParserCleanup docs
  * Portability fixes: Older Win32 platforms (Rob Richards), MSVC
    porting fix (Rob Richards), Mac OS X regression tests (Sven Herzberg),
    non GNUCC builds (Rob Richards), compilation on Haiku (Andreas Färber)
  * Bug fixes: various realloc problems (Ashwin), potential double-free
    (Ashwin), regexp crash, icrash with invalid whitespace facets (Rob
    Richards), pattern fix when streaming (William Brack), various XML
    parsing and validation fixes based on the W3C regression tests, reader
    tree skipping function fix (Ashwin), Schemas regexps escaping fix
    (Volker Grabsch), handling of entity push errors (Ashwin), fix a slowdown
    when encoder cant serialize characters on output
  * Code cleanup: compilation fix without the reader, without the output
    (Robert Schwebel), python whitespace (Martin), many space/tabs cleanups,
    serious cleanup of the entity handling code
  * Improvement: switch parser to XML-1.0 5th edition, add parsing flags
    for old versions, switch URI parsing to RFC 3986,
    add xmlSchemaValidCtxtGetParserCtxt (Holger Kaelberer),
    new hashing functions for dictionnaries (based on Stefan Behnel work),
    improve handling of misplaced html/head/body in HTML parser, better
    regression test tools and code coverage display, better algorithms
    to detect various versions of the billion laughts attacks, make
    arbitrary parser limits avoidable as a parser option
- dropped obsoleted patches:
  * billion-laughs.patch (included in update)
* Wed Aug 13 2008 prusnak@suse.cz
- fixed billion laughs vulnerability (billion-laughs.patch) [bnc#415371]
* Fri Apr 11 2008 prusnak@suse.cz
- updated to 2.6.32
  * Documentation:
  - returning heap memory to kernel (Wolfram Sang)
  - trying to clarify xmlCleanupParser() use
  - xmlXPathContext improvement (Jack Jansen)
  - improve the *Recover* functions documentation
  - XmlNodeType doc link fix (Martijn Arts)
  * Bug fixes:
  - internal subset memory leak (Ashwin)
  - avoid problem with paths starting with // (Petr Sumbera)
  - streaming XSD validation callback patches (Ashwin)
  - fix redirection on port other than 80 (William Brack)
  - SAX2 leak (Ashwin)
  - XInclude fragment of own document (Chris Ryan)
  - regexp bug with '.' (Andrew Tosh)
  - flush the writer at the end of the document (Alfred Mickautsch)
  - output I/O bug fix (William Brack)
  - writer CDATA output after a text node (Alex Khesin)
  - UTF-16 encoding detection (William Brack)
  - fix handling of empty CDATA nodes for Safari team
  - python binding problem with namespace nodes
  - improve HTML parsing (Arnold Hendriks)
  - regexp automata build bug
  - memory leak fix (Vasily Chekalkin)
  - XSD test crash
  - weird system parameter entity parsing problem
  - allow save to file:///X/ windows paths
  - various attribute normalisation problems
  - externalSubsetSplit fix (Ashwin)
  - attribute redefinition in the DTD (Ashwin)
  - fix in char ref parsing check (Alex Khesin)
  - many out of memory handling fixes (Ashwin)
  - XPath out of memory handling fixes (Alvaro Herrera)
  - various realloc problems (Ashwin)
  - UCS4 encoding conversion buffer size (Christian Fruth)
  - problems with EatName functions on memory errors
  - BOM handling in external parsed entities (Mark Rowe)
  * Code cleanup:
  - fix build under VS 2008 (David Wimsey)
  - remove useless mutex in xmlDict (Florent Guilian)
  - Mingw32 compilation fix (Carlo Bramini)
  - Win and MacOS EOL cleanups (Florent Guiliani)
  - iconv need a const detection (Roumen Petrov)
  - simplify xmlSetProp (Julien Charbon)
  - cross compilation fixes for Mingw (Roumen Petrov)
  - SCO Openserver build fix (Florent Guiliani)
  - iconv uses const on Win32 (Rob Richards)
  - duplicate code removal (Ashwin)
  - missing malloc test and error reports (Ashwin)
  - VMS makefile fix (Tycho Hilhorst)
  * improvements:
  - better plug of schematron in the normal error handling (Tobias Minich)
* Thu Apr 10 2008 ro@suse.de
- added baselibs.conf file to build xxbit packages
  for multilib support
* Fri Mar 21 2008 vuntz@suse.de
- Remove libxml2-2.6.31-gcc4.patch after discussion with upstream.
  I compiled the package on all architectures without the patch
  without any problem, and upstream doesn't see the point of the
  patch.
* Thu Mar 13 2008 rodrigo@suse.de
- Upstream and tag patches
* Thu Jan 24 2008 prusnak@suse.cz
- rename rpmlintrc-libxml2-python to libxml2-python-rpmlintrc :)
* Tue Jan 22 2008 prusnak@suse.cz
- build --without-python to allow compilation from src.rpm
* Tue Jan 22 2008 prusnak@suse.cz
- rename rpmlintrc to rpmlintrc-libxml2-python
* Tue Jan 15 2008 prusnak@suse.cz
- updated to 2.6.31
  o security fix:
  * missing of checks in UTF-8 parsing
  o bug fixes:
  * regexp bug
  * dump attribute from XHTML document
  * fix xmlFree(NULL) to not crash in debug mode
  * Schematron parsing crash
  * XSD crash due to double free
  * indentation fix in xmlTextWriterFullEndElement
  * error in attribute type parsing if attribute redeclared
  * avoid crash in hash list scanner if deleting elements, column counter bug fix
  * HTML embed element saving fix
  * avoid -L/usr/lib output from xml2-config
  * avoid an xmllint crash
  * don't stop HTML parsing on out of range chars
  o code cleanup:
  * fix open() call third argument,
  * regexp cut'n paste copy error,
  * unused variable in __xmlGlobalInitMutexLock
  * some make distcheck realted fixes
  o improvements:
  * HTTP Header: includes port number
  * testURI --debug option
- removed obsolete patches:
  * CVE-2007-6284.patch (included in update)
  * open_create.patch (included in update)
* Fri Jan 11 2008 sbrabec@suse.cz
- Split documentation into a separate packages.
- Install devhelp documentation (#350918).
- Follow upstream documentation structure.
- Build again with strict aliasing.
- Removed s390* work-arounds. New gcc builds it again with -O2.
* Tue Dec 18 2007 prusnak@suse.cz
- fix libxml2 DoS (CVE-2007-6284.patch) [#349151]
* Tue Dec  4 2007 prusnak@suse.cz
- fix call to open() where 3rd parameter is needed (open_create.patch)
* Tue Sep 18 2007 sbrabec@suse.cz
- Updated to version 2.6.30:
  * Portability: Solaris crash on error handling, windows path
    fixes, mingw build
  * Bugfixes: xmlXPathNodeSetSort problem, leak when reusing a
    writer for a new document, Schemas xsi:nil handling patch,
    relative URI build problem, crash in xmlDocFormatDump, invalid
    char in comment detection bug, fix disparity with
    xmlSAXUserParseMemory, automata generation for complex regexp
    counts problems, Schemas IDC import problems, xpath predicate
    evailation error handling
* Thu Sep 13 2007 dmueller@suse.de
- build on s390x
* Tue Aug 28 2007 prusnak@suse.cz
- applied some fixes from 2.6.30 to fix regression that prevents
  the documentation from updating to Beta2 [#300675]
  (up30.patch)
* Mon Aug 20 2007 sbrabec@suse.cz
- Commented out NoSource to provide comfortable rebuild.
* Wed Jun 13 2007 prusnak@suse.cz
- updated to 2.6.29:
  o bug fixes:
  * fixed xmlBufferAdd problem
  * regexp interpretation of '\'
  * XPath number serialization
  * nanohttp gzipped stream fix
  * uri bug
  * XPath string value of PI nodes
  * XPath node set sorting bugs
  * avoid outputting namespace decl dups in the writer
  * xmlCtxtReset bug
  * UTF-8 encoding error handling
  * recustion on next in catalogs
  * Relax-NG crash
  * invalid character in attribute detection bug
  o improved:
  * keep URI query parts in raw form
  * embed tag support in HTML
- dropped obsolete patches:
  * pinode.patch (included in update)
* Tue Jun  5 2007 prusnak@suse.cz
- suppress spurious-executable-perm for test scripts using rpmlintrc
* Thu May 31 2007 prusnak@suse.cz
- moved tests to tests subdirectory in docdir
- cleaned spec file
* Thu May 31 2007 prusnak@suse.cz
- fixed problem with xpath's string-value for a PI node
  with no content (pinode.path) [#278173]
- cleaned spec file
* Tue Apr 24 2007 prusnak@suse.cz
- updated to 2.6.28:
  o bug fixes:
  * XPath memory leak, node comparison error
  * HTML parser autoclose stack usage
  * various regexp fixes
  * htmlCtxtReset fix
  * invalid char in text XInclude
  * fix the big string memory leak
  * fix whitespace usage
  * and many more ... see NEWS
- dropped obsoleted patches:
  * null-retval.patch (included in update)
  * tabs-spaces.patch (included in update)
* Mon Apr  2 2007 rguenther@suse.de
- add zlib-devel BuildRequires
* Thu Feb 22 2007 prusnak@suse.cz
- fixed inconsistent use of tabs and spaces in indentation
  (tabs-spaces.patch) by Andreas Hanke [#246203]
* Thu Jan 25 2007 prusnak@suse.cz
- fixed crash on ENOMEM (null-retval.patch) [#215223]
* Tue Jan  9 2007 sbrabec@suse.cz
- gnomeprefix changed to /usr.
- Removed obsolete PreReq.
* Mon Dec 11 2006 ke@suse.de
- 2.6.27; many improvements and bug fixes.  For details, see the NEWS
  file.
- Remove libxml2-xpath-1.318.patch (obsolete).
* Tue Nov 28 2006 ke@suse.de
- Do not install static Python module; reported by Andreas Hanke
  [#223696].
* Tue Oct 17 2006 ke@suse.de
- Move manpage to devel subpackage; reported by Andreas Hanke [#
  212441].
* Tue Aug 15 2006 ke@suse.de
- Remove left-over SuSEconfig traces in %%files list.
* Mon Aug 14 2006 ke@suse.de
- Remove SuSEconfig related files completely.  /etc/xml/catalog is now
  provided by the sgml-skel package.
* Wed Jun 28 2006 ke@suse.de
- Once the catalog is initialized, remove the SuSEconfig trigger
  file; reported by Stanislav Brabec [# 188885].
* Tue Jun 27 2006 ke@suse.de
- Apply libxml2-xpath-1.318.patch from CVS: Do not return too many
  nodes.
* Fri Jun 16 2006 ke@suse.de
- 2.6.26; NEWS extract from http://xmlsoft.org/ :
  * Bug fixes: encoding buffer problem, mix of code and data in xmlIO.c,
    entities in XSD validation, various XSD validation fixes, memory leak
    in pattern, attribute with colon in name, XPath leak inerror
    reporting, XInclude text include of selfdocument.
  * Xpath optimizations.
* Tue May 16 2006 ke@suse.de
- 2.6.24; NEWS extract from http://xmlsoft.org/ :
  * Improvements: XML catalog debugging; update to Unicode 4.01.
  * Bug fixes: xmlParseChunk() problem in 2.6.23,
    xmlParseInNodeContext() on HTML docs, comment streaming bug
    xmlParseComment, regexp bug fixes, xmlGetNodePath on text/CDATA, one
    Relax-NG interleave bug, XSD bugfixes, etc.
  * Documentation: man pages updates and cleanups
  * New features:
  - Relax NG structure error handlers.
  - xmlDOMWrapReconcileNamespaces xmlDOMWrapCloneNode.
- libxml2-python-whitespace.diff: Remove it, obsolete.
* Fri Feb 17 2006 kukuk@suse.de
- Don't install binaries in doc [#151897]
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 16 2006 ke@suse.de
- libxml2-python-whitespace.diff: Fix inconsistent use of tabs and
  spaces in indentation in libxml2.py.  Reported by Christoph Thiel;
  thanks to Jan Matejek [# 143082].
* Mon Jan  9 2006 ke@suse.de
- Update to version 2.6.23; NEWS extract from http://xmlsoft.org/ :
  * Bug fixes (leaks, XPath, validation issue, etc.).
  * Improvements (XSD Schemas redefinitions/restrictions, node copy
    checks and fix for attribute, handle gzipped HTTP resources, etc.).
  * Documentation.
* Wed Dec 21 2005 aj@suse.de
- Package /usr/include/libxml in -devel package.
* Fri Sep 16 2005 ke@suse.de
- Update to version 2.6.22; NEWS from http://xmlsoft.org/  (extract
  since .21):
  * Bug fixes (too many to list here).
  * Improvements on interfaces for schemas and RNG error reports.
  * Optimization of the char data inner loop parsing.
  * More lax mode for the HTML parser.
  * XML Schemas improvements preparing for derive (Kasimier Buchcik).
- libxml2-printf.patch: Adjust it.
- xml-error-handling.patch: Obsolete.
- Remove misleading link flag statement; thanks for advise to Dirk
  Mueller.
* Tue Aug  9 2005 ke@suse.de
- Add missing require statement; reported by Ludwig Nussel [# 95216].
* Thu Jul 28 2005 ke@suse.de
- Fix error handling.  Reported by Michael Radziej, apply fix from CVS
  as proposed by JP Rosevear [# 98487].
* Mon Jul 11 2005 ke@suse.de
- Update to version 2.6.20; NEWS from
  http://xmlsoft.org/:
  * Major improvement in XSD Schemas.
  * XSD Schemas streaming support (SAX and Reader), flagged as somewhat
    experimental.
  * New DOM importing functions
  * Various build and bug fixes, including memory leaks; for details
    check the NEWS file.
* Wed Apr  6 2005 meissner@suse.de
- make build again on gcc >= 4, added parallel make.
* Mon Apr  4 2005 ke@suse.de
- Update to version 2.6.19; NEWS (extract since .18) from
  http://xmlsoft.org/:
  * Bugfixes: xmlSchemaElementDump namespace, push and xmlreader
    stopping on non-fatal errors, thread support for dictionnaries
    reference counting, internal subset and push problem, URL saved in
    xmlCopyDoc, various schemas bug fixes, Python paths fixup,
    xmlGetNodePath and namespaces, xmlSetNsProp fix, warning should not
    count as error, xmlCreatePushParser empty chunk, XInclude parser
    flags, xmlTextWriterStartAttributeNS fix, xmlWriter bugs,
    xmlSearchNsByHref fix, Python binding leak, aliasing bug exposed by
    gcc4 on s390, xmlTextReaderNext bug, Schemas decimal type fixes,
    xmlByteConsumed static buffer, schemas type decimal fixups, xmmlint
    return code, workaround "DAV:" namespace brokeness in c14n segfault
    in Schemas, Schemas attribute validation, Prop related functions and
    xmlNewNodeEatName, HTML serialization of name attribute on a
    elements, Python error handlers leaks and improvement, Relax-NG
    validation bug, xmlSAXParseDoc and xmlParseDoc signatures, switched
    back to assuming UTF-8 in case no encoding is given at serialization
    time.
  * improvement: speedup parsing comments and DTDs, dictionnary support
    for hash tables, Schemas Identity constraints, streaming XPath
    subset, xmlTextReaderReadString added, Schemas canonical values
    handling, add xmlTextReaderByteConsumed, add a --nodict mode to
    xsltproc to check problems for documents without dictionnaries.
* Fri Apr  1 2005 meissner@suse.de
- disable visibility hacks for gcc >= 4
* Mon Jan 24 2005 meissner@suse.de
- specify printf format attributes to check for bad format string use.
* Mon Jan 17 2005 ke@suse.de
- Update to version 2.6.17; NEWS (extract) from http://xmlsoft.org/:
  * Bug fixes:
    xmlTextReaderHasAttributes, xmlCtxtReadFile() to use the catalog(s),
    loop on output, XPath memory leak, ID deallocation problem,
    xmlStopParser bug, UTF-16 with BOM on DTDs, namespace bug on empty
    elements in push mode, line and col computations fixups,
    xmlURIEscape fix, xmlXPathErr on bad range, patterns with too many
    steps, and more.
  * Improvements:
    XSD Schemas, python generator, xmlUTF8Strpos speedup, Python __str__
    call serialize(), and more.
  * New APIs:
    Add xmlDictExists(), GetLineNumber and GetColumnNumber for the
    xmlReader, Dynamic Shared Libraries APIs, error extraction API from
    regexps, and new XMLSave option for format.
  * Documentation improvements.
* Wed Nov 24 2004 mcihar@suse.cz
- use rpm macros to build correcly with current python
* Thu Nov 11 2004 ke@suse.de
- Update to version 2.6.16; NEWS (extract) from http://xmlsoft.org/:
  * Important bug fix release, it also fixes main bugs raised against
    2.6.15 and memory leaks found by automated testing of the API.
  * Documentation update.
  * Provide DTD validation APIs at the Python level.
* Thu Oct 28 2004 ke@suse.de
- Update to version 2.6.15; NEWS (extract) from http://xmlsoft.org/:
  * Security fixes on the nanoftp and nanohttp modules:
    http://www.securityfocus.com/archive/1/379383/2004-10-24/2004-10-30/0
  * Bug fixes: HTML parser on broken ASCII chars in names, Python paths,
    xmlHasNsProp and default namespace, DTD lookup fix, save back
    <group> in catalogs, tree build fixes, Schemas memory bug and
    another memory leak, xmlValidateDtd in the presence of an internal
    subset, entities and _private problem, xmlBuildRelativeURI error,
    and more.
  * Improvements: Better XInclude error reports, tree debugging module
    and tests, convenience functions at the Reader API, add support for
    PI in the HTML parser.
* Thu Oct  7 2004 ke@suse.de
- Update to version 2.6.14; NEWS since version 2.6.13:
  * Fix and cleanup XML schemas,
    UTF-8 issues, fix default namespace problem,
    encoding error could genrate a
    serialization loop, XInclude testing, Notation serialization, and
    other bugs.
  * Improveme schemas validity, added --path and --load-trace options to
    xmllint.
  * Enhance Python support.
  * Documentation: tutorial update.
- Drop obsolete NS patch.
* Tue Sep  7 2004 ke@suse.de
- libxml2-default-ns.patch: Fix problem with namespaces; provided by
  William M. Brack [# 44214].
* Mon Aug 23 2004 ke@suse.de
- Update to version 2.6.12; NEWS (extract) from http://xmlsoft.org/:
  * Better XSD Schemas support.
  * Python binding improvements
  * Enhancement of command line tools.
  * Documentation fixes.
  * Various bug fixes (RVT, XPath context resets bug, catalog white
    space handling, xmlReader state after attribute reading, out of
    Memory conditions handling, htmlNewDoc() charset, notation
    serialization, etc.).
* Wed Jul 21 2004 bg@suse.de
- disable elfgcchack for hppa to produce working binaries.
* Wed Jul 14 2004 ke@suse.de
- Update to version 2.6.11; NEWS (extract) from http://xmlsoft.org/:
  * Bugfixes and improvements to XML Schemas support.
  * Update to the documentation tutorial and man pages.
  * Bugfixes:
    C14N bug serializing namespaces, empty node set in XPath, XInclude
    xml:base generation, XInclude fallback problem, XPointer and
    xml:base problem, Reader and entities, xmllint related fixes, DTD
    serialization problem xmlReader fixes, Python bindings improvement,
    fix the push parser, URI escaping and filemanes, XHTML1 formatting,
    reverse xmlEncodeSpecialChars() behaviour back to escaping '"', etc.
  * improvements:
    custom per-thread I/O enhancement, dynamically increase the number
    of XPath extension functions in Python and fix a memory leak,
    make xmlTextReaderMode public,
  * Increase performance.
* Mon Apr 19 2004 ke@suse.de
- Update to version 2.6.9; NEWS (extract) from http://xmlsoft.org/:
  * implement xml:id Working Draft, relaxed XPath id() checking.
  * bugfixes: xmlCtxtReset, line number and CDATA, Regexp patches,
    xmlUriEscape, Relax-NG bugs, XInclude duplicate
    fallback, external DTD encoding detection, a DTD
    validation bug, xmlReader Close() fix, recusive extention
    schemas.
  * various improvements an performance patches.
  * documentation fixes.
- Remove obsolete patches (libxml2-parser.patch,
  libxml2-xpath-memleak.patch, libxml2-nanohttp-fd-close.patch).
* Wed Mar 24 2004 ke@suse.de
- libxml2-nanohttp-fd-close.patch: add a close for the local file
  descriptor by William Brack (from libxml2 CVS).
- libxml2-xpath-memleak.patch: fix a memory leak (xmlXPathLangFunction)
  by William Brack (from libxml2 CVS); reported by Mike Hommey.
* Thu Mar 18 2004 ke@suse.de
- Do not install pre-compiled examples; reported by Dirk Mueller [#
  36382].
* Thu Mar 11 2004 ke@suse.de
- Fix memory leak in parser.c.  Patch by Daniel Veillard (from libxml2
  CVS), reported by Holger Rauch.
* Tue Feb 24 2004 ke@suse.de
- Update to version 2.6.7; NEWS (extract) from http://xmlsoft.org/:
  Mostly small bugfixes and performances improvements:
  * Documentation: tutorial updates.
  * xmlWriter: updates and fixes.
  * XPath optimization.
  * DTD ID handling optimization.
  * Python: 2.3 compatibility, whitespace fixes.
  * Add relaxng option to xmllint --shell .
- Add -fno-strict-aliasing to CFLAGS.
* Mon Feb 23 2004 ke@suse.de
- Support C++ exceptions; reported by Ulrich Heinen [# 34865].
* Thu Feb 19 2004 ke@suse.de
- libxml2-id-idref-validation.patch: Remove a non-linear behaviour from
  ID/IDREF by Daniel Veillard (from libxml2 CVS).
* Fri Feb 13 2004 ke@suse.de
- Update to version 2.6.6; NEWS (extract) from http://xmlsoft.org/:
  Mostly a bug fixes including potentially dangerous buffer overflows
  discovered in the FTP and HTTP URL parsing code (historical it was
  written before the module uri.c, ideally that code should now be
  dropped); also a couple of minor API enhancements:
  * nanohttp and nanoftp: buffer overflow error on URI parsing.
  * bugfixes: make test and path issues, xmlWriter attribute
    serialization, xmlWriter indentation , schemas validation, XInclude
    dictionnaries issues, XInclude empty fallback, HTML warnings,
    XPointer in XInclude, Python namespace serialization, isolat1ToUTF8
    bound error, output of parameter entities in internal subset,
    internal subset bug in push mode, <xs:all> fix.
  * XInclude: allow the 2001 namespace without warning.
  * reader API: structured error reporting
  * Parsers: added xmlByteConsumed(ctxt) API to get the byte offest in
    input.
* Mon Jan 26 2004 ke@suse.de
- Update to version 2.6.5; NEWS (extract) from http://xmlsoft.org/:
  * Bugfixes: dictionnaries for schemas, regexp segfault, xs:all
    problem, a number of XPointer bugfixes, xmllint error go to stderr,
    DTD validation problem with namespace, memory leak, SAX1 cleanup and
    minimal options fixes, parser context reset on error, XPath union
    evaluation problem, xmlReallocLoc with NULL, XML Schemas double
    free, XInclude with no href, argument callbacks order for XPath
    callbacks.
  * Documentation enhancements.
  * Python bindings: fixes, enum support, structured error reporting,
    problem related to dictionnary references, recursion.
  * xmlWriter: indentation, memory leaks.
  * xmlSchemas: normalizedString datatype.
  * Parser optimizations, a few new XPath and dictionnary APIs for
    future XSLT optimizations.
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Fri Jan  9 2004 adrian@suse.de
- add %%run_ldconfig to %%postun
* Wed Jan  7 2004 ke@suse.de
- Update to version 2.6.4; NEWS (extract) from http://xmlsoft.org/:
  * Fix serious XInclude problems.
  * Documentation improvements.
  * example fix (Lucas Brasilino)
  * Various bugfixes: xmlTextReaderExpand() with xmlReaderWalker,
    XPath handling of NULL strings, API building reader or parser
    from filedescriptor should not close it, changed XPath
    sorting to be stable again, xmlGetNodePath() generating
    '(null)', DTD validation and namespace bug,
    XML Schemas double inclusion behaviour.
* Thu Dec 11 2003 ke@suse.de
- Update to version 2.6.3; NEWS (extract) from http://xmlsoft.org/:
  Cleanup release (documentation, small bug fixes and enhancements).
  Upgrade XInclude support to the latest draft; this includes namespace
  changes (in case of XInclude warnings, you must fix your documents).
  * Add a repository of examples.
  * Unicode range checking.
  * UTF-16 cleanup and BOM issues.
  * Bug fixes: ID and xmlReader validation, XPath, xmlWriter, hash.h
    inclusion problem, HTML parser, attribute defaulting and validation,
    some serialization cleanups, XML_GET_LINE macro, memory debug when
    using threads, serialization of attributes and entities content,
    xmlWriter.
  * XInclude bugfix, new APIs and update to the last version including
    the namespace change.
  * XML Schemas improvements.
  * Preliminary pattern support for streaming.
- Drop obsolete patch (libxml2-2.6.2-include.patch).
* Wed Nov 12 2003 ke@suse.de
- For libxml2-devel require zlib-devel and readline-devel; reported by
  Tobias Reif.
* Fri Nov  7 2003 ro@suse.de
- change include file hash.h
  define types used in parser.h before including
* Wed Nov  5 2003 ke@suse.de
- Update to version 2.6.2; NEWS (extract) from http://xmlsoft.org/:
  * API additions (should still be API and ABI compatible) and
  performance gains.
  * API to screate a W3C Schemas from an existing document.
  * Deactivate the broken docBook SGML parser code and plug the XML
    parser instead.
  * Enable IPv6 support.
  * Switch to a SAX2 like parser rewrote most of the XML parser core,
    provides namespace resolution and defaulted attributes, minimize memory
    allocations and copies, namespace checking and specific error handling,
    immutable buffers, make predefined entities static structures, etc...
  * Schemas: base64 support.
  * Parser<->HTTP integration fix, proper processing of the Mime-Type
    and charset informations if available.
  * Relax-NG: bug fixes.
  * Documentation fixes.
  * Bug fixes: xmlCleanupParser, threading uninitialized mutexes, HTML
    doctype lowercase, SAX/IO, compression detection and restore,
    attribute declaration in DTDs, namespace on attribute in HTML output,
    input filename, namespace DTD validation, xmlReplaceNode, I/O
    callbacks, CDATA serialization, xmlReader, high codepoint charref
    like &#x10FFFF;, buffer access in push mode, XPath bug,
    xmlCleanupParser, CDATA output, HTTP error handling.
    Mandatory encoding in text decl, serializing Document Fragment
    nodes,
    XPath context unregistration fixes, text node coalescing fixes,
    stdin parsing fix, a posteriori DTD validation fixes and other fixes.
  * xmllint options: --dtdvalidfpi, --sax1 for compat testing, --nodict
    for building without tree dictionnary, --nocdata to replace CDATA by
    text, --nsclean to remove surperfluous namespace declarations.
  * Always generate line numbers when using the new xmlReadxxx functions
  * Add XInclude support to the xmlReader interface.
  * Implement XML_PARSE_NONET parser option.
  * DocBook XSLT processing bug fixed.
  * HTML serialization for <p> elements.
  * XPointer failure in XInclude are now handled as resource errors.
  * Fix xmllint --html to use the HTML serializer on output (add --xmlout
    to implement the previous behaviour of saving it using the XML
    serializer).
* Tue Oct  7 2003 ke@suse.de
- Update to version 2.5.11:
  * Fix bug in Relax-NG.
  * Fix crash when using multithreaded programs.
* Fri Aug 29 2003 mcihar@suse.cz
- require same python version as it was built with
* Fri Aug 29 2003 kukuk@suse.de
- Add %%verify tag to /var/adm/SuSEconfig/run-libxml2
* Wed Aug 27 2003 ke@suse.de
- Add readline-devel to neededforbuild and enable history/readline
  support for xmllint; proposed by Thomas Schreitle.
* Fri Aug 15 2003 ke@suse.de
- Update to version 2.5.10; NEWS from http://xmlsoft.org/:
  * Bugfixes: UTF-16 support, HTML parser, xmlSAXParseDTD().
  * Improve XInclude performance problem
  * Improve XML parser performance.
* Thu Aug 14 2003 ke@suse.de
- Update to version 2.5.9; NEWS from http://xmlsoft.org/:
  * Bugfixes: IPv6 portability, xmlHasNsProp, Schemas, threading,
    hexBinary type, UTF-16 BOM, xmlReader, namespace handling, EXSLT, HTML
    parsing problem, DTD validation for mixed content + namespaces,
    HTML serialization, library initialization, progressive HTML parser.
  * Better interfaces for Relax-NG error handling.
  * Add xmlXIncludeProcessTree() for XInclud'ing in a subtree.
  * Doc fixes and improvements.
  * New UTF-8 helper functions.
  * General encoding cleanup + ISO-8859-x without iconv.
  * xmlTextReader cleanup + enum for node types.
* Tue Jul  8 2003 ke@suse.de
- Update to version 2.5.8; NEWS from http://xmlsoft.org/:
  * Bugfixes: XPath, XInclude, file/URI mapping, UTF-16 save, UTF-8
    checking, URI saving, error printing, PI related memleak,
    compilation without schemas or without xpath, xmlUnlinkNode problem
    with DTDs, xmlIOParseDTD, and xmlSAXParseDTD.
  * Fix multithreading lock problems.
  * IPv6 patch for FTP and HTTP accesses.
  * A few W3C Schemas Structure improvements.
  * W3C Schemas Datatype improvements.
  * Python bindings for thread globals, and method/class generator.
  * Add --nonet option to xmllint.
  * Documentation improvements.
- libxml2-2.5.8-mutex.patch provided by Daniel Veillard.
* Thu Jun 12 2003 kukuk@suse.de
- Add gnome directories to filelist
* Mon May 26 2003 ke@suse.de
- Remove unwanted files from $RPM_BUILD_ROOT.
* Mon Apr 28 2003 ke@suse.de
- Update to version 2.5.7; NEWS from http://xmlsoft.org/:
  * Relax-NG: Compiling to regexp and streaming validation on top of
    the xmlReader interface, add --stream to xmllint.
  * xmlReader: Expand(), Next() and DOM access glue, bug fixes.
  * Support for large files: RGN validated a 4.5GB instance.
  * Thread support is now configured in by default.
  * Fixes: update of the Trio code, WXS Date and Duration fixes, DTD
    and namespaces,
    HTML push parser and zero bytes handling, behaviour of the parser
    and validator in the presence of "out of memory" error conditions.
  * Extend the API to be able to plug a garbage collecting memory
    allocator, add xmlMallocAtomic() and modified the allocations
    accordingly.
  * Performances: remove excessive malloc() calls, speedup of the
    push and xmlReader interfaces, remove excessive thread locking.
  * Documentation: man page, xmlReader documentation
  * Python: add binding for xmlCatalogAddLocal.
* Wed Apr  2 2003 ke@suse.de
- Update to version 2.5.6; NEWS from http://xmlsoft.org/:
  * Fix W3C XML Schemas datatype, should be compliant now except
    for binHex and base64 which are not supported yet.
  * Bug fix: non-ASCII IDs, HTML output, XInclude on large docs and
    XInclude entities handling, encoding detection on external subsets,
    XML Schemas bugs and memory leaks, HTML parser.
  * improved error reporting: xml:space, start/end tag mismatches, Relax
    NG errors.
- Frop obsolete trio patch.
* Wed Mar 26 2003 ke@suse.de
- Update to version 2.5.5; NEWS from http://xmlsoft.org/:
  * Fixes on the Relax NG implementation.
  * Increase support for W3C XML Schemas datatype.
  * Bug fixes in the URI handling layer.
  * Bug fixes: HTML parser, xmlReader, DTD validation, XPath, encoding
  conversion, line counting in the parser.
  * Add support for $XMLLINT_INDENT environment variable, FTP delete.
- Apply patch by Albert Chin to enable use of trio libraries in Python.
* Thu Feb 20 2003 ke@suse.de
- Add /usr/bin/install to PreReq; reported by Thorsten Kukuk
  [# 23891].
* Tue Feb 11 2003 ke@suse.de
- Update to version 2.5.3; NEWS from http://xmlsoft.org/:
  A bugfix release.  Relax-NG and XML Schemas datatypes stabilization:
  * RelaxNG and XML Schemas datatypes improvements; first version of
    RelaxNG Python bindings.
  * Fixes: XLink, XInclude, API fix for serializing namespace nodes,
    encoding conversion bug, XHTML1 serialization.
* Thu Feb  6 2003 ro@suse.de
- fix specfile
* Thu Feb  6 2003 ke@suse.de
- Update to version 2.5.2; NEWS from http://xmlsoft.org/:
  First release with the RelaxNG validation code.  Schemas support is
  also configured in by default now. All this code is still of alpha
  quality.
  This release also includes a number of fixes and some API improvements:
  * First implementation of RelaxNG, added --relaxng flag to xmllint.
  * Schemas support now compiled in by default.
  * Bug fixes: DTD validation, namespace checking, XInclude and entities,
    delegateURI in XML Catalogs, HTML parser, XML reader, XPath parser
    and evaluation, UTF8ToUTF8 serialization, XML reader memory
    consumption, HTML parser, HTML serialization in the presence of
    namespaces.
  * Add an HTML API to check elements and attributes.
  * Documentation improvement.
  * Add python bindings for XPointer, contextual error reporting.
  * Fix URI/file escaping problems.
- Remove obsolete README.SuSE.
* Thu Jan  9 2003 ke@suse.de
- Update to version 2.5.1; NEWS from http://xmlsoft.org/:
  * New XmltextReader interface based on C# API;
    cf. http://xmlsoft.org/xmlreader.html .
  * XInclude fallback fix.
  * Python: bindings for the new API, packaging, drv_libxml2.py Python
    xml.sax driver, fixes, speedup and iterators for Python-2.2.
  * Tutorial fixes, xmllint man update.
  * Fix an XML parser bug.
  * Entities handling fixes
  * new API to optionally track node creation and deletion.
  * Added documentation for the XmltextReader interface and some XML guidelines
* Thu Dec 12 2002 ke@suse.de
- Update to version 2.4.30; NEWS from http://xmlsoft.org/:
  * Main changes are the addition of a new API set closely based on
    the C#/ECMA-334 XmlTextReader interface, allowing to scan an XML
    document in a forward only way but in (near) constant memory size.
  * Fix for prev in python bindings.
  * Fix for entities handling (Marcus Clarke), replacing patch from
    2002-12-02.
  * Refactor the XML and HTML dumps to a single code path, fix XHTML1
    dump.
  * Fix for URI parsing when handling URNs with fragment identifiers
  * Fix for HTTP URL escaping problem.
  * Adde an TextXmlReader (C#) like API (work in progress).
  * Rewrote the API in XML generation script, includes a C parser and saves
    more informations needed for C# bindings.
* Mon Dec  2 2002 ke@suse.de
- Fix "Entity in Entity processing"; patch provided by DV.
  Cf. [# 22208].
* Tue Nov 26 2002 ro@suse.de
- split libxml2-python to own specfile
  (libxml2 is turning more and more into a base package
  and python requires a lot of other things to build)
* Mon Nov 25 2002 ke@suse.de
- Update to version 2.4.28; NEWS from http://xmlsoft.org/:
  * Fix a couple of python binding bugs.
  * Fix 2 bugs in the XML push parser.
  * Remove potential memory leak.
  * Add encoding support for XInclude parse="text".
  * Autodetect XHTML1 and add specific serialization rules.
  * Fix threading bug.
* Mon Nov 18 2002 ke@suse.de
- Update to version 2.4.27; NEWS from http://xmlsoft.org/:
  * Fix Python bindings.
  * A number of bug fixes: SGML catalogs, xmlParseBalancedChunkMemory(),
    HTML parser, Schemas, document fragment support, xmlReconciliateNs,
    XPointer, xmlFreeNode(), xmlSAXParseMemory, xmlGetNodePath,
    entities processing.
  * Add grep to xmllint --shell.
  * Improvement documentation.
- Don't apply obsolete revert-.25-.26.dif patch.
* Mon Nov  4 2002 adrian@suse.de
- revert catalog separator change, accepting ":" again.
  libxml2 is using anyway ":" internal, even when a " " separator
  is given
* Wed Oct 30 2002 ro@suse.de
- removed patch call for removed patch
* Wed Oct 30 2002 ke@suse.de
- Drop libxml2-2.4.19-xml2-config.dif to avoid header file conflicts
  with C++; reported by Andreas Mueller [# 21427].
* Tue Oct 29 2002 ke@suse.de
- Update to version 2.4.26; NEWS from http://xmlsoft.org/:
  * Fix the validation code (DTD and Schemas), xmlNodeGetPath() ,
  HTML serialization, Namespace compliance, and a number of small
  problems.
- "valid" patches are obsolete with his update.
* Fri Oct 11 2002 ke@suse.de
- valid.c: Fix uninitialized memory block (patch by Daniel Veillard).
* Tue Oct  8 2002 ke@suse.de
- Update to version 2.4.25; NEWS from http://xmlsoft.org/:
  * A number of bug fixes: XPath, validation, DOM and tree, XML I/O,
    HTML.
  * Fix and improve Python bindings.
  * Fix HTML <style> and boolean attributes serializer.
  * Improve C14N.
  * Cleanup docs.
  * Serious rewrite of XInclude.
  * Make XML Schemas regexp part of the default build and APIs, small
    fixes and improvement of the regexp core
  * Change the validation code to reuse XML Schemas regexp APIs
  * Tutorial improvements.
  * Remove of all stderr/perror use for error reporting
  * Better error reporting: XPath and DTD validation
  * Update of the trio portability layer (Bjorn Reese)
- spec file: don't delete package files in %%post; change test in
  SuSEconfig.libxml2 accordingly [# 20028].
* Fri Aug 23 2002 ke@suse.de
- Move SuSEconfig.libxml2 from the devel subpackage to the main package
  and check for "/etc" instead of "etc".
  Partly fix for [# 17646].
* Tue Aug  6 2002 ke@suse.de
- Add a PreRequires for zlib [Bug# 17436].
* Sat Jul 27 2002 adrian@suse.de
- add %%run_ldconfig
* Mon Jul  8 2002 ke@suse.de
- Update to version 2.4.23; NEWS from http://xmlsoft.org/, not mentioned
  earlier:
  - Bug fixes: base handling, parser, memory usage, HTML parser, XPath,
    documentation (Christian Cornelssen), indentation, URI parsing.
  - Optimizations for XMLSec; fix and make public some of the network
    protocol handlers.
  - Date and time support for XML Schemas datatypes.
* Tue May 28 2002 ro@suse.de
- tweak python installation for lib64 some more
* Tue May 28 2002 ke@suse.de
- Fix python installation procedure (thanks to Ruediger Oertel and
  Stefan Fent).
* Tue May 28 2002 ke@suse.de
- Update to version 2.4.22:
  - Bug fixes.
  - Increase performance.
* Tue May  7 2002 ke@suse.de
- Create /etc/xml/catalog via SuSEconfig (don't rely on %%post).
  Rported by Petr Ostadal [# 16115].
- Don't claim to own /etc/xml/catalog; thus don't delete it via
  %%postun).
* Thu May  2 2002 ke@suse.de
- Build and install python module as an own subpackage.
- Create initial XML catalog (/etc/xml/catalog).
* Tue Apr 30 2002 ke@suse.de
- Update to version 2.4.21; NEWS from http://xmlsoft.org/:
  This release is both a bug fix release and also contains the early
  XML Schemas structures and datatypes code, beware, all interfaces are
  likely to change, there is huge holes, it is clearly a work in
  progress and don't even think of putting this code in a production
  system, it's actually not compiled in by default.
  The real fixes are:
  o A couple of bugs or limitations introduced in 2.4.20.
  o Fixes on XPath strings and conformance patches.
  o Patch for the ExcC14N specification.
* Fri Apr 19 2002 ke@suse.de
- Update to version 2.4.20; NEWS from http://xmlsoft.org/:
  o Bug fixes: File descriptor leak, XPath, HTML ouput, DTD
    validation.
  o XPath conformance testing by Richard Jinks.
  o Improve Python bindings.
* Tue Apr  9 2002 ro@suse.de
- also provide /usr/include/libxml2/libxml in "xml2-config --cflags"
* Tue Apr  9 2002 ke@suse.de
- Update to version 2.4.19; NEWS since 2.4.13 from http://xmlsoft.org/:
  * Change of Licence to the MIT Licence basisally for integration in
    XFree86 codebase, and removing confusion around the previous
    dual-licencing.
  * Bug fixes: XPath bugs, validation, ISO-Latin to UTF8 encoder,
    tree, SAX, canonicalization, bug "namespace nodes have no parents
    in XPath".
  * Bug fixes: bugs triggered by the XML Testsuite from OASIS and
    W3C. Compliance has been significantly improved.
  * Memory allocation checks using valgrind, and profiling tests
  * Speedup patch to XPath very effective for DocBook stylesheets
  * Add XML Canonalization support.
  * Add xmlSetEntityReferenceFunc() for Keith Isdale work on xsldbg.
  * Add Python bindings.
  * Cleanup of the headers, generation of a reference API definition in XML
  * Cleanup of timing code.
  * Update documentation.
* Mon Feb 11 2002 coolo@suse.de
- use %%_lib and %%_libdir
* Mon Jan 14 2002 hhetter@suse.de
- updated to version 2.4.12
  * a few bug fixes: thread,  xmllint , XML parser
  XPointer , I/O cleanups
  * portability improvements
  * some makefiles cleanups
* Tue Nov 27 2001 ke@suse.de
- Update to version 2.4.11; NEWS from http://xmlsoft.org/ (include some
  items not mentioned earlier):
  - Fix errors and bug (mostly include files related).
  - Fix URI escaping, namespace handling problems when using DTD and
    validation, paths or XPointers generation.
  - Improve xmllint.
  - Fix HTML parser.
* Sun Nov 11 2001 adrian@suse.de
- Update to version 2.4.10:
  - Bugfix / Cleanup release.
* Wed Nov  7 2001 ke@suse.de
- Update to version 2.4.9:
  - Fix XML and SGML catalog handling.
- Drop libxml2-makefile-am.diff; is obsolete.
* Mon Nov  5 2001 ke@suse.de
- Update to version 2.4.8; NEWS from http://xmlsoft.org/:
  - Fix SGML catalog support.
  - Update xmlcatalog tool.
- Apply libxml2-makefile-am.diff on account of automake 1.5 (multiply
  set variables).
* Wed Oct 31 2001 ke@suse.de
- Update to version 2.4.7; NEWS from http://xmlsoft.org/:
  - Serious rewrite of the catalog code.
  - Integrate thread safety patch.
  - Bug fixes: HTML parser, potentially serious validation issues and
    general bug fixes.
  - Integrate the SGML DocBook support in xmllint; update manpage.
  - Change nanoftp anonymous login passwd.
  - Some I/O cleanup and a couple of interfaces for Perl wrapper.
* Thu Oct 11 2001 ke@suse.de
- Compatibility link for SuSE Linux 7.3 and earlier:
  /usr/include/libxml -> libxml2/libxml
  (will go away on version 8.0); cf. [#11709].
- Add README.SuSE.
* Thu Oct 11 2001 ke@suse.de
- Update to version 2.4.6; NEWS from http://xmlsoft.org/:
  - Add and update man pages.
  - Portability and configure fixes.
  - Fix an infinite loop on the HTML parser.
  - Fix half a dozen bugs reported for libxml or libxslt.
  - Update xmlcatalog to be able to modify SGML super catalogs.
- Note, starting with 2.4.5 includes were moved to
  /usr/lib/libxml2/libxml; use 'xml2-config' to locate these files
  (cf. http://mail.gnome.org/archives/xml/2001-October/msg00069.html)
  [#11709].
* Mon Oct  1 2001 ke@suse.de
- Update to version 2.4.5; NEWS from http://xmlsoft.org/ :
  - Bugfixes and some portability changes.
  - Force the HTML serializer to output decimal charrefs since some
    version of Netscape can't handle hexadecimal ones.
  - Add --convert to xmlcatalog, bug fixes and cleanups of XML Catalog.
  - Some documentation cleanups.
- Drop obsolete configure patch.
* Fri Aug 24 2001 ke@suse.de
- Update to version 2.4.3; from the announcement (cf. libxslt):
  - Implement XML Catalog Specification from August 6:
    http://www.oasis-open.org/committees/entity/spec-2001-08-06.html
    http://xmlsoft.org/catalog.html
  - New NaN and Infinity code.
  - A number of small bugfixes.
* Fri Aug 17 2001 ro@suse.de
- re-enabled suse_update_config and added autoconf/automake
  sequence.
* Fri Aug 17 2001 ke@suse.de
- Update to version 2.4.2.
- Drop suse_update_config (seems to confuse auto* at the moment).
* Fri Aug 10 2001 kukuk@suse.de
- Revert change to ldconfig call
* Thu Jul 26 2001 ke@suse.de
- Update to version 2.4.1
- Call 'ldconfig' only for UID = 0.
* Wed Jul 11 2001 ke@suse.de
- Update to version 2.4.0.
- Call 'ldconfig' during build (as required by SuSE Package
  Conventions).
* Wed Jul  4 2001 adrian@suse.de
- xml2-config --cflags will not output -I/usr/include anymore
  this causes compilation failures with gcc3 due to the wrong
  include path order
* Fri Jun 29 2001 ke@suse.de
- Update to version 2.3.13.
- Apply libxml2-no-example.diff not to try to compile the "example".
* Mon May 21 2001 ke@suse.de
- Update to version 2.3.9
* Sat Apr 14 2001 adrian@suse.de
- update to 2.3.6
* Thu Feb 22 2001 ro@suse.de
- added readline/readline-devel to neededforbuild (split from bash)
* Thu Feb 15 2001 ke@suse.de
- Initial package: version 2.3.0 [#2861].