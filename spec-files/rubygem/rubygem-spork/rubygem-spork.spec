# Generated from spork-0.9.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname spork
%define version 0.9.2
%define release 1

Summary: spork
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/timcharper/spork
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(spork) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A forking Drb spec server.


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
%{_bindir}/spork
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/
%{gemdir}/gems/spork-0.9.2/


%{gemdir}/cache/spork-0.9.2.gem
%{gemdir}/specifications/spork-0.9.2.gemspec

%changelog
