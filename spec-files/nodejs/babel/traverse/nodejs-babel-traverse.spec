%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/traverse

Name: %{?scl_prefix}nodejs-babel-traverse
Version: 7.11.5
Release: 1%{?dist}
Summary: The Babel Traverse module maintains the overall tree state, and is responsible for replacing, removing, and adding nodes
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: https://registry.npmjs.org/@babel/traverse/-/traverse-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/code-frame) >= 7.10.4
Requires: npm(@babel/code-frame) < 8.0.0
Requires: npm(@babel/generator) >= 7.11.5
Requires: npm(@babel/generator) < 8.0.0
Requires: npm(@babel/helper-function-name) >= 7.10.4
Requires: npm(@babel/helper-function-name) < 8.0.0
Requires: npm(@babel/helper-split-export-declaration) >= 7.11.0
Requires: npm(@babel/helper-split-export-declaration) < 8.0.0
Requires: npm(@babel/parser) >= 7.11.5
Requires: npm(@babel/parser) < 8.0.0
Requires: npm(@babel/types) >= 7.11.5
Requires: npm(@babel/types) < 8.0.0
Requires: npm(debug) >= 4.1.0
Requires: npm(debug) < 5.0.0
Requires: npm(globals) >= 11.1.0
Requires: npm(globals) < 12.0.0
Requires: npm(lodash) >= 4.17.19
Requires: npm(lodash) < 5.0.0
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
