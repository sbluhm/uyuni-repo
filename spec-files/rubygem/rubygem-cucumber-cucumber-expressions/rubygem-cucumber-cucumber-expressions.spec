# Generated from cucumber-cucumber-expressions-10.3.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname cucumber-cucumber-expressions
%define version 10.3.0
%define release 1

Summary: cucumber-expressions-10.3.0
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/cucumber/cucumber-expressions-ruby#readme
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake >= 13.0
Requires: rubygem-rake < 14
Requires: rubygem-rake >= 13.0.1
Requires: rubygem-rspec >= 3.9
Requires: rubygem-rspec < 4
Requires: rubygem-rspec >= 3.9.0
BuildRequires: ruby >= 2.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(cucumber-cucumber-expressions) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Cucumber Expressions - a simpler alternative to Regular Expressions.

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
%{gemdir}/gems/cucumber-cucumber-expressions-10.3.0/

%{gemdir}/cache/cucumber-cucumber-expressions-10.3.0.gem
%{gemdir}/specifications/cucumber-cucumber-expressions-10.3.0.gemspec

%changelog
