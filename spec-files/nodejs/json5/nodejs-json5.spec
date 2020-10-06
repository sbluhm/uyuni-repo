%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name json5

Name: %{?scl_prefix}nodejs-json5
Version: 0.5.1
Release: 1%{?dist}
Summary: JSON for the ES5 era
License: MIT
Group: Development/Libraries
URL: http://json5.org/
Source0: https://registry.npmjs.org/json5/-/json5-%{version}.tgz
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
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/lib/cli.js
ln -sf %{nodejs_sitelib}/%{npm_name}/lib/cli.js %{buildroot}%{_bindir}/json5

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/json5
%license LICENSE.md
%doc CHANGELOG.md
%doc README.md

%changelog
