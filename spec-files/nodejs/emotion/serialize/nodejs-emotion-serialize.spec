%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @emotion/serialize

Name: %{?scl_prefix}nodejs-emotion-serialize
Version: 0.11.15
Release: 1%{?dist}
Summary: serialization utils for emotion
License: MIT
Group: Development/Libraries
URL: https://github.com/emotion-js/emotion/tree/master/packages/serialize
Source0: https://registry.npmjs.org/@emotion/serialize/-/serialize-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@emotion/hash) = 0.7.4
Requires: npm(@emotion/memoize) = 0.7.4
Requires: npm(@emotion/unitless) = 0.7.5
Requires: npm(@emotion/utils) = 0.11.3
Requires: npm(csstype) >= 2.5.7
Requires: npm(csstype) < 3.0.0
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

%changelog
