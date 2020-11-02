#
# spec file for "byte-buddy"
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

Name:           byte-buddy
Version:        1.8.17
Release:        1.7.uyuni
License:        Apache-2.0
Summary:        Byte Buddy is a code generation and manipulation library for Java
Url:            http://bytebuddy.net
Group:          Development/Libraries/Java
Source0:	https://github.com/raphw/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        build.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
BuildRequires:  java-devel
BuildRequires:  byte-buddy-kit == 09f20221a9e78d6694ae4e2d45b9d1f14057086a
BuildArch:      noarch
Provides:       mvn(net.bytebuddy:byte-buddy) == 1.8.17
Provides:       mvn(net.bytebuddy:byte-buddy-dep) == 1.8.17
Provides:       mvn(net.bytebuddy:byte-buddy-benchmark) == 1.8.17
Provides:       mvn(net.bytebuddy:byte-buddy-agent) == 1.8.17
Provides:       mvn(net.bytebuddy:byte-buddy-android) == 1.8.17
Provides:       mvn(net.bytebuddy:byte-buddy-maven-plugin) == 1.8.17
Provides:       mvn(net.bytebuddy:byte-buddy-gradle-plugin) == 1.8.17
Requires:       java

%description
Byte Buddy is a code generation and manipulation library for creating and modifying Java classes during the runtime of a Java application and without the help of a compiler. Other than the code generation utilities that ship with the Java Class Library, Byte Buddy allows the creation of arbitrary classes and is not limited to implementing interfaces for the creation of runtime proxies. Furthermore, Byte Buddy offers a convenient API for changing classes either manually, using a Java agent or during a build.

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
cp -a byte-buddy-byte-buddy-1.8.17/byte-buddy/target/byte-buddy-1.8.17.jar %{buildroot}%{_javadir}/byte-buddy-1.8.17.jar

(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)


%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
* Fri Dec 21 2018 moio@suse.com
- initial version
