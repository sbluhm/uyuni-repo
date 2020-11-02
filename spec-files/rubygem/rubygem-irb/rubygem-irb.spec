# Generated from irb-1.2.7.gem by gem2rpm -*- rpm-spec -*-
%define rbname irb
%define version 1.2.7
%define release 1

Summary: Interactive Ruby command-line tool for REPL (Read Eval Print Loop).
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ruby/irb
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.5
Requires: rubygems >= 2.7.6.2
Requires: rubygem-reline >= 0.1.5
Requires: rubygem-bundler 
Requires: rubygem-rake 
BuildRequires: ruby >= 2.5
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(irb) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Interactive Ruby command-line tool for REPL (Read Eval Print Loop).

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
%{_bindir}
%{gemdir}/gems/irb-1.2.7/

%{gemdir}/cache/irb-1.2.7.gem
%{gemdir}/specifications/irb-1.2.7.gemspec

%changelog
