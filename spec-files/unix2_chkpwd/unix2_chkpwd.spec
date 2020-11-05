Name:           unix2_chkpwd
#BuildRequires:  bison
#BuildRequires:  flex
#
Version:        1.0.0
Release:        1
Summary:        A Security Tool that Provides Authentication for Applications
License:        GPL-2.0+ or BSD-3-Clause
Group:          System/Libraries
Requires(pre):         permissions

Source0:       unix2_chkpwd.c
Source1:       unix2_chkpwd.8
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Remove with next version update:
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
unix2_chkpwd

%prep

%build
export CFLAGS="%optflags -DNDEBUG"
%__cc -fwhole-program -fpie -pie -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE %{optflags} -I$RPM_BUILD_DIR/Linux-PAM-%{version}/libpam/include %{SOURCE0} -o $RPM_BUILD_DIR/unix2_chkpwd -L$RPM_BUILD_DIR/Linux-PAM-%{version}/libpam/.libs/ -lpam

%check

%install
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8/
#
# Install unix2_chkpwd
install -m 755 $RPM_BUILD_DIR/unix2_chkpwd $RPM_BUILD_ROOT/usr/sbin/
install -m 644 $RPM_SOURCE_DIR/unix2_chkpwd.8 $RPM_BUILD_ROOT%{_mandir}/man8/

%verifyscript
%verify_permissions -e /sbin/unix_chkpwd
%verify_permissions -e /sbin/unix2_chkpwd

%post
%set_permissions /sbin/unix_chkpwd
%set_permissions /sbin/unix2_chkpwd


%files
%defattr(-,root,root)
%doc %{_mandir}/man8/unix2_chkpwd.8.gz
%verify(not mode) %attr(4755,root,shadow) /usr/sbin/unix2_chkpwd


%changelog
* Thu Nov 5 2020 stefan.bluhm@clacee.eu
- First package
