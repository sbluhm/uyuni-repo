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

# jakarta-commons-httpclient
%package -n apache-commons-httpclient
Requires:       jakarta-commons-httpclient >= 3.1
Requires:       jakarta-commons-httpclient < 3.2
Version:        3.1
Summary:        Jakarta Commons HTTPClient implements the client side of HTTP standards
%description -n apache-commons-httpclient
See jakarta-commons-httpclient

# libyui13
%package -n libyui13
Requires:       libyui >= 3.11
Requires:	libyui < 3.12
Version:	3.11.0
Summary:        Libyui - GUI-abstraction library
%description -n libyui13
See libyui

#libsigc++ 2
%package -n libsigc++2-devel
Requires:       libsigc++20-devel
Summary:        See libsigc++20-devel
%description -n libsigc++2-devel
See libsigc++20-devel

# oro
%package -n oro
Requires:       jakarta-oro >= 2.0.8
Requires:       jakarta-oro < 2.1.0
Version:        2.0.8
Summary:        Full regular expressions API
%description -n oro
See jakarta-oro

#yast2
%package -n yast2
Summary:        See Dummy package for yast2
%description -n yast2
No function. Just pretends to provide yast2


%files
%files -n apache-commons-httpclient
%files -n libyui13
%files -n libsigc++2-devel
%files -n oro
%files -n yast2
