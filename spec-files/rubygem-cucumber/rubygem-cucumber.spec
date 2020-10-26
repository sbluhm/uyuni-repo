# Generated from cucumber-1.1.9.gem by gem2rpm -*- rpm-spec -*-
%define rbname cucumber
%define version 1.1.9
%define release 1

Summary: cucumber-1.1.9
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://cukes.info
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-gherkin >= 2.9.0
Requires: rubygem-gherkin < 2.10
Requires: rubygem-term-ansicolor >= 1.0.6
Requires: rubygem-builder >= 2.1.2
Requires: rubygem-diff-lcs >= 1.1.2
Requires: rubygem-json >= 1.4.6
Requires: rubygem-aruba >= 0.4.11
Requires: rubygem-aruba < 0.5
Requires: rubygem-rake >= 0.9.2
Requires: rubygem-rspec >= 2.7.0
Requires: rubygem-rspec < 2.8
Requires: rubygem-nokogiri >= 1.5.0
Requires: rubygem-prawn >= 0.8.4
Requires: rubygem-prawn < 0.9
Requires: rubygem-prawn-layout >= 0.8.4
Requires: rubygem-prawn-layout < 0.9
Requires: rubygem-syntax >= 1.0.0
Requires: rubygem-spork >= 0.9.0.rc9
Requires: rubygem-simplecov >= 0.5.4
Requires: rubygem-yard >= 0.7.4
Requires: rubygem-yard < 0.8
Requires: rubygem-rdiscount >= 1.6.8
Requires: rubygem-rdiscount < 1.7
Requires: rubygem-bcat >= 0.6.2
Requires: rubygem-bcat < 0.7
Requires: rubygem-ramaze 
Requires: rubygem-rack-test >= 0.6.1
Requires: rubygem-webrat >= 0.7.3
Requires: rubygem-sinatra >= 1.3.1
Requires: rubygem-capybara >= 1.1.1
BuildRequires: ruby 
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
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/
%{gemdir}/gems/cucumber-1.1.9/


%{gemdir}/cache/cucumber-1.1.9.gem
%{gemdir}/specifications/cucumber-1.1.9.gemspec

%changelog
