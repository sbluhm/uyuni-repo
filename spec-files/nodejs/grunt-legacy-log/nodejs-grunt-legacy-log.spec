%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name grunt-legacy-log

Name: %{?scl_prefix}nodejs-grunt-legacy-log
Version: 2.0.0
Release: 1%{?dist}
Summary: The Grunt 0
License: MIT
Group: Development/Libraries
URL: http://gruntjs.com/
Source0: https://registry.npmjs.org/grunt-legacy-log/-/grunt-legacy-log-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(colors) >= 1.1.2
Requires: npm(colors) < 1.2.0
Requires: npm(grunt-legacy-log-utils) >= 2.0.0
Requires: npm(grunt-legacy-log-utils) < 2.1.0
Requires: npm(hooker) >= 0.2.3
Requires: npm(hooker) < 0.3.0
Requires: npm(lodash) >= 4.17.5
Requires: npm(lodash) < 4.18.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package 

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr CHANGELOG %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr appveyor.yml %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr examples.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE-MIT
%doc README.md

%changelog
