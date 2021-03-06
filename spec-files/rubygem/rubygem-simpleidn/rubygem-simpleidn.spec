# Generated from simpleidn-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname simpleidn
%define version 0.1.1
%define release 1

Summary: Punycode ACE to unicode UTF-8 (and vice-versa) string conversion.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/mmriis/simpleidn
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby > 1.9
Requires: rubygems >= 2.7.6.2
Requires: rubygem-unf >= 0.1.4
Requires: rubygem-unf < 0.2
Requires: rubygem-bundler >= 1.11
Requires: rubygem-bundler < 2
Requires: rubygem-rake >= 10.0
Requires: rubygem-rake < 11
Requires: rubygem-rspec >= 3.0
Requires: rubygem-rspec < 4
BuildRequires: ruby > 1.9
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: rubygem(simpleidn) = %{version}

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
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/simpleidn-0.1.1/
%doc %{gemdir}/doc/simpleidn-0.1.1/
%{gemdir}/cache/simpleidn-0.1.1.gem
%{gemdir}/specifications/simpleidn-0.1.1.gemspec

%changelog
