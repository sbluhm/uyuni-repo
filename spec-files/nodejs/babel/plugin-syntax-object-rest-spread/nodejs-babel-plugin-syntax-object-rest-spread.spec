%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/plugin-syntax-object-rest-spread

Name: %{?scl_prefix}nodejs-babel-plugin-syntax-object-rest-spread
Version: 7.8.3
Release: 1%{?dist}
Summary: Allow parsing of object rest/spread
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-object-rest-spread
Source0: https://registry.npmjs.org/@babel/plugin-syntax-object-rest-spread/-/plugin-syntax-object-rest-spread-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/helper-plugin-utils) >= 7.8.0
Requires: npm(@babel/helper-plugin-utils) < 8.0.0
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
