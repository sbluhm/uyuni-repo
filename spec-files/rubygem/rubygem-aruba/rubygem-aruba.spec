# Generated from aruba-0.4.11.gem by gem2rpm -*- rpm-spec -*-
%define rbname aruba
%define version 0.4.11
%define release 1

Summary: aruba-0.4.11
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/cucumber/aruba
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-cucumber >= 1.1.1
Requires: rubygem-childprocess >= 0.2.3
Requires: rubygem-ffi >= 1.0.11
Requires: rubygem-rspec >= 2.7.0
Requires: rubygem-bcat >= 0.6.1
Requires: rubygem-rdiscount >= 1.6.8
Requires: rubygem-rake >= 0.9.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(aruba) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
CLI Steps for Cucumber, hand-crafted for you in Aruba.


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
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/
%{gemdir}/gems/aruba-0.4.11/


%{gemdir}/cache/aruba-0.4.11.gem
%{gemdir}/specifications/aruba-0.4.11.gemspec

%changelog
