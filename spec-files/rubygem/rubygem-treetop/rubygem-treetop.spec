# Generated from treetop-1.6.11.gem by gem2rpm -*- rpm-spec -*-
%define rbname treetop
%define version 1.6.11
%define release 1

Summary: A Ruby-based text parsing and interpretation DSL
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/cjheath/treetop
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-polyglot >= 0.3
Requires: rubygem-polyglot < 1
Requires: rubygem-activesupport >= 4
Requires: rubygem-activesupport < 5
Requires: rubygem-i18n >= 0.6
Requires: rubygem-i18n < 1
Requires: rubygem-rr >= 1.0
Requires: rubygem-rr < 2
Requires: rubygem-rspec >= 3
Requires: rubygem-rspec < 4
Requires: rubygem-rake >= 11
Requires: rubygem-rake < 12
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(treetop) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A Parsing Expression Grammar (PEG) Parser generator DSL for Ruby.

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
%{_bindir}/tt
%{gemdir}/gems/treetop-1.6.11/

%{gemdir}/cache/treetop-1.6.11.gem
%{gemdir}/specifications/treetop-1.6.11.gemspec

%changelog
