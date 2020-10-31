# Generated from byebug-11.1.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname byebug
%define version 11.1.3
%define release 1
%global debug_package %{nil}

Summary: Ruby fast debugger - base + CLI
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/deivid-rodriguez/byebug
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.4.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler >= 2.0
Requires: rubygem-bundler < 3
BuildRequires: ruby >= 2.4.0
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(byebug) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Byebug is a Ruby debugger. It's implemented using the
TracePoint C API for execution control and the Debug Inspector C API for
call stack navigation.  The core component provides support that front-ends
can build on. It provides breakpoint handling and bindings for stack frames
among other things and it comes with an easy to use command line interface.

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}/%{_bindir}
#mv %{gembuilddir}/gems/%{rbname}-%{version}/bin/** %{buildroot}/%{_bindir}
mkdir -p %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}
mv %{gembuilddir}/extensions/x86_64-linux/2.5.0/%{rbname}-%{version}/*.so %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}
rm -f %{gembuilddir}/extensions/x86_64-linux/2.5.0/%{rbname}-%{version}/*

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{_bindir}/
%{gemdir}/gems/byebug-11.1.3/
%{_libdir}/gems/ruby/%{rbname}-%{version}/
%{gemdir}/cache/byebug-11.1.3.gem
%{gemdir}/specifications/byebug-11.1.3.gemspec

%changelog
