# Generated from hoe-mercurial-1.3.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname hoe-mercurial
%define version 1.3.1
%define release 1

Summary: This is a fork of the [hoe-hg](https://bitbucket.org/mml/hoe-hg)  plugin
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://bitbucket.org/ged/hoe-mercurial
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-hoe >= 2.12
Requires: rubygem-hoe < 3
Requires: rubygem-hoe-highline >= 0.0.1
Requires: rubygem-hoe-highline < 0.1
Requires: rubygem-hoe >= 2.12
Requires: rubygem-hoe < 3
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(hoe-mercurial) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
This is a fork of the [hoe-hg](https://bitbucket.org/mml/hoe-hg) 
plugin. I forked it because I use quite a few additional Mercurial 
tasks for my development workflow than are provided by the original, 
and I thought they'd possibly be useful to someone else.
I've offered to push my changes back up to the original, but I gave
up waiting for a response.

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
%{gemdir}/gems/hoe-mercurial-1.3.1/

%{gemdir}/cache/hoe-mercurial-1.3.1.gem
%{gemdir}/specifications/hoe-mercurial-1.3.1.gemspec

%changelog
