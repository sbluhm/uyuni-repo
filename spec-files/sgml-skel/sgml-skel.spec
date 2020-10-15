#
# spec file for package sgml-skel
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


Name:           sgml-skel
Version:        0.7.1
Release:        1.15
Summary:        Helper Scripts for the SGML System
License:        GPL-2.0+
Group:          Productivity/Publishing/SGML
Url:            https://github.com/openSUSE/sgml-skel
Source0:        https://github.com/openSUSE/sgml-skel/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  libxml2
Requires:       /bin/awk
Requires:       bash
Requires:       coreutils
Requires:       findutils
Requires:       libxml2-tools
%if 0%{?rhel}
Requires:	libxslt
Requires(post): libxslt
%else
Requires:       libxslt-tools
Requires(post): libxslt-tools
%endif
Requires(post): /bin/awk
Requires(post): bash
Requires(post): coreutils
Requires(post): findutils
Requires(post): libxml2-tools
BuildArch:      noarch

%description
These scripts will help prepare and maintain parts of an SGML system.

%prep
%setup -q

%build
autoreconf -fiv
%configure

%install
%make_install
ln -sf sgml2xmlcat.sh %{buildroot}%{_bindir}/sgmlcat2x.sh
ln -sf install-catalog %{buildroot}%{_bindir}/install-catalog.sh
ln -sf edit-xml-catalog %{buildroot}%{_bindir}/edit-xml-catalog.sh
install -d -m755 %{buildroot}%{_datadir}/sgml
install -d -m755 %{buildroot}%{_sysconfdir}/{sgml,xml}
install -d -m755 %{buildroot}%{_localstatedir}/lib/sgml
touch %{buildroot}%{_sysconfdir}/sgml/catalog
xmlcatalog --noout --create %{buildroot}%{_sysconfdir}/xml/suse-catalog.xml
xmlcatalog --noout --create %{buildroot}%{_sysconfdir}/xml/catalog
# Use correct order: first new method, second old method
xmlcatalog --noout --add  "nextCatalog" "catalog-d.xml" "catalog-d.xml" %{buildroot}%{_sysconfdir}/xml/catalog
xmlcatalog --noout --add  "nextCatalog" "suse-catalog.xml" "suse-catalog.xml" %{buildroot}%{_sysconfdir}/xml/catalog
install -d -m755 %{buildroot}%{_sysconfdir}/xml/catalog.d

%post
# only create suse-catalog.xml at installation time; not in the update case
if [ "$1" = 1 ]; then
  [ -r %{_sysconfdir}/xml/suse-catalog.xml ] \
    || xmlcatalog --create  | sed 's:/>:>\
</catalog>:' >%{_sysconfdir}/xml/suse-catalog.xml
fi
update-xml-catalog

%files
%defattr(-, root, root)
%dir %{_sysconfdir}/sgml
%dir %{_sysconfdir}/xml
%dir %{_sysconfdir}/xml/catalog.d
%dir %{_localstatedir}/lib/sgml
%doc AUTHORS COPYING ChangeLog README*
%ghost %{_sysconfdir}/sgml/catalog
%ghost %{_sysconfdir}/xml/suse-catalog.xml
%ghost %{_sysconfdir}/xml/catalog-d.xml
%config %verify(not md5 size mtime) %{_sysconfdir}/xml/catalog
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Jan 31 2017 mpluskal@suse.com
- Use pretty url
* Tue Jan 31 2017 sven-mario.seeberg-elverfeldt@suse.com
- removed _service
* Tue Jan 31 2017 sven-mario.seeberg-elverfeldt@suse.com
- Version 0.7.1 (bsc#1022632)
  - Fixed handling of empty /etc/xml/catalog.d
  - Fixed handling of hidden files in /etc/xml/catalog.d
* Tue Oct  4 2016 toms@opensuse.org
- Fix for bsc#1002759: change order in /etc/xml/catalog
  Needed to make precedence of catalog-d.xml over older method
  (suse-catalog.xml)
* Tue Jun 14 2016 fvogt@suse.com
- Improve specfile
- Version 0.7:
  - Move to GitHub
  - Integrate:
  - sgml-skel-edit-cat.diff
  - sgml-skel-regcat.diff
  - sgml-skel-regcat2.diff
  - edit-xml-catalog.sh
  - install-catalog.in
* Wed Jul 15 2015 ke@suse.com
- only create suse-catalog.xml at installation time; not in the update case.
- Add Requires(post): libxml2-tools for xmlcatalog.
* Tue Jul 14 2015 ke@suse.de
- %%post: create %%{_sysconfdir}/xml/suse-catalog.xml to avoid validation
  errors if in case no other DTD is installed [bsc#936596].
* Sun Nov 30 2014 Led <ledest@gmail.com>
- remove '-e' option of 'echo' command in install-catalog script.
  That option may be unsupported in some POSIX-complete shells
* Thu Dec  1 2011 coolo@suse.com
- add automake as buildrequire to avoid implicit dependency
* Wed May 14 2008 ke@suse.de
- sgml-skel-edit-cat.diff: Edit catalog file in place; try to keep file
  permissions.  Reported by Jörg Mayer [bnc#386791].
* Mon May 14 2007 ke@suse.de
- PreReq /bin/mv . Reported by Andreas Jaeger [#274128].
* Mon Jan 29 2007 ke@suse.de
- Fix debug code in edit-xml-catalog.  Reported by Andreas Hanke and
  Dirk Mueller [# 237652].
* Mon Aug 14 2006 ke@suse.de
- Provide /etc/xml/catalog.
- SuSEconfig.sgml-skel: Remove it.  It was required to solve on update
  issue while introducing the /usr/share/xml hierarchy.  It is obsolete
  now.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jul  4 2005 ke@suse.de
- PreReq /bin/awk; reported by Marco Michna [# 94798].
* Fri Jun 24 2005 ke@suse.de
- Add %%{_sysconfdir}/xml/suse-catalog.xml and mark it as %%ghost.
* Mon Jun 20 2005 schwab@suse.de
- Mark %%{_sysconfdir}/sgml/catalog as %%ghost and remove %%pre.
* Thu Nov 11 2004 mmj@suse.de
- cp used in %%pre so add to PreReq:
* Wed Aug 25 2004 ke@suse.de
- edit-xml-catalog.sh: Drop dependency on getopt to avoid adding more
  PreReqs in packages depending on sgml-skel.  Reported by Thorsten
  Kukuk [# 44154].
* Mon Feb 23 2004 hmacht@suse.de
- building as non-root
* Thu Feb 12 2004 ke@suse.de
- Fix tei-xsl link.
- Add svg-dtd links.
* Wed Feb 11 2004 ke@suse.de
- Correct resp. change some links; add tei-xsl-stylesheets.
* Thu Feb  5 2004 ke@suse.de
- Correct docbook-xsl-stylesheets related compat links.
- Add links for mathml-dtd.
* Fri Jan 30 2004 ke@suse.de
- Also create docbook-xsl-stylesheets related compat links (FHS 2.3
  related change).
* Fri Jan 23 2004 ke@suse.de
- Add SuSEconfig.sgml-skel: In case of an update provide compatibility
  links.
* Thu Jul 31 2003 meissner@suse.de
- autoreconf -i -f, so the --build arch switch detects ppc64.
* Fri Jun 13 2003 ke@suse.de
- Drop /usr/share/sgml from and add /etc/xml to %%files.
* Tue Apr 29 2003 ke@suse.de
- Add option --group to build <group>...</group> sections with id
  attributes in catalog files.
* Mon Apr 28 2003 ke@suse.de
- Add option --catalog to allow editing arbitrary catalog files.
* Mon Apr 28 2003 ke@suse.de
- Add edit-xml-catalog.sh, a script for editing /etc/xml/catalog.
* Wed Dec 11 2002 ke@suse.de
- sgml-skel-regcat2.diff: Don't register catalogs twice.
* Mon Nov 25 2002 ke@suse.de
- Update to version 0.6:
  * New script: sgml-register-catalog.
- sgml-skel-regcat.diff: Remove subcatalog without checking unrelated
  stuff.
* Thu Nov 21 2002 ke@suse.de
- /etc/sgml/catalog now belongs to this package; preserve backup in case
  sgmltools-lite owns it at the same time.
- Install install-catalog without suffix.
* Tue Nov 19 2002 ke@suse.de
- Add install-catalog.sh (from CVS:docbook-tools/sgml-common).
* Mon May 27 2002 ke@suse.de
- Update to version 0.5:
  - New scripts: sgml2xmlcat.sh (re-written, replacement for
    sgmlcat2x.sh) and parse-sgml-catalog.sh to normalized SGML Open
    catalogs.
* Mon May  6 2002 ke@suse.de
- Add sgmlcat2x.sh to parse normalized traditional SGML catalog files.
* Mon Aug 27 2001 ke@suse.de
- Update to version 0.2 (now it's a proper package):
  - Recognize ISO identifiers (additionally to '-//' and '+//' owner
    tags).
  - Handle language and version field.
  - More error checking.
* Thu Mar 22 2001 ke@suse.de
- New package.
