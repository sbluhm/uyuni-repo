# Generated from minitest-hooks-1.4.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname minitest-hooks
%define version 1.4.2
%define release 1

Summary: Around and before_all/after_all/around_all hooks for Minitest
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/jeremyevans/minitest-hooks
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-minitest > 5
Requires: rubygem-sequel > 4
Requires: rubygem-sqlite3 
Requires: rubygem-rake 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(minitest-hooks) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
minitest-hooks adds around and before_all/after_all/around_all hooks for
Minitest.
This allows you do things like run each suite of specs inside a database
transaction,
running each spec inside its own savepoint inside that transaction, which can
significantly speed up testing for specs that share expensive database setup
code.

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
%{gemdir}/gems/minitest-hooks-1.4.2/

%{gemdir}/cache/minitest-hooks-1.4.2.gem
%{gemdir}/specifications/minitest-hooks-1.4.2.gemspec

%changelog
