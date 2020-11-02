# Generated from simplecov-html-0.12.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname simplecov-html
%define version 0.12.3
%define release 1

Summary: Default HTML formatter for SimpleCov code coverage tool for ruby 2.4+
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/simplecov-ruby/simplecov-html
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.4
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby >= 2.4
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(simplecov-html) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Default HTML formatter for SimpleCov code coverage tool for ruby 2.4+.


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
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/
%{gemdir}/gems/simplecov-html-0.12.3/


%{gemdir}/cache/simplecov-html-0.12.3.gem
%{gemdir}/specifications/simplecov-html-0.12.3.gemspec

%changelog
