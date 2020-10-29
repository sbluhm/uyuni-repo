# Generated from capybara-3.33.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname capybara
%define version 3.33.0
%define release 1

Summary: Capybara aims to simplify the process of integration testing Rack applications, such as Rails, Sinatra or Merb
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/teamcapybara/capybara
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.5.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-addressable 
Requires: rubygem-mini_mime >= 0.1.3
Requires: rubygem-nokogiri >= 1.8
Requires: rubygem-nokogiri < 2
Requires: rubygem-rack >= 1.6.0
Requires: rubygem-rack-test >= 0.6.3
Requires: rubygem-regexp_parser >= 1.5
Requires: rubygem-regexp_parser < 2
Requires: rubygem-xpath >= 3.2
Requires: rubygem-xpath < 4
Requires: rubygem-byebug 
Requires: rubygem-coveralls 
Requires: rubygem-cucumber >= 2.3.0
Requires: rubygem-erubi 
Requires: rubygem-irb 
Requires: rubygem-launchy >= 2.0.4
Requires: rubygem-minitest 
Requires: rubygem-puma 
Requires: rubygem-rake 
Requires: rubygem-rspec >= 3.5.0
Requires: rubygem-rspec-instafail 
Requires: rubygem-rubocop >= 0.72
Requires: rubygem-rubocop < 1
Requires: rubygem-rubocop-performance 
Requires: rubygem-rubocop-rspec 
Requires: rubygem-sauce_whisk 
Requires: rubygem-selenium-webdriver >= 3.5
Requires: rubygem-selenium-webdriver < 4
Requires: rubygem-selenium_statistics 
Requires: rubygem-sinatra >= 1.4.0
Requires: rubygem-uglifier 
Requires: rubygem-webdrivers >= 3.6.0
Requires: rubygem-yard >= 0.9.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(capybara) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Capybara is an integration testing tool for rack based web applications. It
simulates how a user would interact with a website.


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
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/path
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/path
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/path
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/path
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/path
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/path
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/path
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/path
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/path
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/path
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/
%{gemdir}/gems/capybara-3.33.0/path


%{gemdir}/cache/capybara-3.33.0.gem
%{gemdir}/specifications/capybara-3.33.0.gemspec

%changelog
