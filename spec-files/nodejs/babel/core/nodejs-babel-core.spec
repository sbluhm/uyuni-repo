%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/core

Name: %{?scl_prefix}nodejs-babel-core
Version: 7.11.6
Release: 1%{?dist}
Summary: Babel compiler core
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: https://registry.npmjs.org/@babel/core/-/core-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/code-frame) >= 7.10.4
Requires: npm(@babel/code-frame) < 8.0.0
Requires: npm(@babel/generator) >= 7.11.6
Requires: npm(@babel/generator) < 8.0.0
Requires: npm(@babel/helper-module-transforms) >= 7.11.0
Requires: npm(@babel/helper-module-transforms) < 8.0.0
Requires: npm(@babel/helpers) >= 7.10.4
Requires: npm(@babel/helpers) < 8.0.0
Requires: npm(@babel/parser) >= 7.11.5
Requires: npm(@babel/parser) < 8.0.0
Requires: npm(@babel/template) >= 7.10.4
Requires: npm(@babel/template) < 8.0.0
Requires: npm(@babel/traverse) >= 7.11.5
Requires: npm(@babel/traverse) < 8.0.0
Requires: npm(@babel/types) >= 7.11.5
Requires: npm(@babel/types) < 8.0.0
Requires: npm(convert-source-map) >= 1.7.0
Requires: npm(convert-source-map) < 2.0.0
Requires: npm(debug) >= 4.1.0
Requires: npm(debug) < 5.0.0
Requires: npm(gensync) >= 1.0.0-beta.1
Requires: npm(gensync) < 2.0.0
Requires: npm(json5) >= 2.1.2
Requires: npm(json5) < 3.0.0
Requires: npm(lodash) >= 4.17.19
Requires: npm(lodash) < 5.0.0
Requires: npm(resolve) >= 1.3.2
Requires: npm(resolve) < 2.0.0
Requires: npm(semver) >= 5.4.1
Requires: npm(semver) < 6.0.0
Requires: npm(source-map) >= 0.5.0
Requires: npm(source-map) < 0.6.0
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
