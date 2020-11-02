# Generated from uglifier-4.2.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname uglifier
%define version 4.2.0
%define release 1

Summary: Ruby wrapper for UglifyJS JavaScript compressor
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/lautis/uglifier
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-execjs >= 0.3.0
Requires: rubygem-execjs < 3
Requires: rubygem-rspec >= 3.0
Requires: rubygem-rspec < 4
Requires: rubygem-rake >= 12.0
Requires: rubygem-rake < 13
Requires: rubygem-bundler >= 1.3
Requires: rubygem-sourcemap >= 0.1.1
Requires: rubygem-sourcemap < 0.2
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(uglifier) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Uglifier minifies JavaScript files by wrapping UglifyJS to be accessible in
Ruby.

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
%{gemdir}/gems/uglifier-4.2.0/

%{gemdir}/cache/uglifier-4.2.0.gem
%{gemdir}/specifications/uglifier-4.2.0.gemspec

%changelog
