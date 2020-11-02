# Generated from prawn-0.8.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname prawn
%define version 0.8.4
%define release 1

Summary: A fast and nimble PDF generator for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://wiki.github.com/sandal/prawn
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-prawn-core >= 0.8.4
Requires: rubygem-prawn-core < 0.9
Requires: rubygem-prawn-layout >= 0.8.4
Requires: rubygem-prawn-layout < 0.9
Requires: rubygem-prawn-security >= 0.8.4
Requires: rubygem-prawn-security < 0.9
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(prawn) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Prawn is a fast, tiny, and nimble PDF generator for Ruby.

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
%{gemdir}/gems/prawn-0.8.4/

%{gemdir}/cache/prawn-0.8.4.gem
%{gemdir}/specifications/prawn-0.8.4.gemspec

%changelog
