# Generated from cucumber-create-meta-2.0.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname cucumber-create-meta
%define version 2.0.4
%define release 1

Summary: cucumber-create-meta-2.0.4
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/cucumber/create-meta-ruby
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-cucumber-messages >= 13.1
Requires: rubygem-cucumber-messages < 14
Requires: rubygem-cucumber-messages >= 13.1.0
Requires: rubygem-sys-uname >= 1.2
Requires: rubygem-sys-uname < 2
Requires: rubygem-sys-uname >= 1.2.1
Requires: rubygem-rake >= 13.0
Requires: rubygem-rake < 14
Requires: rubygem-rake >= 13.0.1
Requires: rubygem-rspec >= 3.9
Requires: rubygem-rspec < 4
Requires: rubygem-rspec >= 3.9.0
BuildRequires: ruby >= 2.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(cucumber-create-meta) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Produce the meta message for Cucumber Ruby.

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
%{gemdir}/gems/cucumber-create-meta-2.0.4/

%{gemdir}/cache/cucumber-create-meta-2.0.4.gem
%{gemdir}/specifications/cucumber-create-meta-2.0.4.gemspec

%changelog
