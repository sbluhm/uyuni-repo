#
# spec file for "spark-template-jade"
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

Name:           spark-template-jade
Version:        2.3
Release:        1.7.uyuni
License:        Apache-2.0
Summary:        Spark templating system using jade4j
Url:            http://www.sparkjava.com
Group:          Development/Libraries/Java
Source0:        spark-template-engines-2.3.tar.gz
Source1:        build.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  java-devel >= 1.8
BuildRequires:  spark-template-jade-kit == 45c6384b6a216e639c6a1174d08086f6dadcd1f3
BuildArch:      noarch
Provides:       mvn(com.sparkjava:spark-template-jade) == 2.3
Requires:       java

%description
Spark templating system using jade4j

%prep
%setup -q -c src -n src
cp -f %{SOURCE1} .
cp -Rf %{_datadir}/tetra ../kit

%build
cd ..
sh src/build.sh

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p %{buildroot}%{_javadir}
cp -a spark-template-engines-%{version}/%{name}/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in %{name}-*.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
* Mon Sep 21 2015 jrenner@suse.com
- Update to version 2.3
