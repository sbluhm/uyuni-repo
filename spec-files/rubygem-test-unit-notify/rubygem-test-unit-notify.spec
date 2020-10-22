# Generated from test-unit-notify-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname test-unit-notify
%define version 1.0.4
%define release 1

Summary: A test result notify extension for test-unit.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/test-unit/test-unit-notify
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-test-unit >= 2.4.9
Requires: rubygem-bundler 
Requires: rubygem-rake 
Requires: rubygem-yard 
Requires: rubygem-packnga 
Requires: rubygem-kramdown 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(test-unit-notify) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A test result notify extension for test-unit.
This provides test result notification support.


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
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/
%{gemdir}/gems/test-unit-notify-1.0.4/


%{gemdir}/cache/test-unit-notify-1.0.4.gem
%{gemdir}/specifications/test-unit-notify-1.0.4.gemspec

%changelog
