# Generated from rake-compiler-0.9.9.gem by gem2rpm -*- rpm-spec -*-
%define rbname rake-compiler
%define version 0.9.9
%define release 1

Summary: Rake-based Ruby Extension (C, Java) task generator.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/rake-compiler/rake-compiler
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake 
Requires: rubygem-rspec >= 2.8.0
Requires: rubygem-rspec < 2.9
Requires: rubygem-cucumber >= 1.1.4
Requires: rubygem-cucumber < 1.2
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rake-compiler) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Provide a standard and simplified way to build and package
Ruby extensions (C, Java) using Rake as glue.

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
%{_bindir}/rake-compiler
%{gemdir}/gems/rake-compiler-0.9.9/

%{gemdir}/cache/rake-compiler-0.9.9.gem
%{gemdir}/specifications/rake-compiler-0.9.9.gemspec

%changelog
