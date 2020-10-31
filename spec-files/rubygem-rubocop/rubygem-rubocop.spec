# Generated from rubocop-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rubocop
%define version 1.1.0
%define release 1

Summary: Automatic Ruby code style checking tool.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/rubocop-hq/rubocop
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.4.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-parallel >= 1.10
Requires: rubygem-parallel < 2
Requires: rubygem-parser >= 2.7.1.5
Requires: rubygem-rainbow >= 2.2.2
Requires: rubygem-rainbow < 4.0
Requires: rubygem-regexp_parser >= 1.8
Requires: rubygem-rexml 
Requires: rubygem-rubocop-ast >= 1.0.1
Requires: rubygem-ruby-progressbar >= 1.7
Requires: rubygem-ruby-progressbar < 2
Requires: rubygem-unicode-display_width >= 1.4.0
Requires: rubygem-unicode-display_width < 2.0
Requires: rubygem-bundler >= 1.15.0
Requires: rubygem-bundler < 3.0
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rubocop) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
RuboCop is a Ruby code style checking and code formatting tool.
It aims to enforce the community-driven Ruby Style Guide.

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
%{_bindir}/
%{gemdir}/gems/rubocop-1.1.0/

%{gemdir}/cache/rubocop-1.1.0.gem
%{gemdir}/specifications/rubocop-1.1.0.gemspec

%changelog
