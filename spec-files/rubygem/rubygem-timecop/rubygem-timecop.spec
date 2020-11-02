# Generated from timecop-0.9.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname timecop
%define version 0.9.2
%define release 1

Summary: A gem providing "time travel" and "time freezing" capabilities, making it dead simple to test time-dependent code.  It provides a unified method to mock Time.now, Date.today, and DateTime.now in a single call.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/travisjeffery/timecop
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.2
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby >= 1.9.2
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(timecop) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A gem providing "time travel" and "time freezing" capabilities, making it dead
simple to test time-dependent code.  It provides a unified method to mock
Time.now, Date.today, and DateTime.now in a single call.

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
%{gemdir}/gems/timecop-0.9.2/

%{gemdir}/cache/timecop-0.9.2.gem
%{gemdir}/specifications/timecop-0.9.2.gemspec

%changelog
