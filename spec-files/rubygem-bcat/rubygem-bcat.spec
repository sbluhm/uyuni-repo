# Generated from bcat-0.6.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname bcat
%define version 0.6.2
%define release 1

Summary: Concatenate input from standard input, or one or more files, and write progressive output to a browser.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://rtomayko.github.com/bcat/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rack >= 1.0
Requires: rubygem-rack < 2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(bcat) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
pipe to browser utility.


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
%{_bindir}/a2h
%{_bindir}/bcat
%{_bindir}/btee
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/
%{gemdir}/gems/bcat-0.6.2/


%{gemdir}/cache/bcat-0.6.2.gem
%{gemdir}/specifications/bcat-0.6.2.gemspec

%changelog
