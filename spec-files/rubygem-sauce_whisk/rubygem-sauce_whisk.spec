# Generated from sauce_whisk-0.2.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname sauce_whisk
%define version 0.2.2
%define release 1

Summary: Sauce_Whisk lets you mix extra data into your Sauce test results! Fetch and update Job details, screenshots, videos and logs.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.github.com/saucelabs/sauce_whisk
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rest-client >= 2.0
Requires: rubygem-rest-client < 3
Requires: rubygem-json 
Requires: rubygem-vcr >= 3.0.3
Requires: rubygem-vcr < 3.1
Requires: rubygem-webmock >= 3.0
Requires: rubygem-webmock < 4
Requires: rubygem-rspec >= 3.3
Requires: rubygem-rspec < 4
Requires: rubygem-rake >= 10.4
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(sauce_whisk) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
A Wrapper for the Sauce Labs REST API.

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
%{gemdir}/gems/sauce_whisk-0.2.2/

%{gemdir}/cache/sauce_whisk-0.2.2.gem
%{gemdir}/specifications/sauce_whisk-0.2.2.gemspec

%changelog
