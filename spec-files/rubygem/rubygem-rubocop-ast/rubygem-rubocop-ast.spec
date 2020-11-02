# Generated from rubocop-ast-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rubocop-ast
%define version 1.1.0
%define release 1

Summary: RuboCop tools to deal with Ruby code AST.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/rubocop-hq/rubocop-ast
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.3.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-parser >= 2.7.1.5
Requires: rubygem-bundler >= 1.15.0
Requires: rubygem-bundler < 3.0
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rubocop-ast) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
RuboCop's Node and NodePattern classes.

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
%{gemdir}/gems/rubocop-ast-1.1.0/

%{gemdir}/cache/rubocop-ast-1.1.0.gem
%{gemdir}/specifications/rubocop-ast-1.1.0.gemspec

%changelog
