# Generated from childprocess-3.0.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname childprocess
%define version 3.0.0
%define release 1

Summary: A simple and reliable solution for controlling external programs running in the background on any Ruby / OS combination.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/enkessler/childprocess
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rspec >= 3.0
Requires: rubygem-rspec < 4
Requires: rubygem-yard 
Requires: rubygem-yard < 1
Requires: rubygem-coveralls < 1.0
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(childprocess) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
This gem aims at being a simple and reliable solution for controlling external
programs running in the background on any Ruby / OS combination.

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
%{gemdir}/gems/childprocess-3.0.0/

%{gemdir}/cache/childprocess-3.0.0.gem
%{gemdir}/specifications/childprocess-3.0.0.gemspec

%changelog
