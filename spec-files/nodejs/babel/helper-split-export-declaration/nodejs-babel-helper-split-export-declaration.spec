%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/helper-split-export-declaration

Name: %{?scl_prefix}nodejs-babel-helper-split-export-declaration
Version: 7.11.0
Release: 1%{?dist}
Summary: 
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel#readme
Source0: https://registry.npmjs.org/@babel/helper-split-export-declaration/-/helper-split-export-declaration-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/types) >= 7.11.0
Requires: npm(@babel/types) < 8.0.0
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


%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
