#
# spec file for "spark-core"
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

Name:           spark-core
Version:        2.7.2
Release:        1.7.uyuni
License:        Apache-2.0
Summary:        A Sinatra inspired java web framework
Url:            http://www.sparkjava.com
Group:          Development/Libraries/Java
Source0:        %{name}-%{version}.tar.gz
Source1:        build.sh
Patch0:         spark-core-2.7.2-jdk9.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
BuildRequires:  java-devel >= 1.8
BuildRequires:  spark-core-kit == 930ff5156538a6b4cb84d12cea7dbf03cae095f1
BuildArch:      noarch
Provides:       mvn(com.sparkjava:spark-core) == %{version}
Provides:       spark == %{version}
Obsoletes:      spark < %{version}
Requires:       java >= 1.8

%description
A Sinatra inspired framework for creating web applications in Java with minimal effort

%prep
%setup -q -c -n src
%patch0 -p1
cp -f %{SOURCE1} .
cp -Rf %{_datadir}/tetra ../kit

%build
cd ..
sh src/build.sh

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p %{buildroot}%{_javadir}
cp -a spark-%{version}/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
* Tue Apr 10 2018 can.bulut.bayburt@suse.com
- Update to version 2.7.2
  - Fix a security problem in the serving of static files
  - Add support for specific keystore aliases
  - Bump Jetty to the latest version
- Rename package 'spark' to 'spark-core'
* Tue Nov  7 2017 jgonzalez@suse.com
- Fix build for JDK9
- Fix spec according to tetra changes
- Add:
  * spark-2.3-jdk9.patch
- Changed:
  * build.sh
* Wed Oct 28 2015 smoioli@suse.com
- update to version 2.3
  - WebSocket support
  - Thymeleaf template engine support
  - Jetbrick template engine support
  - Major improvements to implementation
  - Newer versions of all dependencies
- unit tests disabled, as they now require access to java.sun.com
- patch for fixing unit test removed, as they are disabled
* Fri Oct 16 2015 mc@suse.de
- increase sleep time for all tests
* Thu Oct 15 2015 jrenner@suse.com
- increase sleep time to make sure server is started
  * increase-sleep-time.patch
* Mon Oct 12 2015 smoioli@suse.com
- Initial version
