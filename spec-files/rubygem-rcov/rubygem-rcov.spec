# Generated from rcov-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rcov
%define version 1.0.0
%define release 1

Summary: Code coverage analysis tool for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/relevance/rcov
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildRequires: ruby-devel
BuildArch: noarch
Provides: ruby(rcov) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
rcov is a code coverage tool for Ruby.


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
%{_bindir}/rcov
%{gemdir}/gems/rcov-1.0.0/
%{gemdir}/cache/rcov-1.0.0.gem
%{gemdir}/specifications/rcov-1.0.0.gemspec

%changelog
