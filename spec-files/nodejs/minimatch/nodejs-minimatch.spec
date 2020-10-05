%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name minimatch

Name: %{?scl_prefix}nodejs-minimatch
Version: 0.2.12
Release: 1%{?dist}
Summary: a glob matcher in javascript
License: [object Object]
Group: Development/Libraries
URL: https://github.com/isaacs/minimatch#readme
Source0: https://registry.npmjs.org/minimatch/-/minimatch-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(lru-cache) >= 2.0.0
Requires: npm(lru-cache) < 3.0.0
Requires: npm(sigmund) >= 1.0.0
Requires: npm(sigmund) < 1.1.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package 

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr minimatch.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
