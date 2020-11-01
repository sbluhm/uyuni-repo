# Generated from sys-uname-1.2.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname sys-uname
%define version 1.2.2
%define release 1

Summary: An interface for returning uname (platform) information
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/djberg96/sys-uname
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-ffi >= 1.1
Requires: rubygem-ffi < 2
Requires: rubygem-rspec >= 3.9
Requires: rubygem-rspec < 4
Requires: rubygem-rake 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(sys-uname) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
The sys-uname library provides an interface for gathering information
about your current platform. The library is named after the Unix 'uname'
command but also works on MS Windows. Available information includes
OS name, OS version, system name and so on. Additional information is
available for certain platforms.

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
%{gemdir}/gems/sys-uname-1.2.2/

%{gemdir}/cache/sys-uname-1.2.2.gem
%{gemdir}/specifications/sys-uname-1.2.2.gemspec

%changelog
