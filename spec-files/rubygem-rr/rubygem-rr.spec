# Generated from rr-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname rr
%define version 1.2.1
%define release 1

Summary: RR is a test double framework that features a rich selection of double techniques and a terse syntax.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://rr.github.io/rr
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rr) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
RR is a test double framework that features a rich selection of double
techniques and a terse syntax.


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
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/
%{gemdir}/gems/rr-1.2.1/


%{gemdir}/cache/rr-1.2.1.gem
%{gemdir}/specifications/rr-1.2.1.gemspec

%changelog
