# Generated from webdrivers-4.4.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname webdrivers
%define version 4.4.1
%define release 1

Summary: Easy download and use of browser drivers.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/titusfortner/webdrivers
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.4.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-ffi >= 1.0
Requires: rubygem-ffi < 2
Requires: rubygem-rake >= 12.0
Requires: rubygem-rake < 13
Requires: rubygem-rspec >= 3.0
Requires: rubygem-rspec < 4
Requires: rubygem-rubocop >= 0.66
Requires: rubygem-rubocop < 1
Requires: rubygem-rubocop-performance 
Requires: rubygem-rubocop-rspec >= 1.32
Requires: rubygem-rubocop-rspec < 2
Requires: rubygem-simplecov >= 0.16
Requires: rubygem-simplecov < 1
Requires: rubygem-nokogiri >= 1.6
Requires: rubygem-nokogiri < 2
Requires: rubygem-rubyzip >= 1.3.0
Requires: rubygem-selenium-webdriver >= 3.0
Requires: rubygem-selenium-webdriver < 4.0
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(webdrivers) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Run Selenium tests more easily with install and updates for all supported
webdrivers.

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
%{gemdir}/gems/webdrivers-4.4.1/

%{gemdir}/cache/webdrivers-4.4.1.gem
%{gemdir}/specifications/webdrivers-4.4.1.gemspec

%changelog
