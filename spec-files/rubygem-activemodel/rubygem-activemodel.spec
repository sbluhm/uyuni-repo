# Generated from activemodel-6.0.3.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname activemodel
%define version 6.0.3.4
%define release 1

Summary: A toolkit for building modeling frameworks (part of Rails).
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
Requires: rubygem-activesupport = 6.0.3.4
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(activemodel) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A toolkit for building modeling frameworks like Active Record. Rich support
for attributes, callbacks, validations, serialization, internationalization,
and testing.


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
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/
%{gemdir}/gems/activemodel-6.0.3.4/


%{gemdir}/cache/activemodel-6.0.3.4.gem
%{gemdir}/specifications/activemodel-6.0.3.4.gemspec

%changelog
