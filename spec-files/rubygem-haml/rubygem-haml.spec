# Generated from haml-5.2.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname haml
%define version 5.2.0
%define release 1

Summary: An elegant, structured (X)HTML/XML templating engine.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://haml.info/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-temple >= 0.8.0
Requires: rubygem-tilt 
Requires: rubygem-rails >= 4.0.0
Requires: rubygem-rbench 
Requires: rubygem-minitest >= 4.0
Requires: rubygem-nokogiri 
Requires: rubygem-simplecov = 0.17.1
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(haml) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Haml (HTML Abstraction Markup Language) is a layer on top of HTML or XML
that's
designed to express the structure of documents in a non-repetitive, elegant,
and
easy way by using indentation rather than closing tags and allowing Ruby to be
embedded with ease. It was originally envisioned as a plugin for Ruby on
Rails,
but it can function as a stand-alone templating engine.

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
%{_bindir}/haml
%{gemdir}/gems/haml-5.2.0/

%{gemdir}/cache/haml-5.2.0.gem
%{gemdir}/specifications/haml-5.2.0.gemspec

%changelog
