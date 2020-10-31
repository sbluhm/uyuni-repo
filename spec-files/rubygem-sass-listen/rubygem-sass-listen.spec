# Generated from sass-listen-4.0.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname sass-listen
%define version 4.0.0
%define release 1

Summary: Fork of guard/listen
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/sass/listen
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rb-fsevent >= 0.9
Requires: rubygem-rb-fsevent < 1
Requires: rubygem-rb-fsevent >= 0.9.4
Requires: rubygem-rb-inotify >= 0.9
Requires: rubygem-rb-inotify < 1
Requires: rubygem-rb-inotify >= 0.9.7
Requires: rubygem-bundler >= 1.3.5
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(sass-listen) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
This fork of guard/listen provides a stable API for users of the ruby Sass
CLI.

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
%{gemdir}/gems/sass-listen-4.0.0/

%{gemdir}/cache/sass-listen-4.0.0.gem
%{gemdir}/specifications/sass-listen-4.0.0.gemspec

%changelog
