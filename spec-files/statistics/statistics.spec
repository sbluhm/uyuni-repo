#
# spec file for package statistics
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           statistics
Version:        1.0.2
Release:        1.7.uyuni
Summary:        A Java statistics framework used inside Ehcache
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            https://github.com/Terracotta-OSS/statistics
Source0:        statistics-1.0.2.tar.gz
# curl -LOJ https://github.com/Terracotta-OSS/statistics/archive/v1.0.2.tar.gz
Source1:        build.sh
Patch0:         0001-Hamcrest-1.2-has-been-pulled-use-1.3.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  java-devel
BuildRequires:  statistics-kit == ddd8053e0e2d5f44696acb18186a0f55ae9b56cb
BuildRequires:  xz
BuildArch:      noarch
Provides:       mvn(org.terracotta.internal:statistics) == 1.0.2
Requires:       java
Requires:       osgi(slf4j.api)

%description
A statistics framework for Java used inside Ehcache and the Terracotta products.

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
cp -a statistics-1.0.2/target/statistics-1.0.2.jar %{buildroot}%{_javadir}/statistics-1.0.2.jar
ln -sf statistics-1.0.2.jar %{buildroot}%{_javadir}/statistics.jar

%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
* Fri Sep  2 2016 moio@suse.com
- Initial version
