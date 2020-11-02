# Generated from shoulda-matchers-4.4.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname shoulda-matchers
%define version 4.4.1
%define release 1

Summary: Simple one-liner tests for common Rails functionality
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://matchers.shoulda.io/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.4.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-activesupport >= 4.2.0
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(shoulda-matchers) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Shoulda Matchers provides RSpec- and Minitest-compatible one-liners to test
common Rails functionality that, if written by hand, would be much longer,
more complex, and error-prone.


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
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/
%{gemdir}/gems/shoulda-matchers-4.4.1/


%{gemdir}/cache/shoulda-matchers-4.4.1.gem
%{gemdir}/specifications/shoulda-matchers-4.4.1.gemspec

%changelog
