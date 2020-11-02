# Generated from powerpack-0.1.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname powerpack
%define version 0.1.2
%define release 1

Summary: A few useful extensions to core Ruby classes.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/bbatsov/powerpack
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler >= 1.3
Requires: rubygem-bundler < 2
Requires: rubygem-rake 
Requires: rubygem-rspec 
Requires: rubygem-yard >= 0.9
Requires: rubygem-yard < 1
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(powerpack) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A few useful extensions to core Ruby classes.

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
%{gemdir}/gems/powerpack-0.1.2/

%{gemdir}/cache/powerpack-0.1.2.gem
%{gemdir}/specifications/powerpack-0.1.2.gemspec

%changelog
