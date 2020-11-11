%global module_name backports.ssl_match_hostname

Name:           python-backports-ssl_match_hostname
Version:        3.5.0.1
Release:        1%{?dist}
Summary:        The ssl.match_hostname() function from Python 3

License:        Python
URL:            https://bitbucket.org/brandon/backports.ssl_match_hostname
Source0:        http://pypi.python.org/packages/source/b/%{module_name}/%{module_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
Requires:       python-backports
Requires:       python-ipaddress

%description
The Secure Sockets layer is only actually secure if you check the hostname in
the certificate returned by the server to which you are connecting, and verify
that it matches to hostname that you are trying to reach.

But the matching logic, defined in RFC2818, can be a bit tricky to implement on
your own. So the ssl package in the Standard Library of Python 3.2 now includes
a match_hostname() function for performing this check instead of requiring
every application to implement the check separately.

This backport brings match_hostname() to users of earlier versions of Python.
The actual code is only slightly modified from Python 3.5.


%prep
%setup -qn %{module_name}-%{version}
cp backports/ssl_match_hostname/README.txt ./
cp backports/ssl_match_hostname/LICENSE.txt ./


%build
python setup.py build


%install
python setup.py install --skip-build --root %{buildroot}
rm %{buildroot}%{python_sitelib}/backports/__init__.py*

 
%files
%doc README.txt LICENSE.txt
%{python_sitelib}/*


%changelog
* Tue Oct 10 2017 Iryna Shcherbina <ishcherb@redhat.com> - 3.5.0.1-1
- Update to 3.5.0.1
Resolves: rhbz#1500373

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.4.0.2-4
- Mass rebuild 2013-12-27

* Thu Dec 19 2013 Endi S. Dewata <edewata@redhat.com> - 3.4.0.2-3
- Restore python-backports dependency on RHEL

* Mon Dec 09 2013 Endi S. Dewata <edewata@redhat.com> - 3.4.0.2-2
- Drop python-backports dependency on RHEL

* Sun Oct 27 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.4.0.2-1
- Update to upstream 3.4.0.2 for a security fix
- http://bugs.python.org/issue17997

* Mon Sep 02 2013 Ian Weller <iweller@redhat.com> - 3.4.0.1-1
- Update to upstream 3.4.0.1

* Mon Aug 19 2013 Ian Weller <iweller@redhat.com> - 3.2-0.5.a3
- Use python-backports instead of providing backports/__init__.py

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-0.4.a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 20 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.2-0.3.a3
- Add patch for CVE 2013-2099 https://bugzilla.redhat.com/show_bug.cgi?id=963260

* Tue Feb 05 2013 Ian Weller <iweller@redhat.com> - 3.2-0.2.a3
- Fix Python issue 12000

* Fri Dec 07 2012 Ian Weller <iweller@redhat.com> - 3.2-0.1.a3
- Initial package build
