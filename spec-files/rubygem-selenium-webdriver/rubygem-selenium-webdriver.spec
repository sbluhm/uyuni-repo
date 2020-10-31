# Generated from selenium-webdriver-3.142.7.gem by gem2rpm -*- rpm-spec -*-
%define rbname selenium-webdriver
%define version 3.142.7
%define release 1

Summary: The next generation developer focused tool for automated testing of webapps
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/SeleniumHQ/selenium
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-childprocess >= 0.5
Requires: rubygem-childprocess < 4.0
Requires: rubygem-rubyzip >= 1.2.2
Requires: rubygem-ffi 
Requires: rubygem-rack >= 2.0
Requires: rubygem-rack < 3
Requires: rubygem-rake 
Requires: rubygem-rspec >= 3.0
Requires: rubygem-rspec < 4
Requires: rubygem-rubocop >= 0.67.0
Requires: rubygem-rubocop < 0.68
Requires: rubygem-rubocop-performance 
Requires: rubygem-rubocop-rspec 
Requires: rubygem-webmock >= 3.5
Requires: rubygem-webmock < 4
Requires: rubygem-yard >= 0.9.11
Requires: rubygem-yard < 0.10
BuildRequires: ruby >= 2.3
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(selenium-webdriver) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
WebDriver is a tool for writing automated tests of websites. It aims to mimic
the behaviour of a real user, and as such interacts with the HTML of the
application.

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
%{gemdir}/gems/selenium-webdriver-3.142.7/

%{gemdir}/cache/selenium-webdriver-3.142.7.gem
%{gemdir}/specifications/selenium-webdriver-3.142.7.gemspec

%changelog
