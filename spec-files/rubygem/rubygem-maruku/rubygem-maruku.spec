# Generated from maruku-0.7.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname maruku
%define version 0.7.3
%define release 1

Summary: Maruku is a Markdown-superset interpreter written in Ruby.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/bhollis/maruku
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(maruku) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Maruku is a Markdown interpreter in Ruby.
It features native export to HTML and PDF (via Latex). The
output is really beautiful!

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
%{_bindir}/maruku
%{_bindir}/marutex
%{gemdir}/gems/maruku-0.7.3/

%{gemdir}/cache/maruku-0.7.3.gem
%{gemdir}/specifications/maruku-0.7.3.gemspec

%changelog
