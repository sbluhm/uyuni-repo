%global srcname ws4py
%global _description %{expand:
WebSocket client and server library.}

Name:           python-ws4py
Version:        0.5.1
Release:        8%{?dist}
Summary:        WebSocket client and server library

# Bundled utf8validator is ASL 2.0 
License:        BSD and ASL 2.0
URL:            https://ws4py.readthedocs.org/en/latest/
Source0:        %pypi_source
Patch01:        0001-Python-3.7-and-3.8-compat.patch

BuildArch:      noarch

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-setuptools
Requires:       python3-cherrypy
Requires:       python3-tornado
Requires:       python3-gevent
%{?python_provide:%python_provide python3-%{srcname}}
Provides:       bundled(utf8validator)

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.9

* Thu Mar 12 2020 Fabien Boucher <fboucher@redhat.com> - 0.5.1-2
- Adapt packaging for Rawhide from Software Factory packaging.

* Mon Jun 04 2018 Tristan Cacqueray <tdecacqu@redhat.com> - 0.5.1-1
- Initial packaging
