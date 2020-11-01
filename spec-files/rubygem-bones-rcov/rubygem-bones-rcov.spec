# Generated from bones-rcov-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname bones-rcov
%define version 1.0.1
%define release 1

Summary: The rcov package for Mr Bones provides tasks for running rcov over your unit tests and source code
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/TwP/bones-rcov
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bones >= 3.5.0
Requires: rubygem-rcov >= 0.9.9
Requires: rubygem-bones >= 3.5.0
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(bones-rcov) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
The rcov package for Mr Bones provides tasks for running rcov over your unit
tests and source code.

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
%{gemdir}/gems/bones-rcov-1.0.1/

%{gemdir}/cache/bones-rcov-1.0.1.gem
%{gemdir}/specifications/bones-rcov-1.0.1.gemspec

%changelog
