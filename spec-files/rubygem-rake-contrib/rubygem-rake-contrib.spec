# Generated from rake-contrib-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rake-contrib
%define version 1.0.0
%define release 1

Summary: Additional libraries for Rake
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ruby/rake-contrib
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake 
Requires: rubygem-bundler 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rake-contrib) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Additional libraries for Rake.

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
%{gemdir}/gems/rake-contrib-1.0.0/

%{gemdir}/cache/rake-contrib-1.0.0.gem
%{gemdir}/specifications/rake-contrib-1.0.0.gemspec

%changelog
