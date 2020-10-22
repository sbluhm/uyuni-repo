# Generated from rdoc-3.12.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname rdoc
%define version 3.12.2
%define release 1

Summary: RDoc produces HTML and command-line documentation for Ruby projects
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://docs.seattlerb.org/rdoc
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 2.7.6.2
Requires: rubygem-json >= 1.4
Requires: rubygem-json < 2
Requires: rubygem-minitest >= 4.3
Requires: rubygem-minitest < 5
Requires: rubygem-rdoc >= 3.10
Requires: rubygem-rdoc < 4
Requires: rubygem-racc >= 1.4
Requires: rubygem-racc < 2
Requires: rubygem-ZenTest >= 4
Requires: rubygem-ZenTest < 5
Requires: rubygem-hoe >= 3.5
Requires: rubygem-hoe < 4
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rdoc) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
RDoc produces HTML and command-line documentation for Ruby projects.  RDoc
includes the +rdoc+ and +ri+ tools for generating and displaying online
documentation.
See RDoc for a description of RDoc's markup and basic use.


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
%{gemdir}/gems/rdoc-3.12.2/
%{gemdir}/cache/rdoc-3.12.2.gem
%{gemdir}/specifications/rdoc-3.12.2.gemspec

%changelog
