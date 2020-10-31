# Generated from sourcemap-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname sourcemap
%define version 0.1.1
%define release 1

Summary: Ruby source maps
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/maccman/sourcemap
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bundler >= 1.3
Requires: rubygem-bundler < 2
Requires: rubygem-rake 
Requires: rubygem-minitest 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(sourcemap) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Ruby source maps.

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
%{gemdir}/gems/sourcemap-0.1.1/

%{gemdir}/cache/sourcemap-0.1.1.gem
%{gemdir}/specifications/sourcemap-0.1.1.gemspec

%changelog
