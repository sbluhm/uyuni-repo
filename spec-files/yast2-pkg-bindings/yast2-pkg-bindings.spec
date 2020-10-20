#
# spec file for package yast2-pkg-bindings
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


Name:           yast2-pkg-bindings
Version:        4.3.0
Release:        1.2

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  libzypp-devel >= 14.29.0
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-devtools >= 3.1.10

Summary:        YaST2 - Package Manager Access
License:        GPL-2.0-only
Group:          System/YaST

%description
This package contains a name space for accessing the package manager
library in YaST2.

%prep
%setup -n %{name}-%{version}
# build only the library, ignore documentation (it is in devel-doc package)
echo "src" > SUBDIRS

%build
%yast_build

%install
%yast_install
rm -rf %{buildroot}/%{yast_plugindir}/libpy2Pkg.la
mv "$RPM_BUILD_ROOT"/usr/share/doc/packages/%{name} "$RPM_BUILD_ROOT"%{_docdir}

%files
%defattr(-,root,root)
%{yast_plugindir}/libpy2Pkg.so.*
%{yast_plugindir}/libpy2Pkg.so
%doc %{yast_docdir}
%license COPYING

%changelog
* Mon Aug 24 2020 Ladislav Slezák <lslezak@suse.cz>
- Improved Pkg::Resolvables() call to allow filtering by RPM
  dependencies (provides, obsoletes,...) (related to bsc#1175317)
- 4.3.0
* Wed Jul 22 2020 aschnell@suse.com
- Expand URL when libzypp expects an expanded URL. Fixes weird zypp
  repository name generated during installation. (bsc#1173509)
- 4.2.9
* Fri Jul 10 2020 aschnell@suse.com
- Extensions to handle raw repository name (bsc#1172477)
- 4.2.8
* Wed Feb 26 2020 Josef Reidinger <jreidinger@suse.com>
- Fix SourceRestore when some service is defined (bsc#1163081)
- 4.2.7
* Thu Feb 20 2020 Ladislav Slezák <lslezak@suse.cz>
- Removed obsolete zypp::target::rpm::ConvertDBReport callbacks,
  not used since SLE12 (by mlandres)
- Fixed Pkg.SourceRestore call to allow reading the stored
  repositories even after the initial installation repository has
  been added (bsc#1163081)
- 4.2.6
* Mon Jan 13 2020 Petr Pavlu <petr.pavlu@suse.com>
- Fix calculation of replaced products in Pkg.Resolvable2YCPMap()
  (bsc#1157202)
- 4.2.5
* Thu Dec 12 2019 Imobach Gonzalez Sosa <igonzalezsosa@suse.com>
- Include the "deps" resolvable property even when it is empty
  (bsc#1159120).
- 4.2.4
* Tue Dec  3 2019 Ladislav Slezák <lslezak@suse.cz>
- Fixed Pkg.Resolvables() to return the license text when requested
  (bsc#1158247)
- 4.2.3
* Wed Nov 13 2019 Ladislav Slezák <lslezak@suse.cz>
- Fixed Pkg.Resolvables() to properly filter by status
  (related to bsc#1132650)
- 4.2.2
* Tue Oct 29 2019 schubi@suse.de
- Returning raw packages dependencies while calling
  <Y2Packager::Resolvable>.deps (bsc#1132650).
- 4.2.1
* Thu May 23 2019 Ladislav Slezák <lslezak@suse.cz>
- Added Pkg.Resolvables() and Pkg.AnyResolvable() calls
  (related to bsc#1132650)
- 4.2.0
* Fri Mar  8 2019 mvidner@suse.com
- zypp::TriBool now needs an explicit cast to bool (bsc#1128364)
  (since boost-1.69.0)
- 4.1.2
* Thu Jan 10 2019 lslezak@suse.cz
- SourceFinishAll: drop the cached source manager to reload the
  repositories from disk, avoid restoring the removed repositories
  (bsc#1120568)
- 4.1.1
* Wed Oct 31 2018 jreidinger@suse.com
- Fix probing repository with URL including variable (bsc#1090193)
- 4.1.0
* Mon Oct 29 2018 jreidinger@suse.com
- Drop no longer used methods:
-- SetArchitecture and SystemArchitecture as only user Product
  Creator is dropped
-- AddLock, GetLocks, RemoveLock as it was needed only once for
  specific architecture that is no longer supported
-- TargetRebuildInit as recreating rpm database is no longer used
  during upgrade
-- TargetFileHasOwner as old workaround for upgrade no longer
  needed
-- TargetBlockSize as it is not longer needed to count disk usage
* Tue Oct 16 2018 schubi@suse.de
- Added license file to spec.
* Fri Aug 17 2018 schubi@suse.de
- Switched license in spec file from SPDX2 to SPDX3 format.
* Wed Jul  4 2018 schubi@suse.de
- SavePkgService: Checking if the service file still exists before
  updating it. Otherwise add the service instead of updating it.
  (bsc#1097756)
- 4.0.13
* Tue Jun 19 2018 lslezak@suse.cz
- Do not save plugin service to the target system, it is defined
  by a script (bsc#1094468)
- 4.0.12
* Mon Jun  4 2018 lslezak@suse.cz
- Fixed Pkg.TargetInitializeOptions() to not reset the source
  manager if also the options are the same as used previously
  (bsc#1095702)
- 4.0.11
* Wed May 16 2018 lslezak@suse.cz
- Ignore notification exception for failed plugin services,
  avoid errors when refreshing the zypp-plugin-spacewalk service
  on a system not managed by spacewalk (SUSE Manager)
  (bsc#1086768)
- 4.0.10
* Fri Feb 16 2018 jsrain@suse.cz
- always scan media for products to allow media identification
  (bsc#1080983)
- 4.0.9
* Mon Feb 12 2018 igonzalezsosa@suse.com
- Add a PrdLicenseLocales function to get the list of available
  license translations for a given product (related to
  FATE#322276).
- 4.0.8
* Wed Jan 31 2018 lslezak@suse.cz
- Added "transact_by" key to the PkgPropertiesAll call
  (improvement for bsc#1077882)
- 4.0.7
* Wed Jan 24 2018 lslezak@suse.cz
- Log more details in PkgQueryProvides call
  (related to bsc#1072634)
- 4.0.6
* Thu Dec  7 2017 lslezak@suse.cz
- Fixed Pkg.ExpandedUrl to return also the password part
  of the URL (bsc#1067007)
- 4.0.5
* Fri Oct 27 2017 lslezak@suse.cz
- Pkg.ResolvableProperties: return the "register_flavor" product
  property (related to bsc#896224)
- 4.0.4
* Tue Oct 24 2017 lslezak@suse.cz
- Report error when repository refresh fails during a service
  refresh (bsc#1064210)
- 4.0.3
* Mon Oct 23 2017 mvidner@suse.com
- Do not crash after a callback is set, unset, then called
  (bsc#1063459)
- 4.0.2
* Mon Sep 25 2017 igonzalezsosa@suse.com
- Add a CompareVersions function (related to fate#323273)
- 4.0.1
* Fri Sep 22 2017 lslezak@suse.cz
- Keep enabled recommended packages for the next solver runs
  when doing distribution upgrade (bsc#1059065)
- 4.0.0
* Wed Aug 23 2017 igonzalezsosa@suse.com
- Rename PrdMarkLicenseUnconfirmed to PrdMarkLicenseNotConfirmed
  (FATE#322276)
- 3.3.2
* Mon Aug 21 2017 igonzalezsosa@suse.com
- Add a Pkg.PrdHasLicenseConfirmed and
  Pkg.PrdMarkLicenseUnconfirmed (FATE#322276)
- Pkg.PrdGetLicenseToConfirm always returns the license, no matter
  whether is confirmed or not
- Add a second argument to Pkg.PrdGetLicenseToConfirm in order
  get the license translated to the given language
- 3.3.1
* Wed Aug 16 2017 igonzalezsosa@suse.com
- Add functions to handle product licenses (FATE#322276)
- 3.3.0
* Wed Jun 21 2017 lslezak@suse.cz
- Do not crash when the repository URL is not defined (bsc#1043218)
- 3.2.4
* Fri Jun  2 2017 igonzalezsosa@suse.com
- Fix pkgGpgCheck callback crashing when reporting SrcPackages
  (bsc#1037210) (by mlandres)
- 3.2.3
* Wed Mar 29 2017 lslezak@suse.cz
- Fixed failure when trying to save a plugin service (bsc#1021117)
- 3.2.2
* Wed Mar 29 2017 lslezak@suse.cz
- Return the repository signature flag status in the
  Pkg.SourceGeneralData call (might be used for bsc#1009127)
* Wed Oct 12 2016 lslezak@suse.cz
- Added Pkg.SourceSetPriority() to allow changing the priority
  also for the already loaded packages (bsc#498266)
- 3.2.1
* Fri Oct  7 2016 lslezak@suse.cz
- Added Pkg.UrlSchemeIs*() methods for classifying the URL scheme
  to avoid duplication of the libzypp code in YaST (bsc#948982)
- 3.2.0
* Wed Apr  6 2016 schubi@suse.de
- Added new call: ServiceForceRefresh
  (bnc#967828)
- 3.1.34
* Tue Mar 29 2016 igonzalezsosa@suse.com
- Add a Pkg::ProvidePackage to retrieve a package using
  PackageProvider (fate#319716).
- 3.1.33
* Mon Feb 15 2016 igonzalezsosa@suse.com
- Expose update notifications through PkgFunctions::CommitHelper
- 3.1.32
* Thu Oct  8 2015 igonzalezsosa@suse.com
- Add pkgGpgCheck callback (bsc#948608)
- 3.1.31
* Mon Oct  5 2015 ancor@suse.com
- Added Pkg::SourceRawURL() and Pkg:ExpandedUrl() to deal with
  repositories including repo variables (bnc#944505)
- 3.1.30
* Thu Aug 27 2015 lslezak@suse.cz
- Pkg::SourceGeneralData() - return also the raw URL (without
  expanding the variables), needed for bsc#941563
- 3.1.29
* Thu Aug 20 2015 lslezak@suse.cz
- return the "product_line" product attribute, needed for reading
  an optional OEM release type (bsc#941402)
- 3.1.28
* Fri Jul 10 2015 lslezak@suse.cz
- Pkg.SetSolverFlags(): added DUP mode solver settings, these are
  different that the "normal" mode settings (FATE319128)
- 3.1.27
* Thu Jul  2 2015 lslezak@suse.cz
- added "allowVendorChange" option to Pkg.SetSolverFlags() to
  allow configuring the vendor change flag (FATE#319138)
- 3.1.26
* Fri Jun 19 2015 lslezak@suse.cz
- fixed saving removed services (needed for FATE#315161)
- 3.1.25
* Wed Jun 10 2015 lslezak@suse.cz
- added support for the file conflicts callbacks (bnc#923590)
- 3.1.24
* Tue Mar 31 2015 lslezak@suse.cz
- Pkg::ResolvableProperties(): "version" value contains a full
  edition (in form "[epoch:]version[-release]"), additionaly return
  also "version_epoch", "version_version" and "version_release"
  with the parts of the edition (needed for FATE#318505)
- 3.1.23
* Wed Mar  4 2015 lslezak@suse.cz
- removed obsolete patch callbacks
- 3.1.22
* Fri Feb  6 2015 lslezak@suse.cz
- Pkg::RepositoryAdd: use alias from URL query parameter if present
  (bnc#892431)
- 3.1.21
* Wed Sep 24 2014 schubi@suse.de
- Added onsystem_by_user flag in Pkg.PkgProperties and
  Pkg.ResolvableProperties
- Fixed PkgPropertiesAll. It returns only package information about
  the package which is defined in the parameters. In former versions
  the given package name has not been regarded and the properties
  of ALL packages have been returned, which has been wrong.
  (needed for bnc#897404)
- 3.1.20
* Tue Sep 16 2014 lslezak@suse.cz
- SetTargetDU(): added new options ("growonly" and "filesystem")
  to better handle Btrfs snapshots in disk usage counting
  (part of bnc#896176)
- 3.1.19
* Tue Sep  9 2014 lslezak@suse.cz
- do not hide libzypp exceptions in Pkg::ResolvableProperties()
  call, it makes debugging more difficult, return nil in that case
  (bnc#895418)
- 3.1.18
* Tue Aug 19 2014 lslezak@suse.cz
- explicitly include <ostream> to avoid possible compile failures
  (bnc#891676)
- 3.1.17
* Tue Aug 19 2014 lslezak@suse.cz
- fixed passing an invalid repository ID in GPG key import callback
  (bnc#891389)
- 3.1.16
* Tue Jun 10 2014 lslezak@suse.cz
- fixed ServiceRefresh to not add duplicated repositories (that
  confuses package installation progress during installation)
  (bnc#865037)
- 3.1.15
* Thu Jun  5 2014 lslezak@suse.cz
- added Pkg::TargetInitializeOptions(), allows overriding the
  target distribution autodetection (bnc#881320)
- 3.1.14
* Wed Jun  4 2014 lslezak@suse.cz
- do not log false warning message about missing base product
  when it is actually found (bnc#876677#c14)
- 3.1.13
* Tue May 27 2014 lslezak@suse.cz
- move package cache to target system (copy RPMs to /mnt instead of
  inst-sys (RAM-disk) during installation to avoid freezing the
  installer when installing big packages with small RAM)
  (bnc#877859)
- 3.1.12
* Tue May 20 2014 jreidinger@suse.com
- another fix for repeated service save problem (bnc#876134)
- 3.1.11
* Fri May  9 2014 lslezak@suse.cz
- fixed saving service to installed system (bnc#877053)
- 3.1.10
* Tue Apr 22 2014 lslezak@suse.cz
- remeber the base product NVRA (instead of the zypp product
  reference which might be invalidated) to properly create the
  /etc/products.d/baseproduct symlink (bnc#873885)
- 3.1.9
* Tue Apr 15 2014 lslezak@suse.cz
- fixed repeated service save problem (bnc#873198, bnc#873683#c7)
- 3.1.8
* Wed Apr  2 2014 lslezak@suse.cz
- properly initialize "autorefresh_skipped" attribute (leaving it
  uninitialized might have strange effects sometimes)
- 3.1.7
* Fri Mar  7 2014 lslezak@suse.cz
- add "eol" flag to product data to report "End Of Life" product
  date (FATE#316172)
- 3.1.6
* Fri Feb 14 2014 lslezak@suse.cz
- Pkg::ServiceRefresh() - download metadata for added repositories
- 3.1.5
* Thu Feb 13 2014 lslezak@suse.cz
- Pkg::ServiceRefresh() - add, refresh and load also the new added
  repositories from the service
- 3.1.4
* Fri Jan 10 2014 lslezak@suse.cz
- zypp::filesystem::TmpDir::defaultLocation() already contains
  /var/tmp/ prefix, do not use it it twice (bnc#847794)
- 3.1.3
* Wed Dec 18 2013 lslezak@suse.cz
- eliminate deprecated zypp::DiskUsage class (bnc#852943)
  (by mlandres)
- 3.1.2
* Mon Sep 30 2013 lslezak@suse.cz
- do not use *.spec.in template, use *.spec file with RPM macros
  instead
- 3.1.0
* Mon Sep 30 2013 lslezak@suse.cz
- evaluate DonePackage callback (to close the package installation
  progress popup) when package installation is finished
  (bnc#842465)
- 3.0.3
* Mon Sep  9 2013 lslezak@suse.cz
- do not abort if package installation fails, always ask user
  (evaluate the callback), libzypp no longer uses 3 installation
  attempts (fixes openqa failures when btrfs is used)
- 3.0.2
* Fri Sep  6 2013 lslezak@suse.cz
- use a single RepoManager instance to avoid repository metadata
  removal (bnc#802665#c27)
- 3.0.1
* Tue Jul 30 2013 yast-devel@opensuse.org
- version 3.0.0
* Fri Jun 14 2013 lslezak@suse.cz
- removed obsolete BuildRequires (blocxx, libgcrypt, doxygen,
  perl-XML-Writer)
* Wed May 22 2013 lslezak@suse.cz
- removed logging from finishParameters() function
- 2.24.0
* Wed May 15 2013 ma@suse.de
- No longer use deprecated zypp API methods.
* Mon Jan 28 2013 lslezak@suse.cz
- fixed documentation build (bnc#800692)
- 2.23.1
* Mon Dec 10 2012 jsuchome@suse.cz
- showing patch contents (packages with their versions) as part
  of ResolvableProperties call
- 2.23.0
* Wed Apr 11 2012 lslezak@suse.cz
- 2.22.2
* Wed Apr 11 2012 tgoettlicher@suse.de
- license update: GPL-2.0
  Numerous GPL-2.0 files in the package (see e.g. src/Arch.cc)
* Tue Mar 27 2012 lslezak@suse.cz
- removed libxcrypt-devel from buildrequires (aschnell)
- dropped build support for openSUSE-11.x
- 2.22.1
* Thu Mar  8 2012 lslezak@suse.cz
- added Pkg::ResolvableUpdate() to avoid downgrading resolvables
  (bnc#751147)
* Tue Jan  3 2012 lslezak@suse.cz
- check if downloading optional file really succeeded (bnc#736693)
  (fixes HA add-on installation)
* Fri Dec  9 2011 lslezak@suse.cz
- fixed downloading optional files - pass the optional flag to
  libzypp to skip media change callback for optional files
  (bnc#735340)
* Tue Dec  6 2011 lslezak@suse.cz
- fixed reloading of repositories which have been removed during
  service reload (bnc#724449)
- 2.22.0
* Fri Nov 25 2011 coolo@suse.com
- add libtool as buildrequire to avoid implicit dependency
* Fri Oct  7 2011 lslezak@suse.cz
- solver reset - reset also the distupgrade solver flag
  (bnc#709480)
- 2.21.11
* Fri Sep 23 2011 lslezak@suse.cz
- removed obsoleted selection related functions:
  Pkg::GetSelections(), Pkg::GetPatterns(), Pkg::SelectionData(),
  Pkg::SelectionContent(), Pkg::SetSelection(),
  Pkg::ClearSelection(), Pkg::ActivateSelections()
- removed obsoleted Pkg::TargetLogfile(), Pkg::TargetProducts(),
  Pkg::LastErrorId(), Pkg::Init(), Pkg::SourceSetRamCache(),
  Pkg::InstSysMode(), Pkg::SourceProduct(), Pkg::CallbackYou*(),
  Pkg::SourceCleanupBroken(), Pkg::SourceGetBrokenSources(),
  Pkg::SourceProvideDir(), Pkg::CallbackAcceptNonTrustedGpgKey(),
  Pkg::PkgAnyToDelete(), Pkg::PkgAnyToInstall(),
  Pkg::SourceFinish(), Pkg::GetLocale(), Pkg::SetLocale() functions
- 2.21.10
* Thu Sep 22 2011 lslezak@suse.cz
- use signed type for RepoId, fixes returning 2^32 - 1 instead of
  - 1 on i586 (bnc#718514)
- code cleanup - removed obsoleted unused functions:
  Pkg::SourceSaveRanks(), Pkg::SourceInstallOrder(), Pkg::You*(),
  Pkg::PkgFreshen(), Pkg::PkgEstablish(), Pkg::PatternData()
* Wed Aug 10 2011 lslezak@suse.cz
- Pkg::SourceStartManager() - always display progress, do not
  assume that any repository present cannot trigger refresh,
  that's false if the previous refresh failed and causes crash
  (bnc#711182)
- 2.21.9
* Fri Aug  5 2011 lslezak@suse.cz
- 2.21.8
* Thu Aug  4 2011 lslezak@suse.cz
- added Pkg::SetZConfig() to change some libzypp options at runtime
  e.g. prefer CD/DVD to dowload during installation/update
  (bnc#693230)
* Tue Aug  2 2011 lslezak@suse.cz
- set ignoreAlreadyRecommended solver flag by default - make the
  YaST package management compatible with zypper (bnc#668588)
- 2.21.7
* Mon Aug  1 2011 lslezak@suse.cz
- Pkg::SourceFinishAll() - remove upgrading repositories from the
  solver, fixes solver crash when called later (bnc#709494)
- 2.21.6
* Wed Jul 27 2011 lslezak@suse.cz
- Pkg::ResolvableProperties() supports source packages
  (`srcpackage) resolvables
- 2.21.5
* Mon Jun 27 2011 lslezak@suse.cz
- ignore deleted repositories when checking uniqueness of an alias
  (bnc#702399)
- 2.21.4
* Thu Jun 23 2011 lslezak@suse.cz
- fixed aborting autorefresh (bnc#691828)
- 2.21.3
* Wed Jun 22 2011 lslezak@suse.cz
- 2.21.2
* Tue Jun 21 2011 lslezak@suse.cz
- added Pkg::Add/RemoveUpgradeRepo() and Pkg::GetUpgradeRepos()
  (fate#311994)
* Tue Jun 14 2011 lslezak@suse.cz
- added Pkg::CommitPolicy()
- support for download in advance mode in yast2-wagon (fate#308951)
- Pkg::ResolvableProperties() - return "product_package" value
  for available products (fate#310730)
- 2.21.1
* Tue Apr  5 2011 lslezak@suse.cz
- do not refresh empty repositories, remember loaded status
  (bnc#665488)
- added Pkg::Commit() function which accepts commit options map
  (with download_mode, dry_run... options) (FATE#308951)
- added Pkg::ZConfig() function returning current libzypp config
  (FATE#308951)
- 2.21.0
* Tue Nov  2 2010 lslezak@suse.cz
- updated StartPackage callback - added the package name to the
  arguments (file location is not enough, it's too dificult to get
  just the name from it in YCP)
- 2.20.3
* Mon Oct 25 2010 lslezak@suse.cz
- ignore just the failed repository during autorefresh, load the
  other repositories (bnc#620895)
- put a backtrace to y2log when an unhandled excecptinon is caught
  in the global catch section for easy debugging
- 2.20.2
* Thu Sep 30 2010 lslezak@suse.cz
- don't use spaces in repo alias (bnc#596950)
- 2.20.1
* Thu Sep 30 2010 lslezak@suse.cz
- don't preselect locked patches (bnc#627316)
- 2.20.0
* Wed Apr 21 2010 lslezak@suse.cz
- reload services rnd epositories after service refresh to avoid
  overwriting the updated files (bnc#581766)
- 2.19.1
* Mon Jan 18 2010 lslezak@suse.cz
- Pkg::ResolvableProperties() - return 'product' value from
  <upgrade> section (bnc#571621)
* Wed Jan  6 2010 lslezak@suse.cz
- Pkg::ResolvableProperties() - always return "transact_by" flag,
  Pkg::PkgApplReset() - do not reset "transact_by" flag for
  non-transacting resolvables (bnc#450786, bnc#471340)
- 2.19.0
* Thu Dec  3 2009 lslezak@suse.cz
- return more details when a service refresh fails (bnc#558049)
* Tue Dec  1 2009 lslezak@suse.cz
- Pkg::ResolvableProperties() - return product file and it's
  upgrades section for `product resolvables (bnc#559554)
* Tue Nov 24 2009 lslezak@suse.cz
- use zypp::Url::schemeIsRemote() instead of the hardcoded protocol
  list (bnc#551661)
* Fri Oct 16 2009 lslezak@suse.cz
- added "check_alias" option to Pkg::RepositoryAdd() to allow
  repository overwriting (bnc#543468)
- 2.18.11
* Fri Sep 18 2009 ma@suse.de
- Remove connection to dead zypp::ScanDBReport.
- 2.18.10
* Sun Jul 19 2009 coolo@novell.com
- revert file list changes that slipped in while adding licenses
* Fri Jul 10 2009 lslezak@suse.cz
- clean existing cache for added repositories, do not reuse
  existing aliases for new repositories, make the new aliases
  really unique (bnc#519218, bnc#327490)
- 2.18.9
* Wed Jul  8 2009 ma@suse.de
- Remove references to deprecated UpgradeStatistics.
- 2.18.8
* Tue Jun 16 2009 lslezak@suse.cz
- Do not call RefreshStarted callback when refresh is not needed,
  do not change "Abort" button label when not necessary
  (bnc#504131)
- 2.18.7
* Thu Jun  4 2009 ma@suse.de
- Remove more use of deprecated methods.
- 2.18.6
* Wed May 27 2009 ma@suse.de
- Remove use of deprecated Package::filenames.
- 2.18.5
* Wed Apr 29 2009 lslezak@suse.cz
- report also the URL when repository metadata are not found
  (bnc#439069)
- 2.18.4
* Tue Apr 21 2009 lslezak@suse.cz
- Pkg::ResolvableDependencies() - also return raw (unresolved)
  dependencies in the result (key "deps"), remove duplicated
  dependencies in the result (bnc#479575)
* Mon Mar 30 2009 lslezak@suse.cz
- return "is_update_repo" flag in Pkg::SourceGeneralData() call
  (requires loaded pool) (bnc#459527)
- use zypp::RepoManager::makeStupidAlias() for generating
  repository alias
- 2.18.3
* Wed Mar 25 2009 lslezak@suse.cz
- Fixed Pkg::SourceURL() - remove "credentials" query from URL
  after obtaining the credentials from CredentialManager
* Fri Mar 20 2009 lslezak@suse.cz
- Fixed Pkg::SourceURL() - read username and password using
  CredentialManager (FATE#303652)
* Fri Feb 20 2009 ma@suse.de
- Removed fragile test for service being modified. Leave it up to libzypp
  to decide wich actions must be performed when saving a service. (bnc#476418)
* Wed Jan 28 2009 lslezak@suse.cz
- Fixed Pkg::SetSolverFlags() function - properly set
  "ignoreAlreadyRecommended" flag, do not select extra packages for
  installation (bnc#470185)
- 2.18.2
* Mon Jan 26 2009 lslezak@suse.cz
- implemented RemoveResolvableReport::problem() callback, do not
  abort when [Ignore] is pressed (bnc#465641)
* Fri Jan 16 2009 lslezak@suse.cz
- 2.18.1
* Thu Jan 15 2009 lslezak@suse.cz
- disk usage: do not remove the leading slash in the path
  (bnc#222967)
* Tue Jan 13 2009 lslezak@suse.cz
- 2.18.0
* Tue Jan  6 2009 lslezak@suse.cz
- Translate the help texts displayed when loading/saving the
  package manager (bnc#446054)
- Copy the global and user's credentials (user names and passwords)
  to the target system (bnc#460970)
* Mon Dec 22 2008 lslezak@suse.cz
- call the refresh callbacks only when there is something to
  refresh (bnc#441512)
* Mon Dec 15 2008 lslezak@suse.cz
- Pkg::SetSolverFlags() - support for "reset" key in the map
  for resetting the solver and the fixsystem mode (bnc#439373)
- 2.17.32
* Fri Dec  5 2008 lslezak@suse.cz
- 2.17.31
* Thu Dec  4 2008 lslezak@suse.cz
- Pkg::Solve() replaced by Pkg::GetSolverFlags() and
  Pkg::SetSolverFlags() (bnc#450528)
* Wed Dec  3 2008 lslezak@suse.cz
- added Pkg::Solve() function which allows to set
  ignoreAlreadyRecommended solver flag so Yast does not install
  extra packages (bnc#445476)
- 2.17.30
* Thu Nov 27 2008 lslezak@suse.cz
- honor the download area when downloading signed/digested files
  (do not download the files to the RAM disk during installation),
  remove the downloaded files in Pkg::SourceReleaseAll() to
  release not needed files (bnc#449564)
- 2.17.29
* Fri Nov 21 2008 lslezak@suse.cz
- set the optional flag when downloading signed/digested files
  (bnc#447010)
- 2.17.28
* Wed Nov 12 2008 lslezak@suse.cz
- get/set "keeppackages" repository property in
  Pkg::SourceEditSet(), Pkg::SourceEditGet() and
  Pkg::SourceGeneralData() builtins (bnc#441328, bnc#402617)
- 2.17.27
* Mon Nov 10 2008 lslezak@suse.cz
- moved asYCPList() to ycpTools.h
- 2.17.26
* Fri Nov  7 2008 lslezak@suse.cz
- Pkg::SourceProvideSignedFile() has been renamed to
  Pkg::SourceProvideDigestedFile(), added new
  Pkg::SourceProvideSignedFile() to dowload signed files (like
  "/content") (bnc#409927)
- 2.17.25
* Fri Nov  7 2008 lslezak@suse.cz
- Pkg::SourceProvideSignedFile() - the path may be relative,
  it's changed to absolute automatically (bnc#409927)
- Pkg::SourceProbe() - do not log the password in the URL
  (bnc#441944)
- 2.17.24
* Fri Nov  7 2008 lslezak@suse.cz
- fixed network detection - removed unreliable IPv6 network test
  (bnc#439068)
- 2.17.23
* Thu Nov  6 2008 lslezak@suse.cz
- return more data (URL lists) in Pkg::SourceProductData()
  (bnc#441917)
- 2.17.22
* Mon Nov  3 2008 lslezak@suse.cz
- use AutoIndexes zypp::Fetcher feature, fixed signed file
  downloading (bnc#409927)
* Fri Oct 31 2008 lslezak@suse.cz
- Pkg::ResolvableProperties() - return correct status for selected
  patterns (bnc#440611)
* Thu Oct 23 2008 lslezak@suse.cz
- added Pkg::SourceProvideSignedFile() function for downloading
  a single signed file (bnc#409927)
* Tue Oct 21 2008 lslezak@suse.cz
- fixed ResolvableProperties() - correctly iterate over all
  available/installed objects (bnc#436842)
- added Pkg::CreateSolverTestcase() debugging function to create
  a solver testcase from YCP code
- 2.17.21
* Fri Oct 17 2008 lslezak@suse.cz
- ServiceGet()/ServiceSet() - query/set ReposToEnable and
  ReposToDisable (bnc#435669)
- added ServiceSave() function (bnc#435669)
- fixed ServiceDelete() - delete also the repositories belonging
  to the deleted service, similar fix in enabling/disabling
  a service via ServiceSet() (bnc#435711)
- fixed network detection command (bnc#435970)
- 2.17.20
* Wed Oct 15 2008 lslezak@suse.cz
- report SourceChanged callback also during package installation
  (bnc#362003)
- 2.17.19
* Thu Oct  9 2008 lslezak@suse.cz
- do not print anything on the stdout when detecting network
  status (bnc#433458)
- 2.17.18
* Fri Oct  3 2008 lslezak@suse.cz
- fixed Pkg::PkgReset() - reset the status (instead of unselect)
  (bnc#431565)
- service handling related fixes (bnc#427728)
- 2.17.17
* Thu Oct  2 2008 lslezak@suse.cz
- removed Pkg::ServicesSave(), Pkg::ServicesLoad() and
  Pkg::ServicesReset() - the functionality has been moved to
  Pkg::SourceSaveAll(), Pkg::SourceRestore() and
  Pkg::SourceFinishAll(). The reason is to descrease the amount
  exported functions and lower the required changes in YCP code.
* Wed Oct  1 2008 lslezak@suse.cz
- fixed Pkg::ServiceRefresh() - search for the service URL and pass
  it to libzypp
* Mon Sep 29 2008 lslezak@suse.cz
- do not autorefresh remote repositories when there is no network
  connection (affected calls Pkg::SourceLoad(),
  Pkg::SourceStartManager() and PkgFunctions::SourceStartCache())
  (bnc#401966)
- ResolvableProperties() - return more info about product
  ("register_target", "register_release" and "flavor" keys)
- 2.17.16
* Thu Sep 25 2008 lslezak@suse.cz
- removed another usage of the old logging (bnc#429954)
- 2.17.15
* Thu Sep 25 2008 lslezak@suse.cz
- Pkg::TargetLogfile() is obsoleted, the log file is now entirely
  handled by libzypp. The function does nothing now. (bnc#429954)
  See also http://en.opensuse.org/Libzypp/Package_History
- 2.17.14
* Thu Sep 25 2008 lslezak@suse.cz
- added Pkg::SourceProvideSignedDirectory() to check the signatures
  of the downloaded files (bnc#409927)
- 2.17.13
* Wed Sep 24 2008 lslezak@suse.cz
- create the base product symlink in Pkg::PkgCommit() (bnc#413444)
* Wed Sep 24 2008 ma@suse.de
- fixed retrieval of product data (bnc #429067)
* Wed Sep 24 2008 lslezak@suse.cz
- adapted GPG key callbacks - report also the affected repository
  (bnc#370223)
* Fri Sep 19 2008 lslezak@suse.cz
- added Pkg::ServiceProbe() function for probing service type
  (or for checking if there is a service at all) (bnc#427728)
- use Product::isTargetDistribution() to mark the base product
  (bnc#413444)
* Thu Sep 18 2008 lslezak@suse.cz
- improved callback evaluation - evaluate the callbacks even when
  the change is smaller than 5%% but at least 3 seconds have elapsed
  since the last evaluation, makes better response on slow
  connections (bnc#402593)
* Fri Sep 12 2008 ma@suse.de
- Provide product url lists for registration and smolt.
- 2.17.12
* Wed Sep 10 2008 lslezak@suse.cz
- merged proofread texts (2008-09-08)
- 2.17.11
* Mon Sep  8 2008 lslezak@suse.cz
- added Pkg::ServiceURL() (get a full URL of a service)
- return "service" property of a repository (if it is a part of a
  service)
- 2.17.10
* Thu Sep  4 2008 lslezak@suse.cz
- added support for services, new functions: Pkg::ServiceAliases(),
  Pkg::ServiceAdd() Pkg::ServiceDelete(), Pkg::ServiceGet(),
  Pkg::ServiceSet(), Pkg::ServicesSave(), Pkg::ServicesLoad(),
  Pkg::ServiceRefresh(), Pkg::ServicesReset()
- 2.17.9
* Thu Aug 21 2008 lslezak@suse.cz
- 2.17.8
* Wed Aug 20 2008 lslezak@suse.cz
- added support for zypp::Patch::reloginSuggested() flag
  (Pkg::ResolvableProperties() returns "relogin_need" value for
  patches, Pkg::ResolvableCountPatches() and
  Pkg::ResolvablePreselectPatches() accept `relogin_needed flag)
  (fate#304889)
- use zypp::ui::Selectable object instead of direct access to the
  resolvable pool (bnc#413150)
- return replaced products - "replaces" key in Product properties
  (Pkg::ResolvableProperties()) (fate#301997)
* Tue Aug 12 2008 lslezak@suse.cz
- Fixed pattern status returned by Pkg::ResolvableProperties()
  (pattern was never in state `installed)
- 2.17.7
* Mon Aug 11 2008 lslezak@suse.cz
- added Pkg::SourceForceRefreshNow() - unconditional refresh of
  a selected repository
- 2.17.6
* Thu Aug  7 2008 ma@suse.de
- Adapt to new product handling.
- 2.17.5
* Tue Aug  5 2008 lslezak@suse.cz
- fixed searching for the candidate package - prefer better
  architecture to better version (bnc#413150)
- 2.17.4
* Wed Jul 30 2008 lslezak@suse.cz
- Pkg::Connect() - set LastError() (bnc#280537)
* Wed Jul 30 2008 lslezak@suse.cz
- allow priority >99 in Pkg::SourceSet() (bnc#402135)
* Wed Jul 23 2008 ma@suse.de
- Remove references to obsolete freshens dependencies.
- 2.17.3
* Tue Jul 22 2008 coolo@suse.de
- 2.17.2 (for add-on)
* Thu Jul 17 2008 ma@suse.de
- Remove obsolete references to Script/Message/Atom
* Fri Jun 27 2008 lslezak@suse.cz
- Fixed Pkg::GetPackages(`available) to ignore installed packages
* Fri Jun 27 2008 lslezak@suse.cz
- support for patch messages and patch scripts (bnc#401220)
- 2.17.1
* Tue Jun 17 2008 lslezak@suse.cz
- do not save sources in Pkg::SourceFinishAll() (use
  Pkg::SourceSaveAll() for that), just clean the known repositories
  and allow new source initialization (bnc#395738)
- 2.17.0
* Mon Jun 16 2008 lslezak@suse.cz
- added architecture related functions, needed for fate#301883
  (Pkg::GetArchitecture(), Pkg::SetArchitecture() and
  Pkg::SystemArchitecture())
* Fri Jun 13 2008 lslezak@suse.cz
- removed targetFinish() call in the destructor, it's not needed
  anymore (bnc#381917)
* Thu Jun 12 2008 lslezak@suse.cz
- Fixed tag in the help text (bnc#386076)
* Thu May 29 2008 lslezak@suse.cz
- set the prefix for package cache (do not download packages to
  the current directory) (bnc#394728)
- 2.16.39
* Fri May 23 2008 dmacvicar@suse.de
- fix patch pre-selection
- 2.16.38
* Fri May 23 2008 lslezak@suse.cz
- do not keep downloaded packages by default (bnc#393709)
- 2.16.37
* Wed May 21 2008 lslezak@suse.cz
- fixed name of a key in patch property map to the previous used
  value ("is_broken" back to "is_needed") (bnc#392999)
- 2.16.36
* Wed May 14 2008 lslezak@suse.cz
- fixed evaluation of RemovePkgReceive::start() callback
- changed signature Pkg::RemoveLock(map<string,any>) to
  Pkg::RemoveLock(integer) - that is more error proof
- Pkg::AddLock() - do not save the current config, just merge
  the added lock to the read locks
- documented lock API
- 2.16.35
* Mon May 12 2008 lslezak@suse.cz
- fixed type info (Pkg::RemoveLock())
- 2.16.34
* Mon May 12 2008 lslezak@suse.cz
- added Pkg::AddLock(), Pkg::GetLocks() and Pkg::RemoveLock()
  for manipulating libzypp locks, required to lock 64-bit packages
  on PPC32 during installation (bnc#336678)
  Note: locks are loaded in Pkg::TargetInit(), explicitly saved in
  Pkg::TargetFinish() (implicit loading is in Pkg::PkgSolve(),
  implicit saving in Pkg::PkgCommit())
- 2.16.33
* Fri May  2 2008 lslezak@suse.cz
- pass requested product in the media change callback (bnc#330094,
  comment #10)
- 2.16.32
* Mon Apr 28 2008 lslezak@suse.cz
- RepositoryAdd() - added "priority" key (bnc#381360)
- ResolvableProperties() - return "order" property of pattern
  (bnc#255726)
- 2.16.31
* Tue Apr 22 2008 lslezak@suse.cz
- return dependency kind in Pkg::ResolvableDependencies()
  (bnc#381340)
- 2.16.30
* Fri Apr 18 2008 lslezak@suse.cz
- added Pkg::PkgMediaPackageSizes() to speed up computing
  the download size of the selected packages
- added Pkg::TargetRebuildInit(string root) function which rebuilds
  the RPM DB ('rpm --rebuilddb') before initializing the target
  (bnc#308352)
- 2.16.29
* Thu Apr 17 2008 schubi@suse.de
- do not iterate over the repo's if the target does not exist.
  bnc #380656
* Wed Apr 16 2008 coolo@suse.de
- do not y2error on std:string
* Wed Apr 16 2008 coolo@suse.de
- catching errors - programming defensive (bnc#380283)
- 2.16.28
* Wed Apr 16 2008 lslezak@suse.cz
- searchPackage - use isSystem() property instead of searching
  in repositories (bnc#380141, comment 5)
* Tue Apr 15 2008 lslezak@suse.cz
- added support for `languages in ResolvableProperties()
- set the default RPM log file name in Pkg::PkgCommit() if it
  hasn't been set (bnc#372863)
- 2.16.27
* Fri Apr 11 2008 ma@suse.de
- Fix TargetProducts to return the satisfies products. Is satisfied
  status is computed and updated on each solver run. So it does not
  reflect any changes made since the last solver run. (bnc#368104)
- 2.16.26
* Fri Apr 11 2008 lslezak@suse.cz
- fixed evaluation of StartProvide callback
- fixed logging
- improved remote source detection
- 2.16.25
* Tue Apr  8 2008 lslezak@suse.cz
- return -1 when Pkg::SourceCreate() with non-empty product
  directory fails (bnc#377962)
- fixed handling of 'nil' value in callback registration functions
  (unregistration now works correctly)
- 2.16.24
* Thu Apr  3 2008 coolo@suse.de
- adapt to libzypp 4.7
* Wed Apr  2 2008 lslezak@suse.cz
- changed callback registration - use references to functions
  instead of strings, this enables compile time type checking
  (fate#302296)
- 2.16.23
* Fri Mar 28 2008 lslezak@suse.cz
- Pkg:ResolvableProperties() - added "transact_by" key for selected
  packages
* Thu Mar 27 2008 lslezak@suse.cz
- added priority support - implemented Pkg::SourceLowerPriority(),
  Pkg::SourceRaisePriority(), added "priority" key in
  Pkg::SourceEditSet(), Pkg::SourceEditGet() and
  Pkg::SourceGeneralData() (bnc#369827)
- 2.16.22
* Tue Mar 25 2008 lslezak@suse.cz
- added Pkg::ResolvableInstallRepo() function - install an object
  from the specified repository
- 2.16.21
* Mon Mar 24 2008 coolo@suse.de
- adapt to libzypp 4.6
* Fri Mar 21 2008 lslezak@suse.cz
- media change callback - added error code parameter (bnc#328822)
- 2.16.20
* Mon Mar 17 2008 ma@suse.de
- Remove outdated/obsolete references to zypp
* Fri Mar 14 2008 lslezak@suse.cz
- support for ejecting specified CD/DVD device, handle multiple
  devices (fate#120298)
- 2.6.19
* Wed Mar 12 2008 jkupec@suse.cz
- updated MediaChange callback (fate #120298)
- 2.16.18
* Tue Mar 11 2008 lslezak@suse.cz
- updated ProgressDownload callback - pass the current and the
  average download rate (bnc#168935)
- 2.16.17
* Wed Mar  5 2008 coolo@suse.de
- reduce build requires
* Wed Mar  5 2008 lslezak@suse.cz
- added Pkg::CallbackStartRefresh() and Pkg::CallbackDoneRefresh()
  callbacks, added Pkg::SkipRefresh() call to abort and skip
  running source refresh (FATE #30962, bnc #231745)
- use zypp::sat::WhatProvides instead of obsoleted byCapability
  iterators
- 2.16.16
* Wed Feb 27 2008 lslezak@suse.cz
- update - 'keep_intalled_patches' and 'delete_unmaintained' options
  were removed from the libzypp API
- 2.16.15
* Fri Feb 22 2008 lslezak@suse.cz
- Pkg::ResolvablePreselectPatches(): Properly select patches for
  installation - check only the latest version of a patch (#355509)
- 2.16.14
* Mon Feb 18 2008 lslezak@suse.cz
- don't use deprecated libzypp API (use byIdent iterators,
  sat pool, ZConfig)
* Fri Feb 15 2008 coolo@suse.de
- port to new libzypp (based on satsolver)
- 2.16.13
* Thu Jan 24 2008 lslezak@suse.cz
- Pkg::TargetInit(), Pkg::TargetLoad(), Pkg::SourceStartManager(),
  Pkg::SourceStartCache() - don't display callbacks for repeated
  calls (avoids flashing windows with no action)
- 2.16.12
* Thu Jan 17 2008 lslezak@suse.cz
- GPG key callbacks - pass a map with key information in one
  parameter (instead of 2 or 3 parameters), the map contains more
  information (see FATE 300754)
- fixed documentaion of the changed callbacks
- 2.16.11
* Tue Jan 15 2008 lslezak@suse.cz
- Pkg::ImportGPGKey() return boolean (true on success) instead of
  void
* Mon Jan 14 2008 lslezak@suse.cz
- 2.16.10
* Thu Jan 10 2008 lslezak@suse.cz
- added Pkg::CheckGPGKeyFile() function - check whether the file
  contains a valid GPG key
* Mon Jan  7 2008 lslezak@suse.cz
- added missing "log.h" file in Makefile.am
- added GPG key management functions (FATE 300754):
  Pkg::GPGKeys() - get list of the known or trusted GPG keys
  Pkg::DeleteGPGKey() - delete the GPG key from the known or
  trusted keyring
- 2.16.9
* Fri Jan  4 2008 lslezak@suse.cz
- the functionality from PkgModuleFunctions has been moved to
  PkgFunctions to reduce compile dependency, removed unnecessary
  [#]includes
- implemented Pkg::SaveState() and Pkg::RestoreState() (#104579)
  (Pkg::ClearSaveState() is empty, there is only one saved state
  instance which cannot be removed)
- 2.16.8
* Tue Dec 18 2007 lslezak@suse.cz
- use ResPool::repository_iterator for searching resolvables from
  a repository (much faster than iterating over all resolvables)
- added RepoCont and RepoId typedefs to hide implementation
  details and to make the code more understandable
- 2.16.7
* Wed Dec 12 2007 lslezak@suse.cz
- added total progress to Pkg::SourceRefreshNow()
- added total progress to Pkg::SourceSaveAll()
- improved source loading progress - change the total progress
  in parallel to the subprogress
- PkgProgress - don't evaluate the callbacks when the progress
  is not enabled (started)
- added total progress to Pkg::SourceCreate()
- merged Pkg::SourceCreate() and Pkg::SourceScan() code
- added help texts to total progresses
- added POTFILES (to read texts from src/HelpTexts.h)
- 2.16.6
* Fri Dec  7 2007 lslezak@suse.cz
- added Process callbacks for handling multistage progress
- some source files have been split to smaller parts
- added total progress to source and target initialization
- 2.16.5
* Wed Nov 21 2007 lslezak@suse.cz
- Pkg::SourceCreate(): return -1 instead of 4294967295 when
  a non-existing dir:// repository is used (#342242)
* Tue Nov 20 2007 lslezak@suse.cz
- use the correct directory when probing a repository with
  non empty product directory (#341617)
- Pkg::ResolvableProperties() - return download and install size
  of packages (#331538), return status "removed" when the
  resolvable is marked for removal
- use component "Pkg" in y2log
- 2.16.4
* Thu Nov 15 2007 lslezak@suse.cz
- remove temporary files /var/tmp/zypp-xmlstore-*-script-* at
  the end: correctly call the destructor at the end, call
  finishTarget() and release the zypp pointer (#228176)
- 2.16.3
* Thu Nov  8 2007 lslezak@suse.cz
- fixed PkgTaboo() and PkgNeutral() - set all available instaces
  of the package (from all reposiories) (#297083)
- fixed PkgDelete() - mark all installed instances for removal
- 2.16.2
* Thu Oct 11 2007 lslezak@suse.cz
- fixed Pkg::SourceLoad() - don't load resolvables from
  repositories deleted by Pkg::SourceDelete()
- 2.16.1
* Mon Sep 24 2007 lslezak@suse.cz
- set path to metadata files when registering a new repository,
  required to set the media verifier correctly (#293428)
- 2.15.51
* Mon Sep 24 2007 lslezak@suse.cz
- search the correct package instance in license bindings
  (Pkg::PkgGetLicenseToConfirm(), Pkg::PkgGetLicensesToConfirm()
  and Pkg::PkgMarkLicenseConfirmed()) - fixes the double license
  confirmation bug (#326277)
- 2.15.50
* Mon Sep  3 2007 lslezak@suse.cz
- reimplemented media redirection in media change callback
  (#294481)
- 2.15.49
* Fri Aug 31 2007 lslezak@suse.cz
- fixed inverted result of PkgAvailable() and PkgInstalled()
- 2.15.48
* Thu Aug 30 2007 lslezak@suse.cz
- don't log debug messages from zypp if debug logging is turned off
  (#306458)
- preliminary fix for source redirection (compile fix only)
  (#294481)
- report errors when adding a new repository (#306272)
- added new builtins PkgAvailable() and PkgInstalled() which work
  with package names (in contrast to IsAvailable() or IsProvided()
  which work with 'provides' property) (#299683,#302246)
- 2.15.47
* Wed Aug 29 2007 lslezak@suse.cz
- reimplemented Pkg::SourceCacheCopyTo() - copy zypp cache from the
  installation system to the target (#304310)
- 2.15.46
* Thu Aug 23 2007 lslezak@suse.cz
- Pkg::SourceLoad() - load resolvables from all working
  repositories even when some of them fails (#302432)
- Pkg::PkgMediaNames() - return repository names instead of
  product names (#304152)
- 2.15.45
* Mon Aug 20 2007 lslezak@suse.cz
- Pkg::SourceLoad() (and related) - do not refresh already loaded
  repositories (#300891)
- 2.15.44
* Wed Aug 15 2007 lslezak@suse.cz
- return history of exceptions in Pkg::LastError() result (#299716)
- Pkg::SourceCreate() - use the last path component from URL as
  name (#299816)
- Pkg::SourceCreate() - disable autorefresh for CD/DVD repositories
  (#300928)
- 2.15.43
* Thu Aug  9 2007 lslezak@suse.cz
- Pkg::SourceScan(), Pkg::SourceCreate() - use product name or URL
  as alias and name, don't use timestamp (#298723)
- create a shorter version of the URL if it is used as alias or
  name (avoid too long aliases/names)
- Pkg::SourceLoad() - do not load already loaded resolvables
- 2.15.42
* Mon Aug  6 2007 lslezak@suse.cz
- mount repositories in readonly mode (FATE #302347)
- fixed Pkg::RepositoryProbe() - now it accepts two arguments
  (URL and product directory)
- Pkg::ResolvableProperties() - returns type of product (key "TYPE"
  in SUSEtags content file)
- 2.15.41
* Fri Aug  3 2007 lslezak@suse.cz
- added product directory support
- Pkg::ResolvableProperties() returns license and status if
  available
- fixed id of undefined repository (-1 returned as unsigned)
- 2.15.40
* Thu Aug  2 2007 lslezak@suse.cz
- added Pkg::CallbackInitDownload() and Pkg::CallbackDestDownload()
  for registering the initial and the final even when downloading
  a file (to leave the progress popup open and avoid flashing)
- call the new callbacks when scanning, probing, refreshing
  and downloading a file or directory
- Pkg::SourceSaveAll() - remove also raw metadata cache for the
  removed repositories
- ignore errors in the download callback when probing or scanning
  a repository (the downloaded files are optional)
- Pkg::SourceProvideDir() - return the correct value
- 2.15.39
* Wed Aug  1 2007 lslezak@suse.cz
- Pkg::SourceProvideDir() is non-recursive now (backward comaptible
  behavior)
- added Pkg::SourceProvideDirectory() -- optional and/or recursive
  directory download from a repository (required for FATE #302018)
- internal support for Pkg functions with 5 arguments
- 2.15.38
* Tue Jul 31 2007 lslezak@suse.cz
- Pkg::SourceChangeUrl() adapted to the latest libzypp
- implemented Pkg::SourceMoveDownloadArea()
* Tue Jul 31 2007 lslezak@suse.cz
- Pkg::SourceGetCurrent() - return correct IDs (fixed nasty off
  by one bug) (#295901)
- 2.15.37
* Mon Jul 30 2007 lslezak@suse.cz
- download missing metadata before building the cache (required
  for repositories added in offline mode)
- 2.15.36
* Fri Jul 27 2007 lslezak@suse.cz
- support for "raw" Progress callbacks
- 2.15.35
* Thu Jul 26 2007 lslezak@suse.cz
- created yast2-pkg-bindings-devel-doc subpackage with the
  autogenerated documentation (FATE #302461)
- 2.15.34
* Wed Jul 25 2007 lslezak@suse.cz
- more efficient PkgDU() - obtain the current partitioning directly
  from libzypp, do not compute complete disk usage just to get it
- 2.15.33
* Mon Jul 23 2007 lslezak@suse.cz
- added RepositoryAdd(), RepositoryScan() and RepositoryProbe()
- 2.15.32
* Wed Jul 18 2007 lslezak@suse.cz
- SourceLoad(), SourceRefreshNow() - rebuild cache after
  refreshing metadata
- SourceEditGet/Set() - do not change alias, use name instead
  (alias cannot be changed from yast now)
- SourceGeneralData() - return also "name" key
- 2.15.31
* Mon Jul 16 2007 lslezak@suse.cz
- SourceMediaData() - report all base urls (key "base_urls" in the
  result)
- report media number and source ID in the SourceChange() callback
- fixed crash in the Media Change callback (empty baseUrls)
- SourceDelete() - remove resolvables from the pool
- SourceSetEnabled() - load/remove resolvables from the pool
- PkgCommit() - release all sources
- SourceReleaseAll() - return success flag
- reimplemented SourceMediaData() - dropped "media_id" and
  "media_vendor" tags from the result map, now it requires loaded
  resolvables in the pool to get number of the media
- 2.15.30
* Fri Jul 13 2007 lslezak@suse.cz
- convert source ID in source callbacks (pass PkgModuleFunctions
  reference to the callback handler to search the ID)
- tribool fixes (enabled() and autorefresh() return tribool)
- reimplemented PkgMediaSizes() and PkgMediaCount() functions,
  the installation slideshow is now fully working
- 2.15.29
* Fri Jul 13 2007 lslezak@suse.cz
- fixed segfault in logFindRepository() when the repo is not found
- removed extra callbacks in SourceRestore() and SourceLoad()
- SourceLoad() - do not reload the repositories if there is
  at least one repository already registered
- 2.15.28
* Thu Jul 12 2007 lslezak@suse.cz
- handle zypp::ProgressReport callbacks (added new Pkg::
  functions: CallbackProgressReportStart(), CallbackProgress-
  - ReportProgress() and CallbackProgressReportEnd())
- add 'deleted' flag to YRepo, handle deleted repos correctly
- SourceSaveAll() - don't remove all repos, remove the cache when
  removing a repo
- SourceLoad() - build repo cache if it's missing
- 2.15.27
* Wed Jul 11 2007 jkupec@suse.cz
- storing YRepo_Ptr instead of YRepo in the vector
- modified logFindRepository() to retrun YRepo_Ptr
  check its return value:
    if (!returnvalue) found = false;
- reimplemented SourceCallbacks
- FIXED if repo.baseUrlsBegin() is repo.baseUrlsEnd() then do not
  read the value at the iterator (segfault)
- added logFindAlias() for searching an alias in the known repos
- reimplemented PkgMediaNames()
- SourceCreateType() - convert type from Yast string to libzypp string
- 2.15.26
* Wed Jul 11 2007 jkupec@suse.cz
- YRepo structure added to encapsulate RepoInfo, MediaSetAccess, and
  original alias of a repository.
- fixed SourceProvide* methods
- replaced RepoInfo vector with YRepo vector
* Tue Jul 10 2007 jkupec@suse.cz
- added repomedias - vector of MediaSetAccess objects
- SourceProvide*File methods reimplemented with passed
  MediaSetAccess object
- added internal method CreateRepoManager() - create RepoManager
  object with the cofigured target root directory (all pkg-bindings
  functions must use it to use the correct root directory!)
- implemented TargetDisableSources()
- implemented SourceFinishAll()
- SourceReleaseAll() reimplemented
- implemented SourceSaveAll()
- fixed SourceProvideOptionalFile()
- store the new values in SourceSetEnabled(), SourceSetAutorefresh(),
  SourceEditSet()
- 2.15.25
* Tue Jul 10 2007 jkupec@suse.cz
- ReleaseAllSources() has an empty implementation as it is
  (hopefuly) not needed anymore.
- SourceChangeUrl() cleaned-up
- 2.15.24
* Tue Jul 10 2007 jkupec@suse.cz
- SourceProvideFile, SourceProvideOptionalFile, and SourceProvideDir
  reimplemented.
* Mon Jul  9 2007 lslezak@suse.cz
- use RepoInfo objects for representing sources
- implemented SourceCreate()
- SourceEditSet() - do not save changes
- 2.15.23
* Mon Jul  9 2007 lslezak@suse.cz
- compile fixes
- 2.15.22
* Wed Jul  4 2007 lslezak@suse.cz
- The first step to the new libzypp API (RepoManager) - too many
  missing code but it can be at least compiled...
- 2.15.21
* Tue May 29 2007 lslezak@suse.cz
- updated GPG callbacks (#277117)
- 2.15.20
* Thu May 17 2007 lslezak@suse.cz
- Evaluate start/finish callbacks in Pkg::SourceRestore() and
  Pkg::SourceLoad() only when needed (removed the flashing popup
  effect during installation)
- Log not applicable patches to y2log
- 2.15.19
* Mon May 14 2007 lslezak@suse.cz
- Pkg::TargetAvailable() returns -1 instead of uninitialized value
  if an error occurs (#245734)
- 2.15.18
* Fri May 11 2007 lslezak@suse.cz
- log result of statvfs() call to debug #245734
- 2.15.17
* Wed Apr 25 2007 lslezak@suse.cz
- added Pkg::SourceGetBrokenSources() - return list of broken
  sources (initialization has failed) (#265579)
- 2.15.16
* Tue Apr 10 2007 lslezak@suse.cz
- create and register AuthReceive callback object (required
  for Pkg::CallbackAuthentication())
- 2.15.15
* Fri Apr  6 2007 lslezak@suse.cz
- added Pkg::CallbackAuthentication() - handle AuthenticationReport
  callback (#190609)
- 2.15.14
* Mon Apr  2 2007 lslezak@suse.cz
- new callbacks Pkg::CallbackSourceCreateInit/Destroy() and
  Pkg::CallbackSourceReportInit() - handle the ctor/dtor of libzypp
  callbacks (#251726)
- 2.15.13
* Wed Feb 21 2007 lslezak@suse.cz
- display redirected URL instead of the original URL in the media
  change popup (#157040)
- Pkg::SourceEditSet/Get can retrieve and set alias of a source
  (#228978)
- 2.15.12
* Thu Feb 15 2007 lslezak@suse.cz
- Pkg::PkgUpdateAll() - pass all parameters in a map (more general
  solution for future enhancements)
- 2.15.11
* Thu Feb 15 2007 lslezak@suse.cz
- register ScanDB callbacks (RPM DB reading) (#219953)
- additional parameters for Pkg::PkgUpdateAll() - silent_downgrades
  and keep_installed_patches (#238488)
- 2.15.10
* Wed Feb 14 2007 lslezak@suse.cz
- added option `any to Pkg::IsAnyResolvable()
- 2.15.9
* Wed Feb 14 2007 lslezak@suse.cz
- added Pkg::IsAnyResolvable() — is there any resolvable
  in the requried state? (#243568), Pkg::PkgAnyToInstall()
  and Pkg::PkgAnyToDelete() are obsoleted now
- 2.15.8
* Mon Feb 12 2007 lslezak@suse.cz
- added Pkg::CallbackAcceptNonTrustedGpgKey() - register callback
  askUserToAcceptUnknownKey() in libzypp (#242087, #240771)
- 2.15.7
* Wed Feb  7 2007 lslezak@suse.cz
- pass value of ProgressPackage() callback to libzypp when
  a package is removed (#226041)
- do not change the alias of the added source if it is not empty
  (do not replace the product name with a time stamp) (#220195)
- 2.15.6
* Mon Feb  5 2007 lslezak@suse.cz
- Pkg::SourceSetEnabled() - refresh resolvables in the pool after
  enabling/disabling a source (#187352), Pkg::SourceEditSet()
  - doc update, log a warning when changing state of a source
- 2.15.5
* Thu Jan 25 2007 lslezak@suse.cz
- new binding Pkg::PkgDU() - computes disk usage of the package
  in the current partitinoning (#222556)
- new binding Pkg::TargetAvailable() - returns non-root free
  disk space (#237309)
- 2.15.4
* Thu Jan 18 2007 lslezak@suse.cz
- Pkg::SetLocale() and Pkg::GetLocale() have been split into
  Pkg::SetTextLocale(), Pkg::GetTextLocale(),
  Pkg::SetPackageLocale() and Pkg::GetPackageLocale() to set
  the textdomain and the language packages independently (#223624)
- 2.15.3
* Mon Jan  8 2007 lslezak@suse.cz
- Pkg::GetPackages supports `taboo and `locked options,
  Pkg::ResolvableProperties returns "locked" value
  (required for #232506)
- 2.15.2
* Mon Dec 11 2006 lslezak@suse.cz
- Pkg:PkgMediaCount() - correctly report number of packages from
  a YUM source (#220242)
- 2.15.1
* Wed Nov 29 2006 lslezak@suse.cz
- removed undefined methods, removed obsoleted callbacks
- 2.15.0
* Wed Nov 22 2006 lslezak@suse.cz
- provide installation summary about packages from a YUM
  source (medium number is 0) (#220242)
- 2.14.4
* Mon Nov 20 2006 lslezak@suse.cz
- fixed SourceStartManager(): load sources even if some source
  could not have been restored (#221071)
- 2.14.3
* Thu Nov 16 2006 lslezak@suse.cz
- translate the messages: redefine _ gettext macro to use
  "pkg-bindings" text domain (the definition from libzypp uses
  "zypp" textdomain) (#219783)
- 2.14.2
* Wed Nov 15 2006 lslezak@suse.cz
- fixed GPG key callbacks - allow yast to import keys (#219965)
- 2.14.1
* Mon Nov 13 2006 lslezak@suse.cz
- disable refresh of all sources in the target during update
  (workaround for #220056)
- 2.14.0
* Mon Nov 13 2006 lslezak@suse.cz
- fixed Pkg::DoRemoveAllKind() - uninstall only the installed
  resolvables
* Mon Nov 13 2006 lslezak@suse.cz
- added Pkg::SourceCreateType() builtin (#168358)
* Mon Nov 13 2006 lslezak@suse.cz
- added Pkg::TargetStoreRemove() builtin (#210552)
* Thu Nov  9 2006 lslezak@suse.cz
- decreased the timout of acquiring the zypp lock to 15 seconds
  (#216615)
- 2.13.105
* Tue Nov  7 2006 lslezak@suse.cz
- disable the source if the metadata file is corrupt (#217276)
- 2.13.104
* Fri Nov  3 2006 lslezak@suse.cz
- do not search a product in mediaRequest callback, the source
  might not be initialized (#214886)
- 2.13.103
* Tue Oct 31 2006 lslezak@suse.cz
- fixed PkgTaboo() built-in - set lock on the USER level (#186205)
- 2.13.102
* Mon Oct 30 2006 lslezak@suse.cz
- return OPTIONALURLS and EXTRAURLS properties of a Product
  resolvable (#213031)
- ResolvableProperties() supports resolvable type `language
- 2.13.101
* Fri Oct 20 2006 lslezak@suse.cz
- added missing YCP callback evaluation (#213628)
- DoneProvide callback - pass file name argument,
  handle Ignore return value (#200084)
- log a warning when an obsoleted YOU callback is registered
- 2.13.100
* Fri Oct 13 2006 lslezak@suse.cz
- fixed SourceProductData() binding (#201742)
- require libzypp >= 2.4.0
- 2.13.99
* Fri Oct 13 2006 lslezak@suse.cz
- added script callbacks (feature #100233)
* Fri Oct 13 2006 lslezak@suse.cz
- Fixed callback prototypes (revealed by -Woverloaded-virtual)
- 2.13.98
* Thu Oct 12 2006 mvidner@suse.cz
- Use -Woverloaded-virtual to warn about mis-overriden callbacks
* Thu Oct 12 2006 lslezak@suse.cz
- fixed media change callback signature to match zypp library
  (#210208)
- 2.13.97
* Thu Sep 28 2006 schubi@suse.de
- patch autoselect: select only the latest needed patch if
  patches are needed with the same name and different editions.
  Bug: 206927
* Fri Sep 22 2006 lslezak@suse.cz
- added missing download callback handlers (lost during
  implementation of feature #1466)
- 2.13.96
* Mon Sep 18 2006 lslezak@suse.cz
- new source callbacks (feature #1466), require libzypp >= 2.1.0
- 2.13.95
* Wed Aug 30 2006 lslezak@suse.cz
- synced to the new zypp API (keyring, callbacks)
- require libzypp >= 2.0.0 (#202397)
- 2.13.94
* Mon Aug 21 2006 lslezak@suse.cz
- new bindings SourceRestore() and SourceLoad() (#199738)
- TargetInitDU([]) sets the current disk usage (#197497)
- 2.13.93
* Tue Aug 15 2006 lslezak@suse.cz
- 2.13.92
* Fri Aug 11 2006 lslezak@suse.cz
- new finish callbacks: Callback{Delta,Patch}Finish*()
* Thu Aug 10 2006 lslezak@suse.cz
- new callbacks: CallbackSourceCreate*() functions
* Wed Aug  9 2006 jsrain@suse.cz
- let TargetProducts return more data (#66046)
* Wed Aug  9 2006 lslezak@suse.cz
- built-in ResolvableInstallArch() has been changed to
  ResolvableInstallArchVersion() - set architecture and version of
  the installed resolvable (#186912)
* Tue Aug  8 2006 lslezak@suse.cz
- new callbacks: patch and delta file progress
* Tue Aug  8 2006 jsrain@suse.cz
- let PkgCommit return more data about remaining resolvables
  (#186912)
* Mon Aug  7 2006 dmacvicar@suse.de
- use the new initializeTarget method for TargetInitialize
- require zypp version 2.0.0
* Mon Aug  7 2006 lslezak@suse.cz
- new built-in ResolvableInstallArch() - select architecture of
  the installed resolvable (#186912)
* Mon Aug  7 2006 dmacvicar@suse.de
- add TargetInitialize, TargetLoad, deprecate TargetInit.
- port TargetProduct to new zypp api
- 2.13.91
* Thu Aug  3 2006 mvidner@suse.cz
- Fixed makefiles for make 3.81
- 2.13.90
* Thu Jul 13 2006 lslezak@suse.cz
- new binding Pkg::ResolvableCountPatches() - count available
  patches which can be installed
- 2.13.89
* Thu Jun 29 2006 lslezak@suse.cz
- ResolvableProperties(): return "is_needed" property of a patch
  (#188541)
- 2.13.88
* Mon Jun 26 2006 mvidner@suse.cz
- Fixed links in the docs (locilka)
- 2.13.87
* Wed Jun 21 2006 mvidner@suse.cz
- Added Pkg::SourceURL that includes the password (#186842).
- 2.13.86
* Fri Jun  9 2006 jsrain@suse.cz
- report also type of resolvable not installed during 1st stage
  (#181198)
- 2.13.85
* Thu Jun  8 2006 lslezak@suse.cz
- fixed SetLocale() - do not reset additional locales (#172223)
- catch all uncaught exceptions on the global level (prevents
  from crashing yast)
- 2.13.84
* Thu Jun  8 2006 jsrain@suse.cz
- fixed reseting SW selection (#177469)
* Thu Jun  8 2006 lslezak@suse.cz
- fixed the crash when yast is running as non-root user - catch
  an exception in SourceStartCache() (#182390)
* Tue Jun  6 2006 lslezak@suse.cz
- added new callback bindings (CallbackProgressSourceRefresh(),
  CallbackAcceptWrongDigest(), CallbackAcceptUnknownDigest())
- 2.13.83
* Mon Jun  5 2006 lslezak@suse.cz
- updated documentation - descriptions of the functions,
  added obsoleted/don't use notes
- 2.13.82
* Thu Jun  1 2006 lslezak@suse.cz
- get source ID by numericId() call (do not search in all available
  sources) (#179410, #163609)
- 2.13.81
* Thu May 25 2006 mvidner@suse.cz
- Added SourceSaveAll which always saves and does not disable (#176013).
- 2.13.80
* Mon May 22 2006 lslezak@suse.cz
- Pkg::DoProvide - select only the newest item for installation,
  remove the flag from other versions (#176854)
- 2.13.79
* Mon May 22 2006 jsrain@suse.cz
- added PkgApplReset builtin (#176788)
- 2.13.78
* Fri May 19 2006 lslezak@suse.cz
- ignore installed selections in Pkg::GetSelections() when asking
  for available selections (#170537), the same fix has been
  implemented also in Pkg::GetPatterns()
- 2.13.77
* Thu May 18 2006 mvidner@suse.cz
- Say also the URL of a failed source in SourceStartManager (#175153).
- 2.13.76
* Wed May 17 2006 jsrain@suse.cz
- one more fix of reseting resolvable status (#175451)
* Tue May 16 2006 ma@suse.de
- Adapt to libzypp-1.0.0
- 2.13.75
* Tue May 16 2006 mvidner@suse.cz
- SourceDelete: no need to remove resolvables from pool if the source
  has not seen any resolvables yet. Fixes deleting corrupt sources
  (#174840).
- 2.13.74
* Tue May 16 2006 jsrain@suse.cz
- fixed resetting resolvable status (#175711, #175451)
- 2.13.73
* Fri May 12 2006 lslezak@suse.cz
- PkgMediaSizes, PkgMediaCount: don't count packages with
  mediaId == 0, array index was -1 in this case (#174841)
- 2.13.72
* Wed May 10 2006 lslezak@suse.cz
- ResolvableProperties: don't add empty product description
  (#148625)
- 2.13.71
* Tue May  9 2006 visnov@suse.cz
- Do not try to evaluate the same callback twice, the parameters
  are discarded after the first call (#173291)
- 2.13.70
* Tue May  9 2006 mvidner@suse.cz
- When creating a source, prefer an alias that may be passed as a
  query parameter of the URL.
  This is an adaptation for the new output of suseRegister-1.0-59,
  ensuring proper synchronization of YaST and Zenworks for enterprise
  updates (#158850#c17).
- 2.13.69
* Fri Apr 28 2006 lslezak@suse.cz
- fixed reset in PkgReset() and in ResolvableNeutral() builtin
  (#170643)
- 2.13.68
* Wed Apr 26 2006 lslezak@suse.cz
- use other valid sources when a broken source is found (#168632)
- 2.13.67
* Tue Apr 25 2006 lslezak@suse.cz
- updated callback handlers (#168060)
- 2.13.66
* Mon Apr 24 2006 lslezak@suse.cz
- select language packages in SetLocale(), handle the main locale
  when processing additional locales (#162064)
- 2.13.65
* Fri Apr 21 2006 jsrain@suse.de
- SourceCreateBase (#160585)
- 2.13.64
* Fri Apr 21 2006 lslezak@suse.cz
- Pkg::ResolvableNeutral() - added force argument (#168278)
- 2.13.63
* Thu Apr 20 2006 lslezak@suse.cz
- fixed logging
- 2.13.62
* Wed Apr 19 2006 jsrain@suse.de
- fixed building
- 2.13.61
* Wed Apr 19 2006 visnov@suse.cz
- ignore finish with errors in DonePackage callback to be retried (#161298)
- 2.13.60
* Fri Apr 14 2006 visnov@suse.cz
- Adapt for new digest callbacks in ZYPP
- 2.13.59
* Thu Apr 13 2006 lslezak@suse.cz
- Pkg::ResolvableProperties - return patch specific values
* Thu Apr 13 2006 lslezak@suse.cz
- fixed disk usage counting - non-root dirs should not contain
  / at the beginning (#163199)
- updated Pkg::ResolvablePreselectPatches - return number of
  patches, added 'kind' argument (#165540)
- new binding Pkg::CallbackAcceptFileWithoutChecksum() (#165125)
- 2.13.58
* Mon Apr 10 2006 jsrain@suse.de
- call PkgRefresh when added or enabled a source (#156980)
- 2.13.57
* Mon Apr 10 2006 visnov@suse.cz
- Modified PkgMediaNames to return also the installation source
  ID (#161298)
- 2.13.56
* Mon Apr 10 2006 mvidner@suse.cz
- Added update_urls to Pkg::ResolvableProperties (#163192).
- 2.13.55
* Mon Apr 10 2006 visnov@suse.cz
- fix ImportGPGKey
- 2.13.54
* Fri Apr  7 2006 jsrain@suse.de
- let product provide short_name via ResolvableProperties (#163702)
* Thu Apr  6 2006 visnov@suse.cz
- fix build
- 2.13.52
* Thu Apr  6 2006 visnov@suse.cz
- invoke SourceChange callback (#161298)
- 2.13.51
* Thu Apr  6 2006 jsrain@suse.de
- fixed YCP signature of Pkg::SourceCleanupBroken
- 2.13.50
* Thu Apr  6 2006 kkaempf@suse.de
- more debug for DoProvideNameKind()
* Thu Apr  6 2006 schubi@suse.de
- Bug 162745 - Updating from beta8 does not update the kernel sources
* Thu Apr  6 2006 lslezak@suse.cz
- added Pkg::ImportGPGKey() (#164001)
- 2.13.49
* Thu Apr  6 2006 visnov@suse.cz
- implemented SourceCleanupBroken (#157100)
* Wed Apr  5 2006 jsrain@suse.de
- implemented SourceChangeUrl (#163748)
- 2.13.48
* Wed Apr  5 2006 lslezak@suse.cz
- updated keyring callbacks
- 2.13.47
* Tue Apr  4 2006 mvidner@suse.cz
- Added "alias" to Pkg::SourceGeneralData (#156030).
- libzypp API change: use location instead of plainRpm.
- 2.13.46
* Mon Apr  3 2006 kkaempf@suse.de
- new callback: Pkg::PkgFreshen() (#156980)
- 2.13.45
* Mon Apr  3 2006 lslezak@suse.cz
- new callbacks: Pkg::CallbackAcceptUnknownGpgKey(),
  Pkg::CallbackAcceptUnsignedFile(),
  Pkg::CallbackAcceptVerificationFailed(),
  Pkg::CallbackTrustedKeyAdded(),
  Pkg::CallbackTrustedKeyRemoved() (#162858)
- 2.13.44
* Wed Mar 29 2006 visnov@suse.cz
- new callback Pkg::CallbackImportGpgKey
* Wed Mar 29 2006 visnov@suse.cz
- return correct type in SourceCreate and SourceScan if URL wrong
* Wed Mar 29 2006 mvidner@suse.cz
- Find zypp using pkg-config (enables prefix builds).
- 2.13.43
* Tue Mar 28 2006 lslezak@suse.cz
- new binding Pkg::ResolvableSetSoftLock() (#159466)
- initialize zypp when it's needed, retry initialization when
  it fails, new binding Pkg::Connect() (#160319)
- call DoneProvide callback when resolvable download
  fails (#160966)
* Tue Mar 28 2006 visnov@suse.cz
- fix compile
- catch media exception if source cannot be reattached
  to get source product information
- 2.13.42
* Mon Mar 27 2006 lslezak@suse.cz
- new binding Pkg::ResolvableNeutral() (#159466)
- 2.13.41
* Mon Mar 27 2006 lslezak@suse.cz
- 2.13.40
* Mon Mar 27 2006 lslezak@suse.cz
- remove all transactions in PkgTaboo, prevent from installing
  unconfirmed packages (#160588)
* Sat Mar 25 2006 jsrain@suse.de
- do not report repeated SourceStartManager as error
- 2.13.39
* Fri Mar 24 2006 visnov@suse.cz
- mark only patches in ResolvablePreselectPatches (#160573)
- 2.13.38
* Thu Mar 23 2006 lslezak@suse.cz
- return package licenses correctly (#160028)
- 2.13.37
* Wed Mar 22 2006 visnov@suse.cz
- 2.13.36
* Wed Mar 22 2006 lslezak@suse.cz
- new builtin Pkg::CallbackResolvableReport (#160015)
- adapted to new libzypp API
* Wed Mar 22 2006 lslezak@suse.cz
- added `removed option in GetPackages builtin
  (required for #156638)
* Tue Mar 21 2006 visnov@suse.cz
- fix build
- 2.13.35
* Tue Mar 21 2006 visnov@suse.cz
- allow more choices how the media change callback behave (#159116)
- 2.13.34
* Mon Mar 20 2006 lslezak@suse.cz
- new SourceProvideOptionalFile() binding (#159116)
- 2.13.33
* Mon Mar 20 2006 visnov@suse.cz
- adapt for latest libzypp
- 2.13.32
* Sat Mar 18 2006 kkaempf@suse.de
- fix Pkg::IsSelected (and others) to check the right
  item of the pool (#158602)
- 2.13.31
* Thu Mar 16 2006 jsrain@suse.de
- let products provide their flags
* Thu Mar 16 2006 jsrain@suse.de
- added Pkg::ResolvableDependencies
- 2.13.30
* Thu Mar 16 2006 mvidner@suse.cz
- added Pkg::ResolvablePreselectPatches to select Needed items
- 2.13.29
* Wed Mar 15 2006 kkaempf@suse.de
- add PkgEstablish() to calculate needed/unneeded patches.
* Wed Mar 15 2006 visnov@suse.cz
- set alias when creating a source
- 2.13.28
* Tue Mar 14 2006 mvidner@suse.cz
- Use APPL_HIGH level instead of USER for Pkg:: (#156875, thanks ma)
- 2.13.27
* Tue Mar 14 2006 mvidner@suse.cz
- Provide Product::version via TargetProducts,
  fixing crypto update (#153576).
- Use product(name+edition)+current timestamp
  to set the source alias in SourceCreate and SourceScan (#154913).
- 2.13.26
* Tue Mar 14 2006 visnov@suse.cz
- added TargetDisableSources to disable configured sources
  at the target system (#154850)
- if no products found by libzypp, try also the base URL
  in SourceScan and SourceCreate (#157442)
* Sat Mar 11 2006 kkaempf@suse.de
- fix the build.
- 2.13.25
* Thu Mar  9 2006 lslezak@suse.cz
- new pattern related builtins: GetPatterns and PatternData
  (similar to GetSelections and SelectionData)
- use zypp::SourceManager::SourceId instead of 'int' for source ID
* Wed Mar  8 2006 lslezak@suse.cz
- create unique alias for a new installation source,
  use URL + src ID as alias (#154913)
* Tue Mar  7 2006 jsrain@suse.de
- handle installation abort properly (#154936)
- 2.13.24
* Tue Mar  7 2006 kkaempf@suse.de
- bail out early from SourceFinishAll() if there are no enabled
  sources (#155459)
- 2.13.23
* Tue Mar  7 2006 lslezak@suse.cz
- implemented PkgSrcInstall
* Mon Mar  6 2006 lslezak@suse.cz
- implemented PkgSolveCheckTargetOnly
- 2.13.22
* Fri Mar  3 2006 jsrain@suse.de
- fixed Pkg::SourceMoveDownloadArea according to changes in libzypp
* Fri Mar  3 2006 lslezak@suse.cz
- error handling: PkgLastError(), LastErrorDetails(), remember
  error messages
- TargetGetDU - use current system paritioning if TargetInitDU
  has not been called
* Fri Mar  3 2006 visnov@suse.cz
- new builtin Pkg::Init()
- catch Url exceptions in source creation
- SourceRefreshNow()
* Fri Mar  3 2006 jsrain@suse.de
- new builting Pkg::SourceMoveDownloadArea (#151862)
* Thu Mar  2 2006 visnov@suse.cz
- initialize only resolvables from the enabled sources
- catch the restore source exception
- don't initialize all resolvables to get the products from source
- 2.13.21
* Thu Mar  2 2006 visnov@suse.cz
- report user-abort from ProgressPackage callback (#150379)
* Thu Mar  2 2006 kkaempf@suse.de
- assure that PkgInstall always gets the best architecture.
  (#154627)
- assure that PkgRemove removes installed package.
* Thu Mar  2 2006 lslezak@suse.cz
- added missing disconnect()s (#154331)
* Wed Mar  1 2006 jsrain@suse.de
- provide description and summary via generic interface (#153713)
- provide more information about products and patterns
- release all medias after commit (#152709)
- add builtin to release all medias (#154348)
- 2.13.20
* Tue Feb 28 2006 lslezak@suse.cz
- call YCP callbacks only when progress value has changed more
  than 5%% since the last call (lowers CPU usage by Yast during
  installation)
- 2.13.19
* Mon Feb 27 2006 lslezak@suse.cz
- 2.13.18
* Mon Feb 27 2006 visnov@suse.cz
- implement missing download progress callback
* Fri Feb 24 2006 lslezak@suse.cz
- fixed PkgProperties()
- new builtin PkgPropertiesAll()
* Fri Feb 24 2006 lslezak@suse.cz
- catch SourceManager::findSource() exceptions (#153323)
* Fri Feb 24 2006 lslezak@suse.cz
- IsManualSelection, PkgReset, PkgMarkLicenseConfirmed
- fixed PkgGetLicensesToConfirm, PkgGetLicenseToConfirm
- PkgCommit updated to the new commit() API (#153294)
- don't pack libpy2Pkg.la file
- 2.13.17
* Fri Feb 24 2006 visnov@suse.cz
- properly report if source restore failed
* Wed Feb 22 2006 jsrain@suse.de
- TargetLogfile
- 2.13.16
* Wed Feb 22 2006 lslezak@suse.cz
- TargetInitDU
- TargetGetDU
- 2.13.15
* Wed Feb 22 2006 kkaempf@suse.de
- DoProvide now returns the best (architecture/edition) match
  instead of the first.
- 2.13.14
* Wed Feb 22 2006 visnov@suse.cz
- Don't generate doxygen documentation, this is not a C++ library
* Tue Feb 21 2006 visnov@suse.cz
- start of PkgTargetDU (#151430)
- survive if no products found on a media (#152521)
- 2.13.13
* Mon Feb 20 2006 lslezak@suse.cz
- fixed package location in PkgLocation and in PkgProperties
- new builtin PkgPath - returns package name with path relative
  to source root directory
- 2.13.12
* Sun Feb 19 2006 kkaempf@suse.de
- adapt SourceManager::store() call
- 2.13.11
* Fri Feb 17 2006 visnov@suse.cz
- 2.13.10
* Fri Feb 17 2006 visnov@suse.cz
- adapt for new pool iterators
* Thu Feb 16 2006 lslezak@suse.cz
- new builtins ResolvableInstall, ResolvableRemove,
  ResolvableProperties
- 2.13.9
* Thu Feb 16 2006 visnov@suse.cz
- Don't report a package installation twice if it needs to
  use different rpm parameters
- Callback cleanup
* Wed Feb 15 2006 visnov@suse.cz
- PkgMediaCount, PkgMediaSizes, PkgMediaNames
- Callback size fixes
- this makes the download progress behave nicely
- 2.13.8
* Tue Feb 14 2006 visnov@suse.cz
- compile fixes
- SetLocale, GetLocale, SetAdditionalLocales, GetAdditionalLocales,
  updated SelectionContent, SelectionData
- 2.13.7
* Tue Feb 14 2006 visnov@suse.cz
- Pkg::SourceScan, Pkg::SourceEditGet, Pkg::SourceGeneralData improvements
* Tue Feb 14 2006 visnov@suse.cz
- use ZYpp linewriter to log into y2log (#149001)
- Pkg::SourceProductData enhanced to return product name and
  version (#150209)
- 2.13.6
* Mon Feb 13 2006 visnov@suse.cz
- Pkg::SourceProductData basic support
- define LOGGROUP
- 2.13.5
* Mon Feb 13 2006 visnov@suse.cz
- connect also for source data parser and avoid media callback
- 2.13.4
* Sun Feb 12 2006 visnov@suse.cz
- adapt for new libzypp
- 2.13.3
* Fri Feb 10 2006 lslezak@suse.cz
- enable storage in TargetInit (#149869)
- TargetInstall, TargetRemove
- TargetProducts
- version 2.13.2
* Thu Feb  9 2006 kkaempf@suse.de
- honor kind when choosing resolvables
- 2.13.1.10
* Thu Feb  9 2006 visnov@suse.cz
- redirect zypp.log to the location of YaST log
- set pool entries to transact
- 2.13.1.9
* Wed Feb  8 2006 kkaempf@suse.de
- Qt UI adaptions
- 2.13.1.8
* Tue Feb  7 2006 visnov@suse.cz
- All callback handlers implemented
- 2.13.1.7
* Tue Feb  7 2006 visnov@suse.cz
- Store/restore source cache
- More information in install callback
- SourceStartManager, SourceStartCache, SourceGetCurrent
* Mon Feb  6 2006 visnov@suse.cz
- Renamed files
- MediaChange callback fixes
- RPM install problem callback
- PkgQueryProvides
- Selection interface cleaned up
- 2.13.1.6
* Mon Feb  6 2006 visnov@suse.cz
- Adapt for new libzypp
- 2.13.1.5
* Fri Feb  3 2006 visnov@suse.cz
- Fix build for YaST modules using Pkg
- Adapt for new libzypp
- 2.13.1.4
* Thu Feb  2 2006 lslezak@suse.cz
- DownloadProgressCallback
- MediaChangeCallback
- changed Y2PM names (variables, namespaces...) to ZYPP
- 2.13.1.3
* Thu Feb  2 2006 lslezak@suse.cz
- removed yast2-packagemanager-devel from BuildRequires
- don't compile/link PkgModuleError.* files
- RebuildDbCallback
- 2.13.1.2
* Thu Feb  2 2006 visnov@suse.cz
- first drop for ZYPP
- 2.13.1.1
* Fri Dec  2 2005 ma@suse.de
- Remember values sent on CB_StartSourceRefresh, and repeat them
  in subsequent SourceRefresh callbacks. (#133811)
- 2.13.1
* Tue Oct  4 2005 ma@suse.de
- Changed signature of ProgressProvide and ProgressDownload callbacks.
  Both are now expected to return YCPBoolean. Iff the callback returns
  YCPBoolean(FALSE), current download is aborted. (#115534)
- 2.13.0
* Fri Aug 19 2005 ma@suse.de
- Provide installation source attribute 'autorefresh' in
  PKG::SourceGeneralData.
- 2.12.7
* Wed Aug 17 2005 ma@suse.de
- Removed obsolete 'TargetUpdateInf'. That's old YaST(1)
  stuff.
- 2.12.6
* Wed Aug  3 2005 ma@suse.de
- Added YCP {Start,Error,Done}SourceRefresh callbacks.
- 2.12.5
* Wed Jul 27 2005 ma@suse.de
- Fixed conversion from YCPMap to InstSrcManager::SrcStateVector.
- 2.12.4
* Mon Jul 25 2005 ma@suse.de
- Provide new installation source attribute 'autorefresh' in
  PKG::SourceEditGet/SourceEditSet.
- New builtin PKG::SourceRefreshNow.
- 2.12.3
* Wed Jul 20 2005 ma@suse.de
- Adapt build requirements for libxml2
* Fri Jul  8 2005 visnov@suse.cz
- Adapt build requirements for blocxx
- 2.12.2
* Fri Jun 10 2005 ma@suse.de
- Adapt to changes in base classes we use from liby2.
- 2.12.1
* Tue Feb 15 2005 ma@suse.de
- Extended statistics returned from Pkg::PkgUpdateAll. The builtin
  now returns map<symbol,integer>. (#37073)
- 2.11.6
* Tue Feb  8 2005 nashif@suse.de
- Fixed neededforbuild: added sgml-skel
* Sat Feb  5 2005 ma@suse.de
- Base selctions are mutual exclusive. If a new base selection
  is set to install, take care the old one gets deleted. (#46998)
- 2.11.4
* Mon Jan 24 2005 ma@suse.de
- Code cleanup. Explicit casts removed.
- 2.11.3
* Fri Jan 21 2005 nashif@suse.de
- Fixed packages needed for build
* Fri Jan 21 2005 ma@suse.de
- Updated media change callback to allow to provide more
  information via callback.
- 2.11.2
* Fri Oct 29 2004 mvidner@suse.cz
- Added pkgconfig support.
- 2.11.1
* Wed Oct 13 2004 visnov@suse.de
- Initial version