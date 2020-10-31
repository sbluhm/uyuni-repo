# Generated from minitest-global_expectations-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname minitest-global_expectations
%define version 1.0.1
%define release 1

Summary: Support minitest expectation methods for all objects
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/jeremyevans/minitest-global_expectations
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-minitest > 5
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(minitest-global_expectations) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
minitest-global_expectations allows you to keep using simple code in your
minitest specs, without having to wrap every single object you are calling
an expectation method on with an underscore.

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
%{gemdir}/gems/minitest-global_expectations-1.0.1/

%{gemdir}/cache/minitest-global_expectations-1.0.1.gem
%{gemdir}/specifications/minitest-global_expectations-1.0.1.gemspec

%changelog
