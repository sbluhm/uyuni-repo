%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name formatio

Name: %{?scl_prefix}nodejs-formatio
Version: 1.2.0
Release: 1%{?dist}
Summary: Human-readable object formatting
License: BSD-3-Clause
Group: Development/Libraries
URL: http://busterjs.org/docs/formatio/
Source0: https://registry.npmjs.org/formatio/-/formatio-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(samsam) >= 1.0.0
Requires: npm(samsam) < 2.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package 

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr appveyor.yml %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr autolint.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr buster.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc AUTHORS
%doc Readme.md

%changelog
