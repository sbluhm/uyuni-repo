# Generated from atomic-1.1.16.gem by gem2rpm -*- rpm-spec -*-
%define rbname atomic
%define version 1.1.16
%define release 1

Summary: An atomic reference implementation for JRuby, Rubinius, and MRI
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/headius/ruby-atomic
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(atomic) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
An atomic reference implementation for JRuby, Rubinius, and MRI.


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
%{gemdir}/gems/atomic-1.1.16/
%{gemdir}/cache/atomic-1.1.16.gem
%{gemdir}/specifications/atomic-1.1.16.gemspec

%changelog
