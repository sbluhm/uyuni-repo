#
# spec file for package docbook-xsl
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define realversion            %{version}
#
%define db4rootdir             %{_datadir}/xml/docbook/stylesheet/nwalsh
%define db4package             docbook-xsl-stylesheets
%define db4style_catalog       %{db4package}.xml
#
%define db5rootdir             %{_datadir}/xml/docbook/stylesheet/nwalsh5
%define db5package             docbook5-xsl-stylesheets
%define db5style_catalog       %{db5package}.xml
#
%define etcxmlcatalogd         %{_sysconfdir}/xml/catalog.d
#
Name:           docbook-xsl
Version:        1.79.2
Release:        lp152.3.2
Summary:        XSL Stylesheets for DocBook
License:        MPL-1.1 AND MIT
Group:          Productivity/Publishing/DocBook
URL:            https://github.com/docbook/xslt10-stylesheets
Source0:        https://github.com/docbook/xslt10-stylesheets/releases/download/release%%2F%{version}/docbook-xsl-%{version}.tar.bz2
Source1:        https://github.com/docbook/xslt10-stylesheets/releases/download/release%%2F%{version}/docbook-xsl-doc-%{version}.tar.bz2
Source2:        %{db4style_catalog}
Source3:        %{db5style_catalog}
# Build scripts
Source10:       dbxslt-install.sh
Source11:       xslnons-build
## PATCH-FIX-OPENSUSE docbook-xsl-stylesheets-dbtoepub.patch Fixed dirname
Patch0:         %{name}-dbtoepub.patch
## PATCH-FIX-OPENSUSE docbook-xsl-stylesheets-non-recursive_string_subst.patch Use EXSLT replace function to avoid recursive implementation of string.subst
Patch1:         %{name}-non-recursive_string_subst.patch
BuildRequires:  fdupes
BuildRequires:  sgml-skel >= 0.7
BuildRequires:  unzip
BuildRequires:  perl
Requires:       docbook_4
Requires:       sgml-skel >= 0.7
Requires:       xmlcharent
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
Requires(pre):  %{_bindir}/xmlcatalog
BuildArch:      noarch
#--------------------------------------------------------------------------

%description
%{summary}.

Wrapper package for DocBook 4 and 5 stylesheets.

%package        -n %{db4package}
Summary:        XSL Stylesheets for DocBook 4
Group:          Productivity/Publishing/XML
Requires:       docbook_4
Requires:       sgml-skel >= 0.7
Requires:       xmlcharent
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
Suggests:       rubygem(dbtoepub)

%description   -n %{db4package}
These are the XSL stylesheets for DocBook XML and "Simplified" DocBook
DTDs. Use these stylesheets for documents based on DocBook 4 and
earlier; they are not aware of the namespace feature.

The stylesheets transform DocBook 4 documents into HTML, XHTML, Manpages,
XSL-FO (for PDF), and a few other formats.

XSL is a standard W3C stylesheet language for both print and online
rendering. For more information about XSL, see the XSL page at the W3C:
http://www.w3.org/Style/XSL/

%package        -n docbook5-xsl-stylesheets
Summary:        XSL Stylesheets for DocBook 5
Group:          Productivity/Publishing/XML
Requires:       docbook_5
Requires:       sgml-skel >= 0.7
Requires:       xmlcharent
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
Suggests:       rubygem(dbtoepub)

%description   -n docbook5-xsl-stylesheets
These are the XSL stylesheets for DocBook 5 XML and "Simplified" DocBook 5.
Use these stylesheets for documents based on DocBook 5; they are aware
of the namespace feature.

The stylesheets transform DocBook 5 documents into HTML, XHTML, Manpages,
XSL-FO (for PDF), and a few other formats.

XSL is a standard W3C stylesheet language for both print and online
rendering. For more information about XSL, see the XSL page at the W3C:
http://www.w3.org/Style/XSL/

%package        pdf2index
# License:       MPL-1.1 and MIT
Summary:        Script to create Indices for FOP
Group:          Productivity/Publishing/XML
Requires:       ImageMagick
Requires:       perl


%description   pdf2index

Contains the script pdf2index which creates indices for FOP.


%prep
# %%setup -q -n docbook-xsl-%%{realversion} -b1
%setup -q -c -T -n docbook-xsl

# Prepare directories:
mkdir docbook-xsl-%{realversion}-ns docbook-xsl-%{realversion}-nons

# Copy all source files and make scripts executable:
cp %{SOURCE2} %{SOURCE3} %{SOURCE10} %{SOURCE11} .
chmod +x $(basename %{SOURCE10}) $(basename %{SOURCE11})

# Replace version in XML catalog files
db4=$(basename %{SOURCE2})
db5=$(basename %{SOURCE3})
sed --in-place 's/@VERSION@/%{realversion}/' $db4
sed --in-place 's/@VERSION@/%{realversion}/' $db5

# Unpack stylesheet and doc sources into the correct directory:
tar xf %{SOURCE0} -C docbook-xsl-%{realversion}-ns --strip-components 1
tar xf %{SOURCE1} -C docbook-xsl-%{realversion}-ns --strip-components 1

# Patch the orginal source and remove unnecessary files:
(cd docbook-xsl-%{realversion}-ns
%patch0 -p1
%patch1 -p1

# Remove some Python and Java extensions
# Remove dbtoepub Ruby script. This has been moved to devel:languages:ruby:extensions
# see rubygem-dbtoepub
rm -rf extensions/*.py extensions/saxon65.jar extensions/xalan27.jar \
       extensions/build.xml epub/bin
)


%build
pushd docbook-xsl-%{realversion}-ns

find slides -regex ".*\.\(xml\|htc\|\|hu\|js\|svg\|css\|html\.*\|txt\|rnc\|xhtml\)" \
   -exec sed -i 's/\r//' {} \;

# Fix wrong end-of-line encoding:
sed -i 's/\r//' params/*
# Correct file and directory properties:
find -type f -exec chmod 644 {} \;
find -type d -exec chmod 755 {} \;

# Remove any .htaccess files:
find -type f -name "\.htaccess" -exec rm {} \;

popd

# Create the non-NS variant from the NS original source:
./xslnons-build docbook-xsl-%{realversion}-ns docbook-xsl-%{realversion}-nons


%install
mkdir -p %{buildroot}%{_sysconfdir}/xml/catalog.d \
         %{buildroot}%rb_libdir/

./dbxslt-install.sh --debug --buildroot=%{buildroot} \
            --package-version=%{realversion} \
            --package-name=%{db4package} \
            --sourcedir=docbook-xsl-%{realversion}-nons

./dbxslt-install.sh --debug --buildroot=%{buildroot} \
            --package-version=%{realversion} \
            --package-name=%{db5package} \
            --db-xsl-suffix=nwalsh5 \
            --sourcedir=docbook-xsl-%{realversion}-ns

# The directory is already available at this point:
install -m644 %{db4style_catalog} %{db5style_catalog} %{buildroot}%{etcxmlcatalogd}

%fdupes -s %{buildroot}


%post   -n %{db4package}
update-xml-catalog

%postun -n %{db4package}
update-xml-catalog

%post   -n %{db5package}
update-xml-catalog

%postun -n %{db5package}
update-xml-catalog

%files -n %{db4package}
%config %{_sysconfdir}/xml/catalog.d/%{db4style_catalog}
%doc docbook-xsl-%{realversion}-nons/BUGS docbook-xsl-%{realversion}-nons/NEWS
%doc docbook-xsl-%{realversion}-nons/README docbook-xsl-%{realversion}-nons/RELEASE-NOTES.*
%doc docbook-xsl-%{realversion}-nons/TODO
%dir %{_datadir}/xml/docbook/stylesheet
%dir %{db4rootdir}
%dir %{db4rootdir}/%{realversion}
%exclude %{db4rootdir}/%{realversion}/fo/pdf2index

%{db4rootdir}/current
%{db4rootdir}/%{realversion}/*

%files -n %{db5package}
%config %{_sysconfdir}/xml/catalog.d/%{db5style_catalog}
%doc docbook-xsl-%{realversion}-ns/BUGS docbook-xsl-%{realversion}-ns/NEWS
%doc docbook-xsl-%{realversion}-ns/README docbook-xsl-%{realversion}-ns/RELEASE-NOTES.*
%doc docbook-xsl-%{realversion}-ns/TODO
%dir %{_datadir}/xml/docbook/stylesheet
%dir %{db5rootdir}
%dir %{db5rootdir}/%{realversion}
%exclude %{db5rootdir}/%{realversion}/fo/pdf2index

%{db5rootdir}/current
%{db5rootdir}/%{realversion}/*

%files pdf2index
%attr(0755,root,root) %{_bindir}/pdf2index

%changelog
* Wed Nov 22 2017 thomas.schraitle@suse.com
- Abandom the docbook-xsl-stylesheets-script package.
  The dbtoepub script is available from the rubygem-dbtoepub
  package.
  The script pdf2index is available in docbook-xsl-pdf2index
* Sun Nov 19 2017 thomas.schraitle@suse.com
- First attempt to build the two DocBook stylesheet packages
  from a single source:
  - Added xslnons-build script from upstream.
  - Improved dbxslt-install.sh script a lot
* Tue Nov 14 2017 thomas.schraitle@suse.com
- Fix bsc#1063066:
  From 1.79.1 and later, upstream decided to release namespace
  aware stylesheets only. The non-NS stylesheets have to be built
  with the "xslnons-build" script (taken from upstream).
  This is integrated now.
  The switch from NS-aware to non-NS stylesheets help to fix this
  problem.
* Fri Oct 27 2017 mpluskal@suse.com
- Restore working patch (bsc#1063066):
  * Rebase docbook-xsl-stylesheets-non-recursive_string_subst.patch
* Sun Oct  1 2017 aavindraa@gmail.com
- Update to version 1.79.2
- Rebase docbook-xsl-stylesheets-non-recursive_string_subst.patch
- callout-gen is removed
* Sat Aug 26 2017 thomas.schraitle@suse.com
- Add docbook-xsl-stylesheets-non-recursive_string_subst.patch
  Use str:replace from exslt.org to implement string.subst
  string.subst implementation causes recursion issues when building
  systemd documentation. This issue has been reported in
  https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=765567 and
  https://bugs.archlinux.org/task/54694 .
  Taken from https://github.com/fishilico/xslt10-stylesheets/commit/a7df4fbbef3ab0f97d50aa47f2ccfa0630a2686e
* Tue Feb  7 2017 dimstar@opensuse.org
- Explicitly package %%{_docdir}/%%{name} to fix build with RPM 4.13.
* Tue Jul 19 2016 fvogt@suse.com
- Use update-xml-catalog
* Mon Dec 21 2015 mpluskal@suse.com
- Update download urls
* Sat Dec 12 2015 p.drouand@gmail.com
- Update to version 1.79.0, see
  http://snapshots.docbook.org/xsl/RELEASE-NOTES.html#V1.79.0
  for details (Mostly bugfix release)
- Remove obsolete patches
  * docbook-xsl-stylesheets-epub3-base.dir.patch
  * docbook-xsl-stylesheets-manpages-other-r9847.patch
- Perform a spec-cleaner on the spec file
* Wed Apr 29 2015 toms@opensuse.org
- Fixed bsc#928753 (added missing template directory)
- Slightly corrected file list
* Thu Feb 19 2015 toms@opensuse.org
- Slightly adapted %%post and %%postun section to fix bsc#918565
* Mon Jan 12 2015 fsundermeyer@opensuse.org
- Added missing images directory to install-script dbxslt-install.sh
* Thu Feb  6 2014 toms@opensuse.org
- Fixed bnc#842844 and added upstream patch from r9847 of docbook#1313
  (File docbook-xsl-stylesheets-manpages-other-r9847.patch)
* Thu Feb  6 2014 ke@suse.com
- .spec: syntax fix.
* Mon Dec  9 2013 toms@opensuse.org
- Added missing patch description to follow Patch Guidlines
  (see http://en.opensuse.org/openSUSE:Packaging_Patches_guidelines)
- Added upstream patch (r9732-r9743 for base.dir parameter in EPUB3)
* Mon Sep 23 2013 toms@opensuse.org
- Moved installation procedure into dbxslt-install.sh Shell script
* Fri Jun 28 2013 toms@opensuse.org
- Corrected conflict with docbook5-xsl-stylesheets:
  Created subpackage with pdf2index (which raised this conflict)
  and moved other scripts too (db2epub, callout-gen).
  This makes it easier to install both variantes of the
  stylesheets
* Fri May 31 2013 varkoly@suse.com
- Fix spec to avoid conflict with docbook5-xsl-stylesheets
* Mon Mar 18 2013 toms@opensuse.org
- Update to 1.78.1, see http://snapshots.docbook.org/xsl/RELEASE-NOTES.html#V1.78.1
  for details
- Added %%exclude in SPEC file for .htaccess files
* Thu Jan 17 2013 p.drouand@gmail.com
- Updated to 1.78.0, see http://snapshots.docbook.org/xsl/RELEASE-NOTES.html#V1.78.0
  for details (Mostly bugfix release)
* Mon Jun 11 2012 toms@opensuse.org
- Fixed SPEC file:
  * added missing db2epub in /epub/bin/
  * create symbolic links (-s) with fdupes
* Tue Jun  5 2012 toms@opensuse.org
- Updated to 1.77.1, see http://snapshots.docbook.org/xsl/RELEASE-NOTES.html#V1.77.1
  for details (Mostly bugfix release)
- Fixed spec file to copy VERSION.xsl instead of VERSION
* Fri May 25 2012 toms@opensuse.org
- Updated to 1.77.0, see http://snapshots.docbook.org/xsl/RELEASE-NOTES.html#V1.77.0
  for details
  (Merged from Factory)
* Thu Jan 12 2012 coolo@suse.com
- change license to be in spdx.org format
* Wed Sep 21 2011 coolo@suse.com
- remove ruby requires, there is nothing in here using ruby and
  ruby needs this package indirectly - creating a build cycle
* Sun Sep 18 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
  (cf. packaging guidelines)
* Tue Apr 12 2011 toms@suse.de
- Update to 1.76.1; for news, see
  http://lists.oasis-open.org/archives/docbook-apps/201011/msg00007.html
- Moved pdf2index and dbtoepub to /usr/bin
- Cleaned up Spec file to avoid rpmlint warnings
- Removed now obsolete chunktoc-fix.patch
* Wed Apr 14 2010 mmarek@suse.cz
- chunktoc.xsl: Added missing namespace declarations. Closes
  bug #2890069.
* Wed Dec 23 2009 aj@suse.de
- Fix last patch to remove another release number.
* Mon Aug 17 2009 aj@suse.de
- Only remove file from catalog if it disappeared.
- Do not use release numbers, they're not needed anymore.
* Tue Jul 28 2009 ke@suse.de
- Update to 1.75.2; for news, see
  http://lists.oasis-open.org/archives/docbook-apps/200907/msg00046.html
* Tue Jun 16 2009 ke@suse.de
- Update to 1.75.1; for news, see
  http://lists.oasis-open.org/archives/docbook-apps/200905/msg00165.html
  http://lists.oasis-open.org/archives/docbook-apps/200905/msg00018.html
* Fri May  8 2009 ke@suse.de
- Update to version 1.75.0; for news, see
  http://sourceforge.net/forum/forum.php?forum_id=951185.
* Wed Mar 11 2009 ke@suse.de
- Update to version 1.74.3; for news, see
  http://sourceforge.net/forum/forum.php?forum_id=920190.
* Wed Jul 23 2008 ke@suse.de
- 1.74.0: Important bug fixes and the following significant feature
  changes.  For more information, see
  http://sourceforge.net/forum/forum.php?forum_id=831189; excerpt:
  * .epub target.  Read more about this target in epub/README.
  * XHTML 1.1 target.
  * A number of locales have been updated.
  * Table, figure, template syncronization, and character style
  improvements  have been made for WordML & Pages. Support added for
  OpenOffice.org.
* Mon Jan 14 2008 ke@suse.de
- 1.73.2: minor bug-fix release:
  * Fix footnote handling in FO output.
- Remove obsolete Provides/Obsoletes (docbkxsl).
* Mon Aug 20 2007 toms@suse.de
- Update to version 1.73.1, bugfix release:
  Gentext:
  * Mauritz Jeanson: locale/de.xml
    Applied patch #1766009.
  * Michael(tm) Smith: locale/lv.xml
    Added localization for ProductionSet.
  FO:
  * Mauritz Jeanson: table.xsl
    Modified the tgroup template so that, for tables with multiple tgroups,
    a width attribute is output on all corresponding fo:tables. Previously,
    there was a test prohibiting this (and a comment saying that outputting more
    than one width attribute will cause an error). But this seems to be no longer
    relevant; it is not a problem with FOP 0.93 or XEP 4.10. Closes bug #1760559.
  * Mauritz Jeanson: graphics.xsl
    Replaced useless <a> elements with warning messages (textinsert extension).
  * Mauritz Jeanson: admon.xsl
    Enabled generation of ids (on fo:wrapper) for indexterms in admonition titles,
    so that page references in the index can be created. Closes bug #1775086.
  HTML:
  * Mauritz Jeanson: titlepage.xsl
    Added <xsl:call-template name="process.footnotes"/> to abstract template
    so that footnotes in info/abstract are processed. Closes bug #1760907.
  * Michael(tm) Smith: pi.xsl; synop.xsl
    Changed handling of HTML output for the cmdsynopsis and
    funcsynopsis elements, such that a@id instances are generated for
    them if they are descendants of any element containing a dbcmdlist
    or dbfunclist PI. Also, update the embedded reference docs for the
    dbcmdlist and dbfunclist PIs to make it clear that they can be
    used within any element for which cmdsynopsis or funcsynopsis are
    valid children.
  * Michael(tm) Smith: formal.xsl
    Reverted the part of revision 6952 that caused a@id anchors to be
    generated for output of informal objects. Thanks to Sam Steingold
    for reporting.
  * Robert Stayton: glossary.xsl
    Account for a glossary with no glossdiv or glossentry children.
  * Mauritz Jeanson: titlepage.xsl
    Modified legalnotice template so that the base.name parameter is calculated
    in the same way as for revhistory chunks. Using <xsl:apply-templates
    mode="chunk-filename" select="."/> did not work for single-page output since
    the template with that mode is in chunk-code.xsl.
  * Mauritz Jeanson: graphics.xsl
    Updated support for SVG (must be a child of imagedata in DB 5).
    Added support for MathML in imagedata.
  * Mauritz Jeanson: pi.xsl
    Added documentation for the dbhh PI (used for context-sensitive HTML Help).
    (The two templates matching 'dbhh' are still in htmlhelp-common.xsl).
  Manpages:
  * Michael(tm) Smith: endnotes.xsl
    In manpages output, generate warnings about notesources with
    non-para children only if the notesource is a footnote or
    annotation. Thanks to Sam Steingold for reporting problems with
    the existing handling.
  HTMLHelp:
  * Michael(tm) Smith: htmlhelp-common.xsl
    Added single-pass namespace-stripping support to the htmlhelp,
    eclipse, and javahelp stylesheets.
  Eclipse:
  * Michael(tm) Smith: eclipse.xsl
    Added single-pass namespace-stripping support to the htmlhelp,
    eclipse, and javahelp stylesheets.
  JavaHelp:
  * Michael(tm) Smith: javahelp.xsl
    Added single-pass namespace-stripping support to the htmlhelp,
    eclipse, and javahelp stylesheets.
  Roundtrip:
  * Steve Ball: blocks2dbk.xsl; blocks2dbk.dtd; pages2normalise.xsl
    Modularised blocks2dbk to allow customisation,
    Added support for tables to pages2normalise
  Params:
  * Robert Stayton: procedure.properties.xml
    procedure was inheriting keep-together from formal.object.properties, but
    a procedure does not need to be kept together by default.
  * Dave Pawson: title.font.family.xml;
    component.label.includes.part.label.xml; table.frame.b
    Regular formatting re-org.
* Fri Aug  3 2007 toms@suse.de
- Added missing common/charmap.xsl in manpages/docbook.xsl
- Fixed build problems.
* Fri Jul 27 2007 ke@suse.de
- Revert to previous package state (2007-05-11).
* Wed Jul 25 2007 toms@suse.de
- New release 1.73.0
  * Added Latvian and Esperanto translation, fixes in other locales
  * Description of all available PIs
  * Fix bug 1668629 valign on tbody not inherited.
  * Added template for xref to area/areaset.
    Part of fix for bug #1675513 (xref to area broken).
  * Fixed bug #1711508 (lists.xsl)
  * Added support for spacing="compact" in variablelist,
    per bug report #1722540.
  * Fixed bug #1669601 (footnote.xsl)
  * Fixed #1680755 (keycombo joinchar default incorrect).
  * Fixed bug 1652360 empty link with xlink:href.
  * Add support for default.table.frame parameter.
    Fix bug 1575446 rowsep last check for @morerows.
  => More in NEWS
* Fri May 11 2007 aj@suse.de
- Add unzip to BuildRequires.
* Tue Feb 27 2007 ke@suse.de
- Remove obsolete pre script; reported by Andreas Hanke [# 248672].
* Mon Jan 29 2007 ke@suse.de
- Update to 1.72.0: Many bugfixes and some extensions.  For details,
  see the NEWS file.
- Do no apply manpages-block-sp-2.patch; [# 176111] seems to be fixed
  upstream now.
- Remove obsolete README file.
- PreReq sgml-skel and remove exit statements from pre/post scripts; see
  [#216944].
* Thu Jan 11 2007 ke@suse.de
- Remove /usr/share/xml from the files list.
* Tue Nov 14 2006 ke@suse.de
- Update to 1.71.1: Bugfixes and some extensions:
  Fix problem with variable initialization [#220729].  From the NEWS
  file:
  Common:
  * For backward compatability autoidx-ng.xsl is invoking "kosek"
    indexing method again.
  * Add support for Xalan generating a root xml:base like saxon.
  * Fixed olink database access for Saxon and DB5.
  FO (some fixes also apply for HTML):
  * Complete the support for the info element.
    Add empty templates for titleabbrev in the default mode.
  * Fixed bug 1566358 to add space between orgname and orgdiv.
  * Made xref template target variables into params to fix bug #1559689.
  * Empty rows aren't allowed.
  * Added params to ulink and link templates so call-template by name works.
  * Fix bug in xlink.href (should be xlink:href).
  * Added support for profiling based on xml:lang and status attributes.
  * Create axf attribute before adding fotex element.
  * Add two-stage recursion for hyphenate.verbatim
    to fix recursion depth bug for long programlistings.
  HTML:
  * Made changes in namespace declarations to prevent xmllint's
    canonicalizer from treating them as relative namespace URIs.
  * Added the html.append and chunk.append parameters. By default, the
    value of both is empty; but the internal DocBook XSL stylesheets
    build sets their value to "<xsl:text>&#x0a;</xsl:text>", in order
    to ensure that all files in the docbook-xsl-doc package end in a
    newline character.
  Changes to Highlighting, Manpages, Template, Tools, and WordML.
  Params:
  * Added initial support in manpages output for footnote, annotation,
    and alt instances.
  * Added the html.append and chunk.append parameters. By default, the
    value of both is empty; but the internal DocBook XSL stylesheets
    build sets their value to "<xsl:text>&#x0a;</xsl:text>", in order
    to ensure that all files in the docbook-xsl-doc package end in a
    newline character.
  Profiling:
  * Added support for profiling based on xml:lang and status attributes.
* Mon Sep 11 2006 ke@suse.de
- Update to 1.71.0: many (small) bugfixes and extensions.
* Thu Aug 17 2006 ke@suse.de
- Update to snapshot 2006-08-16 on account of #188559; reported by
  Thorsten Kukuk.
- Update the manpages patch.
* Tue May 30 2006 ke@suse.de
- Update to version 1.70.1; this is a major update.  Changes since
  1.69.1 include:
  * Numerous bug fixes.
  * Support more DocBook features like qandaset; improve refentry
    processing; add more parameters for configuration.
  * Support for DocBook version 5.
  * Enhance all output formats, especially FO, HTML, and Manpages.
* Wed May 17 2006 ke@suse.de
- man/troff output: print a newline before each .sp command; reported by
  Andreas Schwab [# 176111].
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Jan 20 2006 kukuk@suse.de
- Update to version 1.69.1 (fix generation of manual pages from
  xml sources).
* Mon Jul 18 2005 ke@suse.de
- Update to version 1.69.0.
* Fri May 20 2005 ke@suse.de
- Update to 2005-05-17 snapshot for testing.
* Mon Feb 14 2005 ke@suse.de
- Update to version 1.68.1.
* Wed Feb  9 2005 ke@suse.de
- Update to version 1.68.0.
  * Various enhancements, moste FO related.
  * New SVG admonition graphics and navigation images.
* Thu Dec  2 2004 ke@suse.de
- Update to 1.67.2; this is a bug-fix release.
  * Revert some user-visible changes from 1.67.0.
* Wed Nov 10 2004 ke@suse.de
- Update to 1.67.0; this is a bug-fix release that contains a few new
  features.
  * User-visible changes affect HTML and FO output; details are
    listed at
    http://lists.oasis-open.org/archives/docbook-apps/200411/msg00123.html .
  * Saxon and Xalan enhancements.
  * Add Saxon8 extensions.
* Tue Oct 19 2004 ke@suse.de
- Update to 1.66.1; some highlights:
  * Important bug fixes and enhancements (tables, index sorting, olink
    templates, etc.).
  * Better support for DocBook 4.3.
  * In chunked output generic link header element (cf. HTML 4.01).
* Mon Jul 26 2004 ke@suse.de
- Update to 1.65.1:
  * Various bug fixes.
  * Offer alternate indexing mechanism; for details
    cf. /usr/share/doc/packages/docbook-xsl-stylesheets/RELEASE-NOTES.html.
* Thu Feb  5 2004 ke@suse.de
- Correct compat links.
* Fri Jan 30 2004 ke@suse.de
- Adjust directories according to FHS 2.3:
  * Move stylesheets to /usr/share/xml/docbook.
  * Provide compatibility links for SL =< 9.0 (log this info in
    /var/adm/SuSEconfig/run-sgmldir-links for later processing).
* Wed Jan 14 2004 ke@suse.de
- Update to 1.64.1.
* Wed Oct 22 2003 ke@suse.de
- Update to 1.62.4.
* Mon Jun 23 2003 ke@suse.de
- Update to 1.60.3 (various bug fixes; thus far no release notes).
* Fri May 23 2003 ke@suse.de
- Update to 1.61.2: many improvements and fixes; for more info cf.
  http://lists.oasis-open.org/archives/docbook-apps/200305/msg00111.html
  http://lists.oasis-open.org/archives/docbook-apps/200305/msg00228.html
  http://lists.oasis-open.org/archives/docbook-apps/200305/msg00273.html
* Tue Jan 28 2003 ke@suse.de
- Update to 1.60.1: some issues from release notes:
  * Lots of bug fixes.
  * Titlepage handling has changed; for details
  cf. RELEASE-NOTES.html.
  * Format cross references consistently.
  * Improve table handling.
  * Fix bugs in graphic width/height calculations.
- Install XML catalog; thus fixing major part of [# 21717].
* Tue Jan 21 2003 ke@suse.de
- Require docbook_4; reported by Gernot Hillier and Thomas Schraitle.
* Mon Jan 20 2003 ke@suse.de
- Update to 1.59.2: from release notes:
  * Bug fix: FO bug in the page masters that causes FOP to fail.
  * Various bug fixes.
  * Fix aligment problems in equations.
  * Output the type attribute on unordered lists (UL) in HTML only if
  the css.decoration parameter is true.
  * Calculate the font size in formal.title.properties so that it's 1.2
  times the base font size, not a fixed "12pt".
* Wed Jan 15 2003 ke@suse.de
- Update to 1.59.1: from release notes (since 1.57.0):
  * Bug fixes.
  * initial support for extensions in xsltproc.
  * Add Bulgarian localization.
  * Indexing improvements; localize book indexes to books but allow
  setindex to index an entire set.
  * The default value for rowsep and colsep is now "1" as per CALS.
  * Fix bugs in calculation of adjusted column widths to correct for
  rounding errors.
  * Add support for titleabbrev (use them for cross references).
  * Improvements to mediaobject for selecting print vs. online images.
  * Add seperate property sets for figures, examples, equations,
  tabless, and procedures.
  * Make lineannotations italic.
  * Support xrefstyle attribute.
  * Make endterm on xref higher priority than xreflabel target.
  * Support nested refsection elements correctly.
  * Glossary formatting improvements.
  * Reworked gentext.template to take context into consideration. The
  name of elements in localization files is now an xpath-like context
  list, not just a simple name.
  * Some improvements to bibliography formatting.
  * Improve graphical formatting of admonitions.
  * Add support for entrytbl.
  * Support spanning index terms.
  * Support bibliosource.
* Mon Nov 11 2002 ke@suse.de
- Update to 1.57.0.
- Provide version independent link; missing feature reported by eicker,
  Mads Martin Joergensen and Thomas Schraitle [# 19238].
* Thu Oct 10 2002 ke@suse.de
- Update to version 1.56.1
* Thu Aug 15 2002 ke@suse.de
- Add XSL 1.53.0 customization layer for PassiveTeX by Bob Stayton; for
  more info
  cf. http://sourceforge.net/tracker/index.php?func=detail&aid=593600&group_id=21935&atid=373747
  : Use
    xsltproc
  /usr/share/sgml/docbook/docbook-xsl-stylesheets-1.53.0/fo/custom.passivetex.xsl \
    mydoc.xml >mydoc.fo
  to load the customization layer.
* Mon Jul 29 2002 ke@suse.de
- Update to version 1.53.0:
  * Fix some bugs.
  * Refactor FO page masters.
  * And add some new parameters.
* Fri Jul 12 2002 mls@suse.de
- fixed postinstall script
* Wed Jul 10 2002 ke@suse.de
- Update to version 1.52.2:
  * Fix formatting, reference and index handling issues.
* Mon Jul  8 2002 ke@suse.de
- Update to version 1.52.1:
  * Fix reference handling (xref.xsl).
* Mon Jul  8 2002 ke@suse.de
- Update to version 1.52.0; from the announcement: Changes include:
  * A complete and consistent set of chunking parameters;
  * many new HTML Help parameters;
  * support for new-style OLinks;
  * experimental support for xref styles;
  * completely reworked page master/sequence config;
  * support for cross-references to paragraphs;
  * new header/footer, column, and glossary parameters;
  * other new parameters: draft.mode, suppress.footer.navigation and
    suppress.header.navigation, make.graphic.viewport,
    nominal.image.depth, nominal.image.width, use.embed.for.svg,
    refentry.title.properties, section.title.properties,
    use.embed.for.svg, generate.meta.abstract.xml.
- spec file: Remove obsolete variables.
* Tue Jun 18 2002 ke@suse.de
- Update to version 1.51.1.
- Drop the subpackage db2latex (once it's maintained again, I'll
  provide a proper standalone package.
- Provide version related convenience links; proposed by Rolf
  Niepraschk.
* Wed May  8 2002 ke@suse.de
- Update to version 1.50.0 [# 15162].
* Mon Feb 11 2002 ro@suse.de
- tar option for bz2 is "j"
* Mon Aug 20 2001 ke@suse.de
- Add db2latex (version 0.5.1) as a subpackage.
- Re-compress the archives using bzip2.
* Tue Aug  7 2001 ke@suse.de
- Update to version 1.42.
* Mon Jul 16 2001 ke@suse.de
- Update to version 1.41.
* Mon Apr 23 2001 ke@suse.de
- Fix create of compatibility link via %%post; reported by kukuk
  [#7130].
* Mon Mar 26 2001 ke@suse.de
- Provide compatibility link /usr/share/sgml/docbkxsl for SuSE Linux <
  8.0 (cf. README.SuSE).
* Fri Mar 23 2001 ke@suse.de
- Update to version 1.34 (experimental).
- Rename package: docbkxsl -> docbook-xsl-stylesheets.
- Adjust README.SuSE.
* Fri Feb  2 2001 ke@suse.de
- Update to version 1.29.
* Fri Sep 22 2000 ke@suse.de
- Update to version 1.18.
* Wed Aug 16 2000 ke@suse.de
- Update to version 1.17.
* Fri May 26 2000 ke@suse.de
- Update to version 1.13.
- Use %%{_defaultdocdir}.
* Fri Dec 17 1999 ke@suse.de
- Fix %%files list.
* Fri Dec 17 1999 ke@suse.de
- Update: version 1.01.
* Tue Nov 23 1999 ke@suse.de
- Start with version 1.00.
- Add README.SuSE.
