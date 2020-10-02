#
# spec file for package cpu-mitigations-formula
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           cpu-mitigations-formula
Version:        0.1
Release:        1%{?dist}
Summary:        CPU mitigation Salt Formula for SUSE Manager
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/SUSE/salt-formulas
Requires:       salt-master
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

# This would be better with a macro that just strips "-formula" from {name}
%define fname cpu-mitigations

%description
Salt Formula for SUSE Manager. Edits grub entries for kernel cpu mitigation options.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/share/susemanager/formulas/states/%{fname}
mkdir -p %{buildroot}/usr/share/susemanager/formulas/metadata/%{fname}
cp -R states/* %{buildroot}/usr/share/susemanager/formulas/states/%{fname}
cp -R metadata/* %{buildroot}/usr/share/susemanager/formulas/metadata/%{fname}

%files
%defattr(-,root,root,-)
/usr/share/susemanager

%changelog
