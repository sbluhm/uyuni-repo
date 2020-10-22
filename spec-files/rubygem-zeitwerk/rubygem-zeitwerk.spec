# Generated from zeitwerk-2.4.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname zeitwerk
%define version 2.4.0
%define release 1

Summary: Efficient and thread-safe constant autoloader
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/fxn/zeitwerk
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.4.4
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby >= 2.4.4
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(zeitwerk) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem
and application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading,
reloading, and eager loading.


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
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/
%{gemdir}/gems/zeitwerk-2.4.0/


%{gemdir}/cache/zeitwerk-2.4.0.gem
%{gemdir}/specifications/zeitwerk-2.4.0.gemspec

%changelog
