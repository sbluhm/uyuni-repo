# Generated from jeweler-1.8.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname jeweler
%define version 1.8.4
%define release 1

Summary: Opinionated tool for creating and managing RubyGem projects
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/technicalpickles/jeweler
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake 
Requires: rubygem-git >= 1.2.5
Requires: rubygem-bundler >= 1.0
Requires: rubygem-bundler < 2
Requires: rubygem-rdoc 
Requires: rubygem-yard >= 0.7.4
Requires: rubygem-yard < 0.8
Requires: rubygem-rdoc 
Requires: rubygem-bluecloth 
Requires: rubygem-cucumber >= 1.1.4
Requires: rubygem-cucumber < 1.2
Requires: rubygem-rcov 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(jeweler) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Simple and opinionated helper for creating Rubygem projects on GitHub.


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
%{_bindir}/jeweler
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/
%{gemdir}/gems/jeweler-1.8.4/


%{gemdir}/cache/jeweler-1.8.4.gem
%{gemdir}/specifications/jeweler-1.8.4.gemspec

%changelog
