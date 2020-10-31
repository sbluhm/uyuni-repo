# Generated from webmock-3.9.3.gem by gem2rpm -*- rpm-spec -*-
%define rbname webmock
%define version 3.9.3
%define release 1

Summary: Library for stubbing HTTP requests in Ruby.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/bblimke/webmock
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-addressable >= 2.3.6
Requires: rubygem-crack >= 0.3.2
Requires: rubygem-hashdiff >= 0.4.0
Requires: rubygem-hashdiff < 2.0.0
Requires: rubygem-patron >= 0.4.18
Requires: rubygem-curb >= 0.7.16
Requires: rubygem-typhoeus >= 0.5.0
Requires: rubygem-http >= 0.8.0
Requires: rubygem-rack > 1.6
Requires: rubygem-rspec >= 3.1.0
Requires: rubygem-httpclient >= 2.2.4
Requires: rubygem-em-http-request >= 1.0.2
Requires: rubygem-em-synchrony >= 1.0.0
Requires: rubygem-excon >= 0.27.5
Requires: rubygem-async-http >= 0.48.0
Requires: rubygem-minitest >= 5.0.0
Requires: rubygem-test-unit >= 3.0.0
Requires: rubygem-rdoc > 3.5.0
BuildRequires: ruby >= 2.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(webmock) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
WebMock allows stubbing HTTP requests and setting expectations on HTTP
requests.

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
%{gemdir}/gems/webmock-3.9.3/

%{gemdir}/cache/webmock-3.9.3.gem
%{gemdir}/specifications/webmock-3.9.3.gemspec

%changelog
