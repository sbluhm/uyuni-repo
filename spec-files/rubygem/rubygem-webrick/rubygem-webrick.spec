# Generated from webrick-1.6.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname webrick
%define version 1.6.1
%define release 1

Summary: HTTP server toolkit
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://www.ruby-lang.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake 
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(webrick) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
WEBrick is an HTTP server toolkit that can be configured as an HTTPS server, a
proxy server, and a virtual-host server.

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
%{gemdir}/gems/webrick-1.6.1/

%{gemdir}/cache/webrick-1.6.1.gem
%{gemdir}/specifications/webrick-1.6.1.gemspec

%changelog
