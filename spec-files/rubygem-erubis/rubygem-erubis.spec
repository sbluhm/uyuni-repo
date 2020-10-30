# Generated from erubis-2.7.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname erubis
%define version 2.7.0
%define release 1

Summary: a fast and extensible eRuby implementation which supports multi-language
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.kuwata-lab.com/erubis/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(erubis) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Erubis is an implementation of eRuby and has the following features:
* Very fast, almost three times faster than ERB and about 10% faster than
eruby.
* Multi-language support (Ruby/PHP/C/Java/Scheme/Perl/Javascript)
* Auto escaping support
* Auto trimming spaces around '<% %>'
* Embedded pattern changeable (default '<% %>')
* Enable to handle Processing Instructions (PI) as embedded pattern (ex. '<?rb
... ?>')
* Context object available and easy to combine eRuby template with YAML
datafile
* Print statement available
* Easy to extend and customize in subclass
* Ruby on Rails support.

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
%{_bindir}/erubis
%{gemdir}/gems/erubis-2.7.0/

%{gemdir}/cache/erubis-2.7.0.gem
%{gemdir}/specifications/erubis-2.7.0.gemspec

%changelog
