# Generated from cheetah-0.5.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname cheetah
%define version 0.5.2
%define release 1

Summary: Your swiss army knife for executing external commands in Ruby safely and conveniently.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/openSUSE/cheetah
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-abstract_method >= 1.2
Requires: rubygem-abstract_method < 2
Requires: rubygem-rspec >= 3.3
Requires: rubygem-rspec < 4
Requires: rubygem-yard >= 0.9.11
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: rubygem(cheetah) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Your swiss army knife for executing external commands in Ruby safely and
conveniently.


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
%defattr(-, root, root)
%{gemdir}/gems/cheetah-0.5.2/
%doc %{gemdir}/doc/cheetah-0.5.2/
%{gemdir}/cache/cheetah-0.5.2.gem
%{gemdir}/specifications/cheetah-0.5.2.gemspec

%changelog
