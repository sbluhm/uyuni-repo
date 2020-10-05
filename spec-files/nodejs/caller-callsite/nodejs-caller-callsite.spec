%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name caller-callsite

Name: %{?scl_prefix}nodejs-caller-callsite
Version: 2.0.0
Release: 1%{?dist}
Summary: Get the callsite of the caller function
License: MIT
Group: Development/Libraries
URL: https://github.com/sindresorhus/caller-callsite#readme
Source0: https://registry.npmjs.org/caller-callsite/-/caller-callsite-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(callsites) >= 2.0.0
Requires: npm(callsites) < 3.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package 

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license license
%doc readme.md

%changelog
