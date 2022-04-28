#
# spec file for package salt-netapi-client
#
# Copyright (c) 2021 SUSE LLC
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


Name:           salt-netapi-client
Version:        0.19.0
Release:        0
Summary:        Java bindings for the Salt API
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/SUSE/salt-netapi-client
Source0:        salt-netapi-client-0.19.0.tar.gz
Source1:        build.sh
# Fix for (bsc#1192550)
Patch1:         0001-enable-arrays-in-StateApplyResult-name-bsc-1192550.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
%if 0%{?suse_version} >= 1500
BuildRequires:  java-devel >= 11
%else
BuildRequires:  java-devel >= 1.8
%endif
BuildRequires:  salt-netapi-client-kit == b9650a8c77f471a417fcf98d673b64c30d8df095
BuildArch:      noarch
Provides:       mvn(com.suse.salt:salt-netapi-client) == 0.18.0
%if 0%{?suse_version} >= 1500
Requires:       java >= 11
%else
Requires:       java >= 1.8
%endif
Requires:       google-gson >= 2.8.2
Requires:       httpcomponents-asyncclient >= 4.1.3
Requires:       mvn(org.apache.tomcat:tomcat-websocket-api) >= 8.0.23
# This package has been renamed with version 0.7.0
Provides:       saltstack-netapi-client-java == 0.7.0
Obsoletes:      saltstack-netapi-client-java < 0.7.0

%description
Java bindings for the Salt API

%prep
%setup -q -c -n src
%patch1 -p2
cp -f %{SOURCE1} .
cp -Rf %{_datadir}/tetra ../kit

%build
cd ..
sh src/build.sh

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p %{buildroot}%{_javadir}
cp -a %{name}-%{version}/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in %{name}-*.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%files
%defattr(-,root,root)
%{_javadir}/*
%doc %{name}-%{version}/LICENSE %{name}-%{version}/README.md

%changelog
