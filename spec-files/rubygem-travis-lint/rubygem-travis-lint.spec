# Generated from travis-lint-1.4.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname travis-lint
%define version 1.4.0
%define release 1

Summary: Checks your .travis.yml for possible issues, deprecations and so on
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/travis-ci
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-hashr >= 0.0.19
Requires: rubygem-rspec >= 2.8.0
Requires: rubygem-rspec < 2.9
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(travis-lint) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
travis-lint is a tool that check your .travis.yml for possible issues,
deprecations and so on. Recommended for all travis-ci.org users.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/gems/%{rbname}-%{version}/bin/** %{buildroot}/%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{_bindir}/travis-lint
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/
%{gemdir}/gems/travis-lint-1.4.0/


%{gemdir}/cache/travis-lint-1.4.0.gem
%{gemdir}/specifications/travis-lint-1.4.0.gemspec

%changelog
