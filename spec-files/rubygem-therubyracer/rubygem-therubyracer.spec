# Generated from therubyracer-0.5.0-x86_64-linux.gem by gem2rpm -*- rpm-spec -*-
%define rbname therubyracer
%define version 0.5.0
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
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
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
sed -i '1 s/python\b/python3/g' %{gembuilddir}/gems/%{rbname}-%{version}-x86_64-linux/ext/v8/upstream/2.0.6/tools/*.py

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}-x86_64-linux/
%defattr(-, root, root)
%{gemdir}/gems/therubyracer-0.5.0-x86_64-linux/
%{gemdir}/cache/therubyracer-0.5.0-x86_64-linux.gem
%{gemdir}/specifications/therubyracer-0.5.0-x86_64-linux.gemspec

%changelog
