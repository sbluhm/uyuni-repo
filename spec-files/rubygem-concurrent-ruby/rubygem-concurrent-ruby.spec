# Generated from concurrent-ruby-0.7.2-x86_64-linux.gem by gem2rpm -*- rpm-spec -*-
%define rbname concurrent-ruby
%define version 0.7.2
%define release 1

Summary: Modern concurrency tools for Ruby. Inspired by Erlang, Clojure, Scala, Haskell, F#, C#, Java, and classic concurrency patterns.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.concurrent-ruby.com
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.9.3
Requires: rubygems >= 2.7.6.2
Requires: rubygem-ref >= 1.0.5
Requires: rubygem-ref < 1.1
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(Concurrent-ruby) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Modern concurrency tools including agents, futures, promises, thread
pools, actors, supervisors, and more.
Inspired by Erlang, Clojure, Go, JavaScript, actors, and classic concurrency
patterns.


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
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/
%{gemdir}/gems/concurrent-ruby-0.7.2/


%{gemdir}/cache/concurrent-ruby-0.7.2-x86_64-linux.gem
%{gemdir}/specifications/concurrent-ruby-0.7.2-x86_64-linux.gemspec

%changelog
