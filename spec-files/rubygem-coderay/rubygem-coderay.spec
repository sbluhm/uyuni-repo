# Generated from coderay-1.0.9.gem by gem2rpm -*- rpm-spec -*-
%define rbname coderay
%define version 1.0.9
%define release 1

Summary: Fast syntax highlighting for selected languages.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://coderay.rubychan.de
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.6
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby >= 1.8.6
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(coderay) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Fast and easy syntax highlighting for selected languages, written in Ruby.
Comes with RedCloth integration and LOC counter.

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
%{_bindir}/coderay
%{gemdir}/gems/coderay-1.0.9/

%{gemdir}/cache/coderay-1.0.9.gem
%{gemdir}/specifications/coderay-1.0.9.gemspec

%changelog
