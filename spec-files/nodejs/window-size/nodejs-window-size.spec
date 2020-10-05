%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name window-size

Name: %{?scl_prefix}nodejs-window-size
Version: 0.1.0
Release: 1%{?dist}
Summary: Reliable way to to get the height and width of the terminal/console in a node
License: MIT
Group: Development/Libraries
URL: https://github.com/jonschlinkert/window-size
Source0: https://registry.npmjs.org/window-size/-/window-size-%{version}.tgz
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
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE-MIT
%doc README.md

%changelog
