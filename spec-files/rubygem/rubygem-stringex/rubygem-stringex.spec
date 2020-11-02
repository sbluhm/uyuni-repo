# Generated from stringex-1.5.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname stringex
%define version 1.5.1
%define release 1

Summary: Some [hopefully] useful extensions to Ruby's String class
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/rsl/stringex
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-activerecord 
Requires: rubygem-jeweler = 1.8.4
Requires: rubygem-RedCloth 
Requires: rubygem-sqlite3 
Requires: rubygem-travis-lint = 1.4.0
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(stringex) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Some [hopefully] useful extensions to Ruby's String class. Stringex is made up
of three libraries: ActsAsUrl [permalink solution with better character
translation], Unidecoder [Unicode to ASCII transliteration], and
StringExtensions [miscellaneous helper methods for the String class].


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
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/
%{gemdir}/gems/stringex-1.5.1/


%{gemdir}/cache/stringex-1.5.1.gem
%{gemdir}/specifications/stringex-1.5.1.gemspec

%changelog
