# Generated from ruby-augeas-0.5.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname ruby-augeas
%define version 0.5.0
%define release 1

%global debug_package %{nil}

Summary: Ruby bindings for augeas
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://augeas.net/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.1
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby >= 1.8.1
BuildRequires: rubygems >= 2.7.6.2
BuildRequires: ruby-devel
BuildRequires: augeas-devel
Provides: ruby(ruby-augeas) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Provides bindings for augeas.


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
%defattr(-, root, root)
%{gemdir}/gems/ruby-augeas-0.5.0/
%doc %{gemdir}/doc/%{rbname}-%{version}/
%{gemdir}/cache/ruby-augeas-0.5.0.gem
%{gemdir}/specifications/ruby-augeas-0.5.0.gemspec

%changelog
