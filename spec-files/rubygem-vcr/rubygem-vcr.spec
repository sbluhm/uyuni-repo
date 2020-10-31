# Generated from vcr-3.0.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname vcr
%define version 3.0.3
%define release 1

Summary: Record your test suite's HTTP interactions and replay them during future test runs for fast, deterministic, accurate tests.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://vcr.github.io/vcr
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler >= 1.3
Requires: rubygem-bundler < 2
Requires: rubygem-rspec >= 3.0
Requires: rubygem-rspec < 4
Requires: rubygem-test-unit >= 3.1.4
Requires: rubygem-test-unit < 3.2
Requires: rubygem-rake >= 10.1
Requires: rubygem-rake < 11
Requires: rubygem-pry >= 0.9
Requires: rubygem-pry < 1
Requires: rubygem-pry-doc >= 0.6
Requires: rubygem-pry-doc < 1
Requires: rubygem-codeclimate-test-reporter >= 0.4
Requires: rubygem-codeclimate-test-reporter < 1
Requires: rubygem-yard 
Requires: rubygem-rack 
Requires: rubygem-fakeweb 
Requires: rubygem-webmock 
Requires: rubygem-cucumber >= 2.0.2
Requires: rubygem-cucumber < 2.1
Requires: rubygem-aruba >= 0.5.3
Requires: rubygem-aruba < 0.6
Requires: rubygem-faraday 
Requires: rubygem-httpclient 
Requires: rubygem-excon 
Requires: rubygem-timecop 
Requires: rubygem-multi_json 
Requires: rubygem-json 
Requires: rubygem-relish 
Requires: rubygem-mime-types 
Requires: rubygem-sinatra 
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(vcr) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Record your test suite's HTTP interactions and replay them during future test
runs for fast, deterministic, accurate tests.

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
%{gemdir}/gems/vcr-3.0.3/

%{gemdir}/cache/vcr-3.0.3.gem
%{gemdir}/specifications/vcr-3.0.3.gemspec

%changelog
