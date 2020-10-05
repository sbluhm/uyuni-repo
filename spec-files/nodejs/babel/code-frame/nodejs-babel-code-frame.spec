%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/code-frame

Name: %{?scl_prefix}nodejs-babel-code-frame
Version: 7.10.4
Release: 1%{?dist}
Summary: Generate errors that contain a code frame that point to source locations
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: https://registry.npmjs.org/@babel/code-frame/-/code-frame-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/highlight) >= 7.10.4
Requires: npm(@babel/highlight) < 8.0.0
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
