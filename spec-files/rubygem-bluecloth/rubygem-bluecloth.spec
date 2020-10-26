# Generated from bluecloth-2.2.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname bluecloth
%define version 2.2.0
%define release 1

Summary: BlueCloth is a Ruby implementation of John Gruber's Markdown[http://daringfireball.net/projects/markdown/], a text-to-HTML conversion tool for web writers
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://deveiate.org/projects/BlueCloth
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 2.7.6.2
Requires: rubygem-hoe-mercurial >= 1.3.1
Requires: rubygem-hoe-mercurial < 1.4
Requires: rubygem-hoe-highline >= 0.0.1
Requires: rubygem-hoe-highline < 0.1
Requires: rubygem-tidy-ext >= 0.1
Requires: rubygem-tidy-ext < 1
Requires: rubygem-rake-compiler >= 0.7
Requires: rubygem-rake-compiler < 1
Requires: rubygem-rspec >= 2.6
Requires: rubygem-rspec < 3
Requires: rubygem-hoe >= 2.12
Requires: rubygem-hoe < 3
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 2.7.6.2
BuildRequires: ruby-devel
BuildArch: noarch
Provides: ruby(bluecloth) = %{version}

%define gemdir /usr/share/gems
%define gembuilddir %{buildroot}%{gemdir}

%description
BlueCloth is a Ruby implementation of John Gruber's
Markdown[http://daringfireball.net/projects/markdown/], a text-to-HTML
conversion tool for web writers. To quote from the project page: Markdown
allows you to write using an easy-to-read, easy-to-write plain text format,
then convert it to structurally valid XHTML (or HTML).
It borrows a naming convention and several helpings of interface from
{Redcloth}[http://redcloth.org/], Why the Lucky Stiff's processor for a
similar text-to-HTML conversion syntax called
Textile[http://www.textism.com/tools/textile/].
BlueCloth 2 is a complete rewrite using David Parsons'
Discount[http://www.pell.portland.or.us/~orc/Code/discount/] library, a C
implementation of Markdown. I rewrote it using the extension for speed and
accuracy; the original BlueCloth was a straight port from the Perl version
that I wrote in a few days for my own use just to avoid having to shell out to
Markdown.pl, and it was quite buggy and slow. I apologize to all the good
people that sent me patches for it that were never released.
Note that the new gem is called 'bluecloth' and the old one 'BlueCloth'. If
you have both installed, you can ensure you're loading the new one with the
'gem' directive:
# Load the 2.0 version
gem 'bluecloth', '>= 2.0.0'
# Load the 1.0 version
gem 'BlueCloth'
require 'bluecloth'.


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
%{_bindir}/bluecloth
%{gemdir}/gems/bluecloth-2.2.0/
%{gemdir}/cache/bluecloth-2.2.0.gem
%{gemdir}/specifications/bluecloth-2.2.0.gemspec

%changelog
