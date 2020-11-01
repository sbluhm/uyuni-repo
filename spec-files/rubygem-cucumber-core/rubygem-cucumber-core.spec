# Generated from cucumber-core-8.0.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname cucumber-core
%define version 8.0.1
%define release 1

Summary: cucumber-core-8.0.1
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://cucumber.io
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-cucumber-gherkin >= 15.0
Requires: rubygem-cucumber-gherkin < 16
Requires: rubygem-cucumber-gherkin >= 15.0.2
Requires: rubygem-cucumber-messages >= 13.0
Requires: rubygem-cucumber-messages < 14
Requires: rubygem-cucumber-messages >= 13.0.1
Requires: rubygem-cucumber-tag-expressions >= 2.0
Requires: rubygem-cucumber-tag-expressions < 3
Requires: rubygem-cucumber-tag-expressions >= 2.0.4
Requires: rubygem-coveralls >= 0.8
Requires: rubygem-coveralls < 1
Requires: rubygem-coveralls >= 0.8.23
Requires: rubygem-rake >= 13.0
Requires: rubygem-rake < 14
Requires: rubygem-rake >= 13.0.1
Requires: rubygem-rubocop >= 0.89
Requires: rubygem-rubocop < 1
Requires: rubygem-rubocop >= 0.89.1
Requires: rubygem-rspec >= 3.9
Requires: rubygem-rspec < 4
Requires: rubygem-rspec >= 3.9.0
Requires: rubygem-unindent >= 1.0
Requires: rubygem-unindent < 2
Requires: rubygem-unindent >= 1.0
BuildRequires: ruby >= 2.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(cucumber-core) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Core library for the Cucumber BDD app.

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
%{gemdir}/gems/cucumber-core-8.0.1/

%{gemdir}/cache/cucumber-core-8.0.1.gem
%{gemdir}/specifications/cucumber-core-8.0.1.gemspec

%changelog
