# Generated from octokit-4.19.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname octokit
%define version 4.19.0
%define release 1

Summary: Ruby toolkit for working with the GitHub API
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/octokit/octokit.rb
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler >= 1
Requires: rubygem-bundler < 3
Requires: rubygem-sawyer >= 0.5.3
Requires: rubygem-sawyer >= 0.8.0
Requires: rubygem-sawyer < 0.9
Requires: rubygem-faraday >= 0.9
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(octokit) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Simple wrapper for the GitHub API.

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{gemdir}/gems/octokit-4.19.0/

%{gemdir}/cache/octokit-4.19.0.gem
%{gemdir}/specifications/octokit-4.19.0.gemspec

%changelog
