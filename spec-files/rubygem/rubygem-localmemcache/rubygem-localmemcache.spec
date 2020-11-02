# Generated from localmemcache-0.4.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname localmemcache
%define version 0.4.4
%define release 1

Summary: A persistent key-value database based on mmap()'ed shared memory.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://localmemcache.rubyforge.org/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby
BuildRequires: ruby-devel 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(localmemcache) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Localmemcache is a library for C and ruby that aims to provide
an interface similar to memcached but for accessing local data instead of
remote data.  It's based on mmap()'ed shared memory for maximum speed.
Since version 0.3.0 it supports persistence, also making it a fast
alternative to GDBM and Berkeley DB.
.

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
%{gemdir}/gems/localmemcache-0.4.4/

%{gemdir}/cache/localmemcache-0.4.4.gem
%{gemdir}/specifications/localmemcache-0.4.4.gemspec

%changelog
