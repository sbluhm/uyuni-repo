%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name maxmin

Name: %{?scl_prefix}nodejs-maxmin
Version: 2.1.0
Release: 1%{?dist}
Summary: Get a pretty output of the original, minified, gzipped size of a string or buffer: 130 B → 91 B → 53 B (gzip)
License: MIT
Group: Development/Libraries
URL: https://github.com/sindresorhus/maxmin#readme
Source0: https://registry.npmjs.org/maxmin/-/maxmin-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(chalk) >= 1.0.0
Requires: npm(chalk) < 2.0.0
Requires: npm(figures) >= 1.0.1
Requires: npm(figures) < 2.0.0
Requires: npm(gzip-size) >= 3.0.0
Requires: npm(gzip-size) < 4.0.0
Requires: npm(pretty-bytes) >= 3.0.0
Requires: npm(pretty-bytes) < 4.0.0
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
%license license
%doc readme.md

%changelog
