%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name grunt-legacy-util

Name: %{?scl_prefix}nodejs-grunt-legacy-util
Version: 1.1.1
Release: 1%{?dist}
Summary: Some old grunt utils provided for backwards compatibility
License: MIT
Group: Development/Libraries
URL: http://gruntjs.com/
Source0: https://registry.npmjs.org/grunt-legacy-util/-/grunt-legacy-util-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(async) >= 1.5.2
Requires: npm(async) < 1.6.0
Requires: npm(exit) >= 0.1.1
Requires: npm(exit) < 0.2.0
Requires: npm(getobject) >= 0.1.0
Requires: npm(getobject) < 0.2.0
Requires: npm(hooker) >= 0.2.3
Requires: npm(hooker) < 0.3.0
Requires: npm(lodash) >= 4.17.10
Requires: npm(lodash) < 4.18.0
Requires: npm(underscore.string) >= 3.3.4
Requires: npm(underscore.string) < 3.4.0
Requires: npm(which) >= 1.3.0
Requires: npm(which) < 1.4.0
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
