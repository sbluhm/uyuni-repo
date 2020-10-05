%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name es6-weak-map

Name: %{?scl_prefix}nodejs-es6-weak-map
Version: 2.0.1
Release: 1%{?dist}
Summary: ECMAScript6 WeakMap polyfill
License: MIT
Group: Development/Libraries
URL: https://github.com/medikoo/es6-weak-map#readme
Source0: https://registry.npmjs.org/es6-weak-map/-/es6-weak-map-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(d) >= 0.1.1
Requires: npm(d) < 0.2.0
Requires: npm(es5-ext) >= 0.10.8
Requires: npm(es5-ext) < 0.11.0
Requires: npm(es6-iterator) >= 2.0.0
Requires: npm(es6-iterator) < 3.0.0
Requires: npm(es6-symbol) >= 3.0.0
Requires: npm(es6-symbol) < 4.0.0
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
cp -pfr implement.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr is-implemented.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr is-native-implemented.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr is-weak-map.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr polyfill.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr valid-weak-map.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
