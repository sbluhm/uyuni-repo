# Generated from rdiscount-1.6.8.gem by gem2rpm -*- rpm-spec -*-
%define rbname rdiscount
%define version 1.6.8
%define release 1
%global debug_package %{nil}

Summary: Fast Implementation of Gruber's Markdown in C
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/rtomayko/rdiscount
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(rdiscount) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Fast Implementation of Gruber's Markdown in C.

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
%{_bindir}/rdiscount
%{gemdir}/gems/rdiscount-1.6.8/

%{gemdir}/cache/rdiscount-1.6.8.gem
%{gemdir}/specifications/rdiscount-1.6.8.gemspec

%changelog
