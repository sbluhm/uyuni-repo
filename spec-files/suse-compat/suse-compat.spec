Name:		suse-compat
Version:	1.0
Release:	1%{?dist}
Summary:	Maps SUSE libraries to RHEL libraries,
License:	NONE

# augeas
Requires:	augeas-libs
Provides:	augeas-lenses

# awk
Requires:	gawk
Provides:	awk

# gettext
Requires:	gettext-devel gettext-libs
Provides:	gettext-tools

# libxslt
Requires:       libxslt-devel
Provides:       libxslt-tools

#libsigc++ 2
Requires:	libsigc++20-devel
Provides:	libsigc++2-devel

# libxml2
Requires:       libxml2-devel
Provides:       libxml2-tools

%description
Links SUSE packages to RHEL 8
augeas, awk, gettext, libxslt, libsigc++ 2, 

%package -n libyui13

Provides:       libyui13
Requires:       libyui >= 3.11 < 3.12

Summary:        Libyui - GUI-abstraction library
Group:          System/Libraries

%description -n libyui13
This is the user interface engine that provides the abstraction from
graphical user interfaces (Qt, Gtk) and text based user interfaces
(ncurses).

Originally developed for YaST, it can now be used independently of
YaST for generic (C++) applications. This package has very few
dependencies.



%files


