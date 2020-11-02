#
# spec file for "jade4j"
#
# Copyright (c) 2015 SUSE LLC
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

Name:           jade4j
Version:        1.0.7
Release:        8.6.uyuni
License:        MIT
Summary:        Java implementation of the jade templating
Url:            https://github.com/neuland/jade4j
Group:          Development/Libraries/Java
Source0:        v1.0.7.tar.gz
Source1:        build.sh
Patch0:         0001-JDK9-compatibility-fixes.patch
Patch1:         0002-Javadoc-fix.patch
Patch2:         0003-Update-commons-lang3.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?sle_version} >= 150000
BuildRequires:  java-devel >= 11
%else
BuildRequires:  java-devel-ibm >= 1.8.0
%endif
BuildRequires:  jade4j-kit == 7a828bbbc0c99dbf7b2840d511ba06d9760a2817
BuildArch:      noarch
ExcludeArch:    aarch64
Provides:       mvn(de.neuland-bfi:jade4j) == 1.0.7
%if 0%{?sle_version} >= 150000
Requires:       java >= 11
%else
Requires:       java-ibm >= 1.8.0
%endif
Requires:       apache-commons-jexl == 2.1.1
Requires:       apache-commons-collections == 3.2.2
Requires:       apache-commons-io >= 2.1
Requires:       apache-commons-lang3 >= 3.4
Requires:       concurrentlinkedhashmap-lru == 1.3.1

# This is needed to support inclusion of markdown documents
# Requires:       mvn(org.pegdown:pegdown)

%description
Java implementation of the jade templating - jade4j's intention is to be able to process jade templates in Java
without the need of a JavaScript environment, while being fully compatible with the original jade syntax.

%prep
%setup -q -c -n src
%patch0 -p2
%patch1 -p2
%patch2 -p2
cp -f %{SOURCE1} .
cp -Rf %{_datadir}/tetra ../kit

%build
cd ..
sh src/build.sh

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p %{buildroot}%{_javadir}
cp -a jade4j-1.0.7/target/jade4j-1.0.8-SNAPSHOT.jar %{buildroot}%{_javadir}/jade4j-%{version}.jar
ln -sf jade4j-%{version}.jar %{buildroot}%{_javadir}/jade4j.jar

%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
* Tue Feb 26 2019 Frantisek Kobzik <fkobzik@suse.com>
- Conditional java/java-devel requires based on os version
* Mon Feb 25 2019 jrenner@suse.com
- Update dependency version for commons-lang3 to 3.4
- Add:
  * 0001-JDK9-compatibility-fixes.patch
  * 0002-Javadoc-fix.patch
  * 0003-Update-commons-lang3.patch
- Removed:
  * v1.0.7-jdk9.patch
  * jade4j-javadoc.patch
* Tue Feb  5 2019 mc@suse.com
- fix building javadoc
- Add:
  * jade4j-javadoc.patch
* Tue Nov  7 2017 jgonzalez@suse.com
- Fix build for JDK9
- Add:
  * v1.0.7-jdk9.patch
* Mon Jan 25 2016 mc@suse.de
- require apache-commons-collections 3.2.2
* Mon Nov 16 2015 moio@suse.com
- Updated to 1.0.7
* Mon Oct 12 2015 smoioli@suse.com
- Initial version
