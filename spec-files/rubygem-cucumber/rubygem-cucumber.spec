# Generated from cucumber-2.3.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname cucumber
%define version 2.3.0
%define release 1

Summary: cucumber-2.3.0
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
Requires: rubygem-cucumber-core >= 1.4.0
Requires: rubygem-cucumber-core < 1.5
Requires: rubygem-builder >= 2.1.2
Requires: rubygem-diff-lcs >= 1.1.3
Requires: rubygem-gherkin >= 3.2.0
Requires: rubygem-gherkin < 3.3
Requires: rubygem-multi_json >= 1.7.5
Requires: rubygem-multi_json < 2.0
Requires: rubygem-multi_test >= 0.1.2
Requires: rubygem-cucumber-wire >= 0.0.1
Requires: rubygem-cucumber-wire < 0.1
Requires: rubygem-event-bus >= 0.1.0
Requires: rubygem-event-bus < 0.2
Requires: rubygem-aruba >= 0.6.1
Requires: rubygem-aruba < 0.7
Requires: rubygem-json >= 1.7
Requires: rubygem-json < 2
Requires: rubygem-nokogiri >= 1.5
Requires: rubygem-nokogiri < 2
Requires: rubygem-rake >= 0.9.2
Requires: rubygem-rspec >= 3.0
Requires: rubygem-simplecov >= 0.6.2
Requires: rubygem-coveralls >= 0.7
Requires: rubygem-coveralls < 1
Requires: rubygem-syntax >= 1.0.0
Requires: rubygem-pry 
Requires: rubygem-bcat >= 0.6.2
Requires: rubygem-bcat < 0.7
Requires: rubygem-kramdown >= 0.14
Requires: rubygem-kramdown < 1
Requires: rubygem-yard >= 0.8.0
Requires: rubygem-yard < 0.9
Requires: rubygem-capybara >= 2.1
Requires: rubygem-rack-test >= 0.6.1
Requires: rubygem-sinatra >= 1.3.2
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(cucumber) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Behaviour Driven Development with elegance and joy.

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
%{_bindir}/cucumber
%{gemdir}/gems/cucumber-2.3.0/

%{gemdir}/cache/cucumber-2.3.0.gem
%{gemdir}/specifications/cucumber-2.3.0.gemspec

%changelog
