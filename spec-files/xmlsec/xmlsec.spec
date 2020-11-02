#
# spec file for "xmlsec"
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

Name:           xmlsec
Version:        2.0.7
Release:        3.7.uyuni
License:        Apache-2.0
Summary:        Apache XML Security for Java supports XML-Signature Syntax
Url:            http://santuario.apache.org/
Group:          Development/Libraries/Java
Source0:        xmlsec-2.0.7-source-release.zip
Source1:        build.sh
Patch0:         0001-fix-jdk9-compat.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  unzip
BuildRequires:  java-devel
BuildRequires:  xmlsec-kit == b3b8eb4e03915b8bb8863fb758ebfcbac0a622bb
BuildArch:      noarch
Provides:       mvn(org.apache.santuario:xmlsec) == 2.0.7
Requires:       java
Requires:       osgi(slf4j.api)
Requires:       mvn(org.codehaus.woodstox:woodstox-core-asl) 
Requires:       mvn(commons-codec:commons-codec) 

%description
Apache XML Security for Java supports XML-Signature Syntax and Processing, W3C Recommendation 12 February 2002, and XML Encryption Syntax and Processing, W3C Recommendation 10 December 2002. As of version 1.4, the library supports the standard Java API JSR-105: XML Digital Signature APIs

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
cp -a xmlsec-2.0.7/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%defattr(-,root,root)
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%changelog
* Wed May 15 2019 Michele Bologna <michele.bologna@suse.com>
- Add symlink to package name in /usr/share/java
* Mon Apr 15 2019 Michele Bologna <michele.bologna@suse.com>
- Adapted the sources to be compiled with JDK 9
- Renamed the patch with a meaningful name (add/remove below)
- Add:
  * 0001-fix-jdk9-compat.patch
- Removed:
  * 0001-Sources-updated.patch
* Mon Apr 15 2019 Michele Bologna <michele.bologna@suse.com>
- Initial import of xmlsec
