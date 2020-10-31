# Generated from minitar-0.5.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname minitar
%define version 0.5.4
%define release 1

Summary: Provides POSIX tarchive management from Ruby programs.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.github.com/atoulme/minitar
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.2
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby >= 1.8.2
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(minitar) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Archive::Tar::Minitar is a pure-Ruby library and command-line utility that
provides the ability to deal with POSIX tar(1) archive files. The
implementation is based heavily on Mauricio Ferna'ndez's implementation in
rpa-base, but has been reorganised to promote reuse in other projects. Antoine
Toulme forked the original project on rubyforge to place it on github, under
http://www.github.com/atoulme/minitar.

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
%{_bindir}/minitar
%{gemdir}/gems/minitar-0.5.4/

%{gemdir}/cache/minitar-0.5.4.gem
%{gemdir}/specifications/minitar-0.5.4.gemspec

%changelog
