# Generated from rdoc-5.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rdoc
%define version 5.1.0
%define release 1

Summary: RDoc produces HTML and command-line documentation for Ruby projects
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://rdoc.github.io/rdoc
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake 
Requires: rubygem-racc > 1.4.10
Requires: rubygem-kpeg 
Requires: rubygem-minitest >= 4
Requires: rubygem-minitest < 5
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rdoc) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
RDoc produces HTML and command-line documentation for Ruby projects.
RDoc includes the +rdoc+ and +ri+ tools for generating and displaying
documentation from the command-line.


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
rmdir %{gembuilddir}/gems/%{rbname}-%{version}/bin/*

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{_bindir}/rdoc
%{_bindir}/ri
%{gemdir}/gems/rdoc-5.1.0/
%{gemdir}/cache/rdoc-5.1.0.gem
%{gemdir}/specifications/rdoc-5.1.0.gemspec

%changelog
