%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name gzip-size

Name: %{?scl_prefix}nodejs-gzip-size
Version: 3.0.0
Release: 1%{?dist}
Summary: Get the gzipped size of a string or buffer
License: MIT
Group: Development/Libraries
URL: https://github.com/sindresorhus/gzip-size#readme
Source0: https://registry.npmjs.org/gzip-size/-/gzip-size-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(duplexer) >= 0.1.1
Requires: npm(duplexer) < 0.2.0
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
