#
# spec file for "hibernate5"
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           hibernate5
Version:        5.3.7
Release:        6.1.uyuni
License:        LGPL-2.1
Summary:        Hibernate ORM is a component/library providing Object/Relational Mapping (ORM)
Url:            http://hibernate.org
Group:          Development/Libraries/Java
# curl -LOJ https://github.com/hibernate/hibernate-orm/archive/5.3.7.tar.gz
Source0:        5.3.7.tar.gz
Source1:        build.sh
Patch0:         0001-HHH-14077-CVE-2019-14900-SQL-injection-issue-in-Hibe.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
BuildRequires:  java-devel >= 1.9
BuildRequires:  hibernate5-kit == 06f89f5f40a0b95b08f814879026e8ce444876e5
BuildArch:      noarch
ExcludeArch:    aarch64 ppc64le s390x
Requires:       java
Requires:       antlr-java
Requires:       classmate
Requires:       dom4j
Requires:       hibernate-commons-annotations
Requires:       javassist
Requires:       jboss-logging

%description
Hibernate ORM enables developers to more easily write applications whose data outlives the application process. As an Object/Relational Mapping (ORM) framework, Hibernate is concerned with data persistence as it applies to relational databases (via JDBC).

%prep
%setup -q -c -n src
%patch0 -p2
cp -f %{SOURCE1} .
cp -Rf %{_datadir}/tetra ../kit

%build
cd ..
sh src/build.sh

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p %{buildroot}%{_javadir}
cp -a hibernate-orm-5.3.7/hibernate-c3p0/target/libs/hibernate-c3p0-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-c3p0-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-core/target/libs/hibernate-core-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-core-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-ehcache/target/libs/hibernate-ehcache-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-ehcache-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-entitymanager/target/libs/hibernate-entitymanager-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-entitymanager-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-envers/target/libs/hibernate-envers-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-envers-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-hikaricp/target/libs/hibernate-hikaricp-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-hikaricp-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-java8/target/libs/hibernate-java8-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-java8-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-jcache/target/libs/hibernate-jcache-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-jcache-5.3.7.jar

cp -a hibernate-orm-5.3.7/hibernate-jipijapa/target/libs/hibernate-jipijapa-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-jipijapa-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-osgi/target/libs/hibernate-osgi-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-osgi-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-proxool/target/libs/hibernate-proxool-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-proxool-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-spatial/target/libs/hibernate-spatial-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-spatial-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-testing/target/libs/hibernate-testing-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-testing-5.3.7.jar
cp -a hibernate-orm-5.3.7/hibernate-vibur/target/libs/hibernate-vibur-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-vibur-5.3.7.jar
cp -a hibernate-orm-5.3.7/tooling/hibernate-enhance-maven-plugin/target/libs/hibernate-enhance-maven-plugin-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-enhance-maven-plugin-5.3.7.jar
cp -a hibernate-orm-5.3.7/tooling/hibernate-gradle-plugin/target/libs/hibernate-gradle-plugin-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-gradle-plugin-5.3.7.jar
cp -a hibernate-orm-5.3.7/tooling/metamodel-generator/target/libs/hibernate-jpamodelgen-5.3.7.Final.jar %{buildroot}%{_javadir}/hibernate-jpamodelgen-5.3.7.jar

(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}|-5|g"`; done)

%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
* Wed Aug 12 2020 Silvio Moioli <moio@suse.com>
- Address CVE-2019-14900 (bsc#1172079)
- Add patch:
  * 0001-HHH-14077-CVE-2019-14900-SQL-injection-issue-in-Hibe.patch
* Thu May 30 2019 Julio González Gil <jgonzalez@suse.com>
- Package does not build at aarch64, ppc64le and s390x, so
  build is now disabled, as package is exported from x86_64 to
  such architectures
* Tue Dec 11 2018 moio@suse.com
- Update to version 5.3.7 for JDK 11 compatibility
- Full changelog available at https://github.com/hibernate/hibernate-orm/blob/890a6409a637da6f9fb64e2e11a9b87e01270ee0/changelog.txt#L7-L1283
- Remove:
  * hibernate-orm-5.2.2-src-jdk9.patch (obsoleted)
* Mon Nov 20 2017 jgonzalez@suse.com
- Fix build for JDK9
- Disable javadoc and documentation generation (broken for JDK9)
- Add:
  * hibernate-orm-5.2.2-src-jdk9.patch
* Wed Aug 31 2016 moio@suse.com
- Initial version
