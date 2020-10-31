# Generated from therubyracer-0.9.10.gem by gem2rpm -*- rpm-spec -*-
%define rbname therubyracer
%define version 0.9.10
%define release 1

Summary: Embed the V8 Javascript interpreter into Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/cowboyd/therubyracer
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-libv8 >= 3.3.10
Requires: rubygem-libv8 < 3.4
Requires: rubygem-rake 
Requires: rubygem-rspec >= 2.0
Requires: rubygem-rspec < 3
Requires: rubygem-rake-compiler 
BuildRequires: ruby 
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(therubyracer) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Call javascript code and manipulate javascript objects from ruby. Call ruby
code and manipulate ruby objects from javascript.

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
%{_bindir}/
%{gemdir}/gems/therubyracer-0.9.10/

%{gemdir}/cache/therubyracer-0.9.10.gem
%{gemdir}/specifications/therubyracer-0.9.10.gemspec

%changelog
