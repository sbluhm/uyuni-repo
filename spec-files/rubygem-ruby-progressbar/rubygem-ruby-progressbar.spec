# Generated from ruby-progressbar-1.10.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname ruby-progressbar
%define version 1.10.1
%define release 1

Summary: Ruby/ProgressBar is a flexible text progress bar library for Ruby.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/jfelchner/ruby-progressbar
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rspec >= 3.7
Requires: rubygem-rspec < 4
Requires: rubygem-rspectacular >= 0.70.6
Requires: rubygem-rspectacular < 0.71
Requires: rubygem-fuubar >= 2.3
Requires: rubygem-fuubar < 3
Requires: rubygem-warning_filter >= 0.0.6
Requires: rubygem-warning_filter < 0.1
Requires: rubygem-timecop = 0.6.0
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(ruby-progressbar) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Ruby/ProgressBar is an extremely flexible text progress bar library for Ruby.
The output can be customized with a flexible formatting system including:
percentage, bars of various formats, elapsed time and estimated time
remaining.

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
%{gemdir}/gems/ruby-progressbar-1.10.1/

%{gemdir}/cache/ruby-progressbar-1.10.1.gem
%{gemdir}/specifications/ruby-progressbar-1.10.1.gemspec

%changelog
