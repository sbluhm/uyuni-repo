# Generated from test-unit-3.3.6.gem by gem2rpm -*- rpm-spec -*-
%define rbname test-unit
%define version 3.3.6
%define release 1

Summary: An xUnit family unit testing framework for Ruby.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://test-unit.github.io/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-power_assert 
Requires: rubygem-bundler 
Requires: rubygem-rake 
Requires: rubygem-yard 
Requires: rubygem-kramdown 
Requires: rubygem-packnga 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(test-unit) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
test-unit (Test::Unit) is unit testing framework for Ruby, based on xUnit
principles. These were originally designed by Kent Beck, creator of extreme
programming software development methodology, for Smalltalk's SUnit. It allows
writing tests, checking results and automated testing in Ruby.

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
%{gemdir}/gems/test-unit-3.3.6/

%{gemdir}/cache/test-unit-3.3.6.gem
%{gemdir}/specifications/test-unit-3.3.6.gemspec

%changelog
