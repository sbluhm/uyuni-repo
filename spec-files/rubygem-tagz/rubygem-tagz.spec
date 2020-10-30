# Generated from tagz-9.10.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname tagz
%define version 9.10.0
%define release 1

Summary: tagz
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ahoward/tagz
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(tagz) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
tagz.rb is generates html, xml, or any sgml variant like a small ninja
running across the backs of a herd of giraffes swatting of heads like
a mark-up weedwacker.  weighing in at less than 300 lines of code
tagz.rb adds an html/xml/sgml syntax to ruby that is both unobtrusive,
safe, and available globally to objects without the need for any
builder or superfluous objects.  tagz.rb is designed for applications
that generate html to be able to do so easily in any context without
heavyweight syntax or scoping issues, like a ninja sword through
butter.
.

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
%{gemdir}/gems/tagz-9.10.0/

%{gemdir}/cache/tagz-9.10.0.gem
%{gemdir}/specifications/tagz-9.10.0.gemspec

%changelog
