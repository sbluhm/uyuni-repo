# Generated from webrat-0.7.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname webrat
%define version 0.7.3
%define release 1

Summary: Ruby Acceptance Testing for Web applications
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/brynary/webrat
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-nokogiri >= 1.2.0
Requires: rubygem-rack >= 1.0
Requires: rubygem-rack-test >= 0.5.3
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(webrat) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Webrat lets you quickly write expressive and robust acceptance tests
for a Ruby web application. It supports simulating a browser inside
a Ruby process to avoid the performance hit and browser dependency of
Selenium or Watir, but the same API can also be used to drive real
Selenium tests when necessary (eg. for testing AJAX interactions).
Most Ruby web frameworks and testing frameworks are supported.


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
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/path
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/path
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/path
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/path
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/
%{gemdir}/gems/webrat-0.7.3/


%{gemdir}/cache/webrat-0.7.3.gem
%{gemdir}/specifications/webrat-0.7.3.gemspec

%changelog
