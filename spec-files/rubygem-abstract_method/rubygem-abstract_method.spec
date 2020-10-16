# Generated from abstract_method-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname abstract_method
%define version 1.2.1
%define release 1

Summary: Tiny library enabling you to define abstract methods in Ruby classes and modules
Name: rubygems-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/openSUSE/abstract_method
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rspec 
Requires: rubygem-yard 
Requires: rubygem-redcarpet 
BuildRequires: ruby
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(Abstract_method) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Abstract Method is a tiny library enabling you to define abstract methods in
Ruby classes and modules.


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
%{gemdir}/gems/abstract_method-1.2.1/
%doc %{gemdir}/doc/abstract_method-1.2.1/
%{gemdir}/cache/abstract_method-1.2.1.gem
%{gemdir}/specifications/abstract_method-1.2.1.gemspec

%changelog
