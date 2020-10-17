# Generated from cfa-1.0.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname cfa
%define version 1.0.2
%define release 1

Summary: CFA (Config Files API) provides an easy way to create models on top of configuration files
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/config-files-api/config_files_api
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-ruby-augeas 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: rubygem(cfa) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Library offering separation of parsing and file access from the rest of the
logic for managing configuraton files. It has built-in support for parsing
using augeas lenses and also for working with files directly in memory.


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
%{gemdir}/gems/cfa-1.0.2/
%doc %{gemdir}/doc/cfa-1.0.2/
%{gemdir}/cache/cfa-1.0.2.gem
%{gemdir}/specifications/cfa-1.0.2.gemspec

%changelog
