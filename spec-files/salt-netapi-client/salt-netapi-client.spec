#
# spec file for "salt-netapi-client"
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

Name:           salt-netapi-client
Version:        0.18.0
Release:        1.1.uyuni
License:        MIT
Summary:        Java bindings for the Salt API
Url:            https://github.com/SUSE/salt-netapi-client
Group:          Development/Libraries/Java
Source0:        salt-netapi-client-0.18.0.tar.gz
Source1:        build.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
%if 0%{?suse_version} >= 1500
BuildRequires:  java-devel >= 11
%else
BuildRequires:  java-devel >= 1.8
%endif
BuildRequires:  salt-netapi-client-kit == 441c2ee62d05ff1f414ec80ba9b1cbf22ff16379
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
* Mon Oct 12 2020 Johannes Renner <jrenner@suse.com>
- Version 0.18.0
  See: https://github.com/SUSE/salt-netapi-client/releases/tag/v0.18.0
- Remove:
  * 0001-bring-auth-modules-up-to-date-with-current-salt-docs.patch
  * 0002-cleanup-http-client-after-each-test.patch
* Wed Sep 16 2020 Kevin Walter <kwalter@suse.com>
- Fix text resource usage
- Add:
  * 0002-cleanup-http-client-after-each-test.patch
* Fri Aug 28 2020 Silvio Moioli <moio@suse.com>
- Refresh authentication module list to newer Salt versions
- Add:
  * 0001-bring-auth-modules-up-to-date-with-current-salt-docs.patch
* Thu Feb 27 2020 Abid Mehmood <amehmood@suse.com>
- Version 0.17.0
  See: https://github.com/SUSE/salt-netapi-client/releases/tag/v0.17.0
- Remove:
  * 0001-handle-random-retcode-field-in-batch-mode.patch
* Tue Apr 30 2019 moio@suse.com
- Add workaround for Salt issue 52762
- Add:
  * 0001-handle-random-retcode-field-in-batch-mode.patch
* Wed Apr 10 2019 Abid Mehmood <amehmood@suse.com>
- Version 0.16.0
  see https://github.com/SUSE/salt-netapi-client/releases/tag/v0.16.0
* Mon Feb 11 2019 jgonzalez@suse.com
- Reenable building for JDK 1.8
* Tue Feb  5 2019 jgonzalez@suse.com
- Version 0.15.1
- Fix javadoc building for JDK11 and later
- Change:
  * build.sh
* Tue Jan 22 2019 jgonzalez@suse.com
- Explicitly require JDK11
* Thu Nov  8 2018 jrenner@suse.com
- Version 0.15.0
  See: https://github.com/SUSE/salt-netapi-client/releases/tag/v0.15.0
* Wed May  2 2018 jrenner@suse.com
- Version 0.14.0
  See: https://github.com/SUSE/salt-netapi-client/releases/tag/v0.14.0
- Removed:
  * salt-netapi-client-0.13.0-jdk9.patch
* Tue Nov 21 2017 jgonzalez@suse.com
- Fix build for JDK9
- Add:
  * salt-netapi-client-0.13.0-jdk9.patch
* Tue Sep  5 2017 kwalter@suse.com
- Version 0.13.0
  See: https://github.com/SUSE/salt-netapi-client/releases/tag/v0.13.0
* Fri Jul 14 2017 jrenner@suse.de
- Version 0.12.0
  See: https://github.com/SUSE/salt-netapi-client/releases/tag/v0.12.0
- Removed:
  * 0001-Fix-date-format-for-Schedule-bsc-1034465.patch
  * 0002-fix-sending-kwarg-in-payload-in-RunnerCall.patch
* Tue May  2 2017 jrenner@suse.de
- Fix sending kwarg in payload in RunnerCall
- Added:
  * 0002-fix-sending-kwarg-in-payload-in-RunnerCall.patch
* Wed Apr 19 2017 jrenner@suse.de
- Fix date format for Schedule module (bsc#1034465)
- Added:
  * 0001-Fix-date-format-for-Schedule-bsc-1034465.patch
* Tue Mar 28 2017 jrenner@suse.de
- Version 0.11.1
  See: https://github.com/SUSE/salt-netapi-client/releases/tag/v0.11.1
* Thu Feb  2 2017 jrenner@suse.de
- Version 0.10.0
  See: https://github.com/SUSE/salt-netapi-client/releases/tag/v0.10.0
* Fri Oct 21 2016 jrenner@suse.de
- Version 0.9.0
  See: https://github.com/SUSE/salt-netapi-client/releases/tag/v0.9.0
* Fri Jun 17 2016 jrenner@suse.de
- Version 0.8.0
* Wed Feb 10 2016 jrenner@suse.de
- Install LICENSE and README.md
* Tue Feb  9 2016 jrenner@suse.com
- Version 0.7.0
  See: https://github.com/SUSE/salt-netapi-client/releases/tag/v0.7.0
- This package has been renamed from 'saltstack-netapi-client-java'
