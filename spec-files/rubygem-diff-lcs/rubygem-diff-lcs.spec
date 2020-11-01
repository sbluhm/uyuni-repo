# Generated from diff-lcs-1.4.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname diff-lcs
%define version 1.4.4
%define release 1

Summary: Diff::LCS computes the difference between two Enumerable sequences using the McIlroy-Hunt longest common subsequence (LCS) algorithm
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/halostatue/diff-lcs
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8
Requires: rubygems >= 2.7.6.2
Requires: rubygem-hoe-doofus >= 1.0
Requires: rubygem-hoe-doofus < 2
Requires: rubygem-hoe-gemspec2 >= 1.1
Requires: rubygem-hoe-gemspec2 < 2
Requires: rubygem-hoe-git >= 1.6
Requires: rubygem-hoe-git < 2
Requires: rubygem-hoe-rubygems >= 1.0
Requires: rubygem-hoe-rubygems < 2
Requires: rubygem-rspec >= 2.0
Requires: rubygem-rspec < 4
Requires: rubygem-rake >= 10.0
Requires: rubygem-rake < 14
Requires: rubygem-rdoc 
Requires: rubygem-hoe >= 3.22
Requires: rubygem-hoe < 4
BuildRequires: ruby >= 1.8
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(diff-lcs) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.
This is release 1.4.3, providing a simple extension that allows for
Diff::LCS::Change objects to be treated implicitly as arrays and fixes a
number of formatting issues.
Ruby versions below 2.5 are soft-deprecated, which means that older versions
are no longer part of the CI test suite. If any changes have been introduced
that break those versions, bug reports and patches will be accepted, but it
will be up to the reporter to verify any fixes prior to release. The next
major release will completely break compatibility.

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
%{_bindir}/htmldiff
%{_bindir}/ldiff
%{gemdir}/gems/diff-lcs-1.4.4/

%{gemdir}/cache/diff-lcs-1.4.4.gem
%{gemdir}/specifications/diff-lcs-1.4.4.gemspec

%changelog
