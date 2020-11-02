# Generated from selenium_statistics-0.3.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname selenium_statistics
%define version 0.3.0
%define release 1

Summary: Generate information about Selenium commands
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler 
Requires: rubygem-rspec 
Requires: rubygem-rake 
Requires: rubygem-selenium-webdriver 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(selenium_statistics) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Generate information about Selenium commands.

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
%{gemdir}/gems/selenium_statistics-0.3.0/

%{gemdir}/cache/selenium_statistics-0.3.0.gem
%{gemdir}/specifications/selenium_statistics-0.3.0.gemspec

%changelog
