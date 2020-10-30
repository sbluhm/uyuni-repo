# Generated from sequel-5.37.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname sequel
%define version 5.37.0
%define release 1

Summary: The Database Toolkit for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://sequel.jeremyevans.net
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.2
Requires: rubygems >= 2.7.6.2
Requires: rubygem-minitest >= 5.7.0
Requires: rubygem-minitest-hooks 
Requires: rubygem-minitest-global_expectations 
Requires: rubygem-minitest-shared_description 
Requires: rubygem-tzinfo 
Requires: rubygem-activemodel 
Requires: rubygem-nokogiri 
BuildRequires: ruby >= 1.9.2
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(sequel) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
The Database Toolkit for Ruby.

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
%{_bindir}/sequel
%{gemdir}/gems/sequel-5.37.0/

%{gemdir}/cache/sequel-5.37.0.gem
%{gemdir}/specifications/sequel-5.37.0.gemspec

%changelog
