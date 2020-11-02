# Generated from minitest-shared_description-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname minitest-shared_description
%define version 1.0.0
%define release 1

Summary: Support for shared specs and shared spec subclasses for Minitest
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/jeremyevans/minitest-shared_description
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-minitest > 5
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(minitest-shared_description) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
minitest-shared_description adds support for shared specs and shared spec
subclasses
to Minitest.  Minitest supports shared specs by default using plain ruby
modules, but
does not support shared spec subclasses.  In addition to making it possible to
share
subclasses, minitest-shared_desciption also provides a slightly nicer
interface for
sharing specs.

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
%{gemdir}/gems/minitest-shared_description-1.0.0/

%{gemdir}/cache/minitest-shared_description-1.0.0.gem
%{gemdir}/specifications/minitest-shared_description-1.0.0.gemspec

%changelog
