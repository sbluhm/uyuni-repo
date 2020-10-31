# Generated from cucumber-5.2.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname cucumber
%define version 5.2.0
%define release 1

Summary: cucumber-5.2.0
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://cucumber.io/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.5
Requires: rubygems >= 2.7.6.2
Requires: rubygem-builder >= 3.2
Requires: rubygem-builder < 4
Requires: rubygem-builder >= 3.2.4
Requires: rubygem-cucumber-core >= 8.0
Requires: rubygem-cucumber-core < 9
Requires: rubygem-cucumber-core >= 8.0.1
Requires: rubygem-cucumber-create-meta >= 2.0
Requires: rubygem-cucumber-create-meta < 3
Requires: rubygem-cucumber-create-meta >= 2.0.2
Requires: rubygem-cucumber-cucumber-expressions >= 10.3
Requires: rubygem-cucumber-cucumber-expressions < 11
Requires: rubygem-cucumber-cucumber-expressions >= 10.3.0
Requires: rubygem-cucumber-gherkin >= 15.0
Requires: rubygem-cucumber-gherkin < 16
Requires: rubygem-cucumber-gherkin >= 15.0.2
Requires: rubygem-cucumber-html-formatter >= 9.0
Requires: rubygem-cucumber-html-formatter < 10
Requires: rubygem-cucumber-html-formatter >= 9.0.0
Requires: rubygem-cucumber-messages >= 13.1
Requires: rubygem-cucumber-messages < 14
Requires: rubygem-cucumber-messages >= 13.1.0
Requires: rubygem-cucumber-wire >= 4.0
Requires: rubygem-cucumber-wire < 5
Requires: rubygem-cucumber-wire >= 4.0.1
Requires: rubygem-diff-lcs >= 1.4
Requires: rubygem-diff-lcs < 2
Requires: rubygem-diff-lcs >= 1.4.4
Requires: rubygem-multi_test >= 0.1
Requires: rubygem-multi_test < 1
Requires: rubygem-multi_test >= 0.1.2
Requires: rubygem-sys-uname >= 1.2
Requires: rubygem-sys-uname < 2
Requires: rubygem-sys-uname >= 1.2.1
Requires: rubygem-nokogiri >= 1.10
Requires: rubygem-nokogiri < 2
Requires: rubygem-nokogiri >= 1.10.10
Requires: rubygem-pry >= 0.13
Requires: rubygem-pry < 1
Requires: rubygem-pry >= 0.13.1
Requires: rubygem-rake >= 13.0
Requires: rubygem-rake < 14
Requires: rubygem-rake >= 13.0.1
Requires: rubygem-rspec >= 3.9
Requires: rubygem-rspec < 4
Requires: rubygem-rspec >= 3.9.0
Requires: rubygem-simplecov >= 0.19
Requires: rubygem-simplecov < 1
Requires: rubygem-simplecov >= 0.19.0
Requires: rubygem-syntax >= 1.2
Requires: rubygem-syntax < 2
Requires: rubygem-syntax >= 1.2.2
Requires: rubygem-test-unit >= 3.3
Requires: rubygem-test-unit < 4
Requires: rubygem-test-unit >= 3.3.6
Requires: rubygem-webrick >= 1.6
Requires: rubygem-webrick < 2
Requires: rubygem-webrick >= 1.6.1
Requires: rubygem-octokit >= 4.19
Requires: rubygem-octokit < 5
Requires: rubygem-octokit >= 4.19.0
Requires: rubygem-rack-test >= 1.1
Requires: rubygem-rack-test < 2
Requires: rubygem-rack-test >= 1.1.0
Requires: rubygem-sinatra >= 2.1
Requires: rubygem-sinatra < 3
Requires: rubygem-sinatra >= 2.1.0
Requires: rubygem-capybara >= 3.33
Requires: rubygem-capybara < 4
Requires: rubygem-capybara >= 3.33.0
BuildRequires: ruby >= 2.5
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
%{gemdir}/gems/cucumber-5.2.0/

%{gemdir}/cache/cucumber-5.2.0.gem
%{gemdir}/specifications/cucumber-5.2.0.gemspec

%changelog
