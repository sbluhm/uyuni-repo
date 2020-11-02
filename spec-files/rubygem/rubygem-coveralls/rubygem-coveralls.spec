# Generated from coveralls-0.8.23.gem by gem2rpm -*- rpm-spec -*-
%define rbname coveralls
%define version 0.8.23
%define release 1

Summary: A Ruby implementation of the Coveralls API.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://coveralls.io
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 2.7.6.2
Requires: rubygem-json >= 1.8
Requires: rubygem-json < 3
Requires: rubygem-simplecov >= 0.16.1
Requires: rubygem-simplecov < 0.17
Requires: rubygem-tins >= 1.6
Requires: rubygem-tins < 2
Requires: rubygem-term-ansicolor >= 1.3
Requires: rubygem-term-ansicolor < 2
Requires: rubygem-thor >= 0.19.4
Requires: rubygem-thor < 2.0
Requires: rubygem-bundler >= 2.0
Requires: rubygem-bundler < 3
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(coveralls) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A Ruby implementation of the Coveralls API.

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/gems/%{rbname}-%{version}/bin/** %{buildroot}/%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{_bindir}/coveralls
%{gemdir}/gems/coveralls-0.8.23/

%{gemdir}/cache/coveralls-0.8.23.gem
%{gemdir}/specifications/coveralls-0.8.23.gemspec

%changelog
