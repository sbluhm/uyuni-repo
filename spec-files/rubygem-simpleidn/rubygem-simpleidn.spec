#
# spec file for package rubygem-simpleidn
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

Name:           rubygem-simpleidn
Version:        0.0.9
Release:        lp152.3.5
%define mod_name simpleidn
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  ruby
BuildRequires:  rubygem-gem2rpm
Url:            https://github.com/mmriis/simpleidn
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Punycode ACE to unicode UTF-8 (and vice-versa) string conversion
License:        MIT
Group:          Development/Languages/Ruby

%description
This gem allows easy conversion from punycode ACE strings to unicode UTF-8
strings and vice-versa.

%prep

%build

%install
%gem_install \
  --doc-files="LICENCE README.rdoc" \
  -f

%gem_packages

%changelog
* Fri Dec 15 2017 tampakrap@opensuse.org
- Initial package
