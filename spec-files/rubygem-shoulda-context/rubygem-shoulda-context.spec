# Generated from shoulda-context-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname shoulda-context
%define version 2.0.0
%define release 1

Summary: Context framework extracted from Shoulda
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://thoughtbot.com/community/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(Shoulda-context) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Context framework extracted from Shoulda.


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
%{_bindir}/convert_to_should_syntax
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/
%{gemdir}/gems/shoulda-context-2.0.0/


%{gemdir}/cache/shoulda-context-2.0.0.gem
%{gemdir}/specifications/shoulda-context-2.0.0.gemspec

%changelog
