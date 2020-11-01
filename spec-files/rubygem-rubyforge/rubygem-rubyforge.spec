# Generated from rubyforge-2.0.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname rubyforge
%define version 2.0.4
%define release 1

Summary: A script which automates a limited set of rubyforge operations
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://codeforpeople.rubyforge.org/rubyforge/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-json_pure >= 1.1.7
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rubyforge) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A script which automates a limited set of rubyforge operations.
* Run 'rubyforge help' for complete usage.
* Setup: For first time users AND upgrades to 0.4.0:
* rubyforge setup (deletes your username and password, so run sparingly!)
* edit ~/.rubyforge/user-config.yml
* rubyforge config
* For all rubyforge upgrades, run 'rubyforge config' to ensure you have
latest.

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
%{_bindir}/rubyforge
%{gemdir}/gems/rubyforge-2.0.4/

%{gemdir}/cache/rubyforge-2.0.4.gem
%{gemdir}/specifications/rubyforge-2.0.4.gemspec

%changelog
