# Generated from ruby-prof-0.18.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname ruby-prof
%define version 0.18.0
%define release 1

Summary: Fast Ruby profiler
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ruby-prof/ruby-prof
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-minitest 
Requires: rubygem-rake-compiler 
Requires: rubygem-rdoc 
BuildRequires: ruby >= 1.9.3
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(ruby-prof) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
ruby-prof is a fast code profiler for Ruby. It is a C extension and
therefore is many times faster than the standard Ruby profiler. It
supports both flat and graph profiles.  For each method, graph profiles
show how long the method ran, which methods called it and which
methods it called. RubyProf generate both text and html and can output
it to standard out or to a file.

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
%{_bindir}/ruby-prof
%{_bindir}/ruby-prof-check-trace
%{gemdir}/gems/ruby-prof-0.18.0/

%{gemdir}/cache/ruby-prof-0.18.0.gem
%{gemdir}/specifications/ruby-prof-0.18.0.gemspec

%changelog
