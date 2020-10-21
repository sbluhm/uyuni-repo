# Generated from unf-0.1.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname unf
%define version 0.1.4
%define release 1

Summary: A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/knu/ruby-unf
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-unf_ext 
Requires: rubygem-shoulda 
Requires: rubygem-bundler >= 1.2.0
Requires: rubygem-rake >= 0.9.2.2
Requires: rubygem-rdoc > 2.4.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(unf) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
This is a wrapper library to bring Unicode Normalization Form support
to Ruby/JRuby.


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
%defattr(-, root, root)
%{gemdir}/gems/unf-0.1.4/
%{gemdir}/cache/unf-0.1.4.gem
%{gemdir}/specifications/unf-0.1.4.gemspec
%doc %{gemdir}/doc/%{name}-%{version}/

%changelog
