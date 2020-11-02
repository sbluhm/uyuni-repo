# Generated from bones-3.7.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname bones
%define version 3.7.3
%define release 1

Summary: Mr Bones is a handy tool that creates new Ruby projects from a code skeleton.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://rubygems.org/gems/bones
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake >= 0.8.7
Requires: rubygem-little-plugger >= 1.1.3
Requires: rubygem-little-plugger < 1.2
Requires: rubygem-loquacious >= 1.9.1
Requires: rubygem-loquacious < 1.10
Requires: rubygem-rspec >= 2.6
Requires: rubygem-rspec < 3
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(bones) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Mr Bones is a handy tool that creates new Ruby projects from a code
skeleton. The skeleton contains some starter code and a collection of rake
tasks to ease the management and deployment of your source code. Several Mr
Bones plugins are available for creating git repositories, creating GitHub
projects, running various test suites and source code analysis tools.

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
%{_bindir}/bones
%{gemdir}/gems/bones-3.7.3/

%{gemdir}/cache/bones-3.7.3.gem
%{gemdir}/specifications/bones-3.7.3.gemspec

%changelog
