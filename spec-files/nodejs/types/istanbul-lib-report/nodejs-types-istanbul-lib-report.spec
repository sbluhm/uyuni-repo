%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @types/istanbul-lib-report

Name: %{?scl_prefix}nodejs-types-istanbul-lib-report
Version: 1.1.1
Release: 1%{?dist}
Summary: TypeScript definitions for istanbul-lib-report
License: MIT
Group: Development/Libraries
URL: https://github.com/DefinitelyTyped/DefinitelyTyped#readme
Source0: https://registry.npmjs.org/@types/istanbul-lib-report/-/istanbul-lib-report-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@types/istanbul-lib-coverage)
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n istanbul-lib-report 

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
