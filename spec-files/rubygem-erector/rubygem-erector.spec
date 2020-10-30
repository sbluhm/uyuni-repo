# Generated from erector-0.10.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname erector
%define version 0.10.0
%define release 1

Summary: HTML/XML Builder library
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://erector.rubyforge.org/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-treetop >= 1.2.3
Requires: rubygem-rake >= 10.0.1
Requires: rubygem-rake < 10.1
Requires: rubygem-activesupport >= 3
Requires: rubygem-activesupport < 4
Requires: rubygem-rspec >= 2
Requires: rubygem-rspec < 3
Requires: rubygem-rubyforge 
Requires: rubygem-rr 
Requires: rubygem-nokogiri 
Requires: rubygem-jeweler 
Requires: rubygem-haml 
Requires: rubygem-sass 
Requires: rubygem-erubis 
Requires: rubygem-rdoc >= 3.4
Requires: rubygem-rdoc < 4
Requires: rubygem-wrong >= 0.6.3
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(erector) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Erector is a Builder-like view framework, inspired by Markaby but overcoming
some of its flaws. In Erector all views are objects, not template files, which
allows the full power of object-oriented programming (inheritance, modular
decomposition, encapsulation) in views.

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
%{_bindir}/erector
%{gemdir}/gems/erector-0.10.0/

%{gemdir}/cache/erector-0.10.0.gem
%{gemdir}/specifications/erector-0.10.0.gemspec

%changelog
