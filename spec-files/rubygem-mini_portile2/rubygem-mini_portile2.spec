# Generated from mini_portile2-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname mini_portile2
%define version 2.1.0
%define release 1

Summary: Simplistic port-like solution for developers
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/flavorjones/mini_portile
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.2
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler >= 1.7
Requires: rubygem-bundler < 2
Requires: rubygem-rake >= 10.0
Requires: rubygem-rake < 11
Requires: rubygem-minitest >= 5.8.0
Requires: rubygem-minitest < 5.9
Requires: rubygem-minitest-hooks >= 1.4.0
Requires: rubygem-minitest-hooks < 1.5
Requires: rubygem-minitar >= 0.5.4
Requires: rubygem-minitar < 0.6
BuildRequires: ruby >= 1.9.2
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(mini_portile2) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Simplistic port-like solution for developers. It provides a standard and
simplified way to compile against dependency libraries without messing up your
system.

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
%{gemdir}/gems/mini_portile2-2.1.0/

%{gemdir}/cache/mini_portile2-2.1.0.gem
%{gemdir}/specifications/mini_portile2-2.1.0.gemspec

%changelog
