# Generated from regexp_parser-1.8.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname regexp_parser
%define version 1.8.2
%define release 1

Summary: Scanner, lexer, parser for ruby's regular expressions
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ammar/regexp_parser
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0.0
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(regexp_parser) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A library for tokenizing, lexing, and parsing Ruby regular expressions.

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
%{gemdir}/gems/regexp_parser-1.8.2/

%{gemdir}/cache/regexp_parser-1.8.2.gem
%{gemdir}/specifications/regexp_parser-1.8.2.gemspec

%changelog
