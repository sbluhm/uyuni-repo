%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @jest/test-result

Name: %{?scl_prefix}nodejs-jest-test-result
Version: 24.9.0
Release: 1%{?dist}
Summary: FIXME
License: MIT
Group: Development/Libraries
URL: https://github.com/facebook/jest#readme
Source0: https://registry.npmjs.org/@jest/test-result/-/test-result-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@jest/console) >= 24.9.0
Requires: npm(@jest/console) < 25.0.0
Requires: npm(@jest/types) >= 24.9.0
Requires: npm(@jest/types) < 25.0.0
Requires: npm(@types/istanbul-lib-coverage) >= 2.0.0
Requires: npm(@types/istanbul-lib-coverage) < 3.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr build %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE

%changelog
