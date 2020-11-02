#
# spec file for "java-saml"
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           java-saml
Version:        2.4.0
Release:        2.7.uyuni
License:        MIT
Summary:        A Java SAML toolkit by
Url:            https://github.com/onelogin/java-saml
Group:          Development/Libraries/Java
Source0:        v2.4.0.tar.gz
Source1:        build.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
BuildRequires:  java-devel
BuildRequires:  java-saml-kit == 3b021b8651a2d25d5c44ab97f515bb2999280c26
BuildArch:      noarch
Provides:       mvn(com.onelogin:core) == 2.4.0
Provides:       mvn(com.onelogin:toolkit) == 2.4.0
Provides:       mvn(com.onelogin:samples) == 2.4.0
Requires:       java

%description
A Java SAML toolkit

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
cp -a java-saml-2.4.0/core/target/%{name}-core-%{version}.jar %{buildroot}%{_javadir}/%{name}-core-%{version}.jar
cp -a java-saml-2.4.0/toolkit/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}-core-%{version}.jar %{buildroot}%{_javadir}/%{name}-core.jar
%files
%defattr(-,root,root)
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-core-%{version}.jar
%{_javadir}/%{name}-core.jar

%changelog
* Wed May 15 2019 Michele Bologna <michele.bologna@suse.com>
- Added symlinks to package name in /usr/share/java
* Mon Mar 25 2019 Michele Bologna <michele.bologna@suse.com>
- Initial commit
