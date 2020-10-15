#
# spec file for package rubygem-cheetah
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-cheetah
Version:        0.5.2
Release:        lp152.1.1
%define mod_name cheetah
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/openSUSE/cheetah
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Your swiss army knife for executing external commands in Ruby safely
License:        MIT
Group:          Development/Languages/Ruby

%description
Your swiss army knife for executing external commands in Ruby safely and
conveniently.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG LICENSE README.md" \
  -f

%gem_packages

%changelog
* Mon Jan  6 2020 Josef Reidinger <jreidinger@suse.com>
- updated to version 0.5.2
  see installed CHANGELOG
  0.5.2 (2020-01-06)
  - -----------------
  * If listed in allowed_exitstatus, log exit code as Info, not as Error
    (bsc#1153749)
  * Added support for ruby 2.7
* Thu Oct 17 2019 Josef Reidinger <jreidinger@suse.com>
- updated to version 0.5.1
  see installed CHANGELOG
  0.5.1 (2019-10-16)
  - -----------------
  * Implement closing open fds after call to fork (bsc#1151960). This will work
    only in linux system with mounted /proc. For other Unixes it works as before.
  * drop support for ruby that is EOL (2.3 and lower)
  * Added support for ruby 2.4, 2.5, 2.6
* Sat Dec 19 2015 coolo@suse.com
- updated to version 0.5.0
  see installed CHANGELOG
  0.5.0 (2015-12-18)
  - -----------------
  * Added chroot option for executing in different system root.
  * Added ENV overwrite option.
  * Allowed to specify known exit codes that are not errors.
  * Documented how to execute in different working directory.
  * Allowed passing nil as :stdin to be same as :stdout and :strerr.
  * Converted parameters for command to strings with `.to_s`.
  * Adapted testsuite to new rspec.
  * Updated documentation with various fixes.
  * Dropped support for Ruby 1.9.3.
  * Added support for Ruby 2.1 and 2.2.
* Wed Nov  5 2014 thardeck@suse.com
- adapt to new rubygem packaging
* Fri Nov 22 2013 coolo@suse.com
- updated to version 0.4.0
  * Implemented incremental logging. The input and both outputs of the executed
  command are now logged one-by-line by the default recorder. A custom recorder
  can record them on even finer granularity.
  * Dropped support of Ruby 1.8.7.
  * Added support of Ruby 2.0.0.
  * Internal code improvements.
* Fri Jun 22 2012 jreidinger@suse.com
- use gem2rpm-opensuse instead to get better result
* Fri Jun 22 2012 dmajda@suse.com
- Removed the rpmlintrc file. We should make gem2rpm to produce RPMs that pass
  rpmlint, not fix its bugs after the fact.
- Regenerated the .spec file using gem2rpm.
* Thu Jun 21 2012 dmajda@suse.com
- Updated to version 0.3.0.
* Fri Apr  6 2012 dmajda@suse.com
- Attempted to fix rpmlint warnings produced by OBS.
* Fri Apr  6 2012 dmajda@suse.com
- Packaged version 0.2.0.
