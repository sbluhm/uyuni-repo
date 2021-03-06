%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name event-emitter

Name: %{?scl_prefix}nodejs-event-emitter
Version: 0.3.3
Release: 1%{?dist}
Summary: Environment agnostic event emitter
License: MIT
Group: Development/Libraries
URL: https://github.com/medikoo/event-emitter#readme
Source0: https://registry.npmjs.org/event-emitter/-/event-emitter-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(d) >= 0.1.1
Requires: npm(d) < 0.2.0
Requires: npm(es5-ext) >= 0.10.5
Requires: npm(es5-ext) < 0.11.0
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
cp -pfr all-off.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr benchmark %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr has-listeners.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr pipe.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr unify.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
