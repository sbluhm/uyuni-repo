# Generated from rake-13.0.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname rake
%define version 13.0.1
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
Requires: ruby >= 2.2
Requires: rubygems >= 2.7.6.2
BuildRequires: ruby >= 2.2
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(rake) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.
Rake has the following features:
* Rakefiles (rake's version of Makefiles) are completely defined in standard
Ruby syntax.
No XML files to edit. No quirky Makefile syntax to worry about (is that a tab
or a space?)
* Users can specify tasks with prerequisites.
* Rake supports rule patterns to synthesize implicit tasks.
* Flexible FileLists that act like arrays but know about manipulating file
names and paths.
* Supports parallel execution of tasks.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --user-install --force %{SOURCE0}
mv $(ruby -r rubygems -e 'puts Gem.user_dir')/* %{gembuilddir}
mkdir -p %{buildroot}/%{_bindir}
#mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
#rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/rake
%{gemdir}/gems/rake-13.0.1/
%doc %{gemdir}/doc/%{rbname}-%{version}/
%{gemdir}/cache/rake-13.0.1.gem
%{gemdir}/specifications/rake-13.0.1.gemspec

%changelog
