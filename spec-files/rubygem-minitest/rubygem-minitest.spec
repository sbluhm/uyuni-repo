# Generated from minitest-2.3.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname minitest
%define version 2.3.1
%define release 1

Summary: minitest provides a complete suite of testing facilities supporting TDD, BDD, mocking, and benchmarking
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://rubyforge.org/projects/bfts
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-minitest >= 2.3.0
Requires: rubygem-hoe >= 2.9
Requires: rubygem-hoe < 3
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(minitest) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
minitest provides a complete suite of testing facilities supporting
TDD, BDD, mocking, and benchmarking.
minitest/unit is a small and incredibly fast unit testing framework.
It provides a rich set of assertions to make your tests clean and
readable.
minitest/spec is a functionally complete spec engine. It hooks onto
minitest/unit and seamlessly bridges test assertions over to spec
expectations.
minitest/benchmark is an awesome way to assert the performance of your
algorithms in a repeatable manner. Now you can assert that your newb
co-worker doesn't replace your linear algorithm with an exponential
one!
minitest/mock by Steven Baker, is a beautifully tiny mock object
framework.
minitest/pride shows pride in testing and adds coloring to your test
output.
minitest/unit is meant to have a clean implementation for language
implementors that need a minimal set of methods to bootstrap a working
test suite. For example, there is no magic involved for test-case
discovery.

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
%{gemdir}/gems/minitest-2.3.1/

%{gemdir}/cache/minitest-2.3.1.gem
%{gemdir}/specifications/minitest-2.3.1.gemspec

%changelog
