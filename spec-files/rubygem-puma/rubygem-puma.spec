# Generated from puma-5.0.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname puma
%define version 5.0.4
%define release 1
%global debug_package %{nil}

Summary: Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for Ruby/Rack applications
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://puma.io
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.2
Requires: rubygems >= 2.7.6.2
Requires: rubygem-nio4r >= 2.0
Requires: rubygem-nio4r < 3
BuildRequires: ruby >= 2.2
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(puma) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications. Puma is intended for use in both development and
production environments. It's great for highly concurrent Ruby implementations
such as Rubinius and JRuby as well as as providing process worker support to
support CRuby well.

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
mkdir -p %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}
mv %{gembuilddir}/extensions/x86_64-linux/2.5.0/%{rbname}-%{version}/puma/*.so %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}
rm -f %{gembuilddir}/extensions/x86_64-linux/2.5.0/%{rbname}-%{version}/*

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{_bindir}/
%{gemdir}/gems/puma-5.0.4/
%{_libdir}/gems/ruby/%{rbname}-%{version}/
%{gemdir}/cache/puma-5.0.4.gem
%{gemdir}/specifications/puma-5.0.4.gemspec

%changelog
