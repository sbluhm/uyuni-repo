#
# spec file for package ehcache
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


Name:           ehcache
Version:        2.10.1
Release:        2.10.uyuni
License:        Apache-2.0
Summary:        A cache library for Java projects
Url:            http://www.ehcache.org/
Group:          Development/Libraries/Java
Source0:        ehcache-2.10.1-src.tar.gz
# svn export https://svn.terracotta.org/svn/ehcache/tags/ehcache-2.10.1
# tar czvf ehcache-2.10.1-src.tar.gz ehcache-2.10.1
Source1:        build.sh
Patch0:         ehcache-2.10.1-src-jdk9.path
Patch1:         ehcache-javadoc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
BuildRequires:  java-devel
BuildRequires:  ehcache-kit == b6cea070e6df19be8c962e4c6d225e620115fe4c
BuildRequires:  subversion
BuildArch:      noarch
Provides:       mvn(net.sf.ehcache:ehcache-core) == 2.10.1
Provides:       ehcache-core == 2.10.1
Requires:       java

%description
Ehcache is an open source, standards-based cache that boosts performance, offloads your database, and simplifies scalability. It's the most widely-used Java-based cache because it's robust, proven, full-featured, and integrates with other popular libraries and frameworks. Ehcache scales from in-process caching, all the way to mixed in-process/out-of-process deployments with terabyte-sized caches.

%prep
%setup -q -c -n src
%patch0 -p1
%patch1 -p1
cp -f %{SOURCE1} .
cp -Rf %{_datadir}/tetra ../kit

%build
cd ..
sh src/build.sh

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p %{buildroot}%{_javadir}
cp -a ehcache-2.10.1/ehcache-core/target/ehcache-core-2.10.1.jar %{buildroot}%{_javadir}/ehcache-core-2.10.1.jar
ln -sf ehcache-core-2.10.1.jar %{buildroot}%{_javadir}/ehcache-core.jar

%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
* Tue Feb  5 2019 mc@suse.com
- Fix building javadoc
- Add:
  * ehcache-javadoc.patch
* Wed Nov  8 2017 jgonzalez@suse.com
- Fix build for JDK9
- Add:
  * ehcache-2.10.1-src-jdk9.path
* Wed Aug 31 2016 moio@suse.com
- Initial version for 3.1
* Tue Oct 13 2015 mc@suse.de
- build without checkstyle
- build require regexp
* Wed Dec 11 2013 mc@suse.de
- simplify defines in the spec file
* Tue Sep 24 2013 mc@suse.de
- one spec for with and without hibernate
* Wed Dec 22 2010 kkaempf@novell.com
- Disable tests by default (too resource intensive)
* Wed Dec 22 2010 kkaempf@novell.com
- Give ant (resp the jvm) more memory to execute tests
* Thu Dec  9 2010 mc@suse.de
- initial release
