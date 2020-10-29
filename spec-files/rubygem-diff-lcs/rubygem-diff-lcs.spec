# Generated from diff-lcs-1.1.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname diff-lcs
%define version 1.1.3
%define release 1

Summary: Diff::LCS is a port of Perl's Algorithm::Diff that uses the McIlroy-Hunt longest common subsequence (LCS) algorithm to compute intelligent differences between two sequenced enumerable containers
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rspec >= 2.0
Requires: rubygem-rspec < 3
Requires: rubygem-hoe >= 2.12
Requires: rubygem-hoe < 3
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(diff-lcs) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Diff::LCS is a port of Perl's Algorithm::Diff that uses the McIlroy-Hunt
longest common subsequence (LCS) algorithm to compute intelligent differences
between two sequenced enumerable containers. The implementation is based on
Mario I. Wolczko's {Smalltalk version
1.2}[ftp://st.cs.uiuc.edu/pub/Smalltalk/MANCHESTER/manchester/4.0/diff.st]
(1993) and Ned Konz's Perl version
{Algorithm::Diff 1.15}[http://search.cpan.org/~nedkonz/Algorithm-Diff-1.15/].
This is release 1.1.3, fixing several small bugs found over the years. Version
1.1.0 added new features, including the ability to #patch and #unpatch changes
as well as a new contextual diff callback, Diff::LCS::ContextDiffCallbacks,
that should improve the context sensitivity of patching.
This library is called Diff::LCS because of an early version of
Algorithm::Diff
which was restrictively licensed. This version has seen a minor license
change:
instead of being under Ruby's license as an option, the third optional license
is the MIT license.

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
sed -i 's/#\!ruby -w/#\!\/usr\/bin\/ruby -w/' %{buildroot}/%{_bindir}/*

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{_bindir}/htmldiff
%{_bindir}/ldiff
%{gemdir}/gems/diff-lcs-1.1.3/

%{gemdir}/cache/diff-lcs-1.1.3.gem
%{gemdir}/specifications/diff-lcs-1.1.3.gemspec

%changelog
