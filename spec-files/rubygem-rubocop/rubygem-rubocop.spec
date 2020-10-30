# Generated from rubocop-0.49.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname rubocop
%define version 0.49.1
%define release 1

Summary: Automatic Ruby code style checking tool.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/bbatsov/rubocop
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rainbow >= 1.99.1
Requires: rubygem-rainbow < 3.0
Requires: rubygem-parser >= 2.3.3.1
Requires: rubygem-parser < 3.0
Requires: rubygem-powerpack >= 0.1
Requires: rubygem-powerpack < 1
Requires: rubygem-ruby-progressbar >= 1.7
Requires: rubygem-ruby-progressbar < 2
Requires: rubygem-unicode-display_width >= 1.0
Requires: rubygem-unicode-display_width < 2
Requires: rubygem-unicode-display_width >= 1.0.1
Requires: rubygem-parallel >= 1.10
Requires: rubygem-parallel < 2
Requires: rubygem-bundler >= 1.3
Requires: rubygem-bundler < 2
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rubocop) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Automatic Ruby code style checking tool.
Aims to enforce the community-driven Ruby Style Guide.

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
%{_bindir}/rubocop
%{gemdir}/gems/rubocop-0.49.1/

%{gemdir}/cache/rubocop-0.49.1.gem
%{gemdir}/specifications/rubocop-0.49.1.gemspec

%changelog
