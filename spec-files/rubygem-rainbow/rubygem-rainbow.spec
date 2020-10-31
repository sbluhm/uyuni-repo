# Generated from rainbow-2.2.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname rainbow
%define version 2.2.2
%define release 1

Summary: Colorize printed text on ANSI terminals
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/sickill/rainbow
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.2
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake 
Requires: rubygem-bundler >= 1.3
Requires: rubygem-bundler < 2
BuildRequires: ruby >= 1.9.2
BuildRequires: rubygems >= 2.7.6.2
BuildRequires: rubygem-rake
BuildArch: noarch
Provides: ruby(rainbow) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Colorize printed text on ANSI terminals.

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
rm -Rf %{gembuilddir}/extensions/x86_64-linux/2.5.0/rainbow-2.2.2/

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{gemdir}/gems/rainbow-2.2.2/

%{gemdir}/cache/rainbow-2.2.2.gem
%{gemdir}/specifications/rainbow-2.2.2.gemspec

%changelog
