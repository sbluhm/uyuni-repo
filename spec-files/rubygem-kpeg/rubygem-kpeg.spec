# Generated from kpeg-0.10.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname kpeg
%define version 0.10.0
%define release 1

Summary: KPeg is a simple PEG library for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/evanphx/kpeg
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-minitest >= 2.12
Requires: rubygem-minitest < 3
Requires: rubygem-rdoc >= 3.10
Requires: rubygem-rdoc < 4
Requires: rubygem-hoe >= 2.16
Requires: rubygem-hoe < 3
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(kpeg) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
KPeg is a simple PEG library for Ruby. It provides an API as well as native
grammar to build the grammar.
KPeg strives to provide a simple, powerful API without being too exotic.
KPeg supports direct left recursion of rules via the
{OMeta memoization}[http://www.vpri.org/pdf/tr2008003_experimenting.pdf]
trick.


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
%{_bindir}/kpeg
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/
%{gemdir}/gems/kpeg-0.10.0/


%{gemdir}/cache/kpeg-0.10.0.gem
%{gemdir}/specifications/kpeg-0.10.0.gemspec

%changelog
