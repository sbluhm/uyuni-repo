# Generated from wrong-0.7.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname wrong
%define version 0.7.1
%define release 1

Summary: Wrong provides a general assert method that takes a predicate block.  Assertion failure messages are rich in detail.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/sconover/wrong
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-predicated >= 0.2.6
Requires: rubygem-predicated < 0.3
Requires: rubygem-ruby_parser >= 3.0.1
Requires: rubygem-ruby2ruby >= 2.0.1
Requires: rubygem-sexp_processor >= 4.0
Requires: rubygem-diff-lcs >= 1.2.5
Requires: rubygem-diff-lcs < 1.3
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(wrong) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Wrong provides a general assert method that takes a predicate block. Assertion
failure
messages are rich in detail. The Wrong idea is to replace all those countless
assert_this,
assert_that library methods which only exist to give a more useful failure
message than
"assertion failed". Wrong replaces all of them in one fell swoop, since if you
can write it
in Ruby, Wrong can make a sensible failure message out of it. Also provided
are several
helper methods, like rescuing, capturing, and d.

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
%{gemdir}/gems/wrong-0.7.1/

%{gemdir}/cache/wrong-0.7.1.gem
%{gemdir}/specifications/wrong-0.7.1.gemspec

%changelog
