# Generated from temple-0.8.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname temple
%define version 0.8.2
%define release 1

Summary: Template compilation framework in Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/judofyr/temple
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.2
Requires: rubygems >= 2.7.6.2
Requires: rubygem-tilt 
Requires: rubygem-bacon 
Requires: rubygem-rake 
Requires: rubygem-erubis 
BuildRequires: ruby >= 1.9.2
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(temple) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Template compilation framework in Ruby.

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
%{gemdir}/gems/temple-0.8.2/

%{gemdir}/cache/temple-0.8.2.gem
%{gemdir}/specifications/temple-0.8.2.gemspec

%changelog
