#
# spec file for package rubygem-yast-rake
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


# Only build for the default-ruby version
%define rb_build_versions     %{rb_default_ruby}
%define rb_build_ruby_abis    %{rb_default_ruby_abi}

Name:           rubygem-yast-rake
Version:        0.2.39
Release:        1.2
%define mod_name yast-rake
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby
BuildRequires:  ruby-macros >= 5
%if 0%{?rhel}
BuildRequires:	rubygem-gem2rpm
%else
BuildRequires:  rubygem(%{rb_default_ruby_abi}:gem2rpm)
%endif
URL:            http://github.org/openSUSE/yast-rake
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Rake tasks providing basic work-flow for Yast development
License:        LGPL-2.1-only
Group:          Development/Languages/Ruby

%description
Rake tasks that support work-flow of Yast developer. It allows packaging repo,
send it to build service, create submit request to target repo or run client
from git repo.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING" \
  -f

%gem_packages

%changelog
* Tue Jun 23 2020 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- :sle_latest is SLE15-SP3 now (bsc#1173266).
- 0.2.39
* Wed May 13 2020 Ladislav Slezák <lslezak@suse.cz>
- Enhanced "check:pot" task to check for "%%<foo>" tags in
  translatable strings (should be replaced with "%%{}")
  (bsc#1171555)
- 0.2.38
* Tue Apr 28 2020 Dominique Leuenberger <dimstar@opensuse.org>
- Only build gems for the default ruby version (boo#1169445).
* Wed Feb  5 2020 Ladislav Slezák <lslezak@suse.cz>
- Added "rake server" task (bsc#1162826)
- 0.2.37
* Fri Sep  6 2019 Ladislav Slezák <lslezak@suse.cz>
- Submit the SLE12-SP5 packages to Updates (not to GA) (bsc#1149771)
- Added the SLE15-SP2 target
- 0.2.36
* Thu Aug 22 2019 schubi@suse.de
- Using rb_default_ruby_abi tag in the spec file in order to
  handle several ruby versions (bsc#1146403).
- 0.2.35
* Thu Jun 27 2019 Josef Reidinger <jreidinger@suse.com>
- support proper rubocop version in rake check:rubocop
  (bsc#1139270)
- 0.2.34
* Thu Jun 20 2019 Ladislav Slezák <lslezak@suse.cz>
- :sle_latest is SLE15-SP2 now (bsc#1138835)
- 0.2.33
* Wed Apr 10 2019 Ladislav Slezák <lslezak@suse.cz>
- Submit SLE12-SP5 to GA, it is still in the development mode
  (related to bsc#1130043)
- 0.2.32
* Thu Mar 21 2019 Ladislav Slezak <lslezak@suse.cz>
- Added SLE15-SP1 target (bsc#1130043)
- 0.2.31
* Thu Mar 21 2019 aschnell@suse.com
- added SLE12-SP5 target
* Tue Nov 27 2018 Stasiek Michalski <hellcp@mailbox.org>
- Expose theme directory to allow for installation to theme
  (boo#1108422)
- 0.2.30
* Fri Nov 23 2018 Stasiek Michalski <hellcp@mailbox.org>
- Fix base dir for icons (boo#1109378)
- 0.2.29
* Tue Oct 30 2018 lslezak@suse.cz
- Changed the SLE12-SP4 SR target to the :Update subproject
  (bsc#1113887)
- 0.2.28
* Mon Oct 15 2018 lslezak@suse.cz
- Added CASP-4.0 target (needed for fate#325834)
- 0.2.27
* Wed Aug 22 2018 schubi@suse.de
- Removed installation of file COPYING into the doc directory.
  This file will be packed by the %%license tag in the spec files.
* Fri Jun 22 2018 lslezak@suse.cz
- Added "check:rubocop" and "check:rubocop:auto_correct" tasks
  which run Rubocop in parallel (much faster that the traditional
  sequential way) (bsc#1094875)
- 0.2.26
* Fri Jun 15 2018 jreidinger@suse.com
- switch sle_latest to SLE15 SP1 and switch SLE15 GA to
  maintenance mode (bsc#1044312)
- 0.2.25
* Wed Jun 13 2018 lslezak@suse.cz
- Fallback to the standard "rspec" when "parallel_rspec" is not
  available for running the tests in parallel (bsc#1094875)
- 0.2.24
* Mon May 28 2018 lslezak@suse.cz
- Improved "test:unit" rake task - optionally allow running the
  tests in parallel using the "parallel_tests" gem (bsc#1094875)
- 0.2.23
* Thu Apr 19 2018 jreidinger@suse.com
- add SLE12 SP4 as target and switch sle_latest to nil for now
  until IBS create project for SLE15 SP1. (bsc#1044312)
- 0.2.22
* Tue Apr 10 2018 lslezak@suse.cz
- Install also the custom icons in "rake install" (by wstephenson)
  (bsc#1088844)
- 0.2.21
* Thu Jan 18 2018 igonzalezsosa@suse.com
- Use old fillup-templates for openSUSE/SLE prior to 15
  (bsc#1076602)
- 0.2.20
* Wed Nov 29 2017 igonzalezsosa@suse.com
- Fix fillup-templates path (bsc#1070408)
- 0.2.19
* Thu Nov  2 2017 lslezak@suse.cz
- Keep the current $Y2DIR value in "rake run", just prepend
  the source directories
- 0.2.18
* Wed Aug  2 2017 lslezak@suse.cz
- SLE-12-SP3 and Leap 42.3 have been released, send the OBS submit
  requests to the :Updates projects now (bsc#1044312)
- 0.2.17
* Thu Jul 13 2017 jreidinger@suse.com
- set :Update as a target for Leap 42.1 and 42.2 because it is
  in maintenance mode. (bsc#1044312)
- 0.2.16
* Thu Jun 22 2017 mfilka@suse.com
- bsc#1044312
  - set :GA as a target for SLE-12-SP3 submissions since
    maintenance project is not existing yet.
- 0.2.15
* Wed Jun 14 2017 jreidinger@suse.com
- add sle15 as target and switch sle_latest (bsc#1044312)
- 0.2.14
* Thu Dec  1 2016 igonzalezsosa@suse.com
- Add casp10 target for CASP 1.0 (bnc#1013039)
- 0.2.13
* Wed Nov  9 2016 igonzalezsosa@suse.com
- update sle12sp2 target and add a new one for public
  Jenkins instance (sle12sp2_public) (bnc#1009324)
- 0.2.12
* Tue Sep 13 2016 jreidinger@suse.com
- add target also for leap42.2 (bnc#996865)
- 0.2.11
* Thu Sep  1 2016 jreidinger@suse.com
- prepare for branching for sle12sp3 (bnc#996865)
- add to known words "vc" as part of osc vc command in
  CONTRIBUTING.md
- 0.2.10
* Wed Mar  9 2016 schubi@suse.de
- Requiring packaging_rake_tasks ~> 1.1.4 in order to check
  for bugzilla,fate entries in the changes file.
  (bnc#0)
- 0.2.9
* Thu Mar  3 2016 lslezak@suse.cz
- added "sle12sp1_public" build target to build against SLE12-SP1
  in public OBS (bnc#969358)
- 0.2.8
* Wed Jan 13 2016 igonzalezsosa@suse.com
- update build target for sles12sp1 (bnc#0)
- 0.2.7
* Mon Nov 23 2015 jreidinger@suse.com
- fix build target for sle12sp2 (bnc#0)
- 0.2.6
* Wed Oct 28 2015 ancor@suse.com
- added target sle12sp2 ( needed for SP1 maintenance bnc#1)
- 0.2.5
* Fri Oct 16 2015 igonzalezsosa@suse.com
- add a submit_to method to simplify OBS configuration
* Tue Apr 28 2015 lslezak@suse.cz
- use rubocop for checking the code style
* Tue Apr 28 2015 lslezak@suse.cz
- optionally load the tasks from yast-rake-ci if it is installed
- 0.2.3
* Thu Apr 23 2015 lslezak@suse.cz
- allow to run the "check:spelling" task outside a Git checkout
  (to use it in the Jenkins jobs during package build)
- colorize the misspelled words in the output (if the "rainbow"
  gem is installed)
- use YAML config files
- 0.2.2
* Wed Apr  1 2015 jreidinger@suse.com
- regenerate spec file to fix build for ruby2.2 in OBS
* Thu Mar 26 2015 lslezak@suse.cz
- fixed gem packaging (missing "lib/tasks/spell.dict" file)
- 0.2.1
* Wed Mar 11 2015 lslezak@suse.cz
- added "check:spelling" task - spell check files (by default
  * .md and *.html files), needs "raspell" gem (no explicit
  dependency)
- do not crash when there is no "package/*.spec" file (e.g.
  in yast.github.io repository)
- 0.2.0
* Thu Nov 13 2014 lslezak@suse.cz
- new tasks:
  - "pot" - collect translatable strings and create *.pot files
  - "check:pot" - check for common mistakes in translations
- 0.1.10
* Wed Oct 29 2014 jreidinger@suse.com
- test:unit: run all tests in single run (gh#yast/yast-rake#11)
- 0.1.9
* Mon Jun  9 2014 jreidinger@suse.com
- install: Fix matching for autoyast-rnc directory
- 0.1.8
* Fri Jun  6 2014 locilka@suse.com
- Added support for Yast "data" directory
- 0.1.7
* Wed Jan 15 2014 jreidinger@suse.com
- Add "install" task for installation to proper location
- 0.1.6
* Mon Dec  9 2013 lslezak@suse.cz
- read the version number directly from *.spec file (ignore VERSION
  files), adapted "version:bump" task, removed
  "version:update_spec" task (not needed anymore)
- 0.1.5
* Thu Nov  7 2013 mvidner@suse.com
- Fixed `rake run` to work and `rake run[foo]` to really use
  the local files.
- 0.1.4
* Fri Oct 25 2013 jreidinger@suse.com
- Run test:unit even for nested test directories
  (gh#yast/yast-rake#2)
- 0.1.3
* Mon Oct 14 2013 jreidinger@suse.com
- do not run test before packaging as it is runned in osc:build
  during rpm build
- 0.1.2
* Thu Sep 19 2013 jreidinger@suse.com
- initial version