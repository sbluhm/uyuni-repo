# Generated from launchy-2.0.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname launchy
%define version 2.0.4
%define release 1

Summary: Launchy is helper class for launching cross-platform applications in a fire and forget manner.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.copiousfreetime.org/projects/launchy
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-addressable >= 2.2.6
Requires: rubygem-addressable < 2.3
Requires: rubygem-rake >= 0.9.2
Requires: rubygem-rake < 0.10
Requires: rubygem-minitest >= 2.3.1
Requires: rubygem-minitest < 2.4
Requires: rubygem-bones >= 3.7.0
Requires: rubygem-bones < 3.8
Requires: rubygem-bones-rcov >= 1.0.1
Requires: rubygem-bones-rcov < 1.1
Requires: rubygem-rcov >= 0.9.9
Requires: rubygem-rcov < 0.10
Requires: rubygem-spoon >= 0.0.1
Requires: rubygem-spoon < 0.1
Requires: rubygem-ffi >= 1.0.9
Requires: rubygem-ffi < 1.1
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(launchy) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Launchy is helper class for launching cross-platform applications in a
fire and forget manner.
There are application concepts (browser, email client, etc) that are
common across all platforms, and they may be launched differently on
each platform.  Launchy is here to make a common approach to launching
external application from within ruby programs.

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
%{_bindir}/launchy
%{gemdir}/gems/launchy-2.0.4/

%{gemdir}/cache/launchy-2.0.4.gem
%{gemdir}/specifications/launchy-2.0.4.gemspec

%changelog
