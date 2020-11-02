# Generated from activesupport-3.2.22.5.gem by gem2rpm -*- rpm-spec -*-
%define rbname activesupport
%define version 3.2.22.5
%define release 1

Summary: A toolkit of support libraries and Ruby core extensions extracted from the Rails framework.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.rubyonrails.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 2.7.6.2
Requires: rubygem-i18n >= 0.6
Requires: rubygem-i18n < 1
Requires: rubygem-i18n >= 0.6.4
Requires: rubygem-multi_json >= 1.0
Requires: rubygem-multi_json < 2
BuildRequires: ruby >= 1.8.7
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
%{gemdir}/gems/activesupport-3.2.22.5/

%{gemdir}/cache/activesupport-3.2.22.5.gem
%{gemdir}/specifications/activesupport-3.2.22.5.gemspec

%changelog
