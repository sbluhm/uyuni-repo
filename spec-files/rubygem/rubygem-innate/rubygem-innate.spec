# Generated from innate-2015.10.28.gem by gem2rpm -*- rpm-spec -*-
%define rbname innate
%define version 2015.10.28
%define release 1

Summary: Powerful web-framework wrapper for Rack.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/manveru/innate
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rack >= 1.6.4
Requires: rubygem-rack < 1.7
Requires: rubygem-bacon >= 1.2.0
Requires: rubygem-bacon < 1.3
Requires: rubygem-rack-test >= 0.6.3
Requires: rubygem-rack-test < 0.7
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(innate) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Simple, straight-forward base for web-frameworks.

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
%{gemdir}/gems/innate-2015.10.28/

%{gemdir}/cache/innate-2015.10.28.gem
%{gemdir}/specifications/innate-2015.10.28.gemspec

%changelog
