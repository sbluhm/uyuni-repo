# Generated from xpath-3.2.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname xpath
%define version 3.2.0
%define release 1

Summary: Generate XPath expressions from Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/teamcapybara/xpath
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-nokogiri >= 1.8
Requires: rubygem-nokogiri < 2
Requires: rubygem-pry 
Requires: rubygem-rake 
Requires: rubygem-rspec >= 3.0
Requires: rubygem-rspec < 4
Requires: rubygem-yard >= 0.5.8
BuildRequires: ruby >= 2.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(xpath) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
XPath is a Ruby DSL for generating XPath expressions.

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
%{gemdir}/gems/xpath-3.2.0/

%{gemdir}/cache/xpath-3.2.0.gem
%{gemdir}/specifications/xpath-3.2.0.gemspec

%changelog
