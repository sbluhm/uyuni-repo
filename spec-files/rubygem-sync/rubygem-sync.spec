# Generated from sync-0.5.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname sync
%define version 0.5.0
%define release 1

Summary: A module that provides a two-phase lock with a counter.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ruby/sync
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler 
Requires: rubygem-rake 
Requires: rubygem-test-unit 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(sync) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A module that provides a two-phase lock with a counter.

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
%{gemdir}/gems/sync-0.5.0/

%{gemdir}/cache/sync-0.5.0.gem
%{gemdir}/specifications/sync-0.5.0.gemspec

%changelog
