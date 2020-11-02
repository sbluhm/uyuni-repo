# Generated from rack-contrib-2.2.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rack-contrib
%define version 2.2.0
%define release 1

Summary: Contributed Rack Middleware and Utilities
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/rack/rack-contrib/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.2.2
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rack >= 2.0
Requires: rubygem-rack < 3
Requires: rubygem-bundler >= 1.0
Requires: rubygem-bundler < 3
Requires: rubygem-git-version-bump >= 0.15
Requires: rubygem-git-version-bump < 1
Requires: rubygem-github-release >= 0.1
Requires: rubygem-github-release < 1
Requires: rubygem-i18n >= 0.6
Requires: rubygem-i18n < 1
Requires: rubygem-i18n >= 0.6.8
Requires: rubygem-json >= 2.0
Requires: rubygem-json < 3
Requires: rubygem-mime-types >= 3.0
Requires: rubygem-mime-types < 4
Requires: rubygem-minitest >= 5.6
Requires: rubygem-minitest < 6
Requires: rubygem-minitest-hooks >= 1.0
Requires: rubygem-minitest-hooks < 2
Requires: rubygem-mail >= 2.3
Requires: rubygem-mail < 3
Requires: rubygem-mail >= 2.6.4
Requires: rubygem-nbio-csshttprequest >= 1.0
Requires: rubygem-nbio-csshttprequest < 2
Requires: rubygem-rake >= 10.4
Requires: rubygem-rake < 11
Requires: rubygem-rake >= 10.4.2
Requires: rubygem-rdoc >= 5.0
Requires: rubygem-rdoc < 6
Requires: rubygem-ruby-prof >= 0.17
Requires: rubygem-ruby-prof < 1
Requires: rubygem-timecop >= 0.9
Requires: rubygem-timecop < 1
BuildRequires: ruby >= 2.2.2
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rack-contrib) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Contributed Rack Middleware and Utilities.

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
%{gemdir}/gems/rack-contrib-2.2.0/

%{gemdir}/cache/rack-contrib-2.2.0.gem
%{gemdir}/specifications/rack-contrib-2.2.0.gemspec

%changelog
