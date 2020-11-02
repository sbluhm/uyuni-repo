# Generated from reline-0.1.6.gem by gem2rpm -*- rpm-spec -*-
%define rbname reline
%define version 0.1.6
%define release 1

Summary: Alternative GNU Readline or Editline implementation by pure Ruby.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ruby/reline
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.5
Requires: rubygems >= 2.7.6.2
Requires: rubygem-io-console >= 0.5
Requires: rubygem-io-console < 1
Requires: rubygem-bundler 
Requires: rubygem-rake 
Requires: rubygem-test-unit 
Requires: rubygem-yamatanooroti >= 0.0.6
BuildRequires: ruby >= 2.5
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(reline) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Alternative GNU Readline or Editline implementation by pure Ruby.

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
%{gemdir}/gems/reline-0.1.6/

%{gemdir}/cache/reline-0.1.6.gem
%{gemdir}/specifications/reline-0.1.6.gemspec

%changelog
