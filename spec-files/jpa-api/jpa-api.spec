#
# spec file for "jpa-api"
#
# Copyright (c) 2018 SUSE LLC
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

Name:           jpa-api
Version:        2.2.2
Release:        1.7.uyuni
License:        EPL-2.0
Summary:        Java Persistence API specification
Url:            https://github.com/eclipse-ee4j/jpa-api
Group:          Development/Libraries/Java
Source0:        https://github.com/eclipse-ee4j/jpa-api/archive/2.2.2-RELEASE.tar.gz
Source1:        build.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
BuildRequires:  java-devel >= 1.8.0
BuildRequires:  jpa-api-kit == aab312071abf862f064ce590b6d778b277923980
BuildArch:      noarch
Provides:       mvn(jakarta.persistence:jakarta.persistence-api) == 2.2.2
Requires:       java

%description
The Java Persistence API is the Java API for the management of persistence and object/relational mapping in Jakarta EE and Java SE environments.

%prep
%setup -q -c -n src
cp -f %{SOURCE1} .
cp -Rf %{_datadir}/tetra ../kit

%build
cd ..
sh src/build.sh

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p %{buildroot}%{_javadir}
cp -a jpa-api-2.2.2-RELEASE/target/jakarta.persistence-api-2.2.2.jar %{buildroot}%{_javadir}/jakarta-persistence-api-2.2.2.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
* Fri Dec 21 2018 moio@suse.com
- initial version
