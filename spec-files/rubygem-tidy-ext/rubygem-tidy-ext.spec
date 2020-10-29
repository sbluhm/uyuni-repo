# Generated from tidy-ext-0.1.14.gem by gem2rpm -*- rpm-spec -*-
%define rbname tidy-ext
%define version 0.1.14
%define release 1

Summary: W3C HTML Tidy library implemented as a Ruby native extension.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://bitbucket.org/carldouglas/tidy
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(tidy-ext) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Tidy up web pages.

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
%{gemdir}/gems/tidy-ext-0.1.14/

%{gemdir}/cache/tidy-ext-0.1.14.gem
%{gemdir}/specifications/tidy-ext-0.1.14.gemspec

%changelog
