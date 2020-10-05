%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name pretty-bytes

Name: %{?scl_prefix}nodejs-pretty-bytes
Version: 3.0.0
Release: 1%{?dist}
Summary: Convert bytes to a human readable string: 1337 → 1
License: MIT
Group: Development/Libraries
URL: https://github.com/sindresorhus/pretty-bytes#readme
Source0: https://registry.npmjs.org/pretty-bytes/-/pretty-bytes-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(number-is-nan) >= 1.0.0
Requires: npm(number-is-nan) < 2.0.0
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
