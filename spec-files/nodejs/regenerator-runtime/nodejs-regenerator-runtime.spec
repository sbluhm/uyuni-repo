%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name regenerator-runtime

Name: %{?scl_prefix}nodejs-regenerator-runtime
Version: 0.13.7
Release: 1%{?dist}
Summary: Runtime for Regenerator-compiled generator and async functions
License: MIT
Group: Development/Libraries
URL: https://github.com/facebook/regenerator/tree/master/packages/regenerator-runtime
Source0: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-%{version}.tgz
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
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr path.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr runtime.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
