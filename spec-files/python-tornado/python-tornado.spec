%if 0%{?fedora} > 12
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

%if 0%{?rhel} >= 8
%global __python /usr/bin/python2
%define pythonX python2
%else
%define pythonX python
%endif

%global pkgname tornado

Name:           python-%{pkgname}
Version:        4.2.1
Release:        5%{?dist}
Summary:        Scalable, non-blocking web server and tools

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://www.tornadoweb.org
Source0:        https://files.pythonhosted.org/packages/source/t/%{pkgname}/%{pkgname}-%{version}.tar.gz
# The license file from upstream is not included in the tarball from pypi
# so we add it manually from the project's github repository.
# https://github.com/tornadoweb/tornado/blob/master/LICENSE
Source1:        LICENSE
# Patch to use system CA certs instead of certifi
Patch0:         python-tornado-cert.patch
# Improve introspection of coroutines
# Fixed upstream: https://github.com/tornadoweb/tornado/pull/1890
Patch1:         improve-introspection-of-coroutines.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python2-devel

BuildRequires:  python-backports-ssl_match_hostname

BuildRequires:  mod_wsgi

Requires:       python-pycurl
Requires:       python-backports-ssl_match_hostname
%if 0%{?with_python3}
BuildRequires:  python3-tools
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
%endif

Provides:    python2-tornado = %{version}-%{release}
Provides:    python2-tornado%{?_isa} = %{version}-%{release}

%description
Tornado is an open source version of the scalable, non-blocking web
server and tools.

The framework is distinct from most mainstream web server frameworks
(and certainly most Python frameworks) because it is non-blocking and
reasonably fast. Because it is non-blocking and uses epoll, it can
handle thousands of simultaneous standing connections, which means it is
ideal for real-time web services.

%package doc
Summary:        Examples for python-tornado
Group:          Documentation
Requires:       python-tornado%{?_isa} = %{version}-%{release}
Provides:		python2-tornado-doc = %{version}-%{release}
Provides:		python2-tornado-doc%{?_isa} = %{version}-%{release}

%description doc
Tornado is an open source version of the scalable, non-blocking web
server and and tools. This package contains some example applications.

%if 0%{?with_python3}
%package -n python3-tornado
Summary:        Scalable, non-blocking web server and tools
%description -n python3-tornado
Tornado is an open source version of the scalable, non-blocking web
server and tools.

The framework is distinct from most mainstream web server frameworks
(and certainly most Python frameworks) because it is non-blocking and
reasonably fast. Because it is non-blocking and uses epoll, it can
handle thousands of simultaneous standing connections, which means it is
ideal for real-time web services.

%package -n python3-tornado-doc
Summary:        Examples for python-tornado
Group:          Documentation
Requires:       python3-tornado%{?_isa} = %{version}-%{release}

%description -n python3-tornado-doc
Tornado is an open source version of the scalable, non-blocking web
server and and tools. This package contains some example applications.

%endif # with_python3

%prep 
%setup -q -n %{pkgname}-%{version}

cp -a %{SOURCE1} .

%patch0 -p1
%patch1 -p1

# remove shebang from files
%{__sed} -i.orig -e '/^#!\//, 1d' *py tornado/*.py tornado/*/*.py

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
2to3 --write --nobackups %{py3dir}
%endif # with_python3

%build
%if 0%{?with_python3}
pushd %{py3dir}
    python3 setup.py build
popd
%endif # with_python3

%{pythonX} setup.py build


%install
rm -rf %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
    PATH=$PATH:%{buildroot}%{python3_sitearch}/%{pkgname}
    %{__python3} setup.py install --root=%{buildroot}
popd
%endif # with_python3

PATH=$PATH:%{buildroot}%{python2_sitearch}/%{pkgname}
%{__python2} setup.py install --root=%{buildroot}


%clean
rm -rf %{buildroot}

%check
%if "%{dist}" != ".el6"
    %if 0%{?with_python3}
    pushd %{py3dir}
        PYTHONPATH=%{python3_sitearch} \
        %{__python3} -m tornado.test.runtests --verbose
    popd
    %endif # with_python3
    PYTHONPATH=%{python2_sitearch} \
    %{__python2} -m tornado.test.runtests --verbose
%endif

%files
%defattr(-,root,root,-)
%doc README.rst PKG-INFO
%license LICENSE

%{python2_sitearch}/%{pkgname}/
%{python2_sitearch}/%{pkgname}-%{version}-*.egg-info

%files doc
%defattr(-,root,root,-)
%doc demos

%if 0%{?with_python3}
%files -n python3-tornado
%defattr(-,root,root,-)
%doc README.rst PKG-INFO
%license LICENSE

%{python3_sitearch}/%{pkgname}/
%{python3_sitearch}/%{pkgname}-%{version}-*.egg-info

%files -n python3-tornado-doc
%defattr(-,root,root,-)
%doc demos
%endif


%changelog
* Thu Nov 22 2018 Charalampos Stratakis <cstratak@redhat.com> - 4.2.1-5
- Improve introspection of coroutines
Resolves: rhbz#1607838

* Mon Apr 16 2018 Charalampos Stratakis <cstratak@redhat.com> - 4.2.1-4
- Add mod_wsgi as a build dependency
Resolves: rhbz#1533902

* Tue Oct 03 2017 Charalampos Stratakis <cstratak@redhat.com> - 4.2.1-3
- Fix an rpmlint issue with an un-escaped macro in the changelog.
Resolves: rhbz#1496516

* Wed Sep 27 2017 Charalampos Stratakis <cstratak@redhat.com> - 4.2.1-2
- Provide the license file that was not included in the pypi tarball.
Resolves: rhbz#1463675

* Mon Feb 06 2017 Charalampos Stratakis <cstratak@redhat.com> - 4.2.1-1
- Upgrade to upstream release 4.2.1
Resolves: rhbz#1158617

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.2.1-8
- Mass rebuild 2013-12-27

* Thu Nov 21 2013 Endi S. Dewata <edewata@redhat.com> - 2.2.1-7
- Removed dependency on python-simplejson.

* Wed Oct 09 2013 Endi S. Dewata <edewata@redhat.com> - 2.2.1-6
- Removed custom match_hostname().

* Fri Jun 14 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.2.1-5
- remove rhel conditional for with_python3:
  https://fedorahosted.org/fpc/ticket/200

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 2.2.1-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 20 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.2.1-1
- update to upstream release 2.2.1 (fixes CVE-2012-2374)
- fix typo for epel6 macro bug #822972 (Florian La Roche)

* Thu Feb 9 2012 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 2.2-1
- upgrade to upstream release 2.2

* Thu Feb 9 2012 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 2.1.1-4
- remove python3-simplejson dependency

* Fri Jan 27 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.1.1-3
- build python3 package

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 2.1.1-1
- new upstream version 2.1.1
- remove double word in description and rearrange it (#715272)
- fixed removal of shebangs
- added %%check section to run unittests during package build

* Tue Mar 29 2011 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 1.2.1-1
- new upstream version 1.2.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep  8 2010 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 1.1-1
- new upstream release 1.1

* Tue Aug 17 2010 Ionuț Arțăriși <mapleoin@fedoraproject.org> - 1.0.1-1
- new upstream bugfix release: 1.0.1

* Wed Aug  4 2010 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 1.0-2
- changed upstream source url

* Wed Aug  4 2010 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 1.0-1
- new upstream release 1.0
- there's no longer a problem with spurious permissions, so remove that fix

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Oct 21 2009 Ionuț Arțăriși <mapleoin@fedoraproject.org> - 0.2-3
- changed -doc package group to Documentation
- use global instead of define

* Tue Oct 20 2009 Ionuț Arțăriși <mapleoin@fedoraproject.org> - 0.2-2
- create -doc package for examples
- altered description to not include references to FriendFeed
- rename to python-tornado

* Fri Sep 25 2009 Ionuț Arțăriși <mapleoin@lavabit.com> - 0.2-1
- New upstream version
- Fixed macro usage and directory ownership in spec

* Thu Sep 10 2009 Ionuț Arțăriși <mapleoin@lavabit.com> - 0.1-1
- Initial release

