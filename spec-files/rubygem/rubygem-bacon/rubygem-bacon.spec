# Generated from bacon-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname bacon
%define version 1.2.0
%define release 1

Summary: a small RSpec clone
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/chneukirchen/bacon
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(bacon) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Bacon is a small RSpec clone weighing less than 350 LoC but
nevertheless providing all essential features.
http://github.com/chneukirchen/bacon.

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
%{_bindir}/bacon
%{gemdir}/gems/bacon-1.2.0/

%{gemdir}/cache/bacon-1.2.0.gem
%{gemdir}/specifications/bacon-1.2.0.gemspec

%changelog
