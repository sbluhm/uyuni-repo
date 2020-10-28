# Generated from rspec-mocks-2.8.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rspec-mocks
%define version 2.8.0
%define release 1

Summary: rspec-mocks-2.8.0
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/rspec/rspec-mocks
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rspec-mocks) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
RSpec's 'test double' framework, with support for stubbing and mocking.


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
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/
%{gemdir}/gems/rspec-mocks-2.8.0/


%{gemdir}/cache/rspec-mocks-2.8.0.gem
%{gemdir}/specifications/rspec-mocks-2.8.0.gemspec

%changelog
