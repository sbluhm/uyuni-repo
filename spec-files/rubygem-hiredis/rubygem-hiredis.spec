# Generated from hiredis-0.6.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname hiredis
%define version 0.6.3
%define release 1
%global debug_package %{nil}

Summary: Ruby wrapper for hiredis (protocol serialization/deserialization and blocking I/O)
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/redis/hiredis-rb
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake = 10.0
Requires: rubygem-rake-compiler >= 0.7.1
Requires: rubygem-rake-compiler < 0.8
Requires: rubygem-minitest >= 5.5.1
Requires: rubygem-minitest < 5.6
BuildRequires: ruby 
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(hiredis) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Ruby wrapper for hiredis (protocol serialization/deserialization and blocking
I/O).

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}
mv %{gembuilddir}/extensions/x86_64-linux/2.5.0/%{rbname}-%{version}/hiredis/ext/*.so %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}
rm -Rf %{gembuilddir}/extensions/x86_64-linux/2.5.0/%{rbname}-%{version}/hiredis/*

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{gemdir}/gems/hiredis-0.6.3/
%{_libdir}/gems/ruby/%{rbname}-%{version}/
%{gemdir}/cache/hiredis-0.6.3.gem
%{gemdir}/specifications/hiredis-0.6.3.gemspec

%changelog
