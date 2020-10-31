# Generated from addressable-2.7.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname addressable
%define version 2.7.0
%define release 1

Summary: URI Implementation
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/sporkmonger/addressable
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-public_suffix >= 2.0.2
Requires: rubygem-public_suffix < 5.0
Requires: rubygem-bundler >= 1.0
Requires: rubygem-bundler < 3.0
BuildRequires: ruby >= 2.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(addressable) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Addressable is an alternative implementation to the URI implementation that is
part of Ruby's standard library. It is flexible, offers heuristic parsing, and
additionally provides extensive support for IRIs and URI templates.

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
%{gemdir}/gems/addressable-2.7.0/

%{gemdir}/cache/addressable-2.7.0.gem
%{gemdir}/specifications/addressable-2.7.0.gemspec

%changelog
