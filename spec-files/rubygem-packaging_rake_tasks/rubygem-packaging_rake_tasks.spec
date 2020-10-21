# Generated from packaging_rake_tasks-1.4.11.gem by gem2rpm -*- rpm-spec -*-
%define rbname packaging_rake_tasks
%define version 1.4.11
%define release 1

Summary: Rake tasks providing tasks to package project in git and integration with build service
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/openSUSE/packaging_rake_tasks
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(packaging_rake_tasks) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Rake tasks to allow easy packaging ruby projects in git for Build Service or
other packaging service.


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
%{gemdir}/gems/packaging_rake_tasks-1.4.11/
%doc %{gemdir}/doc/%{rbname}-%{version}/
%{gemdir}/cache/packaging_rake_tasks-1.4.11.gem
%{gemdir}/specifications/packaging_rake_tasks-1.4.11.gemspec

%changelog
