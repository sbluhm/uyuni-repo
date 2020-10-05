%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @emotion/core

Name: %{?scl_prefix}nodejs-emotion-core
Version: 10.0.35
Release: 1%{?dist}
Summary: FIXME
License: MIT
Group: Development/Libraries
URL: https://github.com/emotion-js/emotion/tree/master/packages/core
Source0: https://registry.npmjs.org/@emotion/core/-/core-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/runtime) >= 7.5.5
Requires: npm(@babel/runtime) < 8.0.0
Requires: npm(@emotion/cache) >= 10.0.27
Requires: npm(@emotion/cache) < 11.0.0
Requires: npm(@emotion/css) >= 10.0.27
Requires: npm(@emotion/css) < 11.0.0
Requires: npm(@emotion/serialize) >= 0.11.15
Requires: npm(@emotion/serialize) < 0.12.0
Requires: npm(@emotion/sheet) = 0.9.4
Requires: npm(@emotion/utils) = 0.11.3
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr types %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
