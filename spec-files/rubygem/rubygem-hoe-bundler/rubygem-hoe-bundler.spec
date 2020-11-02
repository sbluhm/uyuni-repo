# Generated from hoe-bundler-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname hoe-bundler
%define version 1.2.0
%define release 1

Summary: Generate a Gemfile based on a Hoe spec's declared dependencies.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/flavorjones/hoe-bundler
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-hoe >= 2.2.0
Requires: rubygem-rdoc >= 3.10
Requires: rubygem-rdoc < 4
Requires: rubygem-rake 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(hoe-bundler) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Generate a Gemfile based on a Hoe spec's declared dependencies.

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
%{gemdir}/gems/hoe-bundler-1.2.0/

%{gemdir}/cache/hoe-bundler-1.2.0.gem
%{gemdir}/specifications/hoe-bundler-1.2.0.gemspec

%changelog
