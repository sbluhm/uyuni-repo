%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @emotion/css

Name: %{?scl_prefix}nodejs-emotion-css
Version: 10.0.27
Release: 1%{?dist}
Summary: a function to serialize css and object styless
License: MIT
Group: Development/Libraries
URL: https://github.com/emotion-js/emotion/tree/master/packages/css
Source0: https://registry.npmjs.org/@emotion/css/-/css-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@emotion/serialize) >= 0.11.15
Requires: npm(@emotion/serialize) < 0.12.0
Requires: npm(@emotion/utils) = 0.11.3
Requires: npm(babel-plugin-emotion) >= 10.0.27
Requires: npm(babel-plugin-emotion) < 11.0.0
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
cp -pfr macro.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr macro.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr macro.js.flow %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr types %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md

%changelog
