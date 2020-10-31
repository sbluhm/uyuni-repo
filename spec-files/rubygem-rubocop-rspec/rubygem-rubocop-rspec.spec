# Generated from rubocop-rspec-1.44.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname rubocop-rspec
%define version 1.44.1
%define release 1

Summary: Code style checking for RSpec files
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/rubocop-hq/rubocop-rspec
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.4.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rubocop >= 0.87
Requires: rubygem-rubocop < 1
Requires: rubygem-rubocop-ast >= 0.7.1
Requires: rubygem-rack 
Requires: rubygem-rake 
Requires: rubygem-rspec >= 3.4
Requires: rubygem-rubocop-performance >= 1.7
Requires: rubygem-rubocop-performance < 2
Requires: rubygem-simplecov < 0.18
Requires: rubygem-yard 
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rubocop-rspec) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Code style checking for RSpec files.
A plugin for the RuboCop code style enforcing & linting tool.

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
%{gemdir}/gems/rubocop-rspec-1.44.1/

%{gemdir}/cache/rubocop-rspec-1.44.1.gem
%{gemdir}/specifications/rubocop-rspec-1.44.1.gemspec

%changelog
