# Generated from packnga-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname packnga
%define version 1.0.4
%define release 1

Summary: An utility library to package i18n-ed library.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://ranguba.org/packnga/en/
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake 
Requires: rubygem-yard >= 0.9
Requires: rubygem-gettext >= 3.1.3
Requires: rubygem-test-unit 
Requires: rubygem-test-unit-notify 
Requires: rubygem-test-unit-rr 
Requires: rubygem-bundler 
Requires: rubygem-RedCloth 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(packnga) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Packnga is a library to translate to many languages by YARD.


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
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/
%{gemdir}/gems/packnga-1.0.4/


%{gemdir}/cache/packnga-1.0.4.gem
%{gemdir}/specifications/packnga-1.0.4.gemspec

%changelog
