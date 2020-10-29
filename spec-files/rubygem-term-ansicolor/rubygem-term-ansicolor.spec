# Generated from term-ansicolor-1.7.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname term-ansicolor
%define version 1.7.1
%define release 1

Summary: Ruby library that colors strings using ANSI escape sequences
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://flori.github.com/term-ansicolor
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-gem_hadar >= 1.9.1
Requires: rubygem-gem_hadar < 1.10
Requires: rubygem-simplecov 
Requires: rubygem-test-unit 
Requires: rubygem-tins >= 1.0
Requires: rubygem-tins < 2
BuildRequires: ruby >= 2.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(term-ansicolor) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
This library uses ANSI escape sequences to control the attributes of terminal
output.


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
%{_bindir}/term_snow
%{_bindir}/term_display
%{_bindir}/term_decolor
%{_bindir}/term_cdiff
%{_bindir}/term_mandel
%{_bindir}/term_colortab
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/
%{gemdir}/gems/term-ansicolor-1.7.1/


%{gemdir}/cache/term-ansicolor-1.7.1.gem
%{gemdir}/specifications/term-ansicolor-1.7.1.gemspec

%changelog
