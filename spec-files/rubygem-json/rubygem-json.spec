# Generated from json-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname json
%define version 2.0.0
%define release 1

Summary: JSON Implementation for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://flori.github.com/json
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0", "< 3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake 
Requires: rubygem-test-unit >= 2.0
Requires: rubygem-test-unit < 3
BuildRequires: ruby >= 2.0", "< 3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(json) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
This is a JSON implementation as a Ruby extension in C.


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
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/
%{gemdir}/gems/json-2.0.0/


%{gemdir}/cache/json-2.0.0.gem
%{gemdir}/specifications/json-2.0.0.gemspec

%changelog
