%{?nodejs_find_provides_and_requires}

%global packagename babel-runtime
%global enable_tests 0

Name:		nodejs-babel-runtime
Version:	7.11.2
Release:	1%{?dist}
Summary:	The babel selfContained runtime

License:	MIT
URL:		https://github.com/babel/babel/tree/master/packages/babel-runtime
Source0:	https://registry.npmjs.org/@babel/runtime/-/runtime-%{version}.tgz

# license file
Source11:	https://raw.githubusercontent.com/babel/babel/v%{version}/LICENSE


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	npm(core-js)
%endif

%description
The babel selfContained runtime


%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package
# copy the license file
cp -p %{SOURCE11} .

# I know you'll be temped to remove the "core-js" directory, thinking that it's
# a bundled copy of the npm(core-js) package.  It's not. Instead, it's a bunch
# of files that refer to the corresponding files from the npm(core-js) package.

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js helpers/ regenerator/ core-js/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[102m -=#=- There are no tests -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"

%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.23.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.23.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.23.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Jared Smith <jsmith@fedoraproject.org> - 6.23.0-1
- Update to upstream 6.23.0 release

* Tue Jul 05 2016 Jared Smith <jsmith@fedoraproject.org> - 6.9.2-1
- Update to upstream 6.9.2 release

* Wed Feb 17 2016 Jared Smith <jsmith@fedoraproject.org> - 6.5.0-1
- Initial packaging
