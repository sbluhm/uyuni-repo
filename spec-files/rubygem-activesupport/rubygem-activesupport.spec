# Generated from activesupport-6.0.3.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname activesupport
%define version 6.0.3.4
%define release 1

Summary: A toolkit of support libraries and Ruby core extensions extracted from the Rails framework.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://rubyonrails.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.5.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-i18n >= 0.7
Requires: rubygem-i18n < 2
Requires: rubygem-tzinfo >= 1.1
Requires: rubygem-tzinfo < 2
Requires: rubygem-minitest >= 5.1
Requires: rubygem-minitest < 6
Requires: rubygem-concurrent-ruby >= 1.0
Requires: rubygem-concurrent-ruby < 2
Requires: rubygem-concurrent-ruby >= 1.0.2
Requires: rubygem-zeitwerk >= 2.2
Requires: rubygem-zeitwerk < 3
Requires: rubygem-zeitwerk >= 2.2.2
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(activesupport) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A toolkit of support libraries and Ruby core extensions extracted from the
Rails framework. Rich support for multibyte strings, internationalization,
time zones, and testing.


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
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/
%{gemdir}/gems/activesupport-6.0.3.4/


%{gemdir}/cache/activesupport-6.0.3.4.gem
%{gemdir}/specifications/activesupport-6.0.3.4.gemspec

%changelog
