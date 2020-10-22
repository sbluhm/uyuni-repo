# Generated from test-unit-rr-1.0.5.gem by gem2rpm -*- rpm-spec -*-
%define rbname test-unit-rr
%define version 1.0.5
%define release 1

Summary: test-unit-rr is a RR adapter for test-unit.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/test-unit/test-unit-rr
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-test-unit >= 2.5.2
Requires: rubygem-rr >= 1.1.1
Requires: rubygem-bundler 
Requires: rubygem-rake 
Requires: rubygem-packnga 
Requires: rubygem-kramdown 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(test-unit-rr) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
You don't need RR setup codes with test-unit-rr. You just require
"test/unit/rr".


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
%{gemdir}/gems/test-unit-rr-1.0.5/
%{gemdir}/gems/test-unit-rr-1.0.5/
%{gemdir}/gems/test-unit-rr-1.0.5/
%{gemdir}/gems/test-unit-rr-1.0.5/
%{gemdir}/gems/test-unit-rr-1.0.5/
%{gemdir}/gems/test-unit-rr-1.0.5/
%{gemdir}/gems/test-unit-rr-1.0.5/
%{gemdir}/gems/test-unit-rr-1.0.5/
%{gemdir}/gems/test-unit-rr-1.0.5/
%{gemdir}/gems/test-unit-rr-1.0.5/


%{gemdir}/cache/test-unit-rr-1.0.5.gem
%{gemdir}/specifications/test-unit-rr-1.0.5.gemspec

%changelog
