# Generated from hoe-gemspec-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname hoe-gemspec
%define version 1.0.0
%define release 1

Summary: Generate a prerelease gemspec based on a Hoe spec.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/flavorjones/hoe-gemspec
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-hoe >= 2.2.0
Requires: rubygem-rubyforge >= 2.0.4
Requires: rubygem-rake 
Requires: rubygem-hoe >= 2.6.1
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(hoe-gemspec) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Generate a prerelease gemspec based on a Hoe spec.

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
%{gemdir}/gems/hoe-gemspec-1.0.0/

%{gemdir}/cache/hoe-gemspec-1.0.0.gem
%{gemdir}/specifications/hoe-gemspec-1.0.0.gemspec

%changelog
