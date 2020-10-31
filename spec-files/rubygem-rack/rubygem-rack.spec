# Generated from rack-1.6.13.gem by gem2rpm -*- rpm-spec -*-
%define rbname rack
%define version 1.6.13
%define release 1

Summary: a modular Ruby webserver interface
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://rack.github.io/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-bacon 
Requires: rubygem-rake 
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rack) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Rack provides a minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.
Also see http://rack.github.io/.

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
sed  '1 s/..\/..\/bin\/rackup\b/\/usr\/share\/gems\/gems\/rack-1.6.13\/test\/bin\/rackup/' %{buildroot}/usr/share/gems/gems/rack-1.6.13/test/cgi/test.ru

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{gemdir}/doc/%{rbname}-%{version}/
%defattr(-, root, root)
%{_bindir}/rackup
%{gemdir}/gems/rack-1.6.13/

%{gemdir}/cache/rack-1.6.13.gem
%{gemdir}/specifications/rack-1.6.13.gemspec

%changelog
