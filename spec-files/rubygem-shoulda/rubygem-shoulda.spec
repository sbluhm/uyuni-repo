# Generated from shoulda-4.0.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname shoulda
%define version 4.0.0
%define release 1

Summary: Making tests easy on the fingers and eyes
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/thoughtbot/shoulda
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-shoulda-context >= 2.0
Requires: rubygem-shoulda-context < 3
Requires: rubygem-shoulda-matchers >= 4.0
Requires: rubygem-shoulda-matchers < 5
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(shoulda) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Making tests easy on the fingers and eyes.


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
%{gemdir}/gems/shoulda-4.0.0/
%doc %{gemdir}/doc/%{rbname}-%{version}/
%{gemdir}/cache/shoulda-4.0.0.gem
%{gemdir}/specifications/shoulda-4.0.0.gemspec

%changelog
