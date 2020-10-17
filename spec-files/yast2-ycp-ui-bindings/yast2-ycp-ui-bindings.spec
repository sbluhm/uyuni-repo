#
# spec file for package yast2-ycp-ui-bindings
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


# YUIWidget_MenuBar
%define min_yui_version	3.11.0
%define yui_so		13

Name:           yast2-ycp-ui-bindings
Version:        4.3.2
Release:        1.3

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  yast2-devtools >= 3.1.10

# autodocs + docbook docs
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libxslt
BuildRequires:  sgml-skel

Requires:       yast2-core
BuildRequires:  yast2-core-devel

BuildRequires:  libyui-devel >= %min_yui_version
Requires:       libyui%yui_so >= %min_yui_version

# libyui ImplPtr
BuildRequires:  boost-devel

Summary:        YaST2 - YCP Bindings for the YaST2 User Interface Engine
License:        GPL-2.0-only
Group:          System/YaST

%description
This package makes the generic YaST2 user interface engine available
for YCP applications (YCP is the scripting language in which most YaST2
modules are written).

%package devel
Requires:       yast2-ycp-ui-bindings = %version

Summary:        YaST2 - YCP Bindings for the YaST2 User Interface Engine
Group:          Development/Libraries

Requires:       boost-devel
Requires:       glibc-devel
Requires:       libstdc++-devel
Requires:       libyui-devel >= %min_yui_version
Requires:       yast2-core-devel
Requires:       yast2-devtools

%description devel
This is the development package that makes the generic YaST2 user
interface engine available for YCP applications (YCP is the scripting
language in which most YaST2 modules are written).

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

mkdir -p "$RPM_BUILD_ROOT"%{yast_logdir}
%perl_process_packlist

%files
%defattr(-,root,root)

%dir %{_libdir}/YaST2
%dir %{yast_plugindir}

%{yast_plugindir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{yast_plugindir}/lib*.so
%{yast_plugindir}/lib*.la
%{yast_includedir}
%{_libdir}/pkgconfig/yast2-ycp-ui-bindings.pc
%doc %{yast_docdir}
%license COPYING

%changelog
* Wed Aug 12 2020 Stefan Hundhammer <shundhammer@suse.com>
- Use new syntax (MenuBar(), Menu()) in MenuBar example (bsc#1175115)
- 4.3.2
* Tue Aug 11 2020 Stefan Hundhammer <shundhammer@suse.com>
- Added MenuBar widget (bsc#1175115)
- Require libyui.so.13
- 4.3.1
* Thu Jun  4 2020 Stefan Hundhammer <shundhammer@suse.com>
- Added widget option autoWrap for label widget (bsc#1172513)
- Require libyui.so.12
- 4.3.0
* Thu Jan 23 2020 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Add support for the option to enable the online search
  feature in the package selector (jsc#SLE-9109).
- 4.2.9
* Thu Jan 23 2020 Stefan Hundhammer <shundhammer@suse.com>
- Allow integer as initial item status (part of bsc#1084674)
- 4.2.8
* Wed Dec 18 2019 aschnell@suse.com
- handle sort key in parser for table item (bsc#1140018)
- 4.2.7
* Thu Dec 12 2019 aschnell@suse.com
- require correct libyui so version 11 (bsc#1132247)
- 4.2.6
* Tue Nov 12 2019 Steffen Winterfeldt <snwint@suse.com>
- require correct libyui version (bsc#1153103)
- 4.2.5
* Thu Nov  7 2019 Stefan Hundhammer <shundhammer@suse.com>
- Support for CustomStatusItemSelector (bsc#1084674)
- 4.2.4
* Tue Sep 24 2019 Stefan Hundhammer <shundhammer@suse.com>
- Added example for icons in ItemSelector widget (bsc#1084674)
- 4.2.3
* Mon Sep 23 2019 Stefan Hundhammer <shundhammer@suse.com>
- Added ItemSelector widget (bsc#1084674)
- 4.2.2
* Fri Sep 13 2019 aschnell@suse.com
- added example using scrollbar positions of RichText widget with
  hyperlinks (bsc#1150498)
- 4.2.1
* Thu Sep 12 2019 aschnell@suse.com
- added example using scrollbar positions of RichText widget
  (bsc#1150498)
- 4.2.0
* Tue Oct 16 2018 schubi@suse.de
- Added license file to spec.
* Tue Oct  9 2018 snwint@suse.com
- increase version to correspond to the libyui version increase
  (related to bsc#991090)
- 4.1.0
* Mon Aug 20 2018 schubi@suse.de
- Switched license in spec file from SPDX2 to SPDX3 format.
* Wed Nov 15 2017 shundhammer@suse.de
- Fixed segfault when comparing YCPValueWidgetIDs with
  YStringWidgetIDs (fate#324098)
- 4.0.0
* Mon Apr 10 2017 jreidinger@suse.com
- added built-in SetApplicationTitle for setting application title
  (bnc#1033161)
- 3.2.0
* Wed Jul  8 2015 mvidner@suse.com
- Added OpenUI, CloseUI (boo#937026).
- 3.1.9
* Wed Jul  1 2015 jreidinger@suse.com
- added built-in SetApplicationIcon for setting application icon
  only (bnc#894220)
- 3.1.8
* Wed Feb 25 2015 gs@suse.de
- Enhance example DateField1.rb
- Add RELEASE-NOTES*.es.* files to examples (bnc#906936)
* Thu Apr 17 2014 jsrain@suse.cz
- Added built-in for setting wizard logo (bnc#868722)
- 3.1.7
* Wed Apr  9 2014 mvidner@suse.com
- Enable wizard title on the left instead of on top (bnc#868859)
- 3.1.6
* Wed Mar 12 2014 jsrain@suse.cz
- more relaxed typeinfo to avoid errors when calling the builtin
- 3.1.5
* Mon Dec  9 2013 lslezak@suse.cz
- added missing locale directory initialization, fixes missing
  translations in Gtk package manager (bnc#801311)
- 3.1.4
* Fri Dec  6 2013 jsrain@suse.cz
- added handling of release notes button (fate#314695)
- 3.1.3
* Thu Nov 14 2013 locilka@suse.com
- Removed warning if checking for TextMode. It became a standard
  check so no warning is necessary anymore.
- 3.1.2
* Mon Oct 14 2013 jreidinger@suse.com
- Fix query for special widget DateField and TimeField resulting
  in bad widget in GUI (BNC#845623)
- 3.1.1
* Thu Sep 19 2013 lslezak@suse.cz
- do not use *.spec.in template, use *.spec file with RPM macros
  instead
- 3.1.0
* Wed Jul 31 2013 yast-devel@opensuse.org
- converted from YCP to Ruby by YCP Killer
  (https://github.com/yast/ycp-killer)
- version 3.0.0
* Wed Jul 24 2013 jreidinger@suse.com
- fix calling SetFunctionKeys as overloaded function (gh#yast/ycp-killer#556)
- removed DemoBrowser.ycp and memtest.ycp examples (lslezak)
- adapt example to changes in NCTable (gs)
- 2.24.1
* Tue Jun 18 2013 jreidinger@suse.com
- fix overloaded method matching (BNC#825263)
- decrease log verbosity for cached component instances
- 2.24.0
* Tue Jun 18 2013 tgoettlicher@suse.de
- Fix for bnc#811842: segfault in ncurses because of
  uninitialized variable
* Tue May 14 2013 tgoettlicher@suse.de
- Fixed libyui dependency
- 2.21.8
* Tue Apr 30 2013 tgoettlicher@suse.de
- Adapted setting prog dir in libyui
- 2.21.7
* Wed Jan  9 2013 locilka@suse.com
- Added references to ButtonBox into the generated documentation
* Mon Nov 12 2012 tgoettlicher@suse.de
- confirmed license
- 2.21.6
* Mon Sep 17 2012 fehr@suse.de
- change Requires>=2.23 to Conflicts<2.23, to avoid build cycle
* Mon Aug  6 2012 tgoettlicher@suse.de
- adapt bindings to work with yast independed standalone libyui package
- 2.21.5
* Tue Jun 26 2012 aschnell@suse.de
- adapted to namespace changes in yast2-core
- 2.21.4
* Mon Mar 26 2012 jreidinger@suse.com
- removed libxcrypt-devel from buildrequires (aschnell)
- add more examples (gs)
-  2.21.3
* Wed Dec  7 2011 coolo@suse.com
- fix license to be in spdx.org format
* Fri Nov 25 2011 coolo@suse.com
- add libtool as buildrequire to avoid implicit dependency
* Tue Aug 16 2011 tgoettlicher@suse.de
- fixed bnc #711760: yast2 segfaults in second stage
- V 2.21.2
* Tue Apr 19 2011 tgoettlicher@suse.de
- version bump
- V 2.21.1
* Fri Apr 15 2011 tgoettlicher@suse.de
- Added support for recursive selection in tree widgets
- V 2.20.4
* Fri Feb 11 2011 tgoettlicher@suse.de
- fixed segfault when calling currentItem()
- V 2.20.3
* Tue Feb  8 2011 tgoettlicher@suse.de
- Added support for currentItem to tree widget
- V 2.20.2
* Sun Feb  6 2011 coolo@novell.com
- fix syntax error
* Fri Feb  4 2011 tgoettlicher@suse.de
- Fixed selection of check boxes in tree widgets (bnc #669138)
- V 2.20.1
* Thu Feb  3 2011 tgoettlicher@suse.de
- V 2.20.0
* Mon Dec 20 2010 tgoettlicher@suse.de
- Added support for check boxes in tree widgets
- V 2.19.1
* Wed Feb 10 2010 tgoettlicher@suse.de
- added license headers
* Wed Mar 11 2009 kmachalkova@suse.cz
- Do not abort in DumpWidgetTree function if there is no dialog
  on the stack (log warning instead)
- V 2.18.5
* Fri Mar  6 2009 tgoettlicher@suse.de
- Added context menus
- V 2.18.4
* Mon Feb  9 2009 sh@suse.de
- Require latest libyui in spec file (API change)
- V 2.18.3
* Wed Jan 14 2009 aschnell@suse.de
- added graph widget
- V 2.18.2
* Wed Oct 15 2008 sh@suse.de
- Added `opt(`confirmUnsupported) for PackageSelector widget
  (bnc #435479)
- V 2.17.11
* Thu Oct  9 2008 sh@suse.de
- Require latest libyui
- V 2.17.10
* Wed Oct  8 2008 sh@suse.de
- Export "y2debug" via UI::GetDisplayInfo()
* Tue Sep 30 2008 tgoettlicher@suse.de
- Added example: Wizard-SetDesktopTitle.ycp
* Fri Sep 26 2008 tgoettlicher@suse.de
- Fixed bnc #418443: Yast modules windows have no title
- V 2.17.8
* Thu Sep 25 2008 sh@suse.de
- Require latest libyui (API change!)
- V 2.17.7
* Wed Sep 17 2008 sh@suse.de
- Fixed segfault in SetLanguage() without optional encoding
* Fri Sep 12 2008 sh@suse.de
- Dropped obsolete widgetName()
- Require latest libyui
- v 2.17.6
* Thu Sep 11 2008 sh@suse.de
- Require latest libyui
- V 2.17.5
* Thu Sep  4 2008 sh@suse.de
- Added `opt(`relaxSanityCheck) for `ButtonBox (bnc #422612)
- V 2.17.4
* Thu Aug 21 2008 sh@suse.de
- Added support for new YButtonBox widget (fate #303446)
- V 2.17.3
* Tue Jul 15 2008 sh@suse.de
- Implemented fate #303492: Multi selection for table widget
- V 2.17.2
* Fri May 16 2008 sh@suse.de
- Handle nonexistent widgets in UI::SetFocus() more gracefully
  (bnc #389126)
- V 2.16.47
* Wed Apr 30 2008 lslezak@suse.cz
- added support for `repoMgr option in
  YCPDialogParser::parsePackageSelector() to make the repository
  management optional (bnc#381956)
- V 2.16.46
* Wed Apr 16 2008 sh@suse.de
- Let YDialog take care of deleting events
- V 2.16.45
* Mon Apr 14 2008 sh@suse.de
- Added `opt(`wizardDialog) to UI::OpenDialog():
  Open a dialog in YWizardDialog mode (if supported by UI)
- V 2.16.44
* Fri Apr 11 2008 sh@suse.de
- Reverted last changes - sub-wizards seem to be a dead end
- V 2.16.43
* Thu Apr 10 2008 sh@suse.de
- Added support for docked sub-wizards
- V 2.16.42
* Thu Apr  3 2008 sh@suse.de
- Added `opt(`helpButton) for PushButton widgets
- V 2.16.41
* Wed Mar 26 2008 sh@suse.de
- Added UI::TextMode() (bnc #222948)
- V 2.16.40
* Wed Mar 12 2008 mvidner@suse.cz
- build fix - prefix friendliness
* Fri Mar  7 2008 aschnell@suse.de
- include open info also of items in closed branches in OpenItems
* Wed Mar  5 2008 sh@suse.de
- Fixed bnc #365999: Shift-F7 affects only UI logging
- V 2.16.38
* Tue Mar  4 2008 sh@suse.de
- Conflict with yast2-core < 2.16.38 (before pkg split) (bnc #366873)
* Thu Feb 21 2008 sh@suse.de
- Package split off from yast2-core
- V 2.16.37
