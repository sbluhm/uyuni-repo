# Generated from hoe-git-1.6.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname hoe-git
%define version 1.6.0
%define release 1

Summary: A set of Hoe plugins for tighter Git integration
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/jbarnette/hoe-git
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rdoc >= 4.0
Requires: rubygem-rdoc < 5
Requires: rubygem-hoe >= 3.7
Requires: rubygem-hoe < 4
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(hoe-git) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A set of Hoe plugins for tighter Git integration. Provides tasks to
automate release tagging and pushing and changelog generation. I
expect it'll learn a few more tricks in the future.

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
%{gemdir}/gems/hoe-git-1.6.0/

%{gemdir}/cache/hoe-git-1.6.0.gem
%{gemdir}/specifications/hoe-git-1.6.0.gemspec

%changelog
