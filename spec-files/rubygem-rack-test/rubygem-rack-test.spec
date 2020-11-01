# Generated from rack-test-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rack-test
%define version 1.1.0
%define release 1

Summary: Simple testing API built on Rack
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/rack-test/rack-test
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.2.2
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rack >= 1.0
Requires: rubygem-rack < 3
Requires: rubygem-rake >= 12.0
Requires: rubygem-rake < 13
Requires: rubygem-rspec >= 3.6
Requires: rubygem-rspec < 4
Requires: rubygem-sinatra >= 1.0
Requires: rubygem-sinatra < 3
Requires: rubygem-rdoc >= 5.1
Requires: rubygem-rdoc < 6
Requires: rubygem-rubocop >= 0.49
Requires: rubygem-rubocop < 0.50
Requires: rubygem-simplecov >= 0.16
Requires: rubygem-simplecov < 1
Requires: rubygem-thor >= 0.19
Requires: rubygem-thor < 1
BuildRequires: ruby >= 2.2.2
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rack-test) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries
to build on. Most of its initial functionality is an extraction of Merb 1.0's
request helpers feature.

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
%{gemdir}/gems/rack-test-1.1.0/

%{gemdir}/cache/rack-test-1.1.0.gem
%{gemdir}/specifications/rack-test-1.1.0.gemspec

%changelog
