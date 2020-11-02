# Generated from i18n-0.9.5.gem by gem2rpm -*- rpm-spec -*-
%define rbname i18n
%define version 0.9.5
%define release 1

Summary: New wave Internationalization support for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/svenfuchs/i18n
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-concurrent-ruby >= 1.0
Requires: rubygem-concurrent-ruby < 2
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(i18n) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
New wave Internationalization support for Ruby.

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
%{gemdir}/gems/i18n-0.9.5/

%{gemdir}/cache/i18n-0.9.5.gem
%{gemdir}/specifications/i18n-0.9.5.gemspec

%changelog
