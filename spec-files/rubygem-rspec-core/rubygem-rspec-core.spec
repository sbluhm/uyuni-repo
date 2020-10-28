# Generated from rspec-core-2.8.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rspec-core
%define version 2.8.0
%define release 1

Summary: rspec-core-2.8.0
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/rspec/rspec-core
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rspec-core) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
BDD for Ruby. RSpec runner and example groups.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}/%{_bindir}
#mv %{gembuilddir}/gems/%{rbname}-%{version}/bin/** %{buildroot}/%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
#%{_bindir}/
%{gemdir}/gems/rspec-core-2.8.0/
%{gemdir}/cache/rspec-core-2.8.0.gem
%{gemdir}/specifications/rspec-core-2.8.0.gemspec

%changelog
