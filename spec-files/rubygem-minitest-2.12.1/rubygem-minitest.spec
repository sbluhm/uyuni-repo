# Generated from minitest-2.12.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname minitest
%define version 2.12.1
%define release 1

Summary: minitest provides a complete suite of testing facilities supporting TDD, BDD, mocking, and benchmarking
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/seattlerb/minitest
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rdoc >= 3.10
Requires: rubygem-rdoc < 4
Requires: rubygem-hoe >= 3.0
Requires: rubygem-hoe < 4
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(minitest) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
minitest provides a complete suite of testing facilities supporting
TDD, BDD, mocking, and benchmarking.
"I had a class with Jim Weirich on testing last week and we were
allowed to choose our testing frameworks. Kirk Haines and I were
paired up and we cracked open the code for a few test
frameworks...
I MUST say that minitest is *very* readable / understandable
compared to the 'other two' options we looked at. Nicely done and
thank you for helping us keep our mental sanity."
-- Wayne E. Seguin
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
output. I guess it is an example of how to write IO pipes too. :P
minitest/unit is meant to have a clean implementation for language
implementors that need a minimal set of methods to bootstrap a working
test suite. For example, there is no magic involved for test-case
discovery.
"Again, I can't praise enough the idea of a testing/specing
framework that I can actually read in full in one sitting!"
-- Piotr Szotkowski.


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
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/
%{gemdir}/gems/minitest-2.12.1/


%{gemdir}/cache/minitest-2.12.1.gem
%{gemdir}/specifications/minitest-2.12.1.gemspec

%changelog