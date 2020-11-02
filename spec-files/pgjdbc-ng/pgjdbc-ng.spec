#
# spec file for "pgjdbc-ng"
#
# Copyright (c) 2020 SUSE LLC
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

Name:           pgjdbc-ng
Version:        0.8.3 
Release:        4.3.uyuni
License:        BSD-3-Clause
Summary:        A new JDBC driver for PostgreSQL
Url:            http://impossibl.github.io/pgjdbc-ng/
Group:          Development/Libraries/Java
Source0:        https://github.com/impossibl/pgjdbc-ng/archive/pgjdbc-ng-0.8.3.tar.gz
Source1:        build.sh
Patch0:         0001-Upgrade-Gradle-to-6.1.1.patch
Patch1:         0002-Latest-netty.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64
BuildRequires:  xz
BuildRequires:  java-devel >= 1.8
BuildRequires:  pgjdbc-ng-kit == 8e8656170ee7b1df5be1071e76a4907e8e5f45fe
BuildArch:      noarch
Provides:       mvn(impossibl:pgjdbc-ng) == 0.8.3
Requires:       java
Requires:       mvn(io.netty:netty-common)
Requires:       mvn(io.netty:netty-buffer)
Requires:       mvn(io.netty:netty-transport)
Requires:       mvn(io.netty:netty-codec)
Requires:       mvn(io.netty:netty-handler)

%description
A new JDBC driver for PostgreSQL aimed at supporting the advanced features of JDBC and Postgres.

%prep
%setup -q -c -n src
%patch0 -p2
%patch1 -p2
cp -f %{SOURCE1} .
cp -Rf %{_datadir}/tetra ../kit

%build
cd ..
sh src/build.sh

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p %{buildroot}%{_javadir}
cp -a pgjdbc-ng-0.8.3/driver/build/libs/pgjdbc-ng-0.8.3.jar %{buildroot}%{_javadir}/pgjdbc-ng-0.8.3.jar
cp -a pgjdbc-ng-0.8.3/spy/build/libs/spy-0.8.3.jar %{buildroot}%{_javadir}/spy-0.8.3.jar

(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
* Mon Feb 10 2020 Silvio Moioli <moio@suse.com>
- Update to 0.8.3
* Fri Aug 23 2019 moio@suse.com
- Allow dots in database name (bsc#1146416)
- Added:
  * 0001-Allow-dots-in-database-name-bsc-1146416.patch
* Tue Sep 11 2018 moio@suse.com
- New JDBC driver for PostgreSQL required for bsc#1099988
- Initial version
