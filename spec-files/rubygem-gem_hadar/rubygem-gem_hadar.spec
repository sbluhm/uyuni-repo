# Generated from gem_hadar-1.9.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname gem_hadar
%define version 1.9.1
%define release 1

Summary: Library for the development of Ruby Gems
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/flori/gem_hadar
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-gem_hadar >= 1.9.1
Requires: rubygem-gem_hadar < 1.10
Requires: rubygem-tins >= 1.0
Requires: rubygem-tins < 2
Requires: rubygem-rake 
Requires: rubygem-yard 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(gem_hadar) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
This library contains some useful functionality to support the development of
Ruby Gems.

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
%{gemdir}/gems/gem_hadar-1.9.1/

%{gemdir}/cache/gem_hadar-1.9.1.gem
%{gemdir}/specifications/gem_hadar-1.9.1.gemspec

%changelog
