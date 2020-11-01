# Generated from multi_test-0.1.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname multi_test
%define version 0.1.2
%define release 1

Summary: multi-test-0.1.2
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://cukes.info
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(multi_test) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Wafter-thin gem to help control rogue test/unit/autorun requires.

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
%{gemdir}/gems/multi_test-0.1.2/

%{gemdir}/cache/multi_test-0.1.2.gem
%{gemdir}/specifications/multi_test-0.1.2.gemspec

%changelog
