%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @jest/test-sequencer

Name: %{?scl_prefix}nodejs-jest-test-sequencer
Version: 24.9.0
Release: 1%{?dist}
Summary: FIXME
License: MIT
Group: Development/Libraries
URL: https://github.com/facebook/jest#readme
Source0: https://registry.npmjs.org/@jest/test-sequencer/-/test-sequencer-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@jest/test-result) >= 24.9.0
Requires: npm(@jest/test-result) < 25.0.0
Requires: npm(jest-haste-map) >= 24.9.0
Requires: npm(jest-haste-map) < 25.0.0
Requires: npm(jest-runner) >= 24.9.0
Requires: npm(jest-runner) < 25.0.0
Requires: npm(jest-runtime) >= 24.9.0
Requires: npm(jest-runtime) < 25.0.0
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

%changelog
