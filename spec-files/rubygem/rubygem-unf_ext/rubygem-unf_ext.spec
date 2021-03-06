# Generated from unf_ext-0.0.7.7.gem by gem2rpm -*- rpm-spec -*-
%define rbname unf_ext
%define version 0.0.7.7
%define release 1




Summary: Unicode Normalization Form support library for CRuby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/knu/ruby-unf_ext
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake >= 0.9.2.2
Requires: rubygem-test-unit 
Requires: rubygem-rdoc > 2.4.2
Requires: rubygem-bundler >= 1.2
Requires: rubygem-rake-compiler >= 0.7.9
Requires: rubygem-rake-compiler-dock >= 1.0.1
BuildRequires: ruby 
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(unf_ext) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Unicode Normalization Form support library for CRuby.

%global debug_package %{nil}

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}
mv %{gembuilddir}/extensions/x86_64-linux/2.5.0/unf_ext-0.0.7.7/*.so %{buildroot}%{_libdir}/gems/ruby/%{rbname}-%{version}
rm -f %{gembuilddir}/extensions/x86_64-linux/2.5.0/unf_ext-0.0.7.7/*


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/unf_ext-0.0.7.7/
%{gemdir}/cache/unf_ext-0.0.7.7.gem
%doc %{gemdir}/doc/%{rbname}-%{version}/
%{gemdir}/specifications/unf_ext-0.0.7.7.gemspec
%{_libdir}/gems/ruby/%{rbname}-%{version}/
%changelog
