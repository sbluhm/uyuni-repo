# Generated from hoe-2.16.1.gem by gem2rpm -*- rpm-spec -*-
%define rbname hoe
%define version 2.16.1
%define release 1

Summary: Hoe is a rake/rubygems helper for project Rakefiles
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://www.zenspider.com/projects/hoe.html
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 2.7.6.2
Requires: rubygem-rake >= 0.8
Requires: rubygem-rake < 1
Requires: rubygem-minitest >= 2.11
Requires: rubygem-minitest < 3
Requires: rubygem-rdoc >= 3.10
Requires: rubygem-rdoc < 4
BuildRequires: ruby 
BuildRequires: rubygems >= 2.7.6.2
BuildArch: noarch
Provides: ruby(hoe) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps you
manage, maintain, and release your project and includes a dynamic
plug-in system allowing for easy extensibility. Hoe ships with
plug-ins for all your usual project tasks including rdoc generation,
testing, packaging, deployment, and announcement..
See class rdoc for help. Hint: `ri Hoe` or any of the plugins listed
below.
For extra goodness, see: http://seattlerb.rubyforge.org/hoe/Hoe.pdf.


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
%{_bindir}/sow
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/
%{gemdir}/gems/hoe-2.16.1/


%{gemdir}/cache/hoe-2.16.1.gem
%{gemdir}/specifications/hoe-2.16.1.gemspec

%changelog
