%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/parser

Name: %{?scl_prefix}nodejs-babel-parser
Version: 7.11.5
Release: 1%{?dist}
Summary: A JavaScript parser
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: https://registry.npmjs.org/@babel/parser/-/parser-%{version}.tgz
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
cp -pfr bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr typings %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/babel-parser.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/babel-parser.js %{buildroot}%{_bindir}/parser


%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/parser
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
