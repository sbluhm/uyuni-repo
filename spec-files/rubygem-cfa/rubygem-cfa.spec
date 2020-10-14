#
# spec file for package rubygem-cfa
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


Name:           rubygem-cfa
Version:        1.0.2
Release:        lp152.1.1
%define mod_name cfa
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/config-files-api/config_files_api
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Summary:        CFA (Config Files API) provides an easy way to create models on top
License:        LGPL-3.0-only
Group:          Development/Languages/Ruby

%description
Library offering separation of parsing and file access from the rest of the
logic for managing configuraton files. It has built-in support for parsing
using augeas lenses and also for working with files directly in memory.

%prep

%build

%install
%gem_install \
  -f

%gem_packages

%changelog
* Mon Dec 30 2019 Josef Reidinger <jreidinger@suse.com>
- fix writting multiple new elements to previously single element
  (found during fixing bsc#1156929)
- 1.0.2
* Wed Jul 17 2019 Josef Reidinger <jreidinger@suse.com>
- fix writting subtree when element change to collection and vice
  versa (bsc#1132362)
- 1.0.1
* Wed Jun 12 2019 Martin Vidner <mvidner@suse.com>
- Dropped the changes_only argument of BaseModel#save,
  it does not work in the generic case.
- Fixed NameError in AugeasTree#replace_entry (bsc#1137948)
- Drop support for Ruby 2.2 and 2.3; add 2.6.
- 1.0.0
* Thu Nov  8 2018 jreidinger@suse.com
- Improve even more error reporting now with specialized exceptions
  that holds all details for better user reports
  (needed for bsc#1113996)
- 0.7.0
* Thu Mar 15 2018 mvidner@suse.com
- Distinguish between parsing and serializing in error reports.
- Mention the file being parsed, and the position inside, in error
  reports (bsc#1077435)
- 0.6.4
* Thu Mar  8 2018 jreidinger@suse.com
- Workaround for augeas lenses that don't handle files without
  a trailing newline (bsc#1064623, bsc#1074891, bsc#1080051
  and gh#hercules-team/augeas#547)
- 0.6.3
* Fri May 26 2017 jreidinger@suse.com
- Fix attributes to work with simple values with trailing comments
  (bsc#1040946)
- Fix using CFA::BaseModel#generic_set without requiring
  CFA::Matcher
- 0.6.2
* Tue Apr 25 2017 jreidinger@suse.com
- fix writing two elements in collection containing nested tree
  (also caused by fix for bsc#1023204)
- 0.6.1
* Tue Mar 21 2017 jreidinger@suse.com
- fix writting two new following nested trees (also caused by fix
  for bsc#1023204)
- fix writing new element with same key as only existing key
- fix writing new element with same key as removed element
- add new method AugeasTree#unique_id that helps with writing new
  entries for augeas sequences
- 0.6.0
* Tue Mar 21 2017 jreidinger@suse.com
- fix AugeasTree#select to not return elements marked as deleted
  (caused by fix for bsc#1023204)
- 0.5.1
* Thu Mar  2 2017 jreidinger@suse.com
- allow generic set/get also on subtree (bsc#1023204)
- do minimal changes when editing file, especially do not eat
  white spaces if value is not modified (bsc#1023204)
- AugeasTree#data now return frozen hash as it is just filtered
  view of data, which cannot be modified
- 0.5.0
* Mon Dec  5 2016 joseivanlopez@gmail.com
- fix regression when passing nil to AugeasTree#delete (bsc#983486)
- 0.4.3
* Wed Nov 30 2016 joseivanlopez@gmail.com
- Improve deletion of elements in the augeas parser (needed to
  fix ntp-client, bsc#983486)
- 0.4.2
* Tue Oct 11 2016 jreidinger@suse.com
- optimize loading configuration files with augeas by reducing
  number of augeas match calls (bsc#877047)
- 0.4.1
* Tue Sep 27 2016 jreidinger@suse.com
- support augeas nodes containing value and also attached tree
  below it like e.g. ntp.conf has (bnc#983486)
- 0.4.0
* Tue May 24 2016 jreidinger@suse.com
- better inspecting of BooleanValue objects (helps with debugging
  various bncs, like bnc#980108 or bnc#940465)
- 0.3.1
* Mon Dec 21 2015 jreidinger@suse.com
- allow specifying a default file handler for all models
- 0.3.0
* Tue Dec 15 2015 jreidinger@suse.com
- add empty method requirement for parsers
- allow using block for matcher
- 0.2.0
* Tue Dec 15 2015 jreidinger@suse.com
- initial version of package
- 0.1.0
