%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name next-tick

Name: %{?scl_prefix}nodejs-next-tick
Version: 0.2.2
Release: 1%{?dist}
Summary: Environment agnostic nextTick polyfill
License: MIT
Group: Development/Libraries
URL: https://github.com/medikoo/next-tick#readme
Source0: https://registry.npmjs.org/next-tick/-/next-tick-%{version}.tgz
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
cp -pfr CHANGES %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr LICENCE %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
