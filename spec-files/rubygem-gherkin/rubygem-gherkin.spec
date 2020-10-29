# Generated from gherkin-2.9.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname gherkin
%define version 2.9.3
%define release 1

Summary: gherkin-2.9.3
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/cucumber/gherkin
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake-compiler >= 0.8.0
Requires: rubygem-json >= 1.4.6
Requires: rubygem-cucumber >= 1.1.9
Requires: rubygem-rake >= 0.9.2
Requires: rubygem-bundler >= 1.1.0
Requires: rubygem-rspec >= 2.9.0
Requires: rubygem-rspec < 2.10
Requires: rubygem-rubyzip >= 0.9.6.1
Requires: rubygem-therubyracer >= 0.9.10
Requires: rubygem-yard >= 0.7.5
Requires: rubygem-rdiscount >= 1.6.8
Requires: rubygem-term-ansicolor >= 1.0.6
Requires: rubygem-builder >= 2.1.2
BuildRequires: ruby 
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(gherkin) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A fast Gherkin lexer/parser based on the Ragel State Machine Compiler.

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
%{gemdir}/gems/gherkin-2.9.3/

%{gemdir}/cache/gherkin-2.9.3.gem
%{gemdir}/specifications/gherkin-2.9.3.gemspec

%changelog
