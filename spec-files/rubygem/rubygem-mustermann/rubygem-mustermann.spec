# Generated from mustermann-1.1.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname mustermann
%define version 1.1.1
%define release 1

Summary: Your personal string matching expert.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/sinatra/mustermann
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.2.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-ruby2_keywords >= 0.0.1
Requires: rubygem-ruby2_keywords < 0.1
BuildRequires: ruby >= 2.2.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(mustermann) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A library implementing patterns that behave like regular expressions.

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
%{gemdir}/gems/mustermann-1.1.1/

%{gemdir}/cache/mustermann-1.1.1.gem
%{gemdir}/specifications/mustermann-1.1.1.gemspec

%changelog
