%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name bytes

Name: %{?scl_prefix}nodejs-bytes
Version: 3.1.0
Release: 1%{?dist}
Summary: Utility to parse a string bytes to bytes and vice-versa
License: MIT
Group: Development/Libraries
URL: https://github.com/visionmedia/bytes.js#readme
Source0: https://registry.npmjs.org/bytes/-/bytes-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
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
%license LICENSE
%doc History.md
%doc Readme.md

%changelog
