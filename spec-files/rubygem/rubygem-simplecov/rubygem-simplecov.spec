# Generated from simplecov-0.17.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname simplecov
%define version 0.17.1
%define release 1

Summary: Code coverage for Ruby 1.9+ with a powerful configuration library and automatic merging of coverage across test suites
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/colszowka/simplecov
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 2.7.6.2
Requires: rubygem-json >= 1.8
Requires: rubygem-json < 3
Requires: rubygem-simplecov-html >= 0.10.0
Requires: rubygem-simplecov-html < 0.11
Requires: rubygem-docile >= 1.1
Requires: rubygem-docile < 2
Requires: rubygem-bundler 
Requires: rubygem-rake 
Requires: rubygem-rspec 
Requires: rubygem-test-unit 
Requires: rubygem-cucumber < 3
Requires: rubygem-aruba 
Requires: rubygem-capybara < 3
Requires: rubygem-phantomjs 
Requires: rubygem-poltergeist 
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(simplecov) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Code coverage for Ruby 1.9+ with a powerful configuration library and
automatic merging of coverage across test suites.

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
%{gemdir}/gems/simplecov-0.17.1/

%{gemdir}/cache/simplecov-0.17.1.gem
%{gemdir}/specifications/simplecov-0.17.1.gemspec

%changelog
