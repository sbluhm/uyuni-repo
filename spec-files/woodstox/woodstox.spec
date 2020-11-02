#
# spec file for package woodstox
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

%define section   free

Name:           woodstox
Version:        4.4.2
Release:        4.7.uyuni
Summary:        The gold standard Stax XML API implementation
License:        LGPL-2.1
Group:          Development/Libraries/Java
Url:            https://github.com/FasterXML/Woodstox4
Source0:        https://github.com/FasterXML/Woodstox4/archive/master.zip
Patch0:		java6-compat.patch
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  unzip
BuildRequires:  woodstox-kit = 1.0
BuildArch:      noarch
Provides:       mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Woodstox is an XML-parser that allows parsing of XML documents in so-called pull mode (aka "pull parsing").

%prep
%setup -n Woodstox4-master
ln -s /usr/share/tetra lib
%patch0 -p0

%build
export CLASSPATH=$(build-classpath jzlib)
export OPT_JAR_LIST=:
ant dist javadoc

%install
# jars
install -Dpm 644 dist/woodstox-core-asl-4.4.2.jar %{buildroot}%{_javadir}/%{name}-core-asl-%{version}.jar
install -Dpm 644 lib/stax2-api-3.1.4.jar %{buildroot}%{_javadir}/stax2-api-3.1.4.jar
install -Dpm 644 lib/stax-api-1.0.1.jar %{buildroot}%{_javadir}/stax-api-1.0.1.jar
ln -s %{name}-core-asl-%{version}.jar %{buildroot}%{_javadir}/%{name}-core-asl.jar
ln -s stax2-api-3.1.4.jar %{buildroot}%{_javadir}/stax2-api.jar
ln -s stax-api-1.0.1.jar %{buildroot}%{_javadir}/stax-api.jar

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc release-notes/asl/LICENSE
%{_javadir}/%{name}-core-asl.jar
%{_javadir}/%{name}-core-asl-%{version}.jar
%{_javadir}/stax-api.jar
%{_javadir}/stax-api-1.0.1.jar
%{_javadir}/stax2-api.jar
%{_javadir}/stax2-api-3.1.4.jar

%changelog
* Wed May 15 2019 Michele Bologna <michele.bologna@suse.com>
- Add stax-api and stax2-api JARs to the installed files
* Wed May 15 2019 Michele Bologna <michele.bologna@suse.com>
- Add symlink to package name in /usr/share/java
* Fri Apr 12 2019 Michele Bologna <michele.bologna@suse.com>
- Move binaries Java libraries to external package "woodstox-kit"
* Tue Mar 26 2019 Michele Bologna <michele.bologna@suse.com>
- Initial import
