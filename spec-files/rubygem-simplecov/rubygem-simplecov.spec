# Generated from simplecov-0.19.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname simplecov
%define version 0.19.1
%define release 1
%global debug_package %{nil}

Summary: Code coverage for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/simplecov-ruby/simplecov
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.5.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-docile >= 1.1
Requires: rubygem-docile < 2
Requires: rubygem-simplecov-html >= 0.11
Requires: rubygem-simplecov-html < 1
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(simplecov) = %{version}
Provides:	rubygem-rcov

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Code coverage for Ruby with a powerful configuration library and automatic
merging of coverage across test suites.


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
%{gemdir}/gems/simplecov-0.19.1/
%{gemdir}/cache/simplecov-0.19.1.gem
%{gemdir}/specifications/simplecov-0.19.1.gemspec

%changelog
