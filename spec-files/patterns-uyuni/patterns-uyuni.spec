#
# spec file for package patterns-uyuni
#
# Copyright (c) 2020 SUSE LLC.
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

Name:           patterns-uyuni
# Macros are not part of package-translations for SLE15
%if 0%{?suse_version} >= 1320
BuildRequires:  patterns-rpm-macros
%endif
BuildRequires:  perl(URI::Escape)
Summary:        Patterns for Uyuni
License:        GPL-2.0+
Group:          Metapackages
Version:        2020.09
Release:        2.1.uyuni
URL:            http://en.opensuse.org/Patterns
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %name-rpmlintrc

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

# Macros are provided patterns-rpm-macros for SLE15
%if 0%{?suse_version} < 1320
%define pattern_primaryfunctions \
Provides: pattern-category() = Primary%20Functions
%endif

%package -n patterns-uyuni_server
%pattern_primaryfunctions
Summary:        Uyuni Server
Group:          Metapackages
Provides:       pattern() = uyuni_server
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 3010
Provides:       pattern-visible()

Requires:       salt-api
Requires:       salt-master
%if 0%{?suse_version} > 1320
Requires:       python3-ws4py
Requires:       python2-salt
%else
Requires:       python3-ws4py
Requires:       python3-salt
%endif
#Requires:       py26-compat-salt

Requires:       mgr-osa-dispatcher
Requires:       release-notes-uyuni
Requires:       spacewalk-base-minimal
Requires:       smdba
Requires:       spacewalk-postgresql
Requires:       spacewalk-reports
Requires:       spacewalk-utils
Requires:       supportutils-plugin-susemanager
Requires:       susemanager
Requires:       uyuni-docs_en
Requires:       uyuni-docs_en-pdf
Requires:       Uyuni-Server-release
Requires:       susemanager-tools
Requires:       postgresql-server >= 12
Requires:       postgresql-contrib >= 12

%ifarch %ix86 x86_64
Requires:       syslinux
%else
Requires:       syslinux-x86_64
%endif

Requires:       cpu-mitigations-formula
Requires:       openvpn-formula
Recommends:     susemanager-tftpsync
Recommends:     golang-github-prometheus-node_exporter
Recommends:     golang-github-wrouesnel-postgres_exporter
Recommends:     golang-github-QubitProducts-exporter_exporter
Recommends:     prometheus-jmx_exporter
Recommends:     prometheus-jmx_exporter-tomcat
Recommends:     spacecmd
Recommends:     grafana-formula
Recommends:     locale-formula
Recommends:     prometheus-exporters-formula
Recommends:     prometheus-formula

# Retail packages
Recommends:     bind-formula
Recommends:     dhcpd-formula
Recommends:     tftpd-formula
Recommends:     virtualization-host-formula
Recommends:     vsftpd-formula
# end of Retail packages

# Monitoring
Recommends:     golang-github-lusitaniae-apache_exporter
Recommends:     golang-github-prometheus-node_exporter
Recommends:     golang-github-wrouesnel-postgres_exporter
Recommends:     golang-github-QubitProducts-exporter_exporter
Recommends:     prometheus-jmx_exporter
# End of Monitoring

%description -n patterns-uyuni_server
Uyuni Server packages.

%files -n patterns-uyuni_server
%defattr(-,root,root)
%dir /usr/share/doc/packages/patterns-uyuni-server
/usr/share/doc/packages/patterns-uyuni-server/uyuni_server.txt

#####################################################################

%package -n patterns-uyuni_retail
%pattern_primaryfunctions
Summary:        Uyuni for Retail
Group:          Metapackages
Provides:       pattern() = uyuni_retail
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 3011
Provides:       pattern-visible()

Requires:       bind-formula
Requires:       dhcpd-formula
Requires:       tftpd-formula
Requires:       vsftpd-formula
Requires:       branch-network-formula
Requires:       pxe-formula
Requires:       saltboot-formula
Requires:       image-sync-formula
Recommends:     virtualization-host-formula
%if 0%{?suse_version} > 1320
Requires:       python3-susemanager-retail
%else
Requires:       python-susemanager-retail
%endif
Requires:       susemanager-retail-tools

%description -n patterns-uyuni_retail
Uyuni for Retail packages.


%files -n patterns-uyuni_retail
%defattr(-,root,root)
%dir /usr/share/doc/packages/patterns-uyuni-retail
/usr/share/doc/packages/patterns-uyuni-retail/uyuni_retail.txt


#####################################################################

%package -n patterns-uyuni_proxy
%pattern_primaryfunctions
Summary:        Uyuni Proxy
Group:          Metapackages
Provides:       pattern() = uyuni_proxy
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 3010
Provides:       pattern-visible()

Requires:       Uyuni-Proxy-release
Requires:       spacewalk-proxy-broker
Requires:       spacewalk-proxy-common
Requires:       spacewalk-proxy-installer
Requires:       spacewalk-proxy-management
Requires:       spacewalk-proxy-package-manager
Requires:       spacewalk-proxy-redirect
Requires:       spacewalk-ssl-cert-check
Requires:       release-notes-uyuni-proxy
Requires:       supportutils-plugin-susemanager-proxy
Requires:       supportutils-plugin-susemanager-client

%if 0%{?suse_version} > 1320
Requires:       python3-rhnlib
%else
Requires:       python2-rhnlib
%endif

Recommends:     susemanager-tftpsync-recv
Recommends:     spacewalk-proxy-docs

# Monitoring
Recommends:     golang-github-boynux-squid_exporter
Recommends:     golang-github-prometheus-node_exporter
Recommends:     golang-github-lusitaniae-apache_exporter
Recommends:     golang-github-QubitProducts-exporter_exporter
# End of Monitoring

%description -n patterns-uyuni_proxy
Uyuni Proxy packages.


%files -n patterns-uyuni_proxy
%defattr(-,root,root)
%dir /usr/share/doc/packages/patterns-uyuni-proxy
/usr/share/doc/packages/patterns-uyuni-proxy/uyuni_proxy.txt

#####################################################################


%prep
# empty on purpose

%build
# empty on purpose

%install

mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-uyuni-server/
echo 'This file marks the pattern uyuni_server to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-uyuni-server/uyuni_server.txt

mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-uyuni-retail/
echo 'This file marks the pattern uyuni_retail to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-uyuni-retail/uyuni_retail.txt

mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-uyuni-proxy/
echo 'This file marks the pattern uyuni_proxy to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns-uyuni-proxy/uyuni_proxy.txt

%changelog
* Fri Sep 18 2020 Julio González Gil <jgonzalez@suse.com>
- Uyuni 2020.09
* Thu Sep 10 2020 Julio González Gil <jgonzalez@suse.com>
- Change PostgreSQL requirements to require at least PostgreSQL 12
* Mon Aug 10 2020 Julio González Gil <jgonzalez@suse.com>
- Add Recommends for golang-github-QubitProducts-exporter_exporter
* Tue Jun 23 2020 Julio González Gil <jgonzalez@suse.com>
- Uyuni 2020.07
* Wed Jun 10 2020 Julio González Gil <jgonzalez@suse.com>
- Uyuni 2020.06
* Mon Jun  1 2020 Julio González Gil <jgonzalez@suse.com>
- Add spacewalk-utils to the required packages for the server
  to get it installed by default
* Thu May 21 2020 Julio González Gil <jgonzalez@suse.com>
- Uyuni 2020.05
* Wed May 13 2020 Hubert Mantel <mantel@suse.com>
- remove Recommends for traditional client from proxy pattern as this
  will install the traditional stack during upgrades (bsc#1171494)
* Thu Apr 30 2020 Julio González Gil <jgonzalez@suse.com>
- Add requires for openvpn-formula
* Mon Apr 13 2020 Julio González Gil <jgonzalez@suse.com>
- Bump version to 2020.04
* Wed Mar 25 2020 Michael Calmer <mc@suse.com>
- remove susemanager-branding-oss package from server pattern
* Tue Mar  3 2020 jgonzalez@suse.com
- Remove system-lock-formula as it is now required by spacewalk-java
* Fri Feb 28 2020 Julio González Gil <jgonzalez@suse.com>
- change traditional tools in proxy pattern to Recommended as
  they are not needed when the proxy is configured as minion
* Mon Feb 10 2020 Michael Calmer <mc@suse.com>
- remove dropped package susemanager-proxy from pattern
* Thu Feb  6 2020 Cédric Bosdonnat <cbosdonnat@suse.com>
- Add recommends for virtualization-host-formula to retail
* Thu Jan 30 2020 Julio González Gil <jgonzalez@suse.com>
- Bump version to 2020.01
* Tue Jan 28 2020 Julio González Gil <jgonzalez@suse.com>
- Remove auditlog-keeper
* Tue Jan 14 2020 Julio González Gil <jgonzalez@suse.com>
- Add system-lock-formula to server pattern as "Required"
* Thu Nov 21 2019 Johannes Renner <jrenner@suse.com>
- Add prometheus-formula and grafana-formula to the server pattern
- Add the apache exporter to the proxy pattern as "Recommends"
* Wed Oct 30 2019 Julio González Gil <jgonzalez@suse.com>
- Install cpu-mitigations-formula by default
* Fri Oct 25 2019 Julio González Gil <jgonzalez@suse.com>
- Bump version to 2019.12
* Thu Sep  5 2019 Julio González Gil <jgonzalez@suse.com>
- Add recommends for virtualization-host-formula
* Fri Aug  2 2019 Julio González Gil <jgonzalez@suse.com>
- Remove susemanager-nagios-plugin
* Wed Jul 31 2019 Julio González Gil <jgonzalez@suse.com>
- Add recommends for cpu-mitigations-formula
* Wed May 15 2019 Julio González Gil <jgonzalez@suse.com>
- SPEC cleanup
* Fri Apr 26 2019 Julio González Gil <jgonzalez@suse.com>
- Fix wrong bugzilla entry at changelog
* Wed Apr 17 2019 Johannes Renner <jrenner@suse.com>
- Add recommends for Prometheus exporters and formula
* Mon Feb 18 2019 Julio González Gil <jgonzalez@suse.com>
- require postgresql at least version 10
- require syslinux-x86_64 for all none x86 architectures
- adjusted python package versions depending on the OS version
* Fri Sep 21 2018 jsrain@suse.cz
- adjusted pacakges list for Retail pattern
* Mon Aug 27 2018 mantel@suse.de
- remove unneeded requires for minion proxy; traditional clients
  still will get those packages via bootstrap repo
* Mon Aug 13 2018 jgonzalez@suse.com
- Refer to new package names for osa-dispatcher and spacewalksd
  (bsc#1104034)
* Mon Aug 13 2018 jgonzalez@suse.com
- Version 4.0 (bsc#1104034)
* Tue May 15 2018 mc@suse.com
- create retail pattern and add specialized formulas to it
- require postgresql >= 9.6 as database
* Sat May  5 2018 mc@suse.com
- add locale-formula as recommended to SUSE Manager Server
* Fri Apr  6 2018 mc@suse.com
- Require py26-compat-salt for SLE11 compatibility
- Require python3-salt for SLE15 compatibility
* Tue Feb 20 2018 jgonzalez@suse.com
- Enable openSUSE support
* Thu Jan 25 2018 mc@suse.com
- require python-ws4py again as we switched back to python2
* Fri Jan 12 2018 jsrain@suse.cz
- added Retail packages
* Thu Dec 14 2017 mc@suse.com
- require python3-ws4py
* Mon Dec  4 2017 jgonzalez@suse.com
- Fix building for SLE15
* Wed Jul 19 2017 mc@suse.com
- version 3.2
* Wed Apr 19 2017 mc@suse.de
- version 3.1
* Thu Mar  3 2016 mc@suse.de
- do not install salt packages with the proxy pattern
* Wed Feb 24 2016 mc@suse.de
- require syslinux or syslinux-x86_64 dependend on the architecture
* Thu Jan 14 2016 mc@suse.de
- add susemanager-sls to proxy pattern
* Wed Jan 13 2016 mc@suse.de
- require new doc packages
* Mon Nov 30 2015 mc@suse.de
- do not require postgresql-pltcl
* Wed Oct 14 2015 mc@suse.de
- do not require flavor package
* Wed Oct 14 2015 mc@suse.de
- drop pgtune from server pattern
* Thu Oct  8 2015 mc@suse.de
- remove salt_master pattern
- simplify salt package definition for server and proxy
* Thu Oct  8 2015 mc@suse.de
- build patterns for SUSE Manager Server and Proxy in one package
* Thu Oct  8 2015 mc@suse.de
- add seperate salt_master pattern
- add python-ws4py to salt_master
* Thu Aug 27 2015 mc@suse.de
- require postgresql >= 9.4
* Mon Aug  3 2015 mc@suse.de
- require salt packages
* Wed Jul  8 2015 mc@suse.de
- initial package
