%global __python /usr/bin/python2
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-pycurl
Version:        7.19.0
Release:        19%{?dist}
Summary:        A Python interface to libcurl

Group:          Development/Languages
License:        LGPLv2+ or MIT
URL:            http://pycurl.sourceforge.net/
Source0:        http://pycurl.sourceforge.net/download/pycurl-%{version}.tar.gz

# upstream patches
Patch1:         0001-No-longer-keep-copies-of-string-options-since-this-i.patch
Patch2:         0002-Fixes-https-sourceforge.net-tracker-func-detail-aid-.patch
Patch3:         0003-Fixes-refcount-bug-and-provides-better-organization-.patch
Patch4:         0004-Test-for-reset-fixes-refcount-bug.patch
Patch5:         0005-Updating-ChangeLog-with-relevant-changes.patch

# downstream patches
Patch101:       0101-test_internals.py-add-a-test-for-ref-counting-of-res.patch
Patch102:       0102-pycurl.c-eliminate-duplicated-code-in-util_write_cal.patch
Patch103:       0103-pycurl.c-allow-to-return-1-from-write-callback.patch
Patch104:       0104-test_write_abort.py-test-returning-1-from-write-call.patch
Patch105:       0105-add-the-GLOBAL_ACK_EINTR-constant-to-the-list-of-exp.patch

# RHEL patches
Patch201:       0201-Keep-a-reference-to-the-object-used-for-CURLOPT_POST.patch
Patch202:       0202-Add-libcurl-7.34.0-sslversion-options.patch

Requires:       keyutils-libs
%if 0%{?rhel} >= 8
BuildRequires:  python2-devel
%else
BuildRequires:  python-devel
%endif
BuildRequires:  openssl-devel

# curl-7.29.0-16 or newer is needed for CURL_SSLVERSION_TLSv1_[0-2]
BuildRequires:  libcurl-devel >= 7.29.0-16

# During its initialization, PycURL checks that the actual libcurl version
# is not lower than the one used when PycURL was built.
# Yes, that should be handled by library versioning (which would then get
# automatically reflected by rpm).
# For now, we have to reflect that dependency.
%global libcurl_sed '/^#define LIBCURL_VERSION "/!d;s/"[^"]*$//;s/.*"//;q'
%global curlver_h /usr/include/curl/curlver.h
%global libcurl_ver %(sed %{libcurl_sed} %{curlver_h} 2>/dev/null || echo 0)
Requires:       libcurl >= %{libcurl_ver}

Provides:       pycurl = %{version}-%{release}

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

%prep
%setup0 -q -n pycurl-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch201 -p1
%patch202 -p1
chmod a-x examples/*

%build
CFLAGS="$RPM_OPT_FLAGS -DHAVE_CURL_OPENSSL" %{__python} setup.py build

%check
export PYTHONPATH=$RPM_BUILD_ROOT%{python_sitearch}
make test PYTHON=%{__python}

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{_datadir}/doc/pycurl

%files
%doc COPYING COPYING2 ChangeLog README TODO examples doc tests
%{python_sitearch}/*

%changelog
* Mon Sep 07 2015 Kamil Dudka <kdudka@redhat.com> - 7.19.0-19
- introduce SSLVERSION_TLSv1_[0-2] (#1260407)

* Wed Oct 15 2014 Kamil Dudka <kdudka@redhat.com> - 7.19.0-18
- fix a use-after-free bug in handling pycurl.POSTFIELDS (#1153321)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 7.19.0-17
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 7.19.0-16
- Mass rebuild 2013-12-27

* Tue Apr 09 2013 Kamil Dudka <kdudka@redhat.com> - 7.19.0-15.1
- add the GLOBAL_ACK_EINTR constant to the list of exported symbols (#920589)

* Wed Mar 06 2013 Kamil Dudka <kdudka@redhat.com> - 7.19.0-15
- allow to return -1 from the write callback (#857875) 
- remove the patch for curl-config --static-libs no longer needed
- run the tests against the just built pycurl, not the system one

* Mon Feb 25 2013 Kamil Dudka <kdudka@redhat.com> - 7.19.0-14
- apply bug-fixes committed to upstream CVS since 7.19.0 (fixes #896025)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.19.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 22 2012 Jan Synáček <jsynacek@redhat.com> - 7.19.0-12
- Improve spec

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.19.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.19.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.19.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Dennis Gilmore <dennis@ausil.us> - 7.19.0-8
- add Missing Requires on keyutils-libs

* Tue Aug 17 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.19.0-7
- Add patch developed by David Malcolm to fix segfaults caused by a missing incref

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 7.19.0-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Mar  2 2010 Karel Klic <kklic@redhat.com> - 7.19.0-5
- Package COPYING2 file
- Added MIT as a package license

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 17 2009 Stepan Kasal <skasal@redhat.com> - 7.19.0-3
- fix typo in the previous change

* Fri Apr 17 2009 Stepan Kasal <skasal@redhat.com> - 7.19.0-2
- add a require to reflect a dependency on libcurl version (#496308)

* Thu Mar  5 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.19.0-1
- Update to 7.19.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 7.18.2-2
- Rebuild for Python 2.6

* Thu Jul  3 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.18.2-1
- Update to 7.18.2
- Thanks to Ville Skyttä re-enable the tests and fix a minor problem
  with the setup.py. (Bug # 45400)

* Thu Jun  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.18.1-1
- Update to 7.18.1
- Disable tests because it's not testing the built library, it's trying to
  test an installed library.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 7.16.4-3
- Autorebuild for GCC 4.3

* Thu Jan  3 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.16.4-2
- BR openssl-devel

* Wed Aug 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.16.4-1
- Update to 7.16.4
- Update license tag.

* Sat Jun  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.16.2.1-1
- Update to released version.

* Thu Dec  7 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.16.0-0.1.20061207
- Update to a CVS snapshot since development has a newer version of curl than is in FC <= 6

* Thu Dec  7 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.15.5.1-4
- Add -DHAVE_CURL_OPENSSL to fix PPC build problem.

* Thu Dec  7 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.15.5.1-3
- Don't forget to Provide: pycurl!!!

* Thu Dec  7 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.15.5.1-2
- Remove INSTALL from the list of documentation
- Use python_sitearch for all of the files

* Thu Dec  7 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 7.15.5.1-1
- First version for Fedora Extras
