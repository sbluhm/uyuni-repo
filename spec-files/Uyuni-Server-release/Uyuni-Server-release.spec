#
# spec file for package Uyuni-Server-release
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           Uyuni-Server-release
Summary:        Uyuni Server 
License:        GPL-2.0-or-later
Group:          System/Fhs
Version:        2020.09
Release:        2.1

# FATE#320199 : default patterns
Provides:       defaultpattern(uyuni_server)

Provides:       %name-%version
Provides:       product() = Uyuni-Server
Provides:       product(Uyuni-Server) = 2020.09-0
Provides:       product-label() = Uyuni%20Server
Provides:       product-cpeid() = cpe%3A%2Fo%3Aopensuse%3Auyuni%2Dserver%3A2020.09
Provides:       product-url(bugtracker) = https%3A%2F%2Fgithub.com%2Fuyuni%2Dproject%2Fuyuni%2Fissues%2F
Provides:       product-url(repository) = https%3A%2F%2Fdownload.opensuse.org%2Frepositories%2Fsystemsmanagement%3A%2FUyuni%3A%2FStable%2Fimages%2Frepo%2FUyuni%2DServer%2DPOOL%2D%{_target_cpu}%2DMedia1


Requires:       product(openSUSE) >= 15.2


BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Uyuni lets you efficiently manage physical, virtual,
and cloud-based Linux systems. It provides automated and cost-effective
configuration and software management, asset management, and system
provisioning.



%prep

%build

%install

mkdir -p $RPM_BUILD_ROOT/etc/products.d
cat >$RPM_BUILD_ROOT/etc/products.d/Uyuni-Server.prod << EOF
<?xml version="1.0" encoding="UTF-8"?>
<product schemeversion="0">
  <vendor>openSUSE</vendor>
  <name>Uyuni-Server</name>
  <version>2020.09</version>
  <release>0</release>
  <arch>%{_target_cpu}</arch>
  <cpeid>cpe:/o:opensuse:uyuni-server:2020.09</cpeid>
  <productline>uyuni</productline>
  <register>
    <pool>
    </pool>
    <updates>
    </updates>
  </register>
  <repositories>
  </repositories>
  <summary>Uyuni Server</summary>
  <shortsummary>Uyuni Server</shortsummary>
  <description>Uyuni lets you efficiently manage physical, virtual,
and cloud-based Linux systems. It provides automated and cost-effective
configuration and software management, asset management, and system
provisioning.</description>
  <urls>
    <url name="bugtracker">https://github.com/uyuni-project/uyuni/issues/</url>
    <url name="repository">https://download.opensuse.org/repositories/systemsmanagement:/Uyuni:/Stable/images/repo/Uyuni-Server-POOL-%{_target_cpu}-Media1</url>
  </urls>
  <buildconfig>
    <producttheme>openSUSE</producttheme>
  </buildconfig>
  <installconfig>
    <defaultlang>en_US</defaultlang>
    <datadir>suse</datadir>
    <descriptiondir>suse/setup/descr</descriptiondir>
    <releasepackage name="Uyuni-Server-release" flag="EQ" version="%{version}" release="%{release}"/>
    <distribution>openSUSE</distribution>
  </installconfig>
  <runtimeconfig/>
  <productdependency relationship="requires" name="openSUSE" version="15.2" flag="GE"/>
</product>

EOF



%clean
rm -rf %buildroot

%files
%defattr(644,root,root,755)
%dir /etc/products.d
/etc/products.d/*

%changelog
