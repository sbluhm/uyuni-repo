%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name grunt-known-options

Name: %{?scl_prefix}nodejs-grunt-known-options
Version: 1.1.0
Release: 1%{?dist}
Summary: The known options used in Grunt
License: MIT
Group: Development/Libraries
URL: http://gruntjs.com/
Source0: https://registry.npmjs.org/grunt-known-options/-/grunt-known-options-%{version}.tgz
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
%doc README.md

%changelog
