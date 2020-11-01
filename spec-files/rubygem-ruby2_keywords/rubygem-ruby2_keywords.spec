# Generated from ruby2_keywords-0.0.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname ruby2_keywords
%define version 0.0.2
%define release 1

Summary: Shim library for Module#ruby2_keywords
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ruby/ruby2_keywords
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(ruby2_keywords) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Shim library for Module#ruby2_keywords.

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
%{gemdir}/gems/ruby2_keywords-0.0.2/

%{gemdir}/cache/ruby2_keywords-0.0.2.gem
%{gemdir}/specifications/ruby2_keywords-0.0.2.gemspec

%changelog
