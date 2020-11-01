# Generated from nbio-csshttprequest-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname nbio-csshttprequest
%define version 1.0.3
%define release 1

Summary: CSSHttpRequest is cross-domain AJAX using CSS as a transport.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/nbio/csshttprequest
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(nbio-csshttprequest) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Please see the latest info at http://nb.io/hacks/csshttprequest/.

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
%{gemdir}/gems/nbio-csshttprequest-1.0.3/

%{gemdir}/cache/nbio-csshttprequest-1.0.3.gem
%{gemdir}/specifications/nbio-csshttprequest-1.0.3.gemspec

%changelog
