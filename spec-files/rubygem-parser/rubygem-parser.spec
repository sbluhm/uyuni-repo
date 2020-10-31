# Generated from parser-2.7.2.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname parser
%define version 2.7.2.0
%define release 1

Summary: A Ruby parser written in pure Ruby.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/whitequark/parser
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-ast >= 2.4.1
Requires: rubygem-ast < 2.5
Requires: rubygem-bundler >= 1.15
Requires: rubygem-bundler < 3.0.0
Requires: rubygem-rake >= 13.0.1
Requires: rubygem-rake < 13.1
Requires: rubygem-racc = 1.4.15
Requires: rubygem-cliver >= 0.3.2
Requires: rubygem-cliver < 0.4
Requires: rubygem-yard 
Requires: rubygem-kramdown 
Requires: rubygem-minitest >= 5.10
Requires: rubygem-minitest < 6
Requires: rubygem-simplecov >= 0.15.1
Requires: rubygem-simplecov < 0.16
Requires: rubygem-gauntlet 
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(parser) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A Ruby parser written in pure Ruby.

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
%{_bindir}/ruby-parse
%{_bindir}/ruby-rewrite
%{gemdir}/gems/parser-2.7.2.0/

%{gemdir}/cache/parser-2.7.2.0.gem
%{gemdir}/specifications/parser-2.7.2.0.gemspec

%changelog
