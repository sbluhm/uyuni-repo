# Generated from cucumber-messages-13.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname cucumber-messages
%define version 13.1.0
%define release 1

Summary: cucumber-messages-13.1.0
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/cucumber/messages-ruby#readme
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-protobuf-cucumber >= 3.10
Requires: rubygem-protobuf-cucumber < 4
Requires: rubygem-protobuf-cucumber >= 3.10.8
Requires: rubygem-rake >= 13.0
Requires: rubygem-rake < 14
Requires: rubygem-rake >= 13.0.1
Requires: rubygem-rspec >= 3.9
Requires: rubygem-rspec < 4
Requires: rubygem-rspec >= 3.9.0
BuildRequires: ruby >= 2.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(cucumber-messages) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Protocol Buffer messages for Cucumber's inter-process communication.

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
%{gemdir}/gems/cucumber-messages-13.1.0/

%{gemdir}/cache/cucumber-messages-13.1.0.gem
%{gemdir}/specifications/cucumber-messages-13.1.0.gemspec

%changelog
