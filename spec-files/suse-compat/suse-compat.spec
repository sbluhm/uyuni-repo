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

%description
Links SUSE packages to RHEL 8
augeas, awk, gettext, libxslt, libsigc++ 2, 


%files


