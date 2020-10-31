# Generated from rainbow-3.0.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rainbow
%define version 3.0.0
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
Requires: ruby >= 2.1.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler >= 1.3
Requires: rubygem-bundler < 2
BuildRequires: ruby >= 2.1.0
BuildRequires: rubygems >= 2.7.6.2
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

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{gemdir}/gems/rainbow-3.0.0/

%{gemdir}/cache/rainbow-3.0.0.gem
%{gemdir}/specifications/rainbow-3.0.0.gemspec

%changelog
