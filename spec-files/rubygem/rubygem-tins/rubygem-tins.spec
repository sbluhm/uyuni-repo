# Generated from tins-1.26.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname tins
%define version 1.26.0
%define release 1

Summary: Useful stuff.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/flori/tins
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-gem_hadar >= 1.11.0
Requires: rubygem-gem_hadar < 1.12
Requires: rubygem-test-unit >= 3.1
Requires: rubygem-test-unit < 4
Requires: rubygem-simplecov 
Requires: rubygem-sync 
BuildRequires: ruby >= 2.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(tins) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
All the stuff that isn't good/big enough for a real library.

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
%{gemdir}/gems/tins-1.26.0/

%{gemdir}/cache/tins-1.26.0.gem
%{gemdir}/specifications/tins-1.26.0.gemspec

%changelog
