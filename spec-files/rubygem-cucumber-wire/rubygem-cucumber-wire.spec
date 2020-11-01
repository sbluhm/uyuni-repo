# Generated from cucumber-wire-4.0.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname cucumber-wire
%define version 4.0.1
%define release 1

Summary: cucumber-wire-4.0.1
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://cucumber.io
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-cucumber-core >= 8.0
Requires: rubygem-cucumber-core < 9
Requires: rubygem-cucumber-core >= 8.0.1
Requires: rubygem-cucumber-cucumber-expressions >= 10.3
Requires: rubygem-cucumber-cucumber-expressions < 11
Requires: rubygem-cucumber-cucumber-expressions >= 10.3.0
Requires: rubygem-cucumber-messages >= 13.0
Requires: rubygem-cucumber-messages < 14
Requires: rubygem-cucumber-messages >= 13.0.1
Requires: rubygem-cucumber >= 4.1
Requires: rubygem-cucumber < 5
Requires: rubygem-cucumber >= 4.1.0
Requires: rubygem-rake >= 13.0
Requires: rubygem-rake < 14
Requires: rubygem-rake >= 13.0.1
Requires: rubygem-rspec >= 3.9
Requires: rubygem-rspec < 4
Requires: rubygem-rspec >= 3.9.0
Requires: rubygem-aruba >= 1.0
Requires: rubygem-aruba < 2
Requires: rubygem-aruba >= 1.0.2
BuildRequires: ruby >= 2.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(cucumber-wire) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Wire protocol for Cucumber.

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
%{gemdir}/gems/cucumber-wire-4.0.1/

%{gemdir}/cache/cucumber-wire-4.0.1.gem
%{gemdir}/specifications/cucumber-wire-4.0.1.gemspec

%changelog
