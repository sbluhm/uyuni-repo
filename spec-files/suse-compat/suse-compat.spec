Name:		suse-compat
Version:	1.0
Release:	1%{?dist}
Summary:	Maps SUSE libraries to RHEL libraries,
License:	NONE

Provides:       python3-CherryPy = 18.4.0
Requires:       python3-cherrypy >= 18.4.0
Requires:       python3-cherrypy < 18.5.0

Provides:	python-backports-ssl_match_hostname
Requires:	python2-backports-ssl_match_hostname



%description
Links SUSE packages to RHEL 8
augeas, awk, gettext, libxslt, libsigc++ 2, 

%files
