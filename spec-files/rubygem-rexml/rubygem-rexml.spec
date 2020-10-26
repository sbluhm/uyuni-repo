# Generated from rexml-3.2.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname rexml
%define version 3.2.4
%define release 1

Summary: An XML toolkit for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ruby/rexml
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler 
Requires: rubygem-rake 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rexml) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
An XML toolkit for Ruby.


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
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/path
%{gemdir}/gems/rexml-3.2.4/path
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/
%{gemdir}/gems/rexml-3.2.4/path
%{gemdir}/gems/rexml-3.2.4/path
%{gemdir}/gems/rexml-3.2.4/


%{gemdir}/cache/rexml-3.2.4.gem
%{gemdir}/specifications/rexml-3.2.4.gemspec

%changelog
