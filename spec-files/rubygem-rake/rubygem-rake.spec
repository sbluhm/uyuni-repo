# Generated from rake-10.5.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname rake
%define version 10.5.0
%define release 1

Summary: Rake is a Make-like program implemented in Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ruby/rake
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 2.7.6.2
Requires: rubygem-minitest >= 5.8
Requires: rubygem-minitest < 6
Requires: rubygem-rdoc >= 4.0
Requires: rubygem-rdoc < 5
Requires: rubygem-hoe >= 3.14
Requires: rubygem-hoe < 4
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 2.7.6.2
Provides: ruby(Rake) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.
Rake has the following features:
* Rakefiles (rake's version of Makefiles) are completely defined in
standard Ruby syntax.  No XML files to edit.  No quirky Makefile
syntax to worry about (is that a tab or a space?)
* Users can specify tasks with prerequisites.
* Rake supports rule patterns to synthesize implicit tasks.
* Flexible FileLists that act like arrays but know about manipulating
file names and paths.
* A library of prepackaged tasks to make building rakefiles easier. For
example,
tasks for building tarballs and publishing to FTP or SSH sites.  (Formerly
tasks for building RDoc and Gems were included in rake but they're now
available in RDoc and RubyGems respectively.)
* Supports parallel execution of tasks.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}%{_bindir}
mv %{gembuilddir}/gems/rake-13.0.1/bin/* %{buildroot}%{_bindir}
#rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/
%{gemdir}/gems/rake-10.5.0/
%{gemdir}/gems/rake-10.5.0/path
%doc %{gemdir}/doc/%{rbname}-%{version}/
%{gemdir}/cache/rake-10.5.0.gem
%{gemdir}/specifications/rake-10.5.0.gemspec

%changelog
