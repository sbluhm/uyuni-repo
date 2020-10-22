# Generated from tzinfo-1.2.7.gem by gem2rpm -*- rpm-spec -*-
%define rbname tzinfo
%define version 1.2.7
%define release 1

Summary: Daylight savings aware timezone library
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://tzinfo.github.io
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 2.7.6.2
Requires: rubygem-thread_safe >= 0.1
Requires: rubygem-thread_safe < 1
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(tzinfo) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
TZInfo provides daylight savings aware transformations between times in
different time zones.


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
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/
%{gemdir}/gems/tzinfo-1.2.7/


%{gemdir}/cache/tzinfo-1.2.7.gem
%{gemdir}/specifications/tzinfo-1.2.7.gemspec

%changelog
