# Generated from rspec-3.10.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rspec
%define version 3.10.0
%define release 1

Summary: rspec-3.10.0
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/rspec
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rspec-core >= 3.10.0
Requires: rubygem-rspec-core < 3.11
Requires: rubygem-rspec-expectations >= 3.10.0
Requires: rubygem-rspec-expectations < 3.11
Requires: rubygem-rspec-mocks >= 3.10.0
Requires: rubygem-rspec-mocks < 3.11
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rspec) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
BDD for Ruby.

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
%{gemdir}/gems/rspec-3.10.0/

%{gemdir}/cache/rspec-3.10.0.gem
%{gemdir}/specifications/rspec-3.10.0.gemspec

%changelog
