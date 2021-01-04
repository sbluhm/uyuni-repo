# Force out of source build
%undefine __cmake_in_source_build

%global min_libsolv_ver 0.7.11

# Small macro to define (Build)Requires for solv tools
%global req_solv_tool() \
BuildRequires:  %{_bindir}/%{1} \
Requires:       %{_bindir}/%{1}
# End macro

Name:           libzypp
Version:        17.24.1
Release:        1%{?dist}
Summary:        A package management library

License:        GPLv2+
URL:            https://en.opensuse.org/Portal:Libzypp
Source0:        https://github.com/openSUSE/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Backports from upstream
## Fix signature checks with rpm 4.16.x
Patch0001:      0001-Just-collect-details-for-the-signatures-found-fixes-.patch
## Fix libxml2 link error
Patch0002:      0001-Fix-template-with-C-linkage-build-error.patch

# Fedora specific patches
## Fix include paths for fcgi headers
Patch1001:      libzypp-17.23.1-fix-fcgi-header-paths.patch

BuildRequires:  %{_bindir}/asciidoctor
BuildRequires:  %{_bindir}/xsltproc
BuildRequires:  cmake >= 3.1
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  gpgme-devel
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(openssl) >= 1.1
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(zck)
BuildRequires:  boost-devel
BuildRequires:  glib2-devel
BuildRequires:  gettext
BuildRequires:  libsolv-devel >= %{min_libsolv_ver}
BuildRequires:  libsolv-tools >= %{min_libsolv_ver}
# For tests
BuildRequires:  fcgi-devel
BuildRequires:  nginx

# Ensure specific functionality is enabled for libsolv that libzypp needs
%req_solv_tool  repo2solv
%req_solv_tool  rpmmd2solv
%req_solv_tool  helix2solv
%req_solv_tool  susetags2solv
%req_solv_tool  comps2solv
%req_solv_tool  appdata2solv

Requires:       libsolv-tools >= %{min_libsolv_ver}
Requires:       zypp-common = %{version}-%{release}
Requires:       zypp-plugins = %{version}-%{release}
Requires:       zypp-tools = %{version}-%{release}
Requires:       gnupg2

%description
libzypp is a library for package management built on top of the
libsolv library. It is the foundation for the Zypper package manager.

%package -n zypp-common
Summary:        Common files for ZYpp
BuildArch:      noarch

%description -n zypp-common
This package provides the common files expected by %{name}
and its consumers.

%package -n zypp-plugins
Summary:        Plugins for %{name} users
# Features we provide (update doc/autoinclude/FeatureTest.doc):
Provides:       libzypp(plugin) = 0.1
Provides:       libzypp(plugin:appdata) = 0
Provides:       libzypp(plugin:commit) = 1
Provides:       libzypp(plugin:services) = 1
Provides:       libzypp(plugin:system) = 1
Provides:       libzypp(plugin:urlresolver) = 0
Provides:       libzypp(repovarexpand) = 1.1
Requires:       zypp-common = %{version}-%{release}
BuildArch:      noarch

%description -n zypp-plugins
The zypp-plugins package contains various plugin binaries used
by consumers of %{name}.

%package -n zypp-tools
Summary:        Tools for %{name} users
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n zypp-tools
The zypp-tools package contains tools shipped for consumers
of %{name} to use.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libsolv-devel%{?_isa} >= %{min_libsolv_ver}
Requires:       boost-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devel-doc
Summary:        Documentation for development using %{name}
BuildArch:      noarch

%description    devel-doc
The %{name}-devel-doc package contains documentation for
developing applications that use %{name}.

%prep
%autosetup -p1

# Use correct libexecdir
find -type f -exec sed -i -e "s|/usr/lib/zypp|%{_libexecdir}/zypp|g" {} ';'
find -type f -exec sed -i -e "s|\${CMAKE_INSTALL_PREFIX}/lib/zypp|\${CMAKE_INSTALL_PREFIX}/libexec/zypp|g" {} ';'

%build
%cmake \
         -DCMAKE_BUILD_TYPE=RelWithDebInfo \
         -DDOC_INSTALL_DIR=%{_docdir} \
         -DENABLE_BUILD_DOCS=ON \
         -DENABLE_BUILD_TESTS=ON \
         -DENABLE_BUILD_TRANS=ON \
         -DENABLE_ZCHUNK_COMPRESSION=ON

%cmake_build

%install
%cmake_install
%find_lang zypp

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Create directories expected by libzypp
mkdir -p %{buildroot}%{_sysconfdir}/zypp/repos.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/services.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/systemCheck.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/vendors.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/multiversion.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/needreboot.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/credentials.d
mkdir -p %{buildroot}%{_libexecdir}/zypp
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins/appdata
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins/commit
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins/services
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins/system
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins/urlresolver
mkdir -p %{buildroot}%{_sharedstatedir}/zypp
mkdir -p %{buildroot}%{_localstatedir}/log/zypp
mkdir -p %{buildroot}%{_localstatedir}/cache/zypp

# Remove needreboot file, we don't have a Fedora-specific one yet...
rm %{buildroot}%{_sysconfdir}/zypp/needreboot

%check
pushd %{_vpath_builddir}/tests
# Tests need to be compiled first and cannot be run in parallel
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:${LD_LIBRARY_PATH} ctest -VV --output-on-failure .
popd


%pretrans -p <lua> -n zypp-common
-- Purge repos.d symlink if it exists
path = "%{_sysconfdir}/zypp/repos.d"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end


%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/cmake/Modules/*

%files devel-doc
%doc %dir %{_docdir}/libzypp
%doc %{_docdir}/libzypp/*

%files -n zypp-common -f zypp.lang
%dir %{_sysconfdir}/zypp
%dir %{_sysconfdir}/zypp/services.d
%dir %{_sysconfdir}/zypp/systemCheck.d
%dir %{_sysconfdir}/zypp/vendors.d
%dir %{_sysconfdir}/zypp/multiversion.d
%dir %{_sysconfdir}/zypp/needreboot.d
%dir %{_sysconfdir}/zypp/credentials.d
%dir %{_sysconfdir}/zypp/repos.d
%config(noreplace) %{_sysconfdir}/zypp/zypp.conf
%config(noreplace) %{_sysconfdir}/zypp/systemCheck
%config(noreplace) %{_sysconfdir}/logrotate.d/zypp-history.lr
%dir %{_sharedstatedir}/zypp/
%dir %attr(750,root,root) %{_localstatedir}/log/zypp
%dir %{_localstatedir}/cache/zypp
%dir %{_libexecdir}/zypp
%{_mandir}/man5/*.5*
%{_datadir}/zypp/

%files -n zypp-plugins
%{_libexecdir}/zypp/plugins/

%files -n zypp-tools
%{_bindir}/zypp-*
%{_mandir}/man1/*.1*


%changelog
* Sat Aug 08 2020 Neal Gompa <ngompa13@gmail.com> - 17.24.1-1
- Update to 17.24.1 (#1817137)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.23.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.23.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 17.23.5-1
- Update to 17.23.5

* Fri Mar 20 2020 Neal Gompa <ngompa13@gmail.com> - 17.23.2-1
- Update to 17.23.2 (#1800765)

* Sat Mar 07 2020 Neal Gompa <ngompa13@gmail.com> - 17.23.1-1
- Rebase to 17.23.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Neal Gompa <ngompa13@gmail.com> - 17.22.0-1
- Rebase to 17.22.0 (#1777960)

* Tue Nov 12 2019 Neal Gompa <ngompa13@gmail.com> - 17.16.0-1
- Rebase to 17.16.0 (#1755979)
- Replace /etc/zypp/repos.d symlink with empty directory
  as Fedora repos are no longer compatible with Zypper

* Tue Aug 27 2019 Neal Gompa <ngompa13@gmail.com> - 17.14.0-1
- Rebase to 17.14.0 (#1742317)
- Add patch to fix build with RPM 4.15 (#1736067)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 22:13:20 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.12.0-3
- Rebuild for RPM 4.15

* Mon Jun 10 15:42:03 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.12.0-2
- Rebuild for RPM 4.15

* Tue May 28 2019 Björn Esser <besser82@fedoraproject.org> - 17.12.0-1
- Rebase to 17.12.0 (#1714678)

* Wed Apr 10 2019 Björn Esser <besser82@fedoraproject.org> - 17.11.4-1
- Rebase to 17.11.4 (#1696240)

* Mon Mar 25 2019 Björn Esser <besser82@fedoraproject.org> - 17.11.3-1
- Rebase to 17.11.3 (#1680584)

* Mon Mar 25 2019 Björn Esser <besser82@fedoraproject.org> - 17.11.1-2
- Explicitly enable documentation on CMake command line
- Explicitly enable tests on CMake command line
- Explicitly enable translation on CMake command line

* Mon Feb 11 2019 Neal Gompa <ngompa13@gmail.com> - 17.11.1-1
- Rebase to 17.11.1 (#1671486)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 31 2019 Björn Esser <besser82@fedoraproject.org> - 17.8.1-2
- Rebuilt for Boost 1.69

* Sat Nov 03 2018 Neal Gompa <ngompa13@gmail.com> - 17.8.1-1
- Rebase to 17.8.1

* Sun Aug 26 2018 Neal Gompa <ngompa13@gmail.com> - 17.6.2-1
- Rebase to 17.6.2 (#1552594)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 04 2018 Neal Gompa <ngompa13@gmail.com> - 17.2.0-1
- Rebase to 17.2.0 (#1547298)

* Tue Feb 06 2018 Neal Gompa <ngompa13@gmail.com> - 17.1.2-1
- Rebase to 17.1.2 (#1489422)
- Backport fix to fix tests compiled with _GLIBCXX_ASSERTIONS on
- Drop unneeded ldconfig scriptlets
  - See https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets

* Fri Jan 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 16.15.6-2
- Rebuild to pick up OpenSSL 1.1

* Sun Sep 03 2017 Neal Gompa <ngompa13@gmail.com> - 16.15.6-1
- Update to 16.15.6 (#1485326)
- Drop all patches as they are part of this release

* Thu Aug 17 2017 Neal Gompa <ngompa13@gmail.com> - 16.15.3-1
- Update to 16.15.3 (#1480822)
- Backport patches from upstream
  - Fix missing return value
  - Fix typo in changelog
  - Drop RPM 4.4 compatibility code to fix build with RPM 4.14

* Fri Aug 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 16.15.2-4
- Rebuilt after RPM update (№ 3)

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 16.15.2-3
- Rebuilt for RPM soname bump

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 16.15.2-2
- Rebuilt for RPM soname bump

* Sat Aug 05 2017 Neal Gompa <ngompa13@gmail.com> - 16.15.2-1
- Update to 16.15.2 (#1467000)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Neal Gompa <ngompa13@gmail.com> - 16.12.0-1
- Update to 16.12.0 (#1444589)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Apr 17 2017 Neal Gompa <ngompa13@gmail.com> - 16.6.1-1
- Update to 16.6.1
- Split data content and binaries into subpackages
- Use correct libexecdir
- Add BR for libudev

* Fri Feb 24 2017 Neal Gompa <ngompa13@gmail.com> - 16.4.3-1
- Update to 16.4.3
- Add missing directories to be owned by package
- Add missing dependencies on libsolv-tools

* Mon Dec 12 2016 Neal Gompa <ngompa13@gmail.com> - 16.3.1-1
- Update to 16.3.1
- Bump required libsolv version

* Sat Sep  3 2016 Neal Gompa <ngompa13@gmail.com> - 16.2.2-4
- Add test run conditional

* Sat Aug 27 2016 Neal Gompa <ngompa13@gmail.com> - 16.2.2-3
- Rebuild against libsolv to add suserepo support

* Thu Aug 25 2016 Neal Gompa <ngompa13@gmail.com> - 16.2.2-2
- Add patch to use correct name for repo2solv with Fedora libsolv

* Wed Aug 24 2016 Neal Gompa <ngompa13@gmail.com> - 16.2.2-1
- Update to 16.2.2
- Bump required libsolv version

* Fri Jun 10 2016 Neal Gompa <ngompa13@gmail.com> - 16.0.2-1
- Update to 16.0.2

* Tue Apr 26 2016 Neal Gompa <ngompa13@gmail.com> - 15.22.0-1
- Update to 15.22.0

* Wed Apr  6 2016 Neal Gompa <ngompa13@gmail.com> - 15.21.5-1
- Update to 15.21.5

* Thu Feb  4 2016 Neal Gompa <ngompa13@gmail.com> - 15.21.2-1
- Update to 15.21.2

* Sun Jan 31 2016 Neal Gompa <ngompa13@gmail.com> - 15.21.1-1
- Initial packaging
