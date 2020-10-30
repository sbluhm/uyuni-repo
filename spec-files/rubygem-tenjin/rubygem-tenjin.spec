# Generated from tenjin-0.7.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname tenjin
%define version 0.7.1
%define release 1

Summary: very fast and full-featured template engine
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.kuwata-lab.com/tenjin/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(tenjin) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Tenjin is a template engine and has the following features.
* Very fast and lightweight
* Small and only a file
* Auto escaping support
* Auto trimming spaces around embedded statements
* Context object available
* Able to load YAML data file
* Preprocessing support.

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
%{_bindir}/rbtenjin
%{gemdir}/gems/tenjin-0.7.1/

%{gemdir}/cache/tenjin-0.7.1.gem
%{gemdir}/specifications/tenjin-0.7.1.gemspec

%changelog
