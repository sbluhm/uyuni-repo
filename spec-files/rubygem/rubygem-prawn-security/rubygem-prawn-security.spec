# Generated from prawn-security-0.8.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname prawn-security
%define version 0.8.4
%define release 1

Summary: Popular Password Protection & Permissions for Prawn PDFs
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/madriska/prawn-security/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(prawn-security) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Prawn/Security adds document encryption, password protection, and
permissions to Prawn.

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
%{gemdir}/gems/prawn-security-0.8.4/

%{gemdir}/cache/prawn-security-0.8.4.gem
%{gemdir}/specifications/prawn-security-0.8.4.gemspec

%changelog
