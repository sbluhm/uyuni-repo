%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @types/babel__template

Name: %{?scl_prefix}nodejs-types-babel__template
Version: 7.0.3
Release: 1%{?dist}
Summary: TypeScript definitions for @babel/template
License: MIT
Group: Development/Libraries
URL: https://github.com/DefinitelyTyped/DefinitelyTyped#readme
Source0: https://registry.npmjs.org/@types/babel__template/-/babel__template-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/parser) >= 7.1.0
Requires: npm(@babel/parser) < 8.0.0
Requires: npm(@babel/types) >= 7.0.0
Requires: npm(@babel/types) < 8.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n babel__template 

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
