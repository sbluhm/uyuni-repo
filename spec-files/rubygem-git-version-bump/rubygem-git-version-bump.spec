# Generated from git-version-bump-0.17.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname git-version-bump
%define version 0.17.1
%define release 1

Summary: Manage your app version entirely via git tags
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://theshed.hezmatt.org/git-version-bump
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.1.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-github-release 
Requires: rubygem-rake 
Requires: rubygem-bundler 
Requires: rubygem-rdoc 
BuildRequires: ruby >= 2.1.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(git-version-bump) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Manage your app version entirely via git tags.

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
%{_bindir}/git-version-bump
%{gemdir}/gems/git-version-bump-0.17.1/

%{gemdir}/cache/git-version-bump-0.17.1.gem
%{gemdir}/specifications/git-version-bump-0.17.1.gemspec

%changelog
