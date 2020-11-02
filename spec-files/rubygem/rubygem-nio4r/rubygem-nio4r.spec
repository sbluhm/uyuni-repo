# Generated from nio4r-2.5.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname nio4r
%define version 2.5.4
%define release 1
%global debug_package %{nil}

Summary: New IO for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/socketry/nio4r
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.4
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler 
Requires: rubygem-rake 
BuildRequires: ruby >= 2.4
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(nio4r) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Cross-platform asynchronous I/O primitives for scalable network clients and
servers. Inspired by the Java NIO API, but simplified for ease-of-use.

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}
mv %{gembuilddir}/extensions/x86_64-linux/2.5.0/%{rbname}-%{version}/*.so %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}
rm -Rf %{gembuilddir}/extensions/x86_64-linux/2.5.0/%{rbname}-%{version}/*

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{gemdir}/gems/nio4r-2.5.4/
%{_libdir}/gems/ruby/%{rbname}-%{version}/
%{gemdir}/cache/nio4r-2.5.4.gem
%{gemdir}/specifications/nio4r-2.5.4.gemspec

%changelog
