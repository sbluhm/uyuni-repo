# Generated from simpleidn-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname simpleidn
%define version 0.1.1
%define release 1

Summary: Punycode ACE to unicode UTF-8 (and vice-versa) string conversion.
Name: rubygems-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/mmriis/simpleidn
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby > 1.9
Requires: rubygems >= 2.7.6.2
Requires: rubygems-unf >= 0.1.4
Requires: rubygems-unf < 0.2
Requires: rubygems-bundler >= 1.11
Requires: rubygems-bundler < 2
Requires: rubygems-rake >= 10.0
Requires: rubygems-rake < 11
Requires: rubygems-rspec >= 3.0
Requires: rubygems-rspec < 4
BuildRequires: ruby > 1.9
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(Simpleidn) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
This gem allows easy conversion from punycode ACE strings to unicode UTF-8
strings and vice-versa.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/simpleidn-0.1.1/
%{gemdir}/gems/simpleidn-0.1.1/
%{gemdir}/gems/simpleidn-0.1.1/
%{gemdir}/gems/simpleidn-0.1.1/
%{gemdir}/gems/simpleidn-0.1.1/
%{gemdir}/gems/simpleidn-0.1.1/
%{gemdir}/gems/simpleidn-0.1.1/
%{gemdir}/gems/simpleidn-0.1.1/
%{gemdir}/gems/simpleidn-0.1.1/
%{gemdir}/gems/simpleidn-0.1.1/
%{gemdir}/gems/simpleidn-0.1.1/
%{gemdir}/gems/simpleidn-0.1.1/


%{gemdir}/cache/simpleidn-0.1.1.gem
%{gemdir}/specifications/simpleidn-0.1.1.gemspec

%changelog
