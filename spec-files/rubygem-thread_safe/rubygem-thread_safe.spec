# Generated from thread_safe-0.3.6.gem by gem2rpm -*- rpm-spec -*-
%define rbname thread_safe
%define version 0.3.6
%define release 1

Summary: Thread-safe collections and utilities for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ruby-concurrency/thread_safe
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-atomic = 1.1.16
Requires: rubygem-rake < 12.0
Requires: rubygem-rspec >= 3.2
Requires: rubygem-rspec < 4
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(thread_safe) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A collection of data structures and utilities to make thread-safe programming
in Ruby easier.


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
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/
%{gemdir}/gems/thread_safe-0.3.6/


%{gemdir}/cache/thread_safe-0.3.6.gem
%{gemdir}/specifications/thread_safe-0.3.6.gemspec

%changelog
