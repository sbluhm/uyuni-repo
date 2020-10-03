#
# spec file for package release-notes-uyuni
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


Url:            https://www.uyuni-project.org

Name:           release-notes-uyuni
Summary:        Release Notes for Uyuni Server
License:        CC-BY-SA-3.0
Group:          Documentation/SUSE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       release-notes = %{version}
Provides:       release-notes-susemanager
Obsoletes:      release-notes < %{version}
Version:        2020.09
Release:        0
Source:         %{name}.tar.bz2

# for /srv/tomcat
BuildRequires:  tomcat
Requires:       tomcat

%description
This package contains files with the most important changes for this
Uyuni release.  They can be found in the
/usr/share/doc/release-notes directory.

%global debug_package %{nil}

%prep
%setup -n %{name}

%build

%install
rnpath="${RPM_BUILD_ROOT}"/usr/share/doc/release-notes/Uyuni_Server
rnpath_html="${RPM_BUILD_ROOT}"/srv/www/htdocs/docs/release-notes/
mkdir -p "$rnpath"
mkdir -p "$rnpath_html"
cp doc/release-notes.html "$rnpath"/RELEASE-NOTES.en.html
(cd "$rnpath"; ln -s RELEASE-NOTES.en.html RELEASE-NOTES.en.rtf)
cp doc/release-notes.html "$rnpath_html"/release-notes-server.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root,-)
%doc /usr/share/doc/release-notes
%dir /srv/www/htdocs/docs
/srv/www/htdocs/docs/release-notes

%changelog
