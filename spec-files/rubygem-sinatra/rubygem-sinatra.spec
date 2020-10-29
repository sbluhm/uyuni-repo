# Generated from sinatra-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname sinatra
%define version 2.1.0
%define release 1

Summary: Classy web-development dressed in a DSL
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://sinatrarb.com/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rack >= 2.2
Requires: rubygem-rack < 3
Requires: rubygem-tilt >= 2.0
Requires: rubygem-tilt < 3
Requires: rubygem-rack-protection = 2.1.0
Requires: rubygem-mustermann >= 1.0
Requires: rubygem-mustermann < 2
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(sinatra) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.


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
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/
%{gemdir}/gems/sinatra-2.1.0/


%{gemdir}/cache/sinatra-2.1.0.gem
%{gemdir}/specifications/sinatra-2.1.0.gemspec

%changelog
