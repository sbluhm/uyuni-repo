# Generated from lokar-0.2.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname lokar
%define version 0.2.1
%define release 1

Summary: Lokar is a simple fast template engine.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.0
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby >= 1.9.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(lokar) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Lokar is a simple fast template engine.

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
%{gemdir}/gems/lokar-0.2.1/

%{gemdir}/cache/lokar-0.2.1.gem
%{gemdir}/specifications/lokar-0.2.1.gemspec

%changelog
