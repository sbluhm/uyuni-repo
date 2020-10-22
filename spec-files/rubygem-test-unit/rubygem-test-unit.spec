# Generated from test-unit-2.5.5.gem by gem2rpm -*- rpm-spec -*-
%define rbname test-unit
%define version 2.5.5
%define release 1

Summary: test-unit - Improved version of Test::Unit bundled in Ruby 1.8.x.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://test-unit.rubyforge.org/
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler 
Requires: rubygem-rake 
Requires: rubygem-yard 
Requires: rubygem-RedCloth 
Requires: rubygem-packnga 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(test-unit) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Ruby 1.9.x bundles minitest not Test::Unit. Test::Unit
bundled in Ruby 1.8.x had not been improved but unbundled
Test::Unit (test-unit) is improved actively.


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
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/
%{gemdir}/gems/test-unit-2.5.5/


%{gemdir}/cache/test-unit-2.5.5.gem
%{gemdir}/specifications/test-unit-2.5.5.gemspec

%changelog
