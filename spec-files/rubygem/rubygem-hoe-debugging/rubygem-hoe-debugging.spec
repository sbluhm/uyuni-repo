# Generated from hoe-debugging-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname hoe-debugging
%define version 1.2.1
%define release 1

Summary: A Hoe plugin to help you debug your C extensions
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/jbarnette/hoe-debugging
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rdoc >= 4.0
Requires: rubygem-rdoc < 5
Requires: rubygem-hoe >= 3.1
Requires: rubygem-hoe < 4
Requires: rubygem-rspec >= 2.0
Requires: rubygem-rspec < 3
Requires: rubygem-hoe-git 
Requires: rubygem-hoe-gemspec 
Requires: rubygem-hoe-bundler 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(hoe-debugging) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A Hoe plugin to help you debug your C extensions. This plugin provides
<tt>test:gdb</tt> and <tt>test:valgrind</tt> tasks (plus a few
variants).
See the Hoe::Debugging module for a few configuration options.
This plugin expects you to have <tt>gdb</tt> and <tt>valgrind</tt>
available in your <tt>PATH</tt>.
These tasks were extracted from nokogiri / johnson and originally written by
ruby legend, {Mike Dalessio}[http://mike.daless.io].

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
%{gemdir}/gems/hoe-debugging-1.2.1/

%{gemdir}/cache/hoe-debugging-1.2.1.gem
%{gemdir}/specifications/hoe-debugging-1.2.1.gemspec

%changelog
