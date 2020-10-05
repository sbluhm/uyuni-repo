%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @types/yargs-parser

Name: %{?scl_prefix}nodejs-types-yargs-parser
Version: 13.1.0
Release: 1%{?dist}
Summary: TypeScript definitions for yargs-parser
License: MIT
Group: Development/Libraries
URL: https://github.com/DefinitelyTyped/DefinitelyTyped#readme
Source0: https://registry.npmjs.org/@types/yargs-parser/-/yargs-parser-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n yargs-parser 

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
