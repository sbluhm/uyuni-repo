%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name http-errors

Name: %{?scl_prefix}nodejs-http-errors
Version: 1.7.3
Release: 1%{?dist}
Summary: Create HTTP error objects
License: MIT
Group: Development/Libraries
URL: https://github.com/jshttp/http-errors#readme
Source0: https://registry.npmjs.org/http-errors/-/http-errors-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(depd) >= 1.1.2
Requires: npm(depd) < 1.2.0
Requires: npm(inherits) = 2.0.4
Requires: npm(setprototypeof) = 1.1.1
Requires: npm(statuses) >= 1.5.0
Requires: npm(statuses) < 2.0.0
Requires: npm(toidentifier) = 1.0.0
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
%doc HISTORY.md
%doc README.md

%changelog
