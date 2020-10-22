# Generated from rake-0.9.6.gem by gem2rpm -*- rpm-spec -*-
%define rbname rake
%define version 0.9.6
%define release 1

Summary: Ruby based make-like utility.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://rake.rubyforge.org
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.6
Requires: rubygems >= 2.7.6.2
Requires: rubygem-minitest >= 2.1
Requires: rubygem-minitest < 3
BuildRequires: ruby >= 1.8.6
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rake) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies
arespecified in standard Ruby syntax.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/gems/%{rbname}-%{version}/bin/** %{buildroot}/%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{_bindir}/rake
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/path
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/path
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/path
%{gemdir}/gems/rake-0.9.6/path
%{gemdir}/gems/rake-0.9.6/path
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/
%{gemdir}/gems/rake-0.9.6/


%{gemdir}/cache/rake-0.9.6.gem
%{gemdir}/specifications/rake-0.9.6.gemspec

%changelog
