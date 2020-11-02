# Generated from rake-compiler-dock-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname rake-compiler-dock
%define version 1.0.1
%define release 1

Summary: Easy to use and reliable cross compiler environment for building Windows and Linux binary gems.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/rake-compiler/rake-compiler-dock
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler >= 1.7
Requires: rubygem-bundler < 2
Requires: rubygem-rake >= 12.0
Requires: rubygem-rake < 13
Requires: rubygem-test-unit >= 3.0
Requires: rubygem-test-unit < 4
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rake-compiler-dock) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Easy to use and reliable cross compiler environment for building Windows and
Linux binary gems.
Use rake-compiler-dock to enter an interactive shell session or add a task to
your Rakefile to automate your cross build.


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
%{_bindir}/rake-compiler-dock
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/
%{gemdir}/gems/rake-compiler-dock-1.0.1/


%{gemdir}/cache/rake-compiler-dock-1.0.1.gem
%{gemdir}/specifications/rake-compiler-dock-1.0.1.gemspec

%changelog
