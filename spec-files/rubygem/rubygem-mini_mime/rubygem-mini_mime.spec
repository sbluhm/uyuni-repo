# Generated from mini_mime-1.0.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname mini_mime
%define version 1.0.2
%define release 1

Summary: A lightweight mime type lookup toy
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/discourse/mini_mime
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler >= 1.13
Requires: rubygem-rake >= 10.0
Requires: rubygem-rake < 11
Requires: rubygem-minitest >= 5.0
Requires: rubygem-minitest < 6
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(mini_mime) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A lightweight mime type lookup toy.

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
%{gemdir}/gems/mini_mime-1.0.2/

%{gemdir}/cache/mini_mime-1.0.2.gem
%{gemdir}/specifications/mini_mime-1.0.2.gemspec

%changelog
