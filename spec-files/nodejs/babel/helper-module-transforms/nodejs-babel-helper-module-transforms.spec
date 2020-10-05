%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/helper-module-transforms

Name: %{?scl_prefix}nodejs-babel-helper-module-transforms
Version: 7.11.0
Release: 1%{?dist}
Summary: Babel helper functions for implementing ES6 module transformations
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/helper-module-imports) >= 7.10.4
Requires: npm(@babel/helper-module-imports) < 8.0.0
Requires: npm(@babel/helper-replace-supers) >= 7.10.4
Requires: npm(@babel/helper-replace-supers) < 8.0.0
Requires: npm(@babel/helper-simple-access) >= 7.10.4
Requires: npm(@babel/helper-simple-access) < 8.0.0
Requires: npm(@babel/helper-split-export-declaration) >= 7.11.0
Requires: npm(@babel/helper-split-export-declaration) < 8.0.0
Requires: npm(@babel/template) >= 7.10.4
Requires: npm(@babel/template) < 8.0.0
Requires: npm(@babel/types) >= 7.11.0
Requires: npm(@babel/types) < 8.0.0
Requires: npm(lodash) >= 4.17.19
Requires: npm(lodash) < 5.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package 

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
