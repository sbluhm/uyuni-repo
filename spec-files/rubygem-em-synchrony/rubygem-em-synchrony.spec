# Generated from em-synchrony-1.0.6.gem by gem2rpm -*- rpm-spec -*-
%define rbname em-synchrony
%define version 1.0.6
%define release 1

Summary: Fiber aware EventMachine libraries
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/igrigorik/em-synchrony
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-eventmachine >= 1.0.0.beta.1
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(em-synchrony) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Fiber aware EventMachine libraries.

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
%{gemdir}/gems/em-synchrony-1.0.6/

%{gemdir}/cache/em-synchrony-1.0.6.gem
%{gemdir}/specifications/em-synchrony-1.0.6.gemspec

%changelog
