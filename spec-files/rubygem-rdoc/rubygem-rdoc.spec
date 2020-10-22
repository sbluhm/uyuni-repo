# Generated from rdoc-4.3.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rdoc
%define version 4.3.0
%define release 1

Summary: RDoc produces HTML and command-line documentation for Ruby projects
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://docs.seattlerb.org/rdoc
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-kpeg >= 0.9
Requires: rubygem-kpeg < 1
Requires: rubygem-minitest >= 5.9
Requires: rubygem-minitest < 6
Requires: rubygem-racc >= 1.4
Requires: rubygem-racc < 2
Requires: rubygem-racc > 1.4.10
Requires: rubygem-rdoc >= 4.0
Requires: rubygem-rdoc < 5
Requires: rubygem-hoe >= 3.15
Requires: rubygem-hoe < 4
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rdoc) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
RDoc produces HTML and command-line documentation for Ruby projects.  RDoc
includes the +rdoc+ and +ri+ tools for generating and displaying documentation
from the command-line.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e Vputs Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/gems/%{rbname}-%{version}/bin/** %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/gems/%{rbname}-%{version}/bin/*

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{_bindir}/rdoc
%{_bindir}/ri
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/path
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/path
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/
%{gemdir}/gems/rdoc-4.3.0/


%{gemdir}/cache/rdoc-4.3.0.gem
%{gemdir}/specifications/rdoc-4.3.0.gemspec

%changelog
