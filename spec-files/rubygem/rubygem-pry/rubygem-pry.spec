# Generated from pry-0.13.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname pry
%define version 0.13.1
%define release 1

Summary: A runtime developer console and IRB alternative with powerful introspection capabilities.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://pry.github.io
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-coderay >= 1.1
Requires: rubygem-coderay < 2
Requires: rubygem-method_source >= 1.0
Requires: rubygem-method_source < 2
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(pry) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Pry is a runtime developer console and IRB alternative with powerful
introspection capabilities. Pry aims to be more than an IRB replacement. It is
an attempt to bring REPL driven programming to the Ruby language.

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
%{_bindir}/pry
%{gemdir}/gems/pry-0.13.1/

%{gemdir}/cache/pry-0.13.1.gem
%{gemdir}/specifications/pry-0.13.1.gemspec

%changelog
