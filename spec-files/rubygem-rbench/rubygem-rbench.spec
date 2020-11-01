# Generated from rbench-0.2.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname rbench
%define version 0.2.3
%define release 1

Summary: Library for generating nice ruby-benchmarks
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.rbench.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rbench) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Library for generating nice ruby-benchmarks.

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
%{gemdir}/gems/rbench-0.2.3/

%{gemdir}/cache/rbench-0.2.3.gem
%{gemdir}/specifications/rbench-0.2.3.gemspec

%changelog
