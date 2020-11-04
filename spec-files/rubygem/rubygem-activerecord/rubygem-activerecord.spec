# Generated from activerecord-6.0.3.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname activerecord
%define version 6.0.3.4
%define release 1

Summary: Object-relational mapper framework (part of Rails).
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://rubyonrails.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.5.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-activesupport = 6.0.3.4
Requires: rubygem-activemodel = 6.0.3.4
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(activerecord) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations,
aggregations, migrations, and testing come baked-in.


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
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/
%{gemdir}/gems/activerecord-6.0.3.4/


%{gemdir}/cache/activerecord-6.0.3.4.gem
%{gemdir}/specifications/activerecord-6.0.3.4.gemspec

%changelog