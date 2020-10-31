# Generated from nokogiri-1.6.8.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname nokogiri
%define version 1.6.8.1
%define release 1

Summary: Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://nokogiri.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.2
Requires: rubygems >= 2.7.6.2
Requires: rubygem-mini_portile2 >= 2.1.0
Requires: rubygem-mini_portile2 < 2.2
Requires: rubygem-rdoc >= 4.0
Requires: rubygem-rdoc < 5
Requires: rubygem-hoe-bundler >= 1.2.0
Requires: rubygem-hoe-bundler < 1.3
Requires: rubygem-hoe-debugging >= 1.2.1
Requires: rubygem-hoe-debugging < 1.3
Requires: rubygem-hoe-gemspec >= 1.0.0
Requires: rubygem-hoe-gemspec < 1.1
Requires: rubygem-hoe-git >= 1.6.0
Requires: rubygem-hoe-git < 1.7
Requires: rubygem-minitest >= 5.8.4
Requires: rubygem-minitest < 5.9
Requires: rubygem-rake >= 10.5.0
Requires: rubygem-rake < 10.6
Requires: rubygem-rake-compiler >= 0.9.2
Requires: rubygem-rake-compiler < 0.10
Requires: rubygem-rake-compiler-dock >= 0.5.1
Requires: rubygem-rake-compiler-dock < 0.6
Requires: rubygem-racc >= 1.4.14
Requires: rubygem-racc < 1.5
Requires: rubygem-rexical >= 1.0.5
Requires: rubygem-rexical < 1.1
Requires: rubygem-hoe >= 3.15
Requires: rubygem-hoe < 4
BuildRequires: ruby >= 1.9.2
BuildRequires: ruby-devel
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(nokogiri) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser.  Among
Nokogiri's many features is the ability to search documents via XPath
or CSS3 selectors.

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
%{_bindir}/nokogiri
%{gemdir}/gems/nokogiri-1.6.8.1/

%{gemdir}/cache/nokogiri-1.6.8.1.gem
%{gemdir}/specifications/nokogiri-1.6.8.1.gemspec

%changelog
