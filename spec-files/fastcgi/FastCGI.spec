#
# spec file for package FastCGI
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


Name:           FastCGI
%define lname	libfcgi0
Version:        2.4.0
Release:        172.12
Summary:        A Scalable, Open Extension to CGI
License:        OML
Group:          Development/Languages/C and C++
Url:            http://www.fastcgi.com
Source:         http://www.fastcgi.com/dist/fcgi.tar.bz2
Source1:        README.supervise
Patch0:         FastCGI-makefile.am_cppflags.patch
Patch1:         FastCGI-clientdata_pointer.patch
Patch2:         FastCGI-supervise_cgi-fcgi.patch
Patch3:         fastcgi-2.4.0_missing_call_to_fclose.patch
Patch4:         FastCGI-gcc44.patch
Patch5:         FastCGI-perl514.patch
Patch6:         FastCGI-fix_deprecated_api.patch
Patch7:         FastCGI-perl526.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FastCGI is a language-independent, scalable, open extension to CGI that
provides high performance without the limitations of server-specific
APIs.

%package devel
Summary:        A scalable, open extension to CGI
Group:          Development/Languages/C and C++
Requires:       %lname = %version
Requires:       glibc-devel

%description devel
FastCGI is a language independent, scalable, open extension to CGI that
provides high performance without the limitations of server specific
APIs.

%package -n %lname
Summary:        A scalable, open extension to CGI - System library
Group:          System/Libraries
Obsoletes:      libfcgi++-0 < %version-%release
Provides:       libfcgi++-0 = %version-%release

%description -n %lname
FastCGI is a language independent, scalable, open extension to CGI that
provides high performance without the limitations of server specific
APIs.

%package -n perl-FastCGI
Summary:        A scalable, open extension to CGI
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
%if 0%{?suse_version} < 1120 
Requires:       perl >= 5.8.0
%else
%{perl_requires}
%endif

%description -n perl-FastCGI
FastCGI is a language independent, scalable, open extension to CGI that
provides high performance without the limitations of server specific
APIs.

%prep
%setup -n fcgi-%{version}
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7 -p1
touch NEWS AUTHORS ChangeLog COPYING
find doc/{fastcgi-prog-guide,fastcgi-whitepaper} -type f -print0 | xargs -r0 chmod 0644

%build
autoreconf -fi
%configure --disable-static --includedir=%{_includedir}/fastcgi
make all
pushd perl
    %configure --disable-static --includedir=%{_includedir}/fastcgi
    %{__perl} Makefile.PL
    make %{?_smp_mflags} all
popd

%install
%make_install
pushd perl
    %perl_make_install
    %perl_process_packlist
popd
pushd examples
    %{__make} clean
popd
%{__install} -Dd -m 0755                     \
    %{buildroot}%{_mandir}/man{1,3}/         \
    %{buildroot}%{_docdir}/%{name}/examples/
%{__install} -m 0644 examples/* %{buildroot}%{_docdir}/%{name}/examples/
%{__install} -m 0644 doc/*.1    %{buildroot}%{_mandir}/man1/
%{__install} -m 0644 doc/*.3    %{buildroot}%{_mandir}/man3/
%{__install} -m 0644 doc/*.htm* doc/*.gif LICENSE.TERMS README \
    %{buildroot}%{_docdir}/%{name}/
%{__install} -m 0644 perl/README    %{buildroot}%{_docdir}/%{name}/README.perl
%{__install} -m 0644 perl/ChangeLog %{buildroot}%{_docdir}/%{name}/ChangeLog.perl
%{__cp} -vr doc/{fastcgi-prog-guide,fastcgi-whitepaper} java %{S:1} \
    %{buildroot}%{_docdir}/%{name}/
rm -f %{buildroot}%{_libdir}/libfcgi*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/cgi-fcgi
%{_mandir}/man1/*.1.gz
%doc %{_docdir}/%{name}

%files devel
%defattr(-,root,root)
%dir %{_includedir}/fastcgi/
%{_includedir}/fastcgi/*
%{_libdir}/libfcgi*.so
%{_mandir}/man3/*.3.gz

%files -n %lname
%defattr(-,root,root)
%{_libdir}/libfcgi*.so.*

%files -n perl-FastCGI
%defattr(-,root,root)
%{_mandir}/man3/*.3pm.gz
%{perl_vendorarch}/FCGI.pm
%dir %{perl_vendorarch}/auto/FCGI
%{perl_vendorarch}/auto/FCGI/*.*
%if %{?suse_version} < 1140
%{perl_vendorarch}/auto/FCGI/.packlist
%{_var}/adm/perl-modules/%{name}
%endif

%changelog
* Sun Sep 24 2017 coolo@suse.com
- add FastCGI-perl526.patch as perl 5.26 no longer has . in @INC
* Sat Dec 20 2014 jengelh@inai.de
- "libfcgi++-0" package name is wrong (should be "libfcgi++0");
  change to libfcgi0 (due to libfcgi.so.0 being present, which is
  the main one).
- Remove pointless --with-pic (it is enabled by default anyway)
* Sat Dec 13 2014 p.drouand@gmail.com
- Split out the system library, following the shared library
  conventions
- Make devel subpackage depends on shared library package
* Mon Sep  1 2014 fcrozat@suse.com
- Update license tag to spdx 1.2.
* Wed Mar 20 2013 boris@steki.net
- re-enable SLE support as %%perl_requires is too new
* Mon Jun 11 2012 coolo@suse.com
- require the right version of perl
* Tue Mar 27 2012 cfarrell@suse.com
- license update: SUSE-OML
  Use SUSE- proprietary prefix until license is accepted upstream by
  SPDX.org. Fedora tracks this as OML.
* Wed Dec 21 2011 mrueckert@suse.com
- added FastCGI-fix_deprecated_api.patch: (bnc#735882)
  Fixes an issue where CGI.pm received CGI variables from previous
  requests. CVE-2011-2766
* Sat Oct 15 2011 coolo@suse.com
- add libtool as buildrequire to make the spec file more reliable
* Sat Sep 17 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
- Enable parallel build
* Thu May 26 2011 idonmez@novell.com
- Add FastCGI-perl514.patch: fix compilation with Perl 5.14
* Mon Dec  6 2010 coolo@novell.com
- fix build for factory
* Sun Dec 20 2009 jengelh@medozas.de
- enable parallel build
* Thu Sep 17 2009 mrueckert@suse.de
- add fastcgi-2.4.0_missing_call_to_fclose.patch (bnc#525009)
* Fri Jun 26 2009 crrodriguez@suse.de
- disable static libraries
* Mon Feb 16 2009 coolo@suse.de
- fix build with gcc 4.4
* Fri Oct 20 2006 mrueckert@suse.de
- remove perl_make_install for now ... i wont build for fedora
  any time soon.
* Fri Sep 15 2006 mrueckert@suse.de
- add perl_make_install for all distros other than suse.
* Fri Sep  8 2006 mrueckert@suse.de
- add README.supervise
- small spec file cleanup
* Thu Sep  7 2006 mrueckert@suse.de
- applied patch from
  http://rubyists.com/articles/2005/05/03/spawn-fcgi-in-the-foreground
  to run fastcgi application in foreground this is useful for tools
  like runit/daemontools/initng
* Thu Aug 24 2006 mrueckert@suse.de
- run ldconfig
* Wed Mar  8 2006 mrueckert@suse.de
- readded gcc-c++ to the BuildRequires
  Seems it got lost in the automatic BuildRequires conversion.
  fixes C++ bindings.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Aug 17 2005 mrueckert@suse.de
- Initial package with version 2.4.0
