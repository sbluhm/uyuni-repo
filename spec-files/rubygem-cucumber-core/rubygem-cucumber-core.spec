# Generated from cucumber-core-1.4.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname cucumber-core
%define version 1.4.0
%define release 1

Summary: cucumber-core-1.4.0
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://cukes.info
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-gherkin >= 3.2.0
Requires: rubygem-gherkin < 3.3
Requires: rubygem-bundler >= 1.3.5
Requires: rubygem-rake >= 0.9.2
Requires: rubygem-rspec >= 3
Requires: rubygem-rspec < 4
Requires: rubygem-unindent >= 1.0
Requires: rubygem-kramdown >= 1.4.2
Requires: rubygem-kramdown < 1.5
Requires: rubygem-coveralls >= 0.7
Requires: rubygem-coveralls < 1
BuildRequires: ruby >= 1.9.3
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
%{gemdir}/gems/cucumber-core-1.4.0/

%{gemdir}/cache/cucumber-core-1.4.0.gem
%{gemdir}/specifications/cucumber-core-1.4.0.gemspec

%changelog
