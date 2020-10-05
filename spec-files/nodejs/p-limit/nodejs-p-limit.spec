%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name p-limit

Name: %{?scl_prefix}nodejs-p-limit
Version: 1.3.0
Release: 1%{?dist}
Summary: Run multiple promise-returning & async functions with limited concurrency
License: MIT
Group: Development/Libraries
URL: https://github.com/sindresorhus/p-limit#readme
Source0: https://registry.npmjs.org/p-limit/-/p-limit-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(p-try) >= 1.0.0
Requires: npm(p-try) < 2.0.0
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
