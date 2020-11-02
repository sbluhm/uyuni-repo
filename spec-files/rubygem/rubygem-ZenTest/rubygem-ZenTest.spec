# Generated from ZenTest-4.12.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname ZenTest
%define version 4.12.0
%define release 1

Summary: ZenTest provides 4 different tools: zentest, unit_diff, autotest, and multiruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/seattlerb/zentest
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rdoc >= 4.0
Requires: rubygem-rdoc < 7
Requires: rubygem-hoe >= 3.18
Requires: rubygem-hoe < 4
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(zentest) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
ZenTest provides 4 different tools: zentest, unit_diff, autotest, and
multiruby.
zentest scans your target and unit-test code and writes your missing
code based on simple naming rules, enabling XP at a much quicker pace.
zentest only works with Ruby and Minitest or Test::Unit. There is
enough evidence to show that this is still proving useful to users, so
it stays.
unit_diff is a command-line filter to diff expected results from
actual results and allow you to quickly see exactly what is wrong.
Do note that minitest 2.2+ provides an enhanced assert_equal obviating
the need for unit_diff
autotest is a continous testing facility meant to be used during
development. As soon as you save a file, autotest will run the
corresponding dependent tests.
multiruby runs anything you want on multiple versions of ruby. Great
for compatibility checking! Use multiruby_setup to manage your
installed versions.
*NOTE:* The next major release of zentest will not include autotest
(use minitest-autotest instead) and multiruby will use rbenv /
ruby-build for version management.


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
mkdir -p %{buildroot}/usr/local/bin/
ln -s /usr/bin/ruby %{buildroot}/usr/local/bin/ruby
%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{_bindir}/multigem
%{_bindir}/multiruby
%{_bindir}/unit_diff
%{_bindir}/zentest
%{gemdir}/gems/ZenTest-4.12.0/
/usr/local/bin/ruby

%{gemdir}/cache/ZenTest-4.12.0.gem
%{gemdir}/specifications/ZenTest-4.12.0.gemspec

%changelog
