# Generated from rails-6.0.3.4.gem by gem2rpm -*- rpm-spec -*-
%define rbname rails
%define version 6.0.3.4
%define release 1

Summary: Full-stack web application framework.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://rubyonrails.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.5.0
Requires: rubygems >= 2.7.6.2
Requires: rubygem-activesupport = 6.0.3.4
Requires: rubygem-actionpack = 6.0.3.4
Requires: rubygem-actionview = 6.0.3.4
Requires: rubygem-activemodel = 6.0.3.4
Requires: rubygem-activerecord = 6.0.3.4
Requires: rubygem-actionmailer = 6.0.3.4
Requires: rubygem-activejob = 6.0.3.4
Requires: rubygem-actioncable = 6.0.3.4
Requires: rubygem-activestorage = 6.0.3.4
Requires: rubygem-actionmailbox = 6.0.3.4
Requires: rubygem-actiontext = 6.0.3.4
Requires: rubygem-railties = 6.0.3.4
Requires: rubygem-bundler >= 1.3.0
Requires: rubygem-sprockets-rails >= 2.0.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rails) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.

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
%{gemdir}/gems/rails-6.0.3.4/

%{gemdir}/cache/rails-6.0.3.4.gem
%{gemdir}/specifications/rails-6.0.3.4.gemspec

%changelog
