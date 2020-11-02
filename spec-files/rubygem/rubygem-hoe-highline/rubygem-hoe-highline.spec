# Generated from hoe-highline-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname hoe-highline
%define version 0.0.1
%define release 1

Summary: A Hoe plugin for building interactive Rake tasks
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://bitbucket.org/ged/hoe-highline
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 2.7.6.2
Requires: rubygem-highline >= 1.6
Requires: rubygem-highline < 2
Requires: rubygem-hoe >= 2.8
Requires: rubygem-hoe < 3
Requires: rubygem-hoe-mercurial >= 1.2.1
Requires: rubygem-hoe-mercurial < 1.3
Requires: rubygem-hoe >= 2.9.1
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(hoe-highline) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A Hoe plugin for building interactive Rake tasks.
Hoe-highline, as you might have guessed from the name, adds prompting and
displaying functions from the [HighLine][highline] gem to your Rake
environment, allowing you to ask questions, prompt for passwords, build menus,
and other fun stuff.

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
%{gemdir}/gems/hoe-highline-0.0.1/

%{gemdir}/cache/hoe-highline-0.0.1.gem
%{gemdir}/specifications/hoe-highline-0.0.1.gemspec

%changelog
