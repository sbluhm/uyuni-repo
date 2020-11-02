# Generated from Remarkably-0.6.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname Remarkably
%define version 0.6.1
%define release 1

Summary: A very tiny Markaby-like XML,HTML and CSS builder
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.darkarts.co.za/remarkably
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler >= 1.0.0
Requires: rubygem-rake >= 0.8.7
Requires: rubygem-rspec >= 1.3.0
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(Remarkably) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Remarkably is a very tiny Markaby-like XML,HTML and CSS builder.

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
%{gemdir}/gems/Remarkably-0.6.1/

%{gemdir}/cache/Remarkably-0.6.1.gem
%{gemdir}/specifications/Remarkably-0.6.1.gemspec

%changelog
