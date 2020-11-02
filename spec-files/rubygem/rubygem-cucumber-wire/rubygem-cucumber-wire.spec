# Generated from cucumber-wire-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname cucumber-wire
%define version 0.0.1
%define release 1

Summary: cucumber-wire-0.0.1
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://cucumber.io
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-cucumber >= 2.1.0
Requires: rubygem-cucumber < 2.2
Requires: rubygem-bundler >= 1.3.5
Requires: rubygem-rake >= 0.9.2
Requires: rubygem-rspec >= 3
Requires: rubygem-rspec < 4
Requires: rubygem-aruba 
Requires: rubygem-aruba < 1
BuildRequires: ruby >= 1.9.3
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
%{gemdir}/gems/cucumber-wire-0.0.1/

%{gemdir}/cache/cucumber-wire-0.0.1.gem
%{gemdir}/specifications/cucumber-wire-0.0.1.gemspec

%changelog
