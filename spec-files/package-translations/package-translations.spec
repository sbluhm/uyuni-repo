#
# spec file for package package-translations
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


Name:           package-translations
Version:        84.87.20200507.e55fbcdc
Release:        lp152.1.1
Summary:        Summary and Descriptions Translations
License:        BSD-3-Clause
Group:          System/GUI/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch
URL:            https://github.com/openSUSE/packages-i18n/

%define build_languages cs de es fr hu it ja lt nl nn ru uk zh_CN

%description 
This package provides translations for our packages. You don't want to install this
package on your system, it's only useful when you create openSUSE media.

%prep
%setup -q

%build

%install
target_dir=$RPM_BUILD_ROOT/usr/share/locale/en_US/LC_MESSAGES
mkdir -p $target_dir
for lang in %build_languages; do
  msgcat --use-first $lang/po/*.po | msgfmt -o $target_dir/package-translations-$lang.mo -
done

%files
%defattr(-,root,root)
%lang(en) /usr/share/locale/en_US/LC_MESSAGES/*

%changelog
* Thu May 28 2020 opensuse-packaging@opensuse.org
- Update to version 84.87.20200507.e55fbcdc:
  * Translations for openSUSE Leap 15.2 RC poo#61278
  * Translated using Weblate (Swedish)
  * Translated using Weblate (Russian)
  * Translated using Weblate (Portuguese (Brazil))
  * Translated using Weblate (Italian)
  * Translated using Weblate (German)
  * Translated using Weblate (Finnish)
  * Translated using Weblate (Danish)
  * Translated using Weblate (Chinese (China))
  * Translated using Weblate (Catalan)
  * Translated using Weblate (Arabic)
  * Translated using Weblate (German)
  * Translated using Weblate (Indonesian)
* Sat Mar 14 2020 opensuse-packaging@opensuse.org
- Update to version 84.87.20200314.d01661e1:
  * Bump urls for 15.2
  * Manually fix rpm-groups.pot
  * README.md: Document package update, improve format
  * README.md: Document standard use case
  * Added Occidental
  * Update translations.
* Mon May 13 2019 Karl Eichwalder <ke@suse.de>
- Update to version 84.87.20190506.9674f864:
  * Translated using Weblate (Slovak)
  * Translated using Weblate (Indonesian)
  * Translated using Weblate (Finnish)
  * update translations
* Mon May  6 2019 Karl Eichwalder <ke@suse.de>
- Update to version 84.87.20190504.098d3e84:
  * Add output of rpm groups
  * Add rpm-group POT file deduplication and merging
  * Apply provided patch in https://progress.opensuse.org/issues/25074
  * Translated using Weblate (Chinese (China))
  * Translated using Weblate (Finnish)
  * Translated using Weblate (German)
  * Translated using Weblate (Indonesian)
  * Translated using Weblate (Lithuanian)
  * Translated using Weblate (Swedish)
  * Update translations
* Thu Apr 11 2019 Karl Eichwalder <ke@suse.de>
- Update to version 84.87.20190409.959f468b:
  * Translated using Weblate (Chinese (Taiwan))
  * Translated using Weblate (Czech)
  * Translated using Weblate (German)
  * Translated using Weblate (Korean)
  * Translated using Weblate (Slovak)
  * Translated using Weblate (Swedish)
* Mon Mar 25 2019 Karl Eichwalder <ke@suse.de>
- Update to version 84.87.20190321.3eb73b8b:
  * Merge missing LCN translations for patterns
  * Add missing supported po files
  * Translated using Weblate (Catalan)
  * Translated using Weblate (Chinese (China))
  * Translated using Weblate (German)
  * Translated using Weblate (Italian)
  * Translated using Weblate (Spanish)
* Tue Feb 12 2019 opensuse-packaging@opensuse.org
- Update to version 84.87.20190212.03559d3a:
  * Fix more glitches
* Tue Feb 12 2019 ke@suse.com
- Update to version 84.87.20190212.57f204a5:
  * Translated using Weblate (Chinese (China))
  * Translated using Weblate (Czech)
  * Translated using Weblate (French)
  * Translated using Weblate (German)
  * Translated using Weblate (Hungarian)
  * Translated using Weblate (Polish)
  * Translated using Weblate (Spanish)
  * fix glitch
* Tue Feb 12 2019 ke@suse.com
- Update to version 84.87.20190208.4199a3f6:
  * Add 15.1 and non-oss repos
  * Added translation using Weblate (Chinese (Taiwan))
  * Added translation using Weblate (Kabyle)
  * Consistently use LF line ending
  * Fixed a typo fistChar --> firstChar
  * Translated using Weblate (Arabic)
  * Translated using Weblate (Catalan)
  * Translated using Weblate (Chinese (China))
  * Translated using Weblate (Chinese (Taiwan))
  * Translated using Weblate (Czech)
  * Translated using Weblate (Danish)
  * Translated using Weblate (Dutch)
  * Translated using Weblate (French)
  * Translated using Weblate (German)
  * Translated using Weblate (Hungarian)
  * Translated using Weblate (Italian)
  * Translated using Weblate (Japanese)
  * Translated using Weblate (Kabyle)
  * Translated using Weblate (Korean)
  * Translated using Weblate (Portuguese (Brazil))
  * Translated using Weblate (Russian)
  * Translated using Weblate (Spanish)
  * Update strings
* Mon May 14 2018 opensuse-packaging@opensuse.org
- Update to version 84.87.20180514.1ea260af:
  * Translated using Weblate (Catalan)
  * Translated using Weblate (Chinese (China))
  * Translated using Weblate (German)
  * Translated using Weblate (Italian)
  * Translated using Weblate (Lithuanian)
* Tue May  8 2018 opensuse-packaging@opensuse.org
- Update to version 84.87.20180507.1934f9b1:
  * Added translation using Weblate (Hindi)
  * Translated using Weblate (Dutch)
  * Translated using Weblate (French)
  * Translated using Weblate (German)
  * Translated using Weblate (Hindi)
  * Translated using Weblate (Italian)
  * Translated using Weblate (Portuguese (Brazil))
  * Translated using Weblate (Russian)
  * Translated using Weblate (Spanish)
  * weblate supplementary script update
* Tue Apr 24 2018 opensuse-packaging@opensuse.org
- Update to version 84.87.20180423.8e00def2:
  * Translated using Weblate (Arabic)
  * Translated using Weblate (Chinese (China))
  * Translated using Weblate (Czech)
  * Translated using Weblate (Dutch)
  * Translated using Weblate (French)
  * Translated using Weblate (German)
  * Translated using Weblate (Hungarian)
  * Translated using Weblate (Italian)
  * Translated using Weblate (Japanese)
  * Translated using Weblate (Polish)
  * Translated using Weblate (Portuguese (Brazil))
  * Translated using Weblate (Russian)
  * Translated using Weblate (Spanish)
* Mon Apr 16 2018 opensuse-packaging@opensuse.org
- Update to version 84.87.20180416.1a836422:
  * Adjust for Leap 15
- remove translate_packages.pl, no longer needed with product builder
* Wed Jul 19 2017 lnussel@suse.de
- Update to version 84.87.20170719.aabc165:
  * Added translation using Weblate (Catalan)
  * Translated using Weblate (Chinese (China))
  * Translated using Weblate (French)
  * Translated using Weblate (German)
  * Translated using Weblate (Indonesian)
  * Translated using Weblate (Italian)
  * Translated using Weblate (Japanese)
* Mon Jul 17 2017 lnussel@suse.de
- Update to version 84.87.20170717.198bd14:
  * Update package strings
  * Added translation using Weblate (Arabic)
  * Translated using Weblate (Arabic)
  * Translated using Weblate (German)
  * Translated using Weblate (Italian)
  * Translated using Weblate (Japanese)
  * Translated using Weblate (Portuguese (Brazil))
  * Translated using Weblate (Russian)
  * Translated using Weblate (Spanish)
  * Translated using Weblate (Ukrainian)
* Mon Jul 10 2017 lnussel@suse.de
- switch to using a _service file
- Update to version 84.87.20170709.7ea0b2c:
  * Translated using Weblate (German)
* Thu Apr 20 2017 alex239@gmail.com
- automated update on 2017-04-20
* Tue Nov  8 2016 alex239@gmail.com
- automated update on 2016-11-08
- added source service for OBS
* Sun Oct  2 2016 alex239@gmail.com
- automated update on 2016-10-02
* Thu Sep  1 2016 alex239@gmail.com
- automated update on 2016-09-01
* Thu Oct  8 2015 coolo@suse.com
- automated update on 2015-10-08
* Tue Oct 29 2013 coolo@suse.com
- manual update for 13.1
* Tue Jul  9 2013 coolo@suse.com
- automated update on 2013-07-09
* Fri Oct 28 2011 coolo@suse.com
- insert EULAs into the suse tags
* Thu Oct 27 2011 coolo@suse.com
- automated update on 2011-10-27
* Tue Oct 11 2011 coolo@suse.com
- update .changes file and skip non-existant changes
* Wed Aug 31 2011 coolo@suse.com
- update translations
* Fri May 27 2011 ke@suse.de
- Update translations.
* Sat May 29 2010 coolo@novell.com
- fix the PREPAPRE_PACKAGE script
* Fri May 28 2010 coolo@novell.com
- make sure we create utf-8 output
- update translations
* Wed Oct 28 2009 coolo@novell.com
- require perl-gettext
* Wed Oct 28 2009 coolo@novell.com
- fix build
* Mon Oct 26 2009 coolo@novell.com
- initial package
