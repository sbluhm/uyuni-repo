%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/types

Name: %{?scl_prefix}nodejs-babel-types
Version: 7.11.5
Release: 1%{?dist}
Summary: Babel Types is a Lodash-esque utility library for AST nodes
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: https://registry.npmjs.org/@babel/types/-/types-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/helper-validator-identifier) >= 7.10.4
Requires: npm(@babel/helper-validator-identifier) < 8.0.0
Requires: npm(lodash) >= 4.17.19
Requires: npm(lodash) < 5.0.0
Requires: npm(to-fast-properties) >= 2.0.0
Requires: npm(to-fast-properties) < 3.0.0
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
cp -pfr scripts %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
