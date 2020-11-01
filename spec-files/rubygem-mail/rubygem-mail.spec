# Generated from mail-2.7.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname mail
%define version 2.7.1
%define release 1

Summary: Mail provides a nice Ruby DSL for making, sending and reading emails.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/mikel/mail
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-mini_mime >= 0.1.1
Requires: rubygem-bundler >= 1.0.3
Requires: rubygem-rake > 0.8.7
Requires: rubygem-rspec >= 3.0
Requires: rubygem-rspec < 4
Requires: rubygem-rdoc 
Requires: rubygem-rufo 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(mail) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A really Ruby Mail handler.

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
%{gemdir}/gems/mail-2.7.1/

%{gemdir}/cache/mail-2.7.1.gem
%{gemdir}/specifications/mail-2.7.1.gemspec

%changelog
