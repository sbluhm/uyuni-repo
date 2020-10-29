# Generated from ramaze-2012.12.08.gem by gem2rpm -*- rpm-spec -*-
%define rbname ramaze
%define version 2012.12.08
%define release 1

Summary: Ramaze is a simple and modular web framework
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://ramaze.net/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-innate >= 2012.12
Requires: rubygem-rake 
Requires: rubygem-Remarkably 
Requires: rubygem-bacon 
Requires: rubygem-dalli 
Requires: rubygem-erector 
Requires: rubygem-erubis 
Requires: rubygem-ezamar 
Requires: rubygem-haml 
Requires: rubygem-liquid 
Requires: rubygem-locale 
Requires: rubygem-maruku 
Requires: rubygem-mustache 
Requires: rubygem-rack-contrib 
Requires: rubygem-rack-test 
Requires: rubygem-redis 
Requires: rubygem-sass 
Requires: rubygem-sequel 
Requires: rubygem-slim 
Requires: rubygem-slippers 
Requires: rubygem-tagz 
Requires: rubygem-tenjin 
Requires: rubygem-yard 
Requires: rubygem-lokar 
Requires: rubygem-localmemcache 
Requires: rubygem-nokogiri 
Requires: rubygem-rdiscount 
Requires: rubygem-sqlite3 
Requires: rubygem-nagoro 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(ramaze) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Ramaze is a simple and modular web framework.


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
%{_bindir}/ramaze
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/
%{gemdir}/gems/ramaze-2012.12.08/


%{gemdir}/cache/ramaze-2012.12.08.gem
%{gemdir}/specifications/ramaze-2012.12.08.gemspec

%changelog
