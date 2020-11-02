#
# spec file for "ical4j"
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

Name:           ical4j
Version:        3.0.18
Release:        lp152.8.1
License:        BSD-3-Clause
Summary:        A Java library for parsing and building iCalendar data models
Url:            https://github.com/ical4j/ical4j
Group:          Development/Libraries/Java
Source0:        ical4j-ical4j-3.0.18.tar.gz
Source1:        build.sh
ExclusiveArch:  x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
BuildRequires:  java-devel
BuildRequires:  ical4j-kit == c31f3ad42d0d8923eabe8b8c63740017212d82a5
Requires:       java

%description
A Java library for parsing and building iCalendar data models

%package doc
Summary: Javadoc package for ical4j
%description doc
Javadoc package for ical4j

%prep
%setup -q -c -n src
cp -f %{SOURCE1} .
cp -Rf %{_libdir}/tetra ../kit

%build
cd ..
sh src/build.sh

%install
# export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p %{buildroot}%{_javadir}
cp -a ical4j-ical4j-3.0.18/build/libs/ical4j-0.1.0-SNAPSHOT-javadoc.jar %{buildroot}%{_javadir}/ical4j-%{version}-javadoc.jar
cp -a ical4j-ical4j-3.0.18/build/libs/ical4j-0.1.0-SNAPSHOT.jar %{buildroot}%{_javadir}/ical4j-%{version}.jar
ln -sf ical4j-%{version}.jar %{buildroot}%{_javadir}/ical4j.jar

%files
%defattr(-,root,root)
%{_javadir}/ical4j-%{version}.jar
%{_javadir}/ical4j.jar

%files doc
%defattr(-,root,root)
%{_javadir}/ical4j-%{version}-javadoc.jar

%changelog
* Wed Apr 15 2020 Pascal Arlt <parlt@suse.com>
- Initial version
