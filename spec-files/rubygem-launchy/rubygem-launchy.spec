# Generated from launchy-2.5.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname launchy
%define version 2.5.0
%define release 1

Summary: Launchy is helper class for launching cross-platform applications in a fire and forget manner.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/copiousfreetime/launchy
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.4.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-addressable >= 2.7
Requires: rubygem-addressable < 3
Requires: rubygem-rake >= 13.0
Requires: rubygem-rake < 14
Requires: rubygem-minitest >= 5.14
Requires: rubygem-minitest < 6
Requires: rubygem-rdoc >= 6.2
Requires: rubygem-rdoc < 7
Requires: rubygem-simplecov >= 0.18
Requires: rubygem-simplecov < 1
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(launchy) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Launchy is helper class for launching cross-platform applications in a fire
and forget manner. There are application concepts (browser, email client, etc)
that are common across all platforms, and they may be launched differently on
each platform. Launchy is here to make a common approach to launching external
applications from within ruby programs.

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
%{gemdir}/gems/launchy-2.5.0/

%{gemdir}/cache/launchy-2.5.0.gem
%{gemdir}/specifications/launchy-2.5.0.gemspec

%changelog
