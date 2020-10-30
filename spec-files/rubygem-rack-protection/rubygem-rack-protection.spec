# Generated from rack-protection-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rack-protection
%define version 2.1.0
%define release 1

Summary: Protect against typical web attacks, works with all Rack apps, including Rails.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://sinatrarb.com/protection/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rack 
Requires: rubygem-rack-test 
Requires: rubygem-rspec >= 3.6
Requires: rubygem-rspec < 4
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rack-protection) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Protect against typical web attacks, works with all Rack apps, including
Rails.

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
%{gemdir}/gems/rack-protection-2.1.0/

%{gemdir}/cache/rack-protection-2.1.0.gem
%{gemdir}/specifications/rack-protection-2.1.0.gemspec

%changelog
