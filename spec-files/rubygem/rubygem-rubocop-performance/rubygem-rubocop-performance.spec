# Generated from rubocop-performance-1.8.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname rubocop-performance
%define version 1.8.1
%define release 1

Summary: Automatic performance checking tool for Ruby code.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/rubocop-hq/rubocop-performance
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.4.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rubocop >= 0.87.0
Requires: rubygem-rubocop-ast >= 0.4.0
Requires: rubygem-simplecov 
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rubocop-performance) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A collection of RuboCop cops to check for performance optimizations
in Ruby code.

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
%{gemdir}/gems/rubocop-performance-1.8.1/

%{gemdir}/cache/rubocop-performance-1.8.1.gem
%{gemdir}/specifications/rubocop-performance-1.8.1.gemspec

%changelog
