# Generated from liquid-4.0.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname liquid
%define version 4.0.3
%define release 1

Summary: A secure, non-evaling end user template engine with aesthetic markup.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.liquidmarkup.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.1.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake >= 11.3
Requires: rubygem-rake < 12
Requires: rubygem-minitest 
BuildRequires: ruby >= 2.1.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(liquid) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A secure, non-evaling end user template engine with aesthetic markup.

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
%{gemdir}/gems/liquid-4.0.3/

%{gemdir}/cache/liquid-4.0.3.gem
%{gemdir}/specifications/liquid-4.0.3.gemspec

%changelog
