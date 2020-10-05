%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name samsam

Name: %{?scl_prefix}nodejs-samsam
Version: 1.1.2
Release: 1%{?dist}
Summary: Value identification and comparison functions
License: FIXME
Group: Development/Libraries
URL: http://busterjs.org/docs/buster-assertions
Source0: https://registry.npmjs.org/samsam/-/samsam-%{version}.tgz
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
cp -pfr autolint.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr jsTestDriver.conf %{buildroot}%{nodejs_sitelib}/%{npm_name}
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
