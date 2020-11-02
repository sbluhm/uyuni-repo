# Generated from rest-client-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rest-client
%define version 2.1.0
%define release 1

Summary: Simple HTTP and REST client for Ruby, inspired by microframework syntax for specifying actions.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/rest-client/rest-client
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-webmock >= 2.0
Requires: rubygem-webmock < 3
Requires: rubygem-rspec >= 3.0
Requires: rubygem-rspec < 4
Requires: rubygem-pry 
Requires: rubygem-pry < 1
Requires: rubygem-pry-doc 
Requires: rubygem-pry-doc < 1
Requires: rubygem-rdoc >= 2.4.2
Requires: rubygem-rdoc < 6.0
Requires: rubygem-rubocop >= 0.49
Requires: rubygem-rubocop < 1
Requires: rubygem-http-accept >= 1.7.0
Requires: rubygem-http-accept < 2.0
Requires: rubygem-http-cookie >= 1.0.2
Requires: rubygem-http-cookie < 2.0
Requires: rubygem-mime-types >= 1.16
Requires: rubygem-mime-types < 4.0
Requires: rubygem-netrc >= 0.8
Requires: rubygem-netrc < 1
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rest-client) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A simple HTTP and REST client for Ruby, inspired by the Sinatra microframework
style of specifying actions: get, put, post, delete.

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
%{_bindir}/restclient
%{gemdir}/gems/rest-client-2.1.0/

%{gemdir}/cache/rest-client-2.1.0.gem
%{gemdir}/specifications/rest-client-2.1.0.gemspec

%changelog
