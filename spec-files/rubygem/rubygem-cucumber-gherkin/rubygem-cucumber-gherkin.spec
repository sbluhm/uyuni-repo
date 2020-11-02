# Generated from cucumber-gherkin-15.0.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname cucumber-gherkin
%define version 15.0.2
%define release 1

Summary: cucumber-gherkin-15.0.2
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/cucumber/gherkin-ruby
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-cucumber-messages >= 13.0
Requires: rubygem-cucumber-messages < 14
Requires: rubygem-cucumber-messages >= 13.0.1
Requires: rubygem-rake >= 13.0
Requires: rubygem-rake < 14
Requires: rubygem-rake >= 13.0.1
Requires: rubygem-rspec >= 3.9
Requires: rubygem-rspec < 4
Requires: rubygem-rspec >= 3.9.0
BuildRequires: ruby >= 2.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(cucumber-gherkin) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Gherkin parser.

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
%{_bindir}/gherkin-ruby
%{_bindir}/gherkin
%{gemdir}/gems/cucumber-gherkin-15.0.2/

%{gemdir}/cache/cucumber-gherkin-15.0.2.gem
%{gemdir}/specifications/cucumber-gherkin-15.0.2.gemspec

%changelog
