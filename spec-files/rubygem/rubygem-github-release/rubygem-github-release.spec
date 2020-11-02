# Generated from github-release-0.2.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname github-release
%define version 0.2.0
%define release 1

Summary: Upload tag annotations to github
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://theshed.hezmatt.org/github-release
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-octokit >= 3.0
Requires: rubygem-octokit < 5
Requires: rubygem-git-version-bump 
Requires: rubygem-rake 
Requires: rubygem-bundler 
Requires: rubygem-rdoc 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(github-release) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Upload tag annotations to github.

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
%{_bindir}/git-release
%{gemdir}/gems/github-release-0.2.0/

%{gemdir}/cache/github-release-0.2.0.gem
%{gemdir}/specifications/github-release-0.2.0.gemspec

%changelog
