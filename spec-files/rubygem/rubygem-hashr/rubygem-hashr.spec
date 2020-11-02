# Generated from hashr-2.0.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname hashr
%define version 2.0.1
%define release 1

Summary: Simple Hash extension to make working with nested hashes (e.g. for configuration) easier and less error-prone
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/svenfuchs/hashr
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(hashr) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Simple Hash extension to make working with nested hashes (e.g. for
configuration) easier and less error-prone.


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
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/
%{gemdir}/gems/hashr-2.0.1/


%{gemdir}/cache/hashr-2.0.1.gem
%{gemdir}/specifications/hashr-2.0.1.gemspec

%changelog
