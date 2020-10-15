#
# spec file for package augeas
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define libname lib%{name}0
Name:           augeas
Version:        1.12.0
Release:        1.2
Summary:        An utility for changing configuration files
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://augeas.net/
Source0:        http://download.augeas.net/augeas-%{version}.tar.gz
Source1:        http://download.augeas.net/augeas-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
Patch0:         augeas-modprobe-lense.patch
Patch1:         gcc9-disable-broken-test.patch
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libxml-2.0)

%description
An utility for programmatically editing configuration files. Augeas
parses configuration files into a tree structure.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the
file format and the transformation into a tree.

%package        devel
Summary:        A library for changing configuration files
Requires:       %{libname} = %{version}

%description    devel
A library for programmatically editing configuration files. Augeas
parses configuration files into a tree structure, which it exposes
through its public API. Changes made through the API are written back
to the initially read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the
file format and the transformation into a tree.

%package        -n %{libname}
Summary:        A library for changing configuration files
Recommends:     %{name}-lenses = %{version}

%description    -n %{libname}
A library for programmatically editing configuration files. Augeas
parses configuration files into a tree structure, which it exposes
through its public API. Changes made through the API are written back
to the initially read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the
file format and the transformation into a tree.

%package        lenses
Summary:        Official set of lenses for use by %{libname}
Requires:       %{libname} = %{version}

%description    lenses
Augeas parses configuration files described in lenses into a tree
structure, which it exposes through its public API. Lenses are the
building blocks of the file <-> tree transformation. The transformation
is controlled by ``lens'' definitions that describe the file format and
mapping of its contents into a tree. This package includes the official
set of lenses.

%package        lense-tests
Summary:        Set of tests for official Augeas lenses
Requires:       %{name}-lenses = %{version}

%description    lense-tests
Set of tests for official Augeas lenses. These can be used when
modifying the official lenses, or when creating new ones.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-static \
	--disable-silent-rules \
	--disable-rpath
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# move vim files to the right location
mv %{buildroot}/%{_datadir}/vim/vimfiles %{buildroot}/%{_datadir}/vim/site

%check
%make_build check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_bindir}/augmatch
%{_bindir}/augtool
%{_bindir}/augparse
%{_bindir}/fadot
%{_mandir}/man1/*
%license COPYING
%doc AUTHORS NEWS

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/augeas.pc
# vim support files
%dir %{_datadir}/vim
%dir %{_datadir}/vim/site
%dir %{_datadir}/vim/site/ftdetect
%{_datadir}/vim/site/ftdetect/augeas.vim
%dir %{_datadir}/vim/site/syntax
%{_datadir}/vim/site/syntax/augeas.vim

%files lenses
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lenses
%dir %{_datadir}/%{name}/lenses/dist
%{_datadir}/%{name}/lenses/dist/*.aug

%files lense-tests
%dir %{_datadir}/%{name}/lenses/dist/tests
%{_datadir}/%{name}/lenses/dist/tests/*.aug

%changelog
* Tue Jul  7 2020 Matthias Eliasson <elimat@opensuse.org>
- update to 1.12.0
  General changes/additions
  - update gnulib to 91584ed6
  Lens changes/additions
  - Anaconda: new lens to process /etc/sysconfig/anaconda instead of Shellvars (Pino Toscano) (Issue #597)
  - DevfsRules: add lens for FreeBSD devfs.rules files
  - Dovecot: permit ! in block titles (Nathan Ward) (Issue #599)
  - Hostname: Allow creation of hostname when file is missing (David Farrell) (Issue #606)
  - Krb5: add more pkinit_* options (Issue #603)
  - Logrotate: fix missing recognition of double quoted filenames (Issue #611)
  - Multipath: accept values enclosed in quotes (Issue #583)
  - Nginx: support unix sockets as server address (Issue #618)
  - Nsswitch: add merge action (Issue #609)
  - Pam: accept continuation lines (Issue #590)
  - Puppetfile: allow symbols as (optional) values (Issue #619) allow comments in entries (Issue #620)
  - Rsyslog: support dynamic file paths (Issue #622) treat #!/+/- as comment (arnolda, PR #595)
  - Syslog: accept 'include' directive (Issue #486)
  - Semanage: new lens to process /etc/selinux/semanage.conf instead of Simplevars (Pino Toscano) (Issue #594)
  - Shellvars: allow and/or in @if conditions (#582) accept functions wrapped in round brackets, accept variables with a dash in their name, exclude csh/tcsh profile scripts (Pino Toscano) (Issue #600) accept variable as command (Issue #601)
  - Ssh: accept RekeyLimit (Issue #605)
  - Sshd: accept '=' to separate option names from their values (Emil Dragu, #587)
  - Sudoers: support 'always_query_group_plugin' flag (Steve Traylen, #588)
  - Strongswan: parse lists. This is a backwards-incompatible change since list entries that were parsed into a single string are now split into a list of entries (Kaarle Ritvanen)
  - Toml: new lens to parse .toml files (PR #91)
  - Xorg: accept empty values for options (arnolda, PR #596)
- refresh patches
- run spec-cleaner
* Mon Mar 11 2019 Martin Liška <mliska@suse.cz>
- Add gcc9-disable-broken-test.patch in order to address bsc#1120894.
* Tue Feb 12 2019 Vítězslav Čížek <vcizek@suse.com>
- Don't ignore %%check test result, the testsuite now successfully
  passes
* Mon Dec 24 2018 ecsos@opensuse.org
- update to 1.11.0
  General changes/additions
  - augmatch: add a --quiet option; make the exit status useful
    to tell whether there was a match or not
  - Drastically reduce the amount of memory needed to evaluate
    complex path expressions against large files (Issue #569)
  - Fix a segfault on OSX when 'augmatch' is run without any
    arguments (Issue #556)
  API changes
  - aug_source did not in fact return the source; and always
    returned NULL for that. That has been fixed.
  Lens changes/additions
  - Chrony: add new options supported in chrony 3.2 and 3.3
    (Miroslav Lichvar)
  - Dhclient: fix parsing of append/prepend and similar
    directives (John Morrissey)
  - Fstab: allow leading whitespace in mount entry lines
    (Pino Toscano) (Issue #544)
  - Grub: tolerate some invalid entries. Those invalid entries
    get mapped to '#error' nodes
  - Httpd: accept comments with whitespace right after a tag
    opening a section (Issue #577)
  - Json: allow escaped slashes in strings (Issue #557)
  - Multipath: accept regular expressions for devnode, wwid,
    and property in blacklist and blacklist_exceptions sections
    (Issue #564)
  - Nginx: parse /etc/nginx/sites-enabled (plumbeo) allow
    semicolons inside double quoted strings in simple directives,
    and allow simple directives without an argument (Issue #566)
  - Redis: accept the 'bind' statement with multiple IP addresses
    (yannh) (Issue #194)
  - Rsyslog: support include() directive introduced in
    rsyslog 8.33
  - Strongswan: new lens (Kaarle Ritvanen)
  - Systemd: do not try to treat *.d or *.wants directories as
    configuration files (Issue #548)
* Tue Mar 20 2018 jengelh@inai.de
- Fix RPM groups.
* Tue Mar 20 2018 vcizek@suse.com
- update to 1.10.1:
  General changes/additions
    New CLI utility 'augmatch' to print the tree for a file and select
    some of its contents
    New command 'count' in augtool
    New function 'not(bool) -> bool' for path expressions
    The path expression 'label[. = "value"]' can now be written more
    concisely as 'label["value"]'
  API changes
    libfa has now a function fa_json to export an FA as a JSON file, and
    fa_state_* functions that make it possible to iterate over the FA's
    states and transitions. (Pedro Valero Mejia)
    Add functions aug_ns_label, aug_ns_value, aug_ns_count, and
    aug_ns_path to get the label (with index), the value, the number of
    nodes, and the fully qualified path for nodes stored in a nodeset in
    a variable efficiently
  Lens changes/additions
    Grubenv: new lens to process /boot/grub/grubenv (omgold)
    Httpd: also read files from /etc/httpd/conf.modules.d/*.conf
    (Tomas Meszaros) (Issue #537)
    Nsswitch: allow comments at the end of a line (Philip Hahn) (Issue #517)
    Ntp: accept 'ntpsigndsocket' statement (Philip Hahn) (Issue #516)
    Properties: accept empty comments with DOS line endings (Issue #161)
    Rancid: new lens for RANCiD router databases (Matt Dainty)
    Resolv: accept empty comments with DOS line endings (Issue #161)
    Systemd: also process /etc/systemd/logind.conf (Pat Riehecky)
    YAML: process a document that is just a sequence (John Vandenberg)
- drop chrpath dependency, the offending dump binary is no longer shipped
* Thu Feb 22 2018 fvogt@suse.com
- Use %%license (boo#1082318)
* Thu Oct 26 2017 vcizek@suse.com
- Version update to 1.9.0:
  - General changes/additions
  * Fix error in handling escaped whitespace at the end of path expressions
    (addresses CVE-2017-7555)
  * several improvements to the error messages when transforming a tree
    back to text fails. They now make it clearer what part of the tree
    was problematic, and what the tree should have looked like.
  * Fixed the pkg-config file, which should now be usable
  * Fix handling of backslash-escaping in strings and regular expressions
    in the lens language. We used to handle constructs like "\\" and
    /\\\\/ incorrectly. (Issue #495)
  * do not unescape the default value of a del on create; otherwise we are
    double unescaping these strings (Issue #507)
  * remove tempfile when saving files because destination is not writable
    (Issue #479)
  * span information is now updated on save (Issue #467)
  * fix lots of warnings generated by gcc 7.1
  * Various changes to reduce bashisms in tests and make them run on
    FreeBSD (Romain Tartière)
  - API changes
  * add function aug_ns_attr to allow iterating through a nodeset
    quickly. See examples/dump.c for an example of how to use them
    instead of aug_get, aug_label etc. and for a way to measure
    performance gains.
  - Lens changes/additions
  * Ceph: new lens for /etc/ceph/ceph.conf
  * Cgconfig: accept fperm & dperm in admin & task (Pino Toscano)
  * Dovecot: also load files from /usr/local/etc (Roy Hubbard)
  * Exports: relax the rules for the path at the beginning of a line so
    that double-quoted paths are legal, too
  * Getcap: new lens to parse generic termcap-style capability databases
  * Grub: accept toplevel 'boot' entry (Pino Toscano)
  * Httpd: handle empty comments with a continuation line (Issue #423);
    handle '>""' in a directive properly (Issue #429); make space between
    quoted arguments optional (Issue #435); accept quoted strings as part
    of bare arguments (Issue #470)
  * Nginx: load files from sites-available directory (Omer Katz) (Issue #471)
  * Nslcd: new lens for nss-pam-ldapd config (Jose Plana)
  * Oz: New lense for /etc/oz/oz.cnf
  * postfix lenses: also load files from /usr/local/etc (Roy Hubbard)
  * Properties: accept DOS line endings (Issue #468)
  * Rtadvd: new lens to parse the rtadvd configuration file (Matt Dainty)
  * Rsyslog: load files from /etc/rsyslog.d (Doug Wilson) (Issue #475);
    allow spaces before the # starting a comment; allow comments inside
    config statements like 'module'
  * Ssh: accept '=' to separate keyword from arguments
  * Sshd: split HostKeyAlgorithms into list of values; recognize quoted
    group names with spaces in them (Issue #477)
  * Sudoers: recognize "match_group_by_gid" (Luigi Toscano) (Issue #482)
  * Syslog: allow spaces before the # starting a comment
  * Termcap: new lens to parse termcap capability databases (Matt Dainty)
  * Vsftpd: accept seccomp_sandbox (Denys Stroebel)
  * Xymon: accept 'group-sorted' directive (Issue #462)
* Tue May 30 2017 tchvatal@suse.com
- Version update to 1.8.0:
  * See the News file for all the details
- Verified it contains fixes for bsc#933210 bsc#975729 bsc#925225
  bsc#1023204 CVE-2014-8119
* Fri Oct 28 2016 tchvatal@suse.com
- Version update to 1.6.0:
  * See the NEWS file for the details
* Thu May 12 2016 mlatimer@suse.com
- Update to version 1.5.0:
  - General changes/additions
  * augtool: new --timing option that prints after each operation how long
    it took
  * augtool: print brief help message when incorrect options are given rather
    than dumping all help text
  * Path expressions: optimize performance of evaluating certain
    expressions
  * lots of safety improvements in libfa to avoid using uninitialized
    values and the like (Daniel Trebbien)
  * tolerate building against OSX' libedit (Issue #256)
  - API changes
  * aug_match: fix a bug where expressions like /foo/*[2] would match a
    hidden node and pretend there was no match at all. We now make sure
    we never match a hidden node. Thanks to Xavier Mol for reporting the
    problem.
  * aug_get: make sure we set *value to NULL, even if the provided path is
    invalid (Issue #372)
  * aug_rm: fix segfault when deleting a tree and one of its ancestors
    (Issue #319)
  * aug_save: fix segfault when trying to save an invalid subtree. A
    routine that was generating details for the error message overflowed
    a buffer it had created (Issue #349)
  - Lens changes/additions
  * AptConf: support hash comments
  * AptSources: support options (Issue #295),
    support brackets with spaces in URI (GH #296)
    rename test file to test_aptsources.aug
  * Chrony: allow signed numbers and indentation, fix stray EOL entry,
    disallow comment on EOL, add many missing directives and
    options (Miroslav Lichvar, RHBZ#1213281)
    add new directives and options that were added in
    chrony-2.2 and chrony-2.3 and improve parsing of
    access configuration (Miroslav Lichvar, Issue #348)
    add new options for chrony-2.4 (Miroslav Lichvar)
  * Dhclient: avoid put ambiguity for node without value (Issue #294)
  * Group: support NIS map, support an overridden and disabled password,
    i.e. `+:*::` (Matt Dainty) (Issue #258)
  * Host_Conf: support spaces between list items (Cedric Bosdonnat, Issue #358)
  * Httpd: add paths to SLES vhosts
    (Jan Doleschal) (Issue #268)
    parse backslashes in directive arguments (Issue #307)
    parse mismatching case of opening/closing tags
    parse multiple ending section tags on one line
    parse wordlists in braces in SSLRequire directives
    parse directive args starting with double quote (Issue #330)
    parse directive args containing quotes
    support perl directives (Issue #327)
    parse line breaks/continuations in section arguments
    parse escaped spaces in directive/section arguments
    parse backslashes at the start of directive args (Issue #324)
  * Inputrc: support $else (Cedric Bosdonnat, Issue #359)
  * Interfaces: add support for source-directory (Issue #306)
  * Json: add comments support, refactor,
    allow escaped quotes and blackslashes
  * Keepalived: fix space/tag alignments and hanging spaces,
    add vrrp_mcast_group4 and vrrp_mcast_group6,
    add more vrrp_instance flags,
    add mcast/unicast_src_ip and unicast_peer,
    add missing garp options,
    add vrrp_script options,
    expand vrrp_sync_group block,
    allow notify option
    (Joe Topjian) (Issue #266)
  * Known_Hosts: refactoring and description fixed
  * Logrotate: support dateyesterday option (Chris Reeves) (GH #367, #368)
  * MasterPasswd: new lens to parse /etc/master.passwd
    (Matt Dainty) (Issue #258)
  * Multipath: add various missing keywoards (Olivier Mangold) (Issue #289)
  * MySQL: include /etc/my.cnf.d/*.cnf (Issue #353)
  * Nginx: improve typechecking of lens,
    allow masks in IP keys and IPv6 (Issue #260)
    add @server simple nodes (Issue #335)
  * Ntp: add support for basic interface syntax
  * OpenShift_Quickstarts: Use Json.lns
  * OpenVPN: add all options available in OpenVPN 2.3o
    (Justin Akers) (Issue #278)
  * Puppetfile: name separator is not mandatory
    add support for moduledir (Christoph Maser)
  * Rabbitmq: remove space in option name,
    add support for cluster_partitioning_handling,
    add missing simple options (Joe Topjian) (Issue #264)
  * Reprepro_Uploaders: add support for distribution field
    (Mathieu Alorent) (Issue #277),
    add support for groups (Issue #283)
  * Rhsm: new lens to parse subscription-manager's /etc/rhsm/rhsm.conf
  * Rsyslog: improve property filter parsing,
    treat whitespace after commas as optional.
    recognize '~' as a valid syslog action (discard)
    (Gregory Smith) (Issue #282),
    add support for redirecting output to named pipes
    (Gerlof Fokkema) (Issue #366)
  * Shellvars: allow partial quoting, mixing multiple styles
    (Kaarle Ritvanen) (Issue #183);
    allow wrapping builtin argument to multiple lines
    (Kaarle Ritvanen) (Issue #184);
    support ;; on same line with multiple commands
    (Kaarle Ritvanen) (Issue #185);
    allow line wrapping and improve quoting support
    (Kaarle Ritvanen) (Issue #187);
    accept [] and [[]] builtins (Issue #188);
    allow && and || constructs after condition
    (Kaarle Ritvanen) (Issue #265);
    add pattern nodes in case entries
    (BREAKING CHANGE: case entry values are now in a
    @pattern subnode) (Kaarle Ritvanen) (Issue #265)
    add eval builtin support;
    add alias builtin support;
    allow (almost) any command;
    allow && and || after commands (Issue #215);
    allow wrapping command sequences
    (Kaarle Ritvanen) (Issue #333);
    allow command-specific environment variable
    (Kaarle Ritvanen) (Issue #332);
    support subshells (Issue #339)
    newlines in start of functions
    allow newlines after actions
    support comments after function name (Issue #339)
    exclude SuSEfirewall2 (Cedric Bosdonnat, Issue #357)
  * Simplelines: parse OpenBSD's hostname.if(5)
    files (Jasper Lievisse Adriaanse) (Issue #252)
  * Smbusers: add support for ; comments
  * Spacevars: support flags (Issue #279)
  * Ssh: add support for HostKeyAlgorithms, KexAlgorithms
    and PubkeyAcceptedKeyTypes (Oliver Mangold) (Issue #290),
    add support for GlobalKnownHostsFile (Issue #316)
  * Star: New lens to parse /etc/default/star
  * Sudoers: support for negated command alias
    (Geoff Williams) (Issue #262)
  * Syslog: recognize '~' as a valid syslog action (discard)
    (Gregory Smith) (Issue #282)
  * Tmpfiles: new lens to parse systemd's tempfiles.d configuration
    files (Julien Pivotto) (Issue #269)
  * Trapperkeeper: new lens for Puppet server configuration files
  * Util: add comment_c_style_or_hash lens
    add empty_any lens
  * Vsftpd: add isolate and isolate_network options
    (Florian Chazal) (Issue #334)
  * Xml: allow empty document (Issue #255)
  * YAML: new lens (subset) (Dimitar Dimitrov) (Issue #338)
- Drop upstreamed patches:
    27d8457-inputrc-lens-support-mapping-like.patch
    2d12670-inputrc-lens-support-else.patch
    49bcfbe-Exclude-network-if-up.d-SuSEfirewall2-in-shellvars-l.patch
    7558c12-host_conf-lens-spaces-between-list-items-support.patch
* Tue Apr  5 2016 cbosdonnat@suse.com
- Fix errors showing up in guestfs tools.
  Add upstreamed patches:
    27d8457-inputrc-lens-support-mapping-like.patch
    2d12670-inputrc-lens-support-else.patch
    49bcfbe-Exclude-network-if-up.d-SuSEfirewall2-in-shellvars-l.patch
    7558c12-host_conf-lens-spaces-between-list-items-support.patch
* Thu Jul 16 2015 tchvatal@suse.com
- Version bump to 1.4.0:
  * Loads of bugfixes all around the package
  * Read up NEWS file for the detailed changes
* Fri Mar 13 2015 tchvatal@suse.com
- Whitespace
* Thu Dec 18 2014 meissner@suse.com
- restore keyring and .sig file, as this is checked by the OBS
  source service
* Thu Dec 18 2014 p.drouand@gmail.com
- Update  to version 1.3.0
  + General changes/additions
  * Add missing cp entry in manpage (GH issue #78)
  * Add seq to vim syntax highlight (Robert Drake)
  * Update augtool.1 man page with new commands and --span, RHBZ#1100077
  * augtool autocomplete includes command aliases, RHBZ#1100184
  * Remove unused "filename" argument from dump-xml command, RHBZ#1100106
  * aug_save returns non-zero result when unable to delete files,
    RHBZ#1091143
  + Lens changes/additions
  * Aliases: permit missing whitespace between colon and recipients
  * AptPreferences: Support spaces in origin fields
  * Cgconfig: handle additional valid controllers (Andy Grimm)
  * Chrony: New lens to parse /etc/chrony.conf (Pat Riehecky)
  * CPanel: New lens to parse cpanel.config files
  * Desktop: Allow @ in keys (GH issue #92)
  * Device_map: Parse all device.map files under /boot (Mike Latimer)
  * Dhclient: Add support for option modifiers (Robert Drake,
    GH issue #95)
    Parse hash statements with dhcp-eval strings
  * Dhcpd: stmt_string quoted blocks no longer store quote marks
    (incompatible change),
    many changes to support more record types (Robert Drake)
  * Group: NIS support (KaMichael)
  * Grub: handle "foreground" option, RHBZ#1059383 (Miguel Armas)
  * Gshadow: New lens (Lorenzo Catucci)
  * Httpd: Allow eol comments after section tags
    Allow continued lines inside quoted value (GH issue #104)
    Allow comparison operators in tags (GH issue #154)
  * IPRoute2: handle "/" in protocol name, swap ID and name fields
    (incompatible change), RHBZ#1063968,
    handle hex IDs and hyphens, as present in
    rt_dsfield, RHBZ#1063961
  * Iptables: parse /etc/sysconfig/iptables.save, RHBZ#1144651
  * Kdump: parse new options, permit EOL comments, refactor, RHBZ#1139298
  * Keepalived: Add more virtual/real server settings and checks, RHBZ#1064388
  * Known_Hosts: New lens for SSH known hosts files
  * Krb5: permit braces in values when not in sub-section, RHBZ#1066419
  * Ldso: handle "hwcap" lines (GH issue #100)
  * Lvm: support negative numbers, parse /etc/lvm/lvm.conf (Pino Toscano)
  * Multipath: add support for rr_min_io_rq (Joel Loudermilk)
  * NagiosConfig and NagiosObjects: Fix documentation (Simon Sehier)
  * NetworkManager: Use the Quote module, support # in values (no eol comments)
  * OpenVPN: Add support for fragment, mssfix, and script-security
    (Frank Grötzner)
  * Pagekite: New lens (Michael Pimmer)
  * Pam: Add partial support for arguments enclosed in [] (Vincent Brillault)
  * Passwd: Refactor lens (Lorenzo Catucci)
  * Redis: Allow empty quoted values (GH issue #115)
  * Rmt: New lens to parse /etc/default/rmt, RHBZ#1100549
  * Rsyslog: support complex $template lines, property filters and file
    actions with templates, RHBZ#1083016
  * Services: permit colons in service name, RHBZ#1121263
  * Shadow: New lens (Lorenzo Catucci)
  * Shellvars: Handle case statements with same-line ';;', RHBZ#1033799
    Allow any kind of quoted values in block
    conditions (GH issue #118)
    Support $(( .. )) arithmetic expansion in variable
    assignment, RHBZ#1100550
  * Simplevars: Support flags and empty values
  * Sshd: Allow all types of entries in Match groups (GH issue #75)
  * Sssd: Allow ; for comments
  * Squid: Support configuration files for squid 3 (Mykola Nikishov)
  * Sudoers: Allow wuoted string in default str/bool params (Nick Piacentine)
  * Syslog: Support "# !" style comments (Robert Drake, GH issue #65)
    Permit IPv6 loghost addresses, RHBZ#1129388
  * Systemd: Allow quoted Environment key=value pairs, RHBZ#1100547
    Parse /etc/sysconfig/*.systemd, RHBZ#1083022
    Parse semicolons inside entry values, RHBZ#1139498
  * Tuned: New lens for /etc/tuned/tuned-main.conf (Pat Riehecky)
  * UpdateDB: New lens to parse /etc/updatedb.conf
    (incompatible change as this file used to be processed with
    Simplevars)
  * Xml: Allow backslash in #attribute values (GH issue #145)
    Parse CDATA elements (GH issue #80)
  * Xymon_Alerting: refactor lens (GH issue #89)
- Remove the sig and the keyring file as there is no gpg verification
  anyway
- Remove augeas-device_map-grub2.patch, fixed on upstream release
* Wed Jul  2 2014 tchvatal@suse.com
- Change desc to describe the "tools" not just the library
  bnc#885495.
* Tue Jul  1 2014 tchvatal@suse.com
- Enable tests but "pass" them even with 2 failures.
* Tue May  6 2014 tchvatal@suse.com
- Add check phase, comment out as 2 test fails now.
- Clean up with spec-cleaner
- Version bump to 1.2.0:
  - API changes
  * Add aug_cp and the cp and copy commands
  * aug_to_xml now includes span information in the XML dump
  - General changes/additions
  * Fix documentation link in c_api NaturalDocs menu
  * Fix NaturalDocs documentation for various lenses
  * src/transform.c (filter_matches): wrap fnmatch to ensure that an incl
    pattern containing "//" matches file paths, RHBZ#1031084
  * Correct locations table for transform_save() (Tomas Hoger)
  * Corrections for CVE-2012-0786 tests (Tomas Hoger)
  * Fix umask handling when creating new files, RHBZ#1034261
  - Lens changes/additions
  * Access: support DOMAIN\user syntax for users and groups, bug #353
  * Authorized_Keys: Allow 'ssh-ed25519' as a valid authorized_key
    type (Jasper Lievisse Adriaanse)
  * Automounter: Handle hostnames with dashes in them, GH issue #27
  * Build: Add combinatorics group
  * Cyrus_Imapd: Create new entries without space before separator,
    RHBZ#1014974 (Dietmar Kling)
  * Desktop: Support square brackets in keys
  * Dhclient: Add dhclient.conf path for Debian/Ubuntu (Esteve Fernandez)
  * Dhcpd: Support conditionals, GH issue #34
    Support a wider variety of allow/deny statement, including
    booting and bootp (Yanis Guenane)
    Support a wider variety of DHCP allow/deny/ignore statements
    (Yanis Guenane)
  * Dovecot: Various enhancements and bug fixes (Michael Haslgrübler):
    add mailbox to block_names, fix for block_args in quotes,
    fix for block's brackets upon write,
    fixes broken tests for mailbox,
    fixes indention,
    test case for block_args with ",
    fixes broken indention
    Use Quote module
  * Exports: Permit colons for IPv6 client addresses, bug #366
  * Grub: Support the 'setkey' and 'lock' directives
    NFC fix whitespace errors
    Handle makeactive menu command, bug #340
    Add 'verbose' option, GH issue #73
  * Interfaces: Add in support for the source stanza in
    /etc/network/interfaces files
    Map bond-slaves and bridge-ports to arrays (incompatible
    change) (Kaarle Ritvanen)
    Add /etc/network/interfaces.d/* support
    Allow numeric characters in stanza options (Pascal Lalonde)
  * Koji: New lens to parse Koji configs (Pat Riehecky)
  * MongoDBServer: Accept quoted values (Tomas Klouda)
  * NagiosCfg: Do not try to parse /etc/nagios/nrpe.cfg anymore, GH issue #43
    /etc/nagios/nrpe.cfg is parsed by Nrpe (Yanis Guenane)
  * Nagiosobjects: Add support for optional spaces and indents
    and whole-line comments (Sean Millichamp)
  * OpenVPN: Support daemon, client-config-dir, route, and management
    directives (Freakin https://github.com/Freakin)
  * PHP: allow php-fpm syntax in keys, GH issue #35
  * Postfix_Main: Handle stray whitespace at end of multiline lines, bug #348
  * Postfix_virtual: allow '+' and '=' in email addresses (Tom Hendrikx)
  * Properties: support multiline starting with an empty string, GH issue #19
  * Samba: Permit asterisk in key name, bug #354
  * Shellvars: Read /etc/firewalld/firewalld.conf, bug #363
    Support all types of quoted strings in arrays, bug #357
    Exclude /etc/sysconfig/ip*tables.save files
  * Shellvars, Sysconfig: map "bare" export and unset lines to seq numbered
    nodes to handle multiple variables (incompatible change), RHBZ#1033795
  * Shellvars_list: Handle backtick variable assignments, bug #368
    Allow end-of-line comments, bug #342
  * Simplevars: Add /etc/selinux/semanage.conf
  * Slapd: use smart quotes for database entries; rename by/what to by/access;
    allow access to be absent as per official docs (incompatible change)
  * Sshd: Indent Match entries by 2 spaces by default
    Support Ciphers and KexAlgorithms groups, GH issue #69
    Let all special keys be case-insensitive
  * Sudoers: Permit underscores in group names, bug #370 (Matteo Cerutti)
    Allow uppercase characters in user names, bug #376
  * Sysconfig: Permit empty comments after comment lines, RHBZ#1043636
  * Sysconfig_Route: New lens for RedHat's route configs
  * Syslog: Accept UDP(@) and TCP(@@) protocol, bug #364 (Yanis Guenane)
  * Xymon_Alerting: New lens for Xymon alerting files (François Maillard)
  * Yum: Add yum-cron*.conf files (Pat Riehecky)
    Include only *.repo files from yum.repos.d (Andrew N Golovkov)
    Permit spaces after equals sign in list options, GH issue #45
    Split excludes as lists, bug #275
* Mon May  5 2014 mlatimer@suse.com
- device_map lense: Find device.map in any dir beneath /boot (bnc#875086)
  augeas-device_map-grub2.patch
* Fri Dec 13 2013 meissner@suse.com
- download url changed, also added keyring and .sig ring
* Tue Dec 10 2013 p.drouand@gmail.com
- Update to version 1.1.0
  - Handle files with special characters in their name, bug #343
  - Fix type error in composition ('f; g') of functions, bug #328
  - Improve detection of version script; make build work on Illumos with
    GBU ld (Igor Pashev)
  - augparse: add --trace option to print filenames of all modules being
    loaded
  - Various lens documentation improvements (Jasper Lievisse Adriaanse)
  - Lens changes/additions
  - ActiveMQ_*: new lens for ActiveMQ/JBoss A-MQ (Brian Harrington)
  - AptCacherNGSecurity: new lens for /etc/apt-cacher-ng/security.conf
    (Erik Anderson)
  - Automaster: accept spaces between options
  - BBHosts: support more flags and downtime feature (Mathieu Alorent)
  - Bootconf: new lens for OpenBSD's /etc/boot.conf (Jasper Adriaanse)
  - Desktop: Support dos eol
  - Dhclient: read /etc/dhclient.conf used in OpenBSD (Jasper Adriaanse)
  - Dovecot: New lens for dovecot configurations (Serge Smetana)
  - Fai_Diskconfig: Optimize some regexps
  - Fonts: exclude all README files (Jasper Adriaanse)
  - Inetd: support IPv6 addresses, bug #320
  - IniFile: Add lns_loose and lns_loose_multiline definitions
    Support smart quotes
    Warning: Smart quotes support means users should not add
    escaped double quotes themselves. Tests need to be fixed
    also.
    Use standard Util.comment_generic and Util.empty_generic
    Warning: Existing lens tests must be adapted to use standard
    comments and empty lines
    Allow spaces in entry_multiline* values
    Add entry_generic and entry_multiline_generic
    Add empty_generic and empty_noindent
    Let multiline values begin with a single newline
    Support dos eol
    Warning: Support for dos eol means existing lenses usually
    need to be adapted to exclude \r as well as \n.
  - IPRoute2: Support for iproute2 files (Davide Guerri)
  - JaaS: lens for the Java Authentication and Authorization Service
    (Simon Vocella)
  - JettyRealm: new lens for jetty-realm.properties (Brian Harrington)
  - JMXAccess, JMXPassword: new lenses for ActiveMQ's JMX files
    (Brian Harrington)
  - Krb5: Use standard comments and empty lines
    Support dos eol
    Improve performance
    Accept pkinit_anchors (Andrew Anderson)
  - Lightdm: Use standard comments and empty lines
  - LVM: New lens for LVM metadata (Gabriel)
  - Mdadm_conf: optimize some regexps
  - MongoDBServer: new lens (Brian Harrington)
  - Monit: also load /etc/monitrc (Jasper Adriaanse)
  - MySQL: Use standard comments and empty lines
    Support dos eol
  - NagiosCfg: handle Icinga and resources.cfg (Jasper Adriaanse)
  - Nrpe: accept any config option rather than predefined list (Gonzalo
    Servat); optimize some regexps
  - Ntpd: new lense for OpenNTPD config (Jasper Adriaanse)
  - Odbc: Use standard comments and empty lines
  - Openshift_*: new lenses for Openshift support (Brian Harrington)
  - Quote: allow multiple spaces in quote_spaces; improve docs
  - Passwd: allow period in user names in spec, bug #337; allow overrides
    in nisentry
  - PHP: Support smart quotes
    Use standard comments and empty lines
    Load /etc/php*/fpm/pool.d/*.conf (Enrico Stahn)
  - Postfix_master: allow [] in words, bug #345
  - Resolv: support 'lookup' and 'family' key words, bug #320
    (Jasper Adriaanse))
  - Rsyslog: support :omusrmsg: list of users in actions
  - RX: add CR to RX.space_in
  - Samba: Use standard comments and empty lines
    Support dos eol
  - Schroot: Support smart quotes
  - Services: support port ranges (Branan Purvine-Riley)
  - Shellvars: optimize some regexps; reinstate /etc/sysconfig/network,
    fixes bug #330, RHBZ#904222, RHBZ#920609; parse /etc/rc.conf.local
    from OpenBSD
  - Sip_Conf: New lens for sip.conf configurations (Rob Tucker)
  - Splunk: new lens (Tim Brigham)
  - Subversion: Support smart quotes
    Use standard comments and empty lines
    Use IniFile.entry_multiline_generic
    Use IniFile.empty_noindent
    Support dos eol
  - Sudoers: allow user aliases in specs
  - Sysctl: exclude README file
  - Systemd: Support smart quotes; allow backslashes in values
  - Xinetd: handle missing values in list, bug #307
  - Xorg: allow 'Screen' in Device section, bug #344
  - Yum: Support dos eol, optimize some regexps
* Sun Apr  7 2013 poelzleithner@b1-systems.de
- update to 1.0.0
  - drop bnc-729491-recognize-suse-sysconfig-files.patch:
    upstream ShellVars lense now uses /etc/sysconfig/* include filter
  - drop patches, now upstream: augeas-pkgdeps.diff, augeas-stdio.h.patch
* Wed Oct 10 2012 cfarrell@suse.com
- license update: GPL-3.0+ and LGPL-2.1+
  semicolon is ambiguous
* Fri Jul 27 2012 aj@suse.de
- Fix build with missing gets declaration (glibc 2.16)
* Sat Mar 17 2012 jengelh@medozas.de
- Ensure libxml2 is present in .pc file
* Wed Feb 29 2012 dmacvicar@suse.de
- update to 0.10.0
  - support relative paths by taking them relative to the value of
    /augeas/context in all API functions where paths are used
  - add aug_to_xml to API: transform tree(s) into XML, exposed as dump-xml in
    aug_srun and augtool. Introduces dependency on libxml2
  - fix regular expression escaping. Previously, /[/]/ match either a backslash
    or a slash. Now it only matches a slash
  - path expressions: add function 'int' to convert a node value (string) to an
    integer
  - path expressions: make sure the regexp produced by empty nodesets from
    regexp() and glob() matches nothing, rather than the empty word
  - fix --autosave when running single command from command line, BZ 743023
  - aug_srun: support 'insert' and 'move' as aliases for 'ins' and 'mv'
  - aug_srun: allow escaping of spaces, quotes and brackets with \
  - aug_init: accept AUG_NO_ERR_CLOSE flag; return augeas handle even when
    initialization fails so that caller gets some details about why
    initialization failed
  - aug_srun: tolerate trailing white space in commands
  - much improved, expanded documentation of many lenses
  - always interpret lens filter paths as absolute, bug #238
  - fix bug in libfa that would incorrectly calculate the difference of a case
    sensistive and case insensitive regexp (/[a-zA-Z]+/ - /word/i would match
    'worD')
  - new builtin 'regexp_match' for .aug files to make testing regexp matching
    easier during development
  - fix 'span' command, bug #220
  - Lens changes/additions
  * Access: parse user@host and (group) in users field; field separator need
    not be surrounded by spaces
  * Aliases: allow spaces before colons
  * Aptconf: new lens for /etc/apt/apt.conf
  * Aptpreferences: support origin entries
  * Backuppchosts: new lens for /etc/backuppc/hosts, bug 233 (Adam Helms)
  * Bbhosts: various fixes
  * Cgconfig: id allowed too many characters
  * Cron: variables aren't set like shellvars, semicolons are allowed in
    email addresses; fix parsing of numeric fields, previously upper case
    chars were allowed; support ranges in time specs
  * Desktop: new lens for .desktop files
  * Dhcpd: slashes must be double-quoted; add Red Hat's dhcpd.conf locations
  * Exports: allow empty options
  * Fai_diskconfig: new lens for FAI disk_config files
  * Fstab: allow ',' in file names, BZ 751342
  * Host_access: new lens for /etc/hosts.{allow,deny}
  * Host_conf: new lens for /etc/host.conf
  * Hostname: new lens for /etc/hostname
  * Hosts: also load /etc/mailname by default
  * Iptables: allow digits in ipt_match keys, bug #224
  * Json: fix whitespace handling, removing some cf ambiguities
  * Kdump: new lens for /etc/kdump.conf (Roman Rakus)
  * Keepalived: support many more flags, fields and blocks
  * Krb5: support [pam] section, bug #225
  * Logrotate: be more tolerant of whitespace in odd places
  * Mdadm_conf: new lens for /etc/mdadm.conf
  * Modprobe: Parse commands in install/remove stanzas (this introduces a
    backwards incompatibility); Drop support for include as it is not documented
    in manpages and no unit tests are shipped.
  * Modules: new lens for /etc/modules
  * Multipath: add support for seveal options in defaults section, bug #207
  * Mysql: includedir statements are not part of sections; support !include;
    allow indentation of entries and flags
  * Networks: new lens for /etc/networks
  * Nrpe: allow '=' in commands, bug #218 (Marc Fournier)
  * Php: allow indented entries
  * Phpvars: allow double quotes in variable names; accept case insensitive
    PHP tags; accept 'include_once'; allow empty lines at EOF; support define()
    and bash-style and end-of-line comments
  * ostfix_master: allow a lot more chars in words/commands, including commas
  * PuppetFileserver: support same-line comments and trailing whitespace,
    bug #214
  * Reprepo_uploaders: new lens for reprepro's uploaders files
  * Resolv: permit end-of-line comments
  * Schroot: new lens for /etc/schroot/schroot.conf
  * Shellvars: greatly expand shell syntax understood; support
    various syntactic constructs like if/then/elif/else, for, while,
    until, case, and select; load /etc/blkid.conf by default
  * Spacevars: add toplevel lens 'lns' for consistency
  * Ssh: new lens for ssh_config (Jiri Suchomel)
  * Stunnel: new lens for /etc/stunnel/stunnel.conf (Oliver Beattie)
  * Sudoers: support more parameter flags/options, bug #143
  * Xendconfsxp: lens for Xen configuration (Tom Limoncelli)
  * Xinetd: allow spaces after '{'
- update modprobe lens patch to apply on 0.10.0
- update shellvars lens patch to add some missing files on SUSE
  distros mentioned in bnc#729491
* Sat Feb 11 2012 jengelh@medozas.de
- Remove rednudant tags/sections from specfile
* Thu Jan 26 2012 dmacvicar@suse.de
- Patch shellvars.aug to recognize SUSE specific files in
  sysconfig (bnc#729491)
* Thu Sep 22 2011 dmacvicar@suse.de
- move lenses from /usr/share/libaugeas0/augeas
  to /usr/share/augeas (bnc#719199)
- move vim lenses syntax files from -lenses to -devel package
* Sat Sep 17 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
- Add augeas-devel to baselibs
* Tue Aug 23 2011 dmueller@suse.de
- update to 0.9.0:
  - augtool: keep history in ~/.augeas/history
  - add aug_srun API function; this makes it possible to run a sequence of
    commands through the API
  - aug_mv: report error AUG_EMVDESC on attempts to move a node into one of
    its descendants
  - path expressions: allow whitespace inside names, making '/files/etc/foo
    bar/baz' a legal path, but parse [expr1 or expr2] and [expr1 and expr2]
    as the logical and/or of expr1 and expr2
  - path expressions: interpret escape sequences in regexps; since '.' does
    not match newlines, it has to be possible to write '.|\n' to match any
    character
  - path expressions: allow concatenating strings and regexps; add
    comparison operator '!~'; add function 'glob'; allow passing a nodeset
    to function 'regexp'
  - store the names of the functions available in path expressions under
    /augeas/version
  - fix several smaller memory leaks
  - Lens changes/additions
  * Aliases: allow spaces and commas in aliases (Mathieu Arnold)
  * Grub: allow "bootfs" Solaris/ZFS extension for dataset name, bug #201
    (Dominic Cleal); allow kernel path starting with a BIOS device,
    bug #199
  * Inifile: allow multiline values
  * Php: include files from Zend community edition, bug #210
  * Properties: new lens for Java properties files, bug #194 (Craig Dunn)
  * Spacevars: autoload two ldap files, bug #202 (John Morrissey)
  * Sudoers: support users:groups format in a Runas_Spec line, bug #211;
    add CSW paths (Dominic Cleal)
  * Util: allow comment_or_eol to match whitespace-only comments,
    bug #205 (Dominic Cleal)
  * Xorg: accept InputClass section; autoload from /etc/X11/xorg.conf.d,
    bug #197
* Fri May  6 2011 dmacvicar@suse.de
- fate#311042: Update augeas packages for latest puppet support
  in SLE-11
- update to 0.8.1
  * augtool: respect autosave flag in oneshot mode, bug #193;
    fix segfault caused by unmatched bracket in path expression,
    bug #186
  * eliminate a global variable in the lexer, fixes BZ 690286
  * replace an erroneous assert(0) with a proper error message when
    none of the alternatives in a union match during saving,
    bug #183
  * improve AIX support
  * Lens changes/additions
  * Access: support the format @netgroup@@nisdomain, bug #190
  * Fstab: fix parsing of SELinux labels in the fscontext option
  * Grub: support 'device' directive for UEFI boot, bug #189; support
    'configfile' and 'background'
  * Httpd: handle continuation lines; autoload httpd.conf on
    Fedora/RHEL, BZ 688149; fix support for single-quoted
    strings
  * Iptables: support --tcp-flags, bug #157; allow blank and comment
    lines anywhere
  * Mysql: include /etc/my.cnf used on Fedora/RHEL, BZ 688053
  * NagiosCfg: parse setting multiple values on one line
  * NagiosObjects: process /etc/nagios3/objects/*.cfg
  * Nsswitch: support 'sudoers' as a database, bug #187
  * Shellvars: autoload /etc/rc.conf used in FreeBSD
  * Sudoers: support '#include' and '#includedir', bug #188
  * Yum: exclude /etc/yum/pluginconf.d/versionlock.list
- changes for 0.8.0
  * add new 'square' lens combinator
  * add new aug_span API function
  * augtool: short options for --nostdinc, --noload, and --noautoload
  * augtool: read commands from tty after executing file with --interactive
  * augtool: add --autosave option
  * augtool: add --span option to load nodes' span
  * augtool: add span command to get the node's span according to the input
    file
  * augtool: really be quiet when we shouldn't be echoing
  * fix segfault in get.c with L_MAYBE lens; bug #180
  * fix segfault when a path expression called regexp() with an invalid
    regexp; bug #168
  * improved vim syntax file
  * replace augtest by test-augtool.sh to obviate the need for Ruby to run
    tests
  * use sys_wait module from gnulib; bug #164
  * Lens changes/additions
  * Access: new lens for /etc/security/access.conf
  * Crypttab: new lens for /etc/crypttab
  * Dhcpd: new lens
  * Exports: accept hostnames with dashes; bug #169
  * Grub: add various Solaris extensions; support "map" entries,
    bug #148
  * Httpd: new lens for Apache config
  * Inifile: new lens indented_title_label
  * Interfaces: allow indentation for "iface" entries; bug #182
  * Mysql: change default comment delimiter from ';' to '#'; bug #181
  * Nsswitch: accept various add'l databases; bug #171
  * PuppetFileserver: new lens for Puppet's fileserver.conf
  * REsolv: allow comments starting with ';'; bug #173
  * Shellvars: autoload various snmpd config files; bug #170
  * Solaris_system: new lens for /etc/system on Solaris
  * Util (comment_c_style, empty_generic, empty_c_style): new lenses
  * Xml: generic lens to process XML files
  * Xorg: make "position" in "screen" optional; allow "Extensions"
    section; bug #175
* Mon Apr  4 2011 coolo@novell.com
- add baselibs.conf
* Tue Jan 11 2011 dmacvicar@suse.de
- update to 0.7.4
  * augtool: new clearm command to parallel setm
  * augtool: add --file option
  * Fix SEGV under gcc 4.5, caused by difficulties of the gcc
    optimizer handling bitfields (bug #149; rhbz #651992)
  * Preserve parse errors under /augeas//error: commit 5ee81630,
    released in 0.7.3, introduced a regression that would cause
    the loss of parse errors; bug #138
  * Avoid losing already parsed nodes under certain circumstances;
    bug #144
  * Properly record the new mtime of a saved file; previously the
    mtime in the tree was reset to 0 when a file was saved, causing
    unnecessary file reloads
  * fix a SEGV when using L_MAYBE in recursive lens; bug #136
  * Incompatible lens changes
  * Fstab: parse option values
  * Squid: various improvements, see bug #46;
  * Xinetd: map service names differently
  * Lens changes/additions
  * Aptsources: map comments properly, allow indented lines;
    bug #151
  * Grub: add indomU setting for Debian.
    Allow '=' as separator in title; bug #150
  * Fstab: also process /etc/mtab
  * Inetd: support rpc services
  * Iptables: allow underscore in chain names
  * Keepalived: new lens for /etc/keepalived/keepalived.conf
  * Krb5: allow digits in realm names; bug #139
  * Login_defs: new lens for /etc/login.defs
    (Erinn Looney-Triggs)
  * Mke2fs: new lens for /etc/mke2fs.conf
  * Nrpe: new lens for Nagios nrpe (Marc Fournier)
  * Nsswitch: new lens for /etc/nsswitch.conf
  * Odbc: new lens for /etc/odbc.ini (Marc Fournier)
  * Pg_hba: New lens; bug #140 (Aurelien Bompard).
    Add system path on Debian; bug #154 (Marc Fournier)
  * Postfix_master: parse arguments in double quotes; bug #69
  * Resolv: new lens for /etc/resolv.conf
  * Shells: new lens for /etc/shells
  * Shellvars: parse ulimit builtin
  * Sudoers: load file from /usr/local/etc (Mathieu Arnold)
    Allow 'visiblepw' parameter flag; bug #143. Read files from
    /etc/sudoers.d
  * Syslog: new lens for /etc/syslog.conf (Mathieu Arnold)
  * Util: exclude dpkg backup files; bug #153 (Marc Fournier)
  * Yum: accept continuation lines for gpgkey; bug #132
* Thu Oct  7 2010 pmullaney@novell.com
- added patch for allow_unsupported_modules command in modprobe.d conf files
* Fri Oct  1 2010 jkupec@suse.cz
- added vim files symlinks for lens syntax files
- fixed a few rpmlint warnings (fixed rpm group, no ldconfig run)
* Thu Sep  9 2010 jkupec@suse.cz
  * Update to 0.7.3
  * ug_load: only reparse files that have actually changed; greatly
  speeds up reloading
  * record all variables in /augeas/variables, regardless of whether
  they were defined with aug_defvar or aug_defnode; make sure
  /augeas/variables always exists
  * redefine all variables (by reevaluating their corresponding
  expressions) after a aug_load. This makes variables 'sticky'
  across loads
  * fix behavior of aug_defnode to not fail when the expression
  evaluates to a nonempty node set
  * make gnulib a git submodule so that we record the gnulib commit
  off which we are based
  * allow 'let rec' with non-recursive RHS
  * fix memory corruption when reloading a tree into which a
  variable defined by defnode points (BZ 613967)
  * plug a few small memory leaks, and some segfaults
  * Lens changes/additions
  * Device_map: new lens for grub's device.map (Matt Booth)
  * Limits: also look for files in /etc/security/limits.d
  * Mysql: new lens (Tim Stoop)
  * Shellvars: read /etc/sysconfig/suseconfig (Frederik Wagner)
  * Sudoers: allow escaped spaces in user/group names (Raphael Pinson)
  * Sysconfig: lens for the shell subdialect used in /etc/sysconfig;
    lens strips quotes automatically
* Thu Sep  9 2010 jkupec@suse.cz
  * 0.7.2 - 2010-06-22
  * new API call aug_setm to set/create multiple nodes simultaneously
  * record expression used in a defvar underneath /augeas/variables
  * Lens changes/additions
  * Group: add test for disabled account (Raphael Pinson)
  * Grub: handle comments within a boot stanza
  * Iptables: also look for /etc/iptables-save (Nicolas Valcarcel)
  * Modules_conf: new lens for /etc/modules.conf (Matt Booth)
  * Securetty: added handling of emtpy lines/comments (Frederik Wagner)
  * Shellvars: added SuSE sysconfig puppet files (Frederik Wagner),
    process /etc/environment (seph)
  * Shellvars_list: Shellvars-like lens that treats strings of
    space-separated words as lists (Frederik Wagner)
* Thu Sep  9 2010 jkupec@suse.cz
  * 0.7.1 - 2010-04-21
  * fix crash when recursive lens was used in a nonrecursive lens (bug #100)
  * context free parser/recursive lenses: handle 'l?' properly (bug #119);
  distinguish between successful parse and parse with an error at end of
  input; do caller filtering to avoid spurious ambiguous parses with
  grammars containing epsilon productions
  * aug_get: return -1 when multiple nodes match (bug #121)
  * much better error message when iteration stops prematurely during
  put/create than the dreaded 'Short iteration'
  * src/lens.c (lns_check_rec): fix refcounting mistake on error path (bug #120)
  * Lens changes/additions
  * Approx: lens and test for the approx proxy server (Tim Stoop)
  * Cgconfig: lens and tests for libcgroup config (Ivana Hutarova Varekova)
  * Cgrules: new lens and test (Ivana Hutarova Varekova)
  * Cobblermodules: lens + tests for cobbler's modules.conf (Shannon Hughes)
  * Debctrl: new lens and test (Dominique Dumont)
  * Dput: add 'allow_dcut' parameter (bug #105) (Raphael Pinson)
  * Dhclient: add rfc code parsing (bug #107) (Raphael Pinson)
  * Group: handle disabled passwords
  * Grub: support empty kernel parameters, Suse incl.s (Frederik Wagner)
  * Inittab: allow ':' in the process field (bug #109)
  * Logrotate: tolerate whitespace at the end of a line (bug #101); files
    can be separated by newlines (bug #104) (Raphael Pinson)
  * Modprobe: Suse includes (Frederik Wagner)
  * Nagisocfg: lens and test for /etc/nagios3/nagios.cfg (Tim Stoop)
  * Ntp: add 'tinker' directive (bug #103)
  * Passwd: parse NIS entries on Solaris
  * Securetty: new lens and test for /etc/securetty (Simon Josi)
  * Shellvars: handle a bare 'export VAR'; Suse includes (Frederik
    Wagner); allow spaces after/before opening/closing parens for array
  * Sudoers: allow del_negate even if no negate_node is found (bug #106)
    (Raphael Pinson); accept 'secure_path' (BZ 566134) (Stuart
    Sears)
* Thu Sep  9 2010 jkupec@suse.cz
  * 0.7.0 - 2010-01-14
  * Support for context-free lenses via the 'let rec' keyword. The syntax
  is experimental, though the feature is here to stay. See
  lenses/json.aug for an example of what's possible with that.
  * Support for case-insensitive regular expressions. Simply append 'i' to
  a regexp literal to make it case-insensitive, e.g. /hello/i will match
  all variations of hello, regardless of case.
  * Major revamp of augtool. In particular, path expressions don't need to
  be quoted anymore. The online help has been greatly improved.
  * Check during load/save that each file is only matched by one transform
  under /augeas/load. If there are multiple transforms for a file, the
  file is skipped.
  * New error codes AUG_ENOLENS and AUG_EMXFM
  * Do not choke on non-existing lens during save
  * Change the metadata for files under /augeas/files slightly: the node
  /augeas/files/$PATH/lens now has the name of the lens used to load the
  file; the source location of that lens has moved to
  /augeas/files/$PATH/lens/info
  * New public functions fa_nocase, fa_is_nocase, and fa_expand_nocase in
  libfa
  * Various smaller bug fixes, performance improvements and improved error
  messages
  * Lens changes/additions
  * Cobblersettings: new lens and test (Bryan Kearney)
  * Iptables: allow quoted strings as arguments; handle both negation
    syntaxes
  * Json: lens and tests for generic Json files
  * Lokkit: allow '-' in arguments
  * Samba: accept entry keys with ':' (Partha Aji)
  * Shellvars: allow arrays that span multiple lines
  * Xinetd (name): fix bad '-' in character class
* Thu Sep  9 2010 jkupec@suse.cz
  * 0.6.0 - 2009-11-30
  * Add error reporting API (aug_error and related calls); use to report
  error details in a variety of places
  * Path expressions: add regexp matching; add operator '|' to form union
  of nodesets (ticket #89)
  * Tolerate non-C locales from the environment (ticket #35); it is no
  longer necessary to set the locale to C from the outside
  * use stpcpy/stpncpy from gnulib (needed for building on Solaris)
  * Properly check regexp literals for syntax errors (ticket #93)
  * Distribute and install vim syntax files (ticket #97)
  * many more bugfixes
  * Lens changes/additions
  * Apt_preferences: support version pin; filter out empty lines (Matt
    Palmer)
  * Cron: variables can contain '_' etc. (ticket #94)
  * Ethers: new lens for /etc/ethers (Satoru SATOH)
  * Fstab: allow '#' in spec (ticket #95)
  * Group: allow empty password field (ticket #95)
  * Inittab: parse end-of-line comments into a #comment
  * Krb5: support kdc section; add v4_name_convert subsection to
    libdefaults (ticket #95)
  * Lokkit: add mising eol to forward_port; make argument for --trust
    more permissive
  * Pam: allow '-' before type
  * Postfix_access: new lens for /etc/postfix/access (Partha Aji)
  * Rx: allow '!' in device_name
  * Sudoers: allow certain backslash-quoted characters in a command (Matt
    Palmer)
  * Wine: new lens to read Windows registry files
* Thu Sep  9 2010 jkupec@suse.cz
  * 0.5.3 - 2009-09-14
  * Match trees on label + value, not just label; see
  tests/modules/pass_strip_quotes.aug for how that enables stripping
  quotes
  * Do not trip over symlinks to files on a different device during save;
  fixes problems with writing to /etc/grub.conf on Fedora/RHEL
  * API (defnode): always add the newly created node into the resulting
  nodeset
  * Add preceding-sibling and following-sibling axes to path expressions
  * augtool, augparse: add --version option (bug #88)
  * Change file info recorded under /augeas/files/FILE/*: remove lens/id
  and move lens/info to lens
  * Properly record new files under /augeas/files (bug #78)
  * aug_load: clean up variables to avoid dangling references (bug #79)
  * Make Augeas work on AIX
  * Ignore anything but regular files when globbing
  * Add 'clear' function to language for use in unit tests
  * typechecker: print example trees in tree format
  * libfa: properly support regexps with embedded NUL's
  * Lens changes/additions
  * Xorg: revamped, fixes various parse failures (Matt Booth)
  * Inetd: new lens and test (Matt Palmer)
  * Multipath: new lens and test
  * Slapd: also read /etc/openldap.slapd.conf (bug #85)
* Thu Sep  9 2010 jkupec@suse.cz
  * 0.5.2 - 2009-07-13
  * Make Augeas work on Mac OS/X (bug #66) (Anders Bjoerklund)
  * reduce symbols exported from libfa with linker script
  * add --echo option to augtool
  * require Automake 1.11 (Jim Meyering)
  * avoid spurious save attempts for freshly read files
  * Lens changes/additions
  * Inittab: schema change: use 'id' field as name of subtree for a line,
    instead of a generated number. Map comments as '#comment' (Matt Palmer)
  * Logrotate: make owner/group in create statement optional, allow
    filenames to be indented
  * Ntp: allow additional options for server etc. (bug #72)
  * Shellvars: allow backticks as quote characters (bug #74)
  * Yum: also read files in /etc/yum/pluginconf.d (Marc Fournier)
* Thu Sep  9 2010 jkupec@suse.cz
  * 0.5.1 - 2009-06-09
  * augeas.h: flag AUG_NO_MODL_AUTOLOAD suppresses initial loading
    of modules; exposed as --noautoload in augtool
  * augtool: don't prompt when input is not from tty (Raphael Pinson)
  * augparse: add --notypecheck option
  * path expressions: allow things like '/foo and /bar[3]' in predicates
  * Lens changes/additions
  * Aliases: map comments as #comment (Raphael Pinson)
  * Build, Rx, Sep: new utility modules (Raphael Pinson)
  * Cron: new lens (Raphael Pinson)
  * Dnsmasq: process files in /etc/dnsmasq.d/* (ticket #65)
  * Grub: parse kernel and module args into separate nodes; parse
    arguments for 'serial', 'terminal', and 'chainloader'; allow
    optional argument for 'savedefault'
  * Interfaces: make compliant with actual Debian spec (Matt Palmer)
  * Iptables: relax regexp for chain names; allow comment lines mixed
    in with chains and rules (ticket #51)
  * Logrotate: allow '=' as separator (ticket #61); make newline at end
    of scriptlet optional
  * Modprobe: handle comments at end of line
  * Ntp: parse fudge record (Raphael Pinson); parse all directives in
    default Fedora ntp.conf; process 'broadcastdelay', 'leapfile',
    and enable/disable flags (ticket #62)
  * Pbuilder: new lens for Debian's personal builder (Raphael Pinson)
  * Php: add default path on Fedora/RHEL (Marc Fournier)
  * Squid: handle indented entries (Raphael Pinson)
  * Shellvars: map 'export' and 'unset'; map comments as #comment
    (Raphael Pinson)
  * Sudoers: allow backslashes inside values (ticket #60) (Raphael Pinson)
  * Vsftpd: map comments as #comment; handle empty lines; find
    vsftpd.conf on Fedora/RHEL
  * Xinetd: map comments as #comment (Raphael Pinson)
* Tue Dec 15 2009 jengelh@medozas.de
- enable parallel building
* Tue Mar 31 2009 jkupec@suse.cz
  * Update to 0.5.0
  * Upstream notes:
  Clean up interface for libfa; the interface is now considered stable
  * New aug_load API call; allows controlling which files to load by
  modifying /augeas/load and then calling aug_load; on startup, the
  transforms marked with autoload are reported under /augeas/load
  * New flag AUG_NO_LOAD for aug_init to keep it from loading files on
  startup; add --noload option to augtool
  * New API calls aug_defvar and aug_defnode to define variables for
  path expressions; exposed as 'defvar' and 'defnode' in augtool
  * New program examples/fadot to draw various finite automata (Francis
  Giraldeau)
  * Report line number and character offset in the tree when parsing a
  file with a lens fails
  * Fix error in propagation of dirty flag, which could lead to only
  parts of a tree being saved when multiple files were modified
  * Flush files to disk before moving them
  * Fix a number of memory corruptions in the XPath evaluator
  * Several performance improvements in libfa
  * Lens changes/additions
  * Grub: process embedded comments for update-grub (Raphael Pinson)
  * Iptables: new lens for /etc/sysconfig/iptables
  * Krb5: new lens for /etc/krb5.conf
  * Limits: map dpmain as value of 'domain' node, not as label
    (Raphael Pinson)
  * Lokkit: new lens for /etc/sysconfig/system-config-firewall
  * Modprobe: new lens for /etc/modprobe.d/*
  * Sudoers: more finegrained parsing (ticket #48) (Raphael Pinson)
* Tue Mar 17 2009 jkupec@suse.cz
  * Update to 0.4.2
  * Moved lense tests into separate package 'augeas-lense-tests'
  * Added augeas-lenses-license-fix patch
  * Upstream notes:
  * Do not delete files that had an error upon parsing
  * For Fedora/EPEL RPM's, BuildRequire libselinux-devel (bug #26)
  * In path expressions, the meaning of '<' and '<=' was reversed
  * Always create an entry /files in aug_init
  * New builtin 'Sys' module with functions 'getenv' and 'read_file',
  the latter reads a the contents of a file into a string
  * Lens changes/additions
  * Postfix_main: handle continuation lines
  * Bbhosts, Hosts, Logrotate, Sudoers: label comment nodes as '#comment'
  * Sshd: map comments as '#comment' nodes
  * Squid: add all keywords from squid 2.7 and 3 (Francois Deppierraz)
  * Logrotate: process unit suffixes for 'size' and 'minsize'
* Tue Mar  3 2009 jkupec@suse.cz
  * Update to 0.4.1
  * Moved lenses to separate package 'augeas-lenses'.
  * Upstream notes:
  * Remove files when their entire subtree under /files is deleted
  * Various bug fixes and syntax enhancements for path expressions
  (see tests/xpath.tests for details)
  * Evaluate path expressions with multiple predicates correctly
  * Fix incorrect setting of /augeas/events/saved
  * Major cleanup of matching during get; drastically improves
  performance for very large (on the order of 10k lines) config files
  * Small performance improvement in the typechecker
  * Reject invalid character sets like [x-u] during typecheck
  * Build with compile warnings set to 'maximum' instead of 'error', so
  that builds on platforms with broken headers will work out of the box
  * Lens changes/additions
  * Util.stdexcl now excludes .augsave and .augnew files
  * Logrotate: allow 'yearly' schedule, spaces around braces
  * Ntp: fix so that it processes ntp.conf on Fedora 10
  * Services: lens for /etc/services (Raphael Pinson)
  * Xorg: new lens and tests (Raphael Pinson)
* Mon Feb 23 2009 dmacvicar@suse.de
  * Update to 0.4.0
  * Much improved and expanded support for path expressions in the public API. See doc/xpath.txt and tests/xpath.tests for details.
  * Solaris support: builds at least on OpenSolaris 2008.11
  * Lens changes/additions
  o Grub: support color and savedefault
  o DarkIce: new lens for http://darkice.tyrell.hu/ (Free Ekanayaka)
* Mon Feb  2 2009 dmacvicar@suse.de
  * Update to 0.3.6
  * report version in /augeas/version, report legal save modes in /augeas/version/save/mode for feature tests/version checking
  * dynamically change behavior of aug_save; add noop save mode (Bryan Kearney)
  * plug memory leak, more portable SELinux test (Jim Meyering)
  * fix bz rhbz#478619 - do not use abspath (Arnaud Gomes-do-Vale)
  * fix segfault when branch in a union does not have a ktype
  * Lens changes/additions
  o Dpkg: new lens for Debian's dpkg.cfg (Robin Lee Powell)
  o Limits: new lens for /etc/security/limits.conf (Free Ekanayaka)
  o Soma: new lens for http://www.somasuite.org/ config (Free Ekanayaka)
  o Php, Gdm: fix minor regexp error (Marc Fournier) expand filter for Php config files (Robin Lee Powell)
  o Phpvars: whitspace fixes (Free Ekanayaka)
  o Puppet: accept indented puppet.conf (ticket #25)
