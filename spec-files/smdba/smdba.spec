#
# spec file for package smdba
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{!?python3_sitelib: %global python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}

Name:           smdba
Version:        1.7.4
# Stefan: Revert next two lines back for SUSE build system
Release:        0.1
# Release:        0.<RELEASE1>
Summary:        Tool to maintain the SUSE Manager Database
License:        MIT
Group:          Productivity/Databases/Tools

URL:            https://github.com/suse/smdba
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  python3-devel
%if 0%{?suse_version}
Provides:       spacewalk-dobby = 2.1
Obsoletes:      spacewalk-dobby < 2.1
%endif
Requires:       sudo

%description
SUSE Manager database control to operate various database backends.

%global debug_package %{nil}

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" python3 setup.py build

%install
python3 setup.py install --skip-build --root="$RPM_BUILD_ROOT" --prefix=%{_prefix} --record=INSTALLED_FILES
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0755 src/smdba/smdba $RPM_BUILD_ROOT/%{_bindir}
install -m0644 doc/smdba.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m0644 doc/smdba-netswitch.1 $RPM_BUILD_ROOT%{_mandir}/man1/
# compat link
ln -sf smdba $RPM_BUILD_ROOT/%{_bindir}/db-control

%clean
#rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root,-)
%dir %{python3_sitelib}/smdba
%dir %{python3_sitelib}/smdba/__pycache__
%dir %{python3_sitelib}/smdba/scenarios
%{python3_sitelib}/smdba/
%doc doc/README LICENSE
%{_mandir}/man1/*.1*
%{_bindir}/*

%changelog
