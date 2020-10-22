# Generated from json-1.8.6.gem by gem2rpm -*- rpm-spec -*-
%define rbname json
%define version 1.8.6
%define release 1
%global debug_package %{nil}

Summary: JSON Implementation for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://flori.github.com/json
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake 
Requires: rubygem-test-unit >= 2.0
Requires: rubygem-test-unit < 3
BuildRequires: ruby 
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(json) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
This is a JSON implementation as a Ruby extension in C.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}/lib/json/ext
mv %{gembuilddir}/extensions/x86_64-linux/2.5.0/%{rbname}-%{version}/json/ext/*.so %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}/json/ext
rm -Rf %{gembuilddir}/extensions/x86_64-linux/2.5.0/%{rbname}-%{version}/*

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{gemdir}/gems/json-1.8.6/
%{gemdir}/cache/json-1.8.6.gem
%{gemdir}/specifications/json-1.8.6.gemspec
%{_libdir}/gems/ruby/%{rbname}-%{version}/lib/json/ext/

%changelog
