# Generated from redis-4.2.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname redis
%define version 4.2.2
%define release 1

Summary: A Ruby client library for Redis
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/redis/redis-rb
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-em-synchrony 
Requires: rubygem-hiredis 
Requires: rubygem-mocha 
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(redis) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A Ruby client that tries to match Redis' API one-to-one, while still
providing an idiomatic interface.

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
%{gemdir}/gems/redis-4.2.2/

%{gemdir}/cache/redis-4.2.2.gem
%{gemdir}/specifications/redis-4.2.2.gemspec

%changelog
