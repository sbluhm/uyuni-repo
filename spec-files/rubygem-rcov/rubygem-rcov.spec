# Generated from rcov-0.9.11.gem by gem2rpm -*- rpm-spec -*-
%define rbname rcov
%define version 0.9.11
%define release 1

Summary: Code coverage analysis tool for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/relevance/rcov
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(rcov) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
rcov is a code coverage tool for Ruby. It is commonly used for viewing overall
test unit coverage of target code.  It features fast execution (20-300 times
faster than previous tools), multiple analysis modes, XHTML and several kinds
of text reports, easy automation with Rake via a RcovTask, fairly accurate
coverage information through code linkage inference using simple heuristics,
colorblind-friendliness...


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
%{gemdir}/cache/rcov-0.9.11.gem
%{gemdir}/specifications/rcov-0.9.11.gemspec

%changelog
