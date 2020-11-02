#
# spec file for "prometheus-client-java"
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

Name:           prometheus-client-java
Version:        0.3.0
Release:        1.7.uyuni
License:        Apache-2.0
Summary:        Prometheus instrumentation library for JVM applications
Url:            http://github.com/prometheus/client_java
Group:          Development/Libraries/Java
Source0:        parent-0.3.0.tar.gz
Source1:        build.sh
Patch0:         0001-Upgrade-Mockito-for-JDK10-compatibility.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
BuildRequires:  java-devel
BuildRequires:  prometheus-client-java-kit == 32e6246cc91e4f4f2f4afae0b3c4104088f269e6
BuildArch:      noarch
Provides:       mvn(io.prometheus:simpleclient) == 0.3.0
Provides:       mvn(io.prometheus:simpleclient_common) == 0.3.0
Provides:       mvn(io.prometheus:simpleclient_hibernate) == 0.3.0
Provides:       mvn(io.prometheus:simpleclient_hotspot) == 0.3.0
Provides:       mvn(io.prometheus:simpleclient_servlet) == 0.3.0
Requires:       java

%description
The Prometheus JVM Client allows instrumentation of software running on the JVM
for use with the Prometheus systems monitoring and alerting toolkit.
It supports Java, Clojure, Scala, JRuby, and anything else that runs on the JVM.

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
cp -a client_java-parent-0.3.0/simpleclient/target/simpleclient-0.3.0.jar %{buildroot}%{_javadir}/simpleclient-0.3.0.jar
cp -a client_java-parent-0.3.0/simpleclient_common/target/simpleclient_common-0.3.0.jar %{buildroot}%{_javadir}/simpleclient_common-0.3.0.jar
cp -a client_java-parent-0.3.0/simpleclient_hibernate/target/simpleclient_hibernate-0.3.0.jar %{buildroot}%{_javadir}/simpleclient_hibernate-0.3.0.jar
cp -a client_java-parent-0.3.0/simpleclient_hotspot/target/simpleclient_hotspot-0.3.0.jar %{buildroot}%{_javadir}/simpleclient_hotspot-0.3.0.jar
cp -a client_java-parent-0.3.0/simpleclient_httpserver/target/simpleclient_httpserver-0.3.0.jar %{buildroot}%{_javadir}/simpleclient_httpserver-0.3.0.jar
cp -a client_java-parent-0.3.0/simpleclient_servlet/target/simpleclient_servlet-0.3.0.jar %{buildroot}%{_javadir}/simpleclient_servlet-0.3.0.jar

(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
* Fri Apr 13 2018 moio@suse.com
- jdk10 compatibility fix added
* Fri Apr 13 2018 moio@suse.com
- simpleclient_httpserver added
* Tue Apr 10 2018 moio@suse.com
- Initial version
