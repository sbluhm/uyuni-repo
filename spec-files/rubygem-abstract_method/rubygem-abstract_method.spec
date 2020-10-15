#
# spec file for package rubygem-abstract_method
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           rubygem-abstract_method
Version:        1.2.1
Release:        lp152.3.5
%define mod_name abstract_method
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  ruby
BuildRequires:  rubygem-gem2rpm
Url:            https://github.com/openSUSE/abstract_method
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Tiny library enabling you to define abstract methods in Ruby classes
License:        MIT
Group:          Development/Languages/Ruby

%description
Abstract Method is a tiny library enabling you to define abstract methods in
Ruby classes and modules.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE README.md" \
  -f

%gem_packages

%changelog
* Wed Nov  5 2014 thardeck@suse.com
- adapt to new rubygem packaging
* Fri Aug 30 2013 coolo@suse.com
- updated to version 1.2.1
* Tue Jun 26 2012 jreidinger@suse.com
- use gem2rpm-opensuse to get corect metadata
* Thu Jun 21 2012 dmajda@suse.com
- Use the correct template for the .spec file.
* Thu Jun 21 2012 dmajda@suse.com
- Packaged version 1.2.0.
