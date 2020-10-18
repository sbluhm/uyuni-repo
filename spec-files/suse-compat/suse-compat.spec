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

# libxml2
Requires:       libxml2-devel
Provides:       libxml2-tools

%description
Links SUSE packages to RHEL 8
augeas, awk, gettext, libxslt, libsigc++ 2, 

# libyui13
%package -n libyui13
Requires:       libyui >= 3.11
Requires:	libyui < 3.12
Summary:        Libyui - GUI-abstraction library
%description -n libyui13
See libyui

#libsigc++ 2
%package -n libsigc++2-devel
Requires:       libsigc++20-devel



%files


