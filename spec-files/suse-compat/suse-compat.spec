Name:		suse-compat
Version:	1.0
Release:	1%{?dist}
Summary:	Maps SUSE libraries to RHEL libraries,
License:	NONE
# awk
Requires:	gawk
Provides:	awk

# gettext
Requires:	gettext-devel gettext-libs
Provides:	gettext-tools

%description
Links SUSE packages to RHEL 8



%files


