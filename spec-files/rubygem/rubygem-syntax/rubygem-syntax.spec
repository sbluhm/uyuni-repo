# Generated from syntax-1.2.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname syntax
%define version 1.2.2
%define release 1

Summary: Perform simple syntax highlighting.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/dblock/syntax
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake < 11.0.0
Requires: rubygem-rake-contrib 
Requires: rubygem-rdoc 
Requires: rubygem-test-unit 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(syntax) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Syntax is Ruby library for performing simple syntax highlighting.


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
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/
%{gemdir}/gems/syntax-1.2.2/


%{gemdir}/cache/syntax-1.2.2.gem
%{gemdir}/specifications/syntax-1.2.2.gemspec

%changelog
