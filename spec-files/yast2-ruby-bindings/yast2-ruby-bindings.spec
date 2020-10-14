#
# spec file for package yast2-ruby-bindings
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


Name:           yast2-ruby-bindings
Version:        4.3.4
Release:        1.1
URL:            https://github.com/yast/yast-ruby-bindings
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        yast2-ruby-bindings-%{version}.tar.bz2
Prefix:         /usr

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-devtools >= 3.1.10
%if 0%{?suse_version} == 1310
BuildRequires:  rubygem-fast_gettext < 3.0
BuildRequires:  rubygem-rspec
Requires:       rubygem-fast_gettext < 3.0
%else
BuildRequires:  rubygem(%{rb_default_ruby_abi}:fast_gettext) < 3.0
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
Requires:       rubygem(%{rb_default_ruby_abi}:fast_gettext) < 3.0
%endif
BuildRequires:  ruby-devel
Requires:       yast2-core >= 3.2.2
BuildRequires:  yast2-core-devel >= 3.2.2
# MenuBar widget
Requires:       yast2-ycp-ui-bindings       >= 4.3.1
BuildRequires:  yast2-ycp-ui-bindings-devel >= 4.3.1
# The test suite includes a regression test (std_streams_spec.rb) for a
# libyui-ncurses bug fixed in 2.47.3
BuildRequires:  libyui-ncurses >= 2.47.3
# The mentioned test requires to check if tmux is there, because tmux is
# needed to execute the test in headless systems
BuildRequires:  which

# only a soft dependency, the Ruby debugger is optional
Suggests:       rubygem(%{rb_default_ruby_abi}:byebug)

# Unfortunately we cannot move this to macros.yast,
# bcond within macros are ignored by osc/OBS.
%bcond_with yast_run_ci_tests
%if %{with yast_run_ci_tests}
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake-ci)
%endif

Requires:       ruby
Summary:        Ruby bindings for the YaST platform
License:        GPL-2.0-only
Group:          System/YaST

%description
The bindings allow YaST modules to be written using the Ruby language
and also Ruby scripts can use YaST agents, APIs and modules.

%prep
%setup -n yast2-ruby-bindings-%{version}
%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{prefix} \
      -DLIB=%{_lib} \
      -DCMAKE_C_FLAGS="%{optflags}" \
      -DCMAKE_CXX_FLAGS="%{optflags}" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 \
      ..
make %{?jobs:-j %jobs} VERBOSE=1

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT
cd -

%check
cd build
make test ARGS=-V
cd -

# run extra CI checks (in Jenkins)
%if %{with yast_run_ci_tests}
%yast_ci_check
%endif

%files
%defattr (-, root, root)
%{yast_ybindir}/y2start
%{_libdir}/YaST2/plugin/libpy2lang_ruby.so
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/*.rb
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/yast
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/%{rb_arch}/*x.so
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/%{rb_arch}/yast
%license COPYING

%changelog
* Thu Sep 24 2020 besser82@fedoraproject.org
- Fixes for gensalt handling with libxcrypt (bsc#1176924)
- 4.3.4
* Wed Sep 23 2020 Josef Reidinger <jreidinger@suse.com>
- Improve logger to log also method name in ruby (useful for any
  debug like bsc#1144351)
- 4.3.3
* Wed Aug 12 2020 Stefan Hundhammer <shundhammer@suse.com>
- Fixed yast-ycp-ui-bindings dependency (bsc#1175115)
- 4.3.2
* Wed Aug 12 2020 Stefan Hundhammer <shundhammer@suse.com>
- Added new UI terms: MenuBar(), Menu() (bsc#1175115)
- 4.3.1
* Wed Apr 22 2020 Josef Reidinger <jreidinger@suse.com>
- reimplement Builtins#tointeger to not use scanf removed from ruby
  2.7 (bsc#1169442)
- 4.3.0
* Wed Jan 22 2020 Ancor Gonzalez Sosa <ancor@suse.com>
- Added a COPYING file with the GPL license (bsc#1161470)
- 4.2.8
* Fri Jan  3 2020 Josef Reidinger <jreidinger@suse.com>
- Fix previous fix to really set exit code in ruby wrapper
  (bsc#1144351)
- 4.2.7
* Tue Dec 17 2019 Josef Reidinger <jreidinger@suse.com>
- Fix returning error codes from y2start start point. Helps with
  CLI exit codes and also with failed installation (helps e.g. with
  bsc#1144351 and yast lan CLI)
- 4.2.6
* Thu Dec  5 2019 schubi@suse.de
- S390: Evaluating an architecture specific string which will be
  shown in the title bar (ncurses) or in the banner (qt)
  (jsc#SLE-9424).
- 4.2.5
* Wed Nov  6 2019 Stefan Hundhammer <shundhammer@suse.com>
- Added symbol for new UI CustomStatusItemSelector widget
  (bsc#1084674)
- Added symbol for UI icon term
- 4.2.4
* Mon Sep 23 2019 Stefan Hundhammer <shundhammer@suse.com>
- Added symbols for new UI ItemSelector widget (bsc#1084674)
- 4.2.3
* Thu Aug 22 2019 schubi@suse.de
- Using rb_default_ruby_abi tag in the spec file in order to
  handle several ruby versions (bsc#1146403).
- 4.2.2
* Mon May 20 2019 mvidner@suse.com
- Fixup the textdomain change so that yast2.rpm builds (bsc#1130822)
- 4.2.1
* Thu May 16 2019 mvidner@suse.com
- Raise (an Internal Error) if no textdomain is declared for
  a translatable text and Y2STRICTTEXTDOMAIN is in the environment
  (bsc#1130822)
- 4.2.0
* Tue Mar  5 2019 Ladislav Slezák <lslezak@suse.cz>
- Always return frozen strings from the translation functions,
  make the results unified (related to bsc#1125006)
- 4.1.4
* Mon Mar  4 2019 Michal Filka <mfilka@suse.com>
- bnc#1127685
  - Internal error message popup is scaled according to its content
- 4.1.3
* Tue Jan 22 2019 lslezak@suse.cz
- Support for FastGettext 2.0 (still works with FastGettext 1.6)
  (bsc#1121865)
- 4.1.2
* Tue Dec 18 2018 jlopez@suse.com
- Configure $PATH environment variable to execute external commands
  only from safe paths (part of bsc#1118291).
- 4.1.1
* Tue Oct 23 2018 jreidinger@suse.com
- Fix encoding-related problems by assuming that file contents is
  always UTF-8. (bsc#1111367)
- 4.1.0
* Tue Sep 11 2018 aschnell@suse.com
- adapted testsuite to glibc translation change (bsc#1107953)
- 4.0.7
* Mon Aug 20 2018 schubi@suse.de
- Switched license in spec file from SPDX2 to SPDX3 format.
* Fri Apr  6 2018 jlopez@suse.com
- Allow to directly abort the process (needed for fate#318196).
- 4.0.6
* Tue Mar 27 2018 lslezak@suse.cz
- Log a warning if no text domain is configured for translations,
  this helps with debugging (improved as a part of bsc#1081466)
- 4.0.5
* Tue Jan  9 2018 jreidinger@suse.com
- Set proper title also for YaST2 scc (bsc#1075164)
- 4.0.4
* Tue Dec  5 2017 jreidinger@suse.com
- Set proper title also for YaST2 Firstboot (bsc#1070583)
- 4.0.3
* Fri Nov 24 2017 mvidner@suse.com
- Better backtrace for dynamically defined methods (bsc#1066290)
- 4.0.2
* Thu Nov 23 2017 lslezak@suse.cz
- Hardcode the Ruby version in the y2start script to always use
  the Ruby version used at the build time (bsc#1068863)
- 4.0.1
* Tue Sep 26 2017 jreidinger@suse.com
- Nicer backtrace output in log for internal errors (help for
  debuggging bugs like bsc#1044312)
- 4.0.0
* Wed Jul 12 2017 jreidinger@suse.com
- Always use ::Integer to avoid collision with Yast::Integer
  (bsc#1044312)
- make Builtins.toupper/tolower strictly backward compatible
  in ruby 2.4 (bsc#1044312)
- 3.3.1
* Wed Jul 12 2017 jreidinger@suse.com
- replace all Fixnum and Bignum with Integer as ruby 2.4 make it
  deprecated ( ruby2.4 will be default for TW and SLE15 so part
  of bsc#1044312)
- 3.3.0
* Tue Jul  4 2017 jreidinger@suse.com
- Set proper title also for YaST2 System Log (bsc#1046153)
- 3.2.14
* Tue May 23 2017 jreidinger@suse.com
- Set proper title for YaST2 installation (bsc#1037891)
- 3.2.13
* Tue May  2 2017 jreidinger@suse.com
- fix calling YaST CLI (bsc#1033993)
- 3.2.12
* Mon Apr 10 2017 jreidinger@suse.com
- Set proper title for YaST2 application (bsc#1033161)
- 3.2.11
* Wed Mar 22 2017 jreidinger@suse.com
- Add new y2start as ruby script which have several advantages
  (bsc#1027181):
-- Ruby is no longer embedded into YaST (instead we only use binary
  extensions), so there is less chance of things breaking with
  a new Ruby version
-- show popup when signal is received and also allow YaST modules
  to handle more gracefully when signal is raised
-- better argument passing to y2start itself e.g.
  y2base foo -S '(bar)' qt ----> y2start foo --arg bar qt
-- ruby infrastructure can be used directly on y2start like debugger
  or profiler
-- majority of y2start functionality is covered by unit tests
  allowing easier and less error-prone future changes
- 3.2.10
* Wed Mar 22 2017 jreidinger@suse.com
- Use more friendly exception when an invalid Yast::Path is
  constructed (one with a component starting or ending with
  a dash; bsc#1028081)
- 3.2.9
* Wed Mar 22 2017 jreidinger@suse.com
- add method Yast::WFM.scr_root to get scr changed root directory
  (needed for testing fix for bsc#1023204)
- 3.2.8
* Tue Mar 14 2017 ancor@suse.com
- Use tmux instead of screen to run the Ncurses integration test
  in headless systems (skip the test if tmux is not available).
  The version of screen introduced to fix bsc#1021743 was causing
  the test to fail.
- 3.2.7
* Thu Mar  9 2017 ancor@suse.com
- Display standard output and error channels in case of failure
  running the Ncurses integration tests in a headless system.
  Needed to debug the error produced by the fix to bsc#1021743
- 3.2.6
* Mon Jan  9 2017 jreidinger@suse.com
- allow in Yast::SCR and Yast::WFM to have string as first
  argument where Yast::Path is expected
  (gh#yast/yast-ruby-bindings#82, bsc#1018876)
- make yast specific class shortcuts available via Yast namespace
  like Yast.path() or Yast.term()
- allow path shortcut to get string or path and return always path
- raise exception if wrong type is passed to path including nil
- 3.2.5
* Mon Jan  9 2017 jreidinger@suse.com
- drop Yast.add_module_dir and Yast.add_include_dir as the only
  reliable way is to use Y2DIR env (gh#yast/yast-ruby-bindings#72)
* Wed Jan  4 2017 jreidinger@suse.com
- Throw exception with more detailed error specification when
  loading namespace to component system failed (bsc#932331)
- 3.2.4
* Thu Dec 15 2016 igonzalezsosa@suse.com
- Do not crash when FastGettext is unable to find the empty.mo
  file (bsc#1014458)
- 3.2.3
* Tue Nov 15 2016 lslezak@suse.cz
- Improved debugger support: catch the magic debugging key
  combination (Shift+Ctrl+Alt+D in Qt) returned by UI calls and
  start the Ruby debugger when received (FATE#318421)
- 3.2.2
* Wed Oct 26 2016 jreidinger@suse.com
- fix crash when references passed between clients (bsc#935385)
- 3.2.1
* Thu Oct 13 2016 jreidinger@suse.com
- properly document usage of CallFunction and have useful error
  when misused (bsc#889980)
- 3.2.0
* Fri Sep 16 2016 mvidner@suse.com
- Rescue "invalid byte sequence in UTF-8", with a custom message
  (bsc#992821).
- 3.1.51
* Thu Jun 30 2016 jreidinger@suse.com
- Fix segfault when running rspec tests caused by added ruby
  profiler (bnc#986649 comment2)
- 3.1.50
* Tue Jun 28 2016 jreidinger@suse.com
- Added support for running the Ruby profiler
- Improve performance of code by specialized `caller` call
  (bnc#986649)
- 3.1.49
* Mon May 30 2016 lslezak@suse.cz
- Improve the debugger support - use the same code also at run
  time, allow using `Y2DEBUGGER` also in installed system
  (FATE#318421)
- 3.1.48
* Mon May 23 2016 lslezak@suse.cz
- Added support for running the Ruby debugger (FATE#318421)
- Allow running the Ruby debugger from the generic crash handler
  if the debugger is installed
- 3.1.47
* Mon Mar  7 2016 jreidinger@suse.com
- update code according to updated yast ruby style guide
* Wed Jan 13 2016 jreidinger@suse.com
- Move transdb initialization to C part to keep it together with
  index initialization (bsc#932014)
- 3.1.46
* Wed Jan 13 2016 jreidinger@suse.com
- fixed early return from logging method causing failure of old
  testsuite (bsc#932014)
- 3.1.45
* Tue Jan 12 2016 lslezak@suse.cz
- Fixed conflict between Yast::Encoding and ::Encoding (another fix
  for bsc#932014)
- 3.1.44
* Mon Jan 11 2016 lslezak@suse.cz
- Do not crash when logging an invalid UTF-8 string (bsc#932014)
- 3.1.43
* Tue Dec  1 2015 jreidinger@suse.com
- Reverted the last change because it broke updating the table in
  Service Manager
  (because the distinction between :cell and :Cell was lost)
  (bnc#956380)
- 3.1.42
* Fri Nov 13 2015 jreidinger@suse.com
- Fix Cell ui shortcut as final id have to be lowercase (fake bug
  to get it accepted bnc#0)
- 3.1.41
* Mon Oct  5 2015 jreidinger@suse.com
- Used rb_gc_register_address to fix 'method to_s called on
  terminated object' during package installation (bsc#945299)
- 3.1.40
* Wed Sep 30 2015 ancor@suse.com
- Added a regression test for the fix of bnc#943757 implemented
  in libyui-ncurses 2.47.3
- 3.1.39
* Tue Aug  4 2015 mvidner@suse.com
- Applied the style guide, with Rubocop.
* Mon Jun 29 2015 ancor@suse.com
- Added Yast::Builtins::strftime with full i18n support
  (part of fate#318486)
- 3.1.38
* Thu Jun 25 2015 jreidinger@suse.com
- pass method name to logger (helps with debugging,
  e.g. bnc#922308)
- 3.1.37
* Thu Jun 18 2015 ancor@suse.com
- Fixes in the new Yast::CoreExt functionality (part of the fix
  for bnc#921233)
- 3.1.36
* Wed Jun 17 2015 ancor@suse.com
- Added Yast::CoreExt, a new mechanism to extend ruby base classes
- Added extension to clean ANSI characters from strings (part of
  the fix for bnc#921233)
- 3.1.35
* Wed Jun  3 2015 mvidner@suse.com
- Fixed "Comparable#== will no more rescue exceptions of #<=>"
  (boo#933470).
- Fixed a strdup/delete mismatch (boo#932306).
- 3.1.34
* Mon May 25 2015 jreidinger@suse.com
- add ability to test if scr is local (FATE#317900)
- 3.1.33
* Mon May 18 2015 mvidner@suse.com
- Initialize the YaST UI so that it can be called
  when the main program is not y2base (bsc#922023).
- 3.1.32
* Wed Apr  1 2015 ancor@suse.com
- Added new RSpec argument matcher: path_matching
- 3.1.31
* Thu Mar  5 2015 mvidner@suse.com
- Fix building with yast2-core-3.1.16: use C++11 like core does
  (boo#914255).
- 3.1.30
* Tue Feb 24 2015 jreidinger@suse.com
- fix building for ruby2.2
- 3.1.29
* Wed Jan 28 2015 jreidinger@suse.com
- add more shortcuts for RSpec helpers, that makes tests shorter
- 3.1.28
* Thu Jan 22 2015 jreidinger@suse.com
- enhance usability of Yast::Term class
- 3.1.27
* Thu Jan 22 2015 ancor@suse.com
- Added some RSpec helpers to easy the development of tests
- 3.1.26
* Mon Oct 20 2014 lslezak@suse.cz
- added Travis support (.travis.yml, xcrypt.h detection)
* Wed Oct 15 2014 coolo@suse.com
- switch to rubygem() for Factory too
- 3.1.25
* Fri Sep 12 2014 jreidinger@suse.com
- GC-guard some Ruby values to prevent a crash in slideshow
  (bnc#895964)
- 3.1.24
* Wed Jul 30 2014 mvidner@suse.com
- Fixed to report the right frame for Ops.get_foo (bnc#877758).
- Futureproof tests for RSpec 3 even more, avoid be_true.
- 3.1.23
* Wed Jul 23 2014 locilka@suse.com
- Builtins.mapmap newly only accepts Hash, otherwise raises
  a TypeError (bnc#888585)
- 3.1.22
* Mon Jul  7 2014 mrueckert@suse.de
- switch to rubygem() based requires so we can easily pass the
  preferred ruby version using rb_default_ruby_abi
* Tue Jun 10 2014 jreidinger@suse.com
- fix comparison of float and integer (bnc#865037)
- 3.1.21
* Tue Jun  3 2014 jreidinger@suse.com
- fix crash of n_ as now textdomain is array (bnc#881124)
- 3.1.20
* Mon Jun  2 2014 mvidner@suse.com
- Converted "should" to "expect" in RSpec,
  to be prepared for rspec-3.0.
- 3.1.19
* Thu May 29 2014 jreidinger@suse.com
- fix translation if mixture of textdomain are used in included
  files (bnc#877687)
- 3.1.18
* Wed May 14 2014 mvidner@suse.com
- Mechanically converted the remaining test/unit tests to RSpec
  (bnc#877758)
- 3.1.17
* Tue Apr 22 2014 jreidinger@suse.com
- Fix hang out of YaST2 in Turkish locale(bnc#852242)
- 3.1.16
* Fri Mar 14 2014 mvidner@suse.com
- Show the caller in the Internal error popup.
- 3.1.15
* Mon Mar  3 2014 jreidinger@suse.com
- do not crash if ruby cannot find yast ruby part
- 3.1.14
* Thu Feb 27 2014 jreidinger@suse.com
- fix precedence of loading files in lib
- 3.1.13
* Wed Feb 26 2014 lslezak@suse.cz
- added N_() and Nn_() gettext equivalents (to only mark a text
  for translation)
- 3.1.12
* Thu Feb 20 2014 jreidinger@suse.com
- always log full backtrace when type conversion failed, to help
  with debugging
- 3.1.11
* Mon Feb 17 2014 jreidinger@suse.com
- fix stack level too deep (BNC#864056,BNC#864180)
- 3.1.10
* Mon Feb 10 2014 jreidinger@suse.com
- Do not unload clients after execution (BNC#861529)
- 3.1.9
* Wed Feb  5 2014 lslezak@suse.cz
- Builtins.y2milestone(),... marked as deprecated, use Yast::Logger
  instead in the new code
- 3.1.8
* Tue Feb  4 2014 jreidinger@suse.com
- format spec file
* Mon Feb  3 2014 lslezak@suse.cz
- added Y2Logger - Ruby Logger for writing logs using the Yast
  format, can be used by external libraries for logging into y2log
- 3.1.7
* Mon Feb  3 2014 jreidinger@suse.com
- final fix for Ops.get and Ops.set warnings to not point inside
  their own implementation
- 3.1.6
* Mon Jan 13 2014 jreidinger@suse.com
- Prefer yast lib directory in LOAD_PATH to reduce collisions with
  random rubygem
- 3.1.5
* Mon Dec  9 2013 jreidinger@suse.com
- fixed Ops.get and Ops.set warnings to not point inside their own
  implementation
- 3.1.4
* Wed Nov 27 2013 jreidinger@suse.com
- add detection of invalid type in publish call
- 3.1.3
* Fri Oct 25 2013 jreidinger@suse.com
- report exceptions via Report.Error so there is no hidden failures
- detect invalid response type from clients
  (gh#yast/yast-ruby-bindings#81)
- 3.1.2
* Tue Oct 15 2013 lslezak@suse.cz
- float_to_lstring(): do not crash when glibc-locale is missing,
  fallback to unlocalized version (bnc#803163)
- 3.1.1
* Thu Sep 12 2013 jreidinger@suse.com
- fix loading rubygems in embedded ruby
- when client raise exception set proper exit code
- 3.0.3
* Wed Sep 11 2013 jreidinger@suse.com
- remove workaround for ruby 1.9 as only 2.0 is supported
  (to really fix $0 and ARGV, gh#yast/yast-ruby-bindings#74)
- do not link against UI plugin, because showing UI without y2base
  is not supported
  (may fix a Jenkins failure)
- 3.0.2
* Wed Sep 11 2013 mvidner@suse.com
- link to owcrypt only if it exists (fixes 12.3 builds)
* Wed Sep 11 2013 jreidinger@suse.com
- do not overwrite script name which require yast
  gh#yast/yast-ruby-bindings#73,74
- crypt_gensalt moved to separate library libowcrypt (fate#314945)
  (thanks to Andreas Schwab <schwab@suse.de>)
- 3.0.1
* Tue Jul 30 2013 yast-devel@opensuse.org
- version 3.0.0
* Tue Jul 23 2013 jreidinger@suse.com
- fix path conversion (gh#yast/ycp-killer#562)
- remove deprecated calls and YCP namespace
- improve reporting problematic code when builtin is called in
  wrong way (gh#yast/ycp-killer#575)
- 1.2.0
* Wed Jul 17 2013 lslezak@suse.cz
- added Ops.get_* shortcut methods (dmajda)
- fix detecting of complex path in the last segment (jreidinger)
- unload client class after running it to fully initialize includes
  in the next run (gh#yast/ycp-killer#504)
- 1.1.5
* Tue Jul  9 2013 jreidinger@suse.com
- fix calling methods on namespace that is already used as nested
  namespace (gh#yast/ycp-killer#465)
- 1.1.4
* Thu Jul  4 2013 jreidinger@suse.com
- allow passing single value to Ops.index and Ops.assign
- revert term immutable change as there is modification operation
  on it
- create shortcuts for is builtins
- implement conversion from and to byteblock
- skip fast_gettext initialization if the locale directory does not
  exist
- 1.1.3
* Thu Jun 27 2013 jreidinger@suse.com
- make term and path class immutable, so deep copy can be
  optimalized
- support backtrace in y2log() (lslezak)
- call include init method only if it is there
- update UI shortcuts to allow also terms starting with lowercase
- various small bug fixes
- 1.1.2
* Mon Jun 24 2013 jreidinger@suse.com
- set the source location when calling YaST functions outside Ruby
- few minor fixes in logging
- 1.1.1
* Thu Jun 20 2013 jreidinger@suse.com
- Rename top level namespace from YCP to Yast
- cache translations in dpgettext() builtin (lslezak)
  (https://github.com/yast/ycp-killer/issues/467)
- implement block version of Ops.index
  (https://github.com/yast/y2r/issues/20)
- 1.1.0
* Tue Jun 18 2013 jreidinger@suse.com
- Complete rewrite of ruby bindings to allow migration of ycp code
  to ruby. Few features worth mentioning:
  - ruby clients
  - ruby include files
  - ruby modules with export of specified type
  - support of global variables
  - support of ycp builtins
- 1.0.0
* Wed Jun 27 2012 jreidinger@suse.com
- adapt to changes in yast2-core
- 0.3.13
* Tue Jun 12 2012 coolo@suse.com
- finish the ruby 1.9 port
- 0.3.12
* Thu Jun  7 2012 jreidinger@suse.com
- port to ruby 1.9
* Thu Apr  5 2012 jsuchome@suse.cz
- removed libxcrypt-devel from buildrequires
* Thu Jan 19 2012 jreidinger@suse.com
- improve previous fix to allow loading also file in namespace (
  e.g. Name::Test in name/test ) (bnc#705417)
* Mon Jan 16 2012 coolo@suse.com
- license should be GPL-2.0 without or later
* Mon Jan 16 2012 jreidinger@suse.com
- allows loading modules which follows rails ruby convention
  ( ActiveSupport module is in active_support.rb file )
  (bnc#705417)
* Wed Dec  7 2011 coolo@suse.com
- fix license to be in spdx.org format
* Mon Oct  3 2011 mvidner@suse.cz
- WIP: Ruby objects usable from YCP (FATE#312825).
    except those that get garbage collected :-/)
- Run the tests at RPM build time.
- Less log clutter when importing a Ruby namespace.
- 0.3.8
* Tue Jul 26 2011 kkaempf@novell.com
- Re-init the Ruby stack when calling a Ruby function. bnc#708059
- 0.3.7
* Mon Jul 25 2011 kkaempf@novell.com
- wrap rb_funcall in rb_protect to prevent segfaults if the
  calling function raises an exception (bnc#705425)
- 0.3.6
* Tue Nov  3 2009 dmacvicar@novell.com
- support for nested namespaces (Foo::Bar)
  (bnc #551881)
- 0.3.5
* Mon Nov  2 2009 dmacvicar@suse.de
- fix convertion of ruby hashes to ycp maps
  (bnc #551791)
- 0.3.4
* Thu Apr  9 2009 kkaempf@suse.de
- add and enable CTest
- generate rdoc documentation
- pass explicit rpath to linker so plugins are found
- general code cleanup
- 0.3.3
* Tue May  6 2008 aj@suse.de
- Fix spec file for last change.
* Wed Apr 16 2008 dmacvicar@suse.de
- find yast pugins without requiring LD_LIBRARY_PATH
  (bnc #353405)
- require 'yast' is now require 'ycp'
- misc. fixes
- 0.3.2
* Thu Feb 21 2008 sh@suse.de
- Added new UI packages to Requires/BuildRequires in .spec file
- V 0.3.1
* Wed Feb 20 2008 coolo@suse.de
- fix against latest yast2-core
* Wed Sep 19 2007 dmacvicar@suse.de
- Lot of improvements, examples and
  support for the YaST UI
- 0.2.0
* Thu Aug  9 2007 dmacvicar@suse.de
- Fix build on 64 bits
- Use ruby vendor arch dir
* Mon Aug  6 2007 dmacvicar@suse.de
- Initial release 0.1.0
