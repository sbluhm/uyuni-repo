# Generated from therubyracer-0.12.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname therubyracer
%define version 0.12.3
%define release 1

Summary: Embed the V8 JavaScript interpreter into Ruby
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
Requires: rubygem-ref 
Requires: rubygem-libv8 >= 3.16.14.15
Requires: rubygem-libv8 < 3.16.15
BuildRequires: ruby 
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(therubyracer) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Call JavaScript code and manipulate JavaScript objects from Ruby. Call Ruby
code and manipulate Ruby objects from JavaScript.

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
%{gemdir}/gems/therubyracer-0.12.3/

%{gemdir}/cache/therubyracer-0.12.3.gem
%{gemdir}/specifications/therubyracer-0.12.3.gemspec

%changelog
