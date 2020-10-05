%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name readdirp

Name: %{?scl_prefix}nodejs-readdirp
Version: 0.2.2
Release: 1%{?dist}
Summary: Recursive version of fs
License: MIT
Group: Development/Libraries
URL: https://github.com/thlorenz/readdirp
Source0: https://registry.npmjs.org/readdirp/-/readdirp-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(minimatch) >= 0.2.4
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package 

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr examples %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr readdirp.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr stream-api.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
