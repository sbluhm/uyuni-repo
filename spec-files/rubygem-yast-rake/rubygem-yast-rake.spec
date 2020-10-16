# Generated from yast-rake-0.2.39.gem by gem2rpm -*- rpm-spec -*-
%define rbname yast-rake
%define version 0.2.39
%define release 1

Summary: Rake tasks providing basic work-flow for Yast development
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/yast/yast-rake
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-packaging_rake_tasks >= 1.1.4
Requires: rubygem-rake 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(Yast-rake) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Rake tasks that support work-flow of Yast developer. It allows packaging repo,
send it to build service, create submit request to target repo or run client
from git repo.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
#gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
gem install --local --user-install %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/yast-rake-0.2.39/
%{gemdir}/cache/yast-rake-0.2.39.gem
%{gemdir}/specifications/yast-rake-0.2.39.gemspec

%changelog
