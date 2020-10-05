%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @jest/transform

Name: %{?scl_prefix}nodejs-jest-transform
Version: 24.9.0
Release: 1%{?dist}
Summary: FIXME
License: MIT
Group: Development/Libraries
URL: https://github.com/facebook/jest#readme
Source0: https://registry.npmjs.org/@jest/transform/-/transform-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/core) >= 7.1.0
Requires: npm(@babel/core) < 8.0.0
Requires: npm(@jest/types) >= 24.9.0
Requires: npm(@jest/types) < 25.0.0
Requires: npm(babel-plugin-istanbul) >= 5.1.0
Requires: npm(babel-plugin-istanbul) < 6.0.0
Requires: npm(chalk) >= 2.0.1
Requires: npm(chalk) < 3.0.0
Requires: npm(convert-source-map) >= 1.4.0
Requires: npm(convert-source-map) < 2.0.0
Requires: npm(fast-json-stable-stringify) >= 2.0.0
Requires: npm(fast-json-stable-stringify) < 3.0.0
Requires: npm(graceful-fs) >= 4.1.15
Requires: npm(graceful-fs) < 5.0.0
Requires: npm(jest-haste-map) >= 24.9.0
Requires: npm(jest-haste-map) < 25.0.0
Requires: npm(jest-regex-util) >= 24.9.0
Requires: npm(jest-regex-util) < 25.0.0
Requires: npm(jest-util) >= 24.9.0
Requires: npm(jest-util) < 25.0.0
Requires: npm(micromatch) >= 3.1.10
Requires: npm(micromatch) < 4.0.0
Requires: npm(pirates) >= 4.0.1
Requires: npm(pirates) < 5.0.0
Requires: npm(realpath-native) >= 1.1.0
Requires: npm(realpath-native) < 2.0.0
Requires: npm(slash) >= 2.0.0
Requires: npm(slash) < 3.0.0
Requires: npm(source-map) >= 0.6.1
Requires: npm(source-map) < 0.7.0
Requires: npm(write-file-atomic) = 2.4.1
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
