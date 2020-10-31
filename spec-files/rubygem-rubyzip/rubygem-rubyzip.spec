# Generated from rubyzip-2.3.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rubyzip
%define version 2.3.0
%define release 1

Summary: rubyzip is a ruby module for reading and writing zip files
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/rubyzip/rubyzip
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.4
Requires: rubygems >= 2.7.6.2
Requires: rubygem-coveralls >= 0.7
Requires: rubygem-coveralls < 1
Requires: rubygem-minitest >= 5.4
Requires: rubygem-minitest < 6
Requires: rubygem-pry >= 0.10
Requires: rubygem-pry < 1
Requires: rubygem-rake >= 12.3
Requires: rubygem-rake < 13
Requires: rubygem-rake >= 12.3.3
Requires: rubygem-rubocop >= 0.79
Requires: rubygem-rubocop < 1
BuildRequires: ruby >= 2.4
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rubyzip) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
rubyzip is a ruby module for reading and writing zip files.

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
%{gemdir}/gems/rubyzip-2.3.0/

%{gemdir}/cache/rubyzip-2.3.0.gem
%{gemdir}/specifications/rubyzip-2.3.0.gemspec

%changelog
