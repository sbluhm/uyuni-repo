# Generated from sass-3.7.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname sass
%define version 3.7.4
%define release 1

Summary: A powerful but elegant CSS compiler that makes CSS fun again.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://sass-lang.com/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-sass-listen >= 4.0.0
Requires: rubygem-sass-listen < 4.1
Requires: rubygem-yard >= 0.8.7.6
Requires: rubygem-yard < 0.8.8
Requires: rubygem-redcarpet >= 3.3
Requires: rubygem-redcarpet < 4
Requires: rubygem-nokogiri >= 1.6.0
Requires: rubygem-nokogiri < 1.7
Requires: rubygem-minitest >= 5
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(sass) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Ruby Sass is deprecated! See https://sass-lang.com/ruby-sass for
details.
Sass makes CSS fun again. Sass is an extension of CSS, adding
nested rules, variables, mixins, selector inheritance, and more.
It's translated to well-formatted, standard CSS using the
command line tool or a web-framework plugin.

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
%{_bindir}/sass
%{_bindir}/sass-convert
%{_bindir}/scss
%{gemdir}/gems/sass-3.7.4/

%{gemdir}/cache/sass-3.7.4.gem
%{gemdir}/specifications/sass-3.7.4.gemspec

%changelog
