%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/helper-function-name

Name: %{?scl_prefix}nodejs-babel-helper-function-name
Version: 7.10.4
Release: 1%{?dist}
Summary: Helper function to change the property 'name' of every function
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel#readme
Source0: https://registry.npmjs.org/@babel/helper-function-name/-/helper-function-name-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/helper-get-function-arity) >= 7.10.4
Requires: npm(@babel/helper-get-function-arity) < 8.0.0
Requires: npm(@babel/template) >= 7.10.4
Requires: npm(@babel/template) < 8.0.0
Requires: npm(@babel/types) >= 7.10.4
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
