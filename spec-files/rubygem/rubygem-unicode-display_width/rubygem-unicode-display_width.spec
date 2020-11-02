# Generated from unicode-display_width-1.7.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname unicode-display_width
%define version 1.7.0
%define release 1

Summary: Determines the monospace display width of a string in Ruby.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/janlelis/unicode-display_width
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rspec >= 3.4
Requires: rubygem-rspec < 4
Requires: rubygem-rake >= 10.4
Requires: rubygem-rake < 11
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(unicode-display_width) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
[Unicode 13.0.0] Determines the monospace display width of a string using
EastAsianWidth.txt, Unicode general category, and other data.

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
%{gemdir}/gems/unicode-display_width-1.7.0/

%{gemdir}/cache/unicode-display_width-1.7.0.gem
%{gemdir}/specifications/unicode-display_width-1.7.0.gemspec

%changelog
