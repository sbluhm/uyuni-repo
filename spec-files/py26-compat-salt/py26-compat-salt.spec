#
# spec file for package py26-compat-salt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%bcond_with    test
%bcond_with    docs
%bcond_with    builddocs
%if 0${?rhel} >= 8
%global __python /usr/bin/python2
%endif

%define compatdir %{_datadir}/susemanager/py26-compat
%define origname salt

Name:           py26-compat-salt
Version:        2016.11.10
Release:        2.1.uyuni
Summary:        Python 2.6 compatible salt
License:        Apache-2.0
Group:          System/Management
Url:            http://saltstack.org/
BuildArch:      noarch
# Git: https://github.com/openSUSE/salt.git
Source0:        https://pypi.python.org/packages/a9/0a/31908d158c055248d5b5b22e66863eb98167aecad71edda92b58b223db7b/salt-2016.11.10.tar.gz
Source1:        README.SUSE
Source2:        salt-tmpfiles.d
Source3:        html.tar.bz2
Source4:        update-documentation.sh
Source5:        travis.yml
Source6:        py26-compat-salt.conf
Source7:        py26-compat-salt-sle15-or-newer.conf

# PATCH-FIX-OPENSUSE use-forking-daemon.patch tserong@suse.com -- We don't have python-systemd, so notify can't work
# We do not upstream this patch because this is something that we have to fix on our side
Patch1:         tserong-suse.com-we-don-t-have-python-systemd-so-not.patch
# PATCH-FIX-OPENSUSE use-salt-user-for-master.patch -- Run salt master as dedicated salt user
# We do not upstream this patch because this is suse custom configuration
# (see: https://trello.com/c/wh96lCD4/1528-get-rid-of-0003-check-if-byte-strings-are-properly-encoded-in-utf-8-patch-in-the-salt-package)
Patch2:         run-salt-master-as-dedicated-salt-user.patch
# PATCH-FIX-OPENSUSE https://github.com/saltstack/salt/pull/30424
# We do not upstream this patch because it has been fixed upstream
Patch3:         check-if-byte-strings-are-properly-encoded-in-utf-8.patch
# PATCH-FIX-OPENSUSE prevent rebuilds in OBS
# We do not upstream this patch because the issue is on our side
Patch4:         do-not-generate-a-date-in-a-comment-to-prevent-rebui.patch
# PATCH-FIX-OPENSUSE Generate events from the Salt minion,
# We do not upstream this because this is for SUSE only (15.08.2016) if Zypper has been used outside the Salt infrastructure
Patch5:         add-zypp-notify-plugin.patch
# PATCH-FIX_OPENSUSE
Patch6:         run-salt-api-as-user-salt-bsc-990029.patch
# PATCH-FIX_OPENSUSE
Patch7:         change-travis-configuration-file-to-use-salt-toaster.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/37856 (pending to include in 2016.11)
Patch8:         setting-up-os-grains-for-sles-expanded-support-suse-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/34165
Patch9:         fix-salt-summary-to-count-not-responding-minions-cor.patch
# PATCH-FIX_OPENSUSE
Patch10:        avoid-failures-on-sles-12-sp2-because-of-new-systemd.patch
# PATCH-FIX_OPENSUSE
Patch11:        add-yum-plugin.patch
# PATCH-FIX_OPENSUSE
Patch12:        add-ssh-option-to-salt-ssh.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/38806
Patch13:        add-a-salt-minion-service-control-file.patch
# Description N/A
Patch14:        add-options-for-dockerng.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/39762
Patch15:        fix-regression-in-file.get_managed-add-unit-tests.patch
# PATCH-FIX_OPENSUSE
Patch16:        translate-variable-arguments-if-they-contain-hidden-.patch
# PATCH-FIX_OPENSUSE
Patch17:        special-salt-minion.service-file-for-rhel7.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40266
Patch18:        adding-support-for-installing-patches-in-yum-dnf-exe.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40761
Patch19:        search-the-entire-cache_dir-because-storage-paths-ch.patch
# PATCH-FIX_OPENSUSE
Patch20:        fixing-beacons.list-integration-test-failure.patch
# PATCH-FIX_OPENSUSE (upstream coming soon)
Patch21:        fix-grain-for-os_family-on-suse-series.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41336
Patch22:        fix-setting-language-on-suse-systems.patch
Patch23:        fix-os_family-case-in-unittest.patch
# PATCH-FIX_OPENSUSE
Patch24:        fix-format-error-bsc-1043111.patch
# PATCH-FIX_OPENSUSE (only applied for RHEL6 and SLES11)
Patch25:        adding-salt-minion-watchdog-for-sysv-systems-rhel6-a.patch
# PATCH-FIX_OPENSUSE (only applied for RHEL6 and SLES11)
Patch26:        enables-salt-minion-watchdog-on-init.d-script-for-sy.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/42944
Patch27:        add-clean_id-function-to-salt.utils.verify.py.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/37
Patch28:        revert-we-don-t-have-python-systemd-so-notify-can-t-.patch
# PATCH-FIX_OPENSUSE https://bugzilla.suse.com/1051948
Patch29:        introducing-the-kubernetes-module.patch
# PATCH-FIX_OPENSUSE https://bugzilla.suse.com/1052264
Patch30:        list_pkgs-add-parameter-for-returned-attribute-selec.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43366
#                    https://github.com/saltstack/salt/pull/43646/
Patch31:        catching-error-when-pidfile-cannot-be-deleted.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43235
#                    https://github.com/saltstack/salt/pull/43724/
Patch32:        fix-for-delete_deployment-in-kubernetes-module.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43669
Patch33:        introduce-process_count_max-minion-configuration-par.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/commit/0976f8f7131975a1ae29b2724069a301a870a46d
#                    Missed follow-up commit
Patch34:        escape-the-os.sep.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/44005
Patch35:        bugfix-always-return-a-string-list-on-unknown-job-ta.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/44011
Patch36:        security-fixes-cve-2017-14695-and-cve-2017-14696.patch
# PATCH-FIX_OPENSUSE bsc#1060230
Patch37:        activate-all-beacons-sources-config-pillar-grains.patch
# PATCH-FIX_OPENSUSE bsc#1041993
Patch38:        removes-beacon-configuration-deprecation-warning-48.patch
# PATCH-FIX_OPENSUSE bsc#1068446
Patch39:        bugfix-the-logic-according-to-the-exact-described-pu.patch
# PATCH-FIX_OPENSUSE
Patch40:        avoid-excessive-syslogging-by-watchdog-cronjob-58.patch
# PATCH-FIX_OPENSUSE bsc#1071322
Patch41:        older-logrotate-need-su-directive.patch
# PATCH-FIX_OPENSUSE bsc#1065792
Patch42:        fix-bsc-1065792.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/45060
Patch43:        feat-add-grain-for-all-fqdns.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/44991
Patch44:        split-only-strings-if-they-are-such.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40894
Patch45:        fix-for-broken-jobs-jid-in-2016.11.4.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/45365
Patch46:        return-error-when-gid_from_name-and-group-does-not-e.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/38675
Patch47:        setvcpus-setmem-fix-return-value-parsing-issue-when-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41795
Patch48:        bugfix-use-utc-date.patch
# PATCH-FIX_OPENSUSE
Patch49:        allow-running-tests-on-python-2.6-systems.patch
# PATCH-FIX_OPENSUSE bsc#1068566
Patch50:        yumpkg-don-t-use-diff_attr-when-determining-install-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43039
Patch51:        catch-importerror-for-kubernetes.client-import.patch
# PATCH-FIX_OPENSUSE bsc#1074227
Patch52:        fix-state-files-with-unicode-bsc-1074227.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46104
Patch53:        suppress-missing-fields-typeerror-exception-by-m2cry.patch
# PATCH-FIX_OPENSUSE https://github.com/saltstack/salt/pull/46104
Patch54:        fix-x509-unit-test-to-run-on-2016.11.4-version.patch
# PATCH-FIX_OPENSUSE https://github.com/saltstack/salt/pull/46413
Patch55:        explore-module.run-response-to-catch-the-result-in-d.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46575
Patch56:        fix-decrease-loglevel-when-unable-to-resolve-addr.patch
# PATCH-FIX_OPENSUSE bsc#1085635
Patch57:        make-module-result-usable-in-states-module.run-bsc-1.patch
# PATCH-FIX_OPENSUSE bsc#1088423
Patch58:        disable-cron-logging-only-on-sles11-systems-not-on-r.patch
# PATCH-FIX_OPENSUSE bsc#1090271
Patch59:        add-rsyslog-rule-to-avoid-salt-minion-watcher-cron-l.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46635
Patch60:        fix-for-errno-0-resolver-error-0-no-error-bsc-108758.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41786
Patch61:        fix-regressions-from-not-calling-load_args_and_kwarg.patch
# PATCH-FIX_OPENSUSE bsc#1087342
Patch62:        backport-of-azurearm-from-salt-2018.3-to-opensuse-sa.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47149
Patch63:        strip-trailing-commas-on-linux-user-gecos-fields.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47270
Patch64:        initialize-__context__-retcode-for-functions-handled.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47232
Patch65:        fixed-usage-of-ipaddress.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47211
Patch66:        fix-for-ec2-rate-limit-failures.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47471
Patch67:        do-not-override-jid-on-returners-only-sending-back-t.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47638
Patch68:        add-all_versions-parameter-to-include-all-installed-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47765
Patch69:        prevent-zypper-from-parsing-repo-configuration-from-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47149
Patch70:        add-other-attribute-to-gecos-fields-to-avoid-inconsi.patch
# PATCH-FIX_OPENSUSE bsc#1057635
Patch71:        add-environment-variable-to-know-if-yum-is-invoked-f.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/42541
Patch72:        bugfix-state-file.line-warning-bsc-1093458-86.patch
# PATCH-FIX_OPENSUSE
Patch73:        add-custom-suse-capabilities-as-grains.patch
# PATCH-FIX_OPENSUSE bsc#1098394 backport of https://github.com/saltstack/salt/pull/47061
Patch74:        porting-fix-diffing-binary-files-in-file.get_diff-bs.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47405
Patch75:        fix-unboundlocalerror-in-file.get_diff.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/48294
Patch76:        fix-zypper.list_pkgs-to-be-aligned-with-pkg-state.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49277
Patch77:        prepend-current-directory-when-path-is-just-filename.patch
# PATCH-FIX_OPENSUSE bsc#1094960
Patch78:        backport-46867-string-arg-normalization-bsc-1094960.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49538
Patch79:        fix-for-suse-expanded-support-detection.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49532
Patch80:        fix-wrong-recurse-behavior-on-for-linux_acl.present-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50563
Patch81:        remove-arch-from-name-when-pkg.list_pkgs-is-called-w.patch
# PATCH-FIX_OPENSUSE bsc#1124290 backport of multiple commits from upstream
# https://github.com/openSUSE/salt/commit/539a25d48792e9c470722269880da73ef0a25cc7
Patch82:        fix-minion-arguments-assign-via-sysctl-bsc-1124290.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52527
Patch83:        calculate-fqdns-in-parallel-to-avoid-blockings-bsc-1.patch
# PATCH-FIX_OPENSUSE bsc#1131423 https://github.com/openSUSE/salt/pull/138
Patch84:        add-optimization_order-config-option-with-default-va.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52657
Patch85:        do-not-report-patches-as-installed-when-not-all-the-.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/114
Patch86:        fix-usermod-options-for-sle11-bsc-1117017-114.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52527
Patch87:        use-threadpool-from-multiprocessing.pool-to-avoid-le.patch
# PATCH-FIX_OPENSUSE bsc#1136250
Patch88:        avoid-syntax-error-on-yumpkg-module-running-on-pytho.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/53293
Patch89:        do-not-break-repo-files-with-multiple-line-values-on.patch
Patch90:        catch-sslerror-for-tls-1.2-bootstraps-with-res-rhel6.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/50197
Patch91:        backport-saltutil-state-module-to-2019.2-codebase-bs.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/b713d0b3031faadc17cd9cf09977ccc19e50bef7
Patch92:        add-new-custom-suse-capability-for-saltutil-state-mo.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58871
Patch93:        fix-cve-2020-25592-and-add-tests-bsc-1178319.patch


BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  logrotate
BuildRequires:  python
BuildRequires:  python-devel
# requirements/base.txt
%if 0%{?rhel}
BuildRequires:  python-jinja2
%else
BuildRequires:  python-Jinja2
%endif
BuildRequires:  python-futures >= 2.0
BuildRequires:  python-markupsafe
BuildRequires:  python-msgpack-python > 0.3
BuildRequires:  python-psutil
BuildRequires:  python-requests >= 1.0.0
BuildRequires:  python-tornado >= 4.2.1
BuildRequires:  python-yaml

# requirements/zeromq.txt
%if 0%{?suse_version} >= 1500
BuildRequires:       python2-M2Crypto
%else
BuildRequires:       python-pycrypto >= 2.6.1
%endif
BuildRequires:  python-pyzmq >= 2.2.0
%if %{with test}
# requirements/dev_python27.txt
BuildRequires:  python-boto >= 2.32.1
BuildRequires:  python-mock
BuildRequires:  python-moto >= 0.3.6
BuildRequires:  python-pip
BuildRequires:  python-salt-testing >= 2015.2.16
BuildRequires:  python-unittest2
BuildRequires:  python-xml
%endif
%if %{with builddocs}
BuildRequires:  python-sphinx
%endif
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif

Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd

%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
Requires(pre):  pwdutils
%endif

%if 0%{?suse_version}
Requires(pre):  dbus-1
%else
Requires(pre):  dbus
%endif

Requires:       procps
Requires:       logrotate
Requires:       python
#
%if ! 0%{?suse_version} > 1110
Requires:       python-certifi
%endif
# requirements/base.txt
%if 0%{?rhel}
Requires:       python-jinja2
Requires:       yum
%if 0%{?rhel} == 6
Requires:       yum-plugin-security
%endif
%else
Requires:       python-Jinja2
%endif
Requires:       python-futures >= 2.0
Requires:       python-markupsafe
%if 0%{?suse_version} >= 1500
Requires:       py26-compat-msgpack-python
Requires:       py26-compat-tornado
%else
Requires:       python-msgpack-python > 0.3
Requires:       python-tornado >= 4.2.1
%endif
Requires:       python-psutil
Requires:       python-requests >= 1.0.0
Requires:       python-backports.ssl_match_hostname
Requires:       python-yaml
%if 0%{?suse_version}
# required for zypper.py
Requires:       rpm-python
Requires(pre):  libzypp(plugin:system) >= 0
Requires:       zypp-plugin-python
# requirements/opt.txt (not all)
# Suggests:     python-MySQL-python  ## Disabled for now, originally Recommended
Suggests:       python-timelib
Suggests:       python-gnupg
# requirements/zeromq.txt
%endif
%if 0%{?suse_version} >= 1500
Requires:       python2-M2Crypto
%else
Requires:       python-pycrypto >= 2.6.1
%endif
Requires:       python-pyzmq >= 2.2.0
#
%if 0%{?suse_version}
# python-xml is part of python-base in all rhel versions
Requires:       python-xml
Suggests:       python-Mako
Recommends:     python-netaddr
%endif

%if %{with systemd}
BuildRequires:  systemd
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre): %insserv_prereq
%endif
%endif

%if %{with fish_completion}
%define fish_dir %{_datadir}/fish/
%define fish_completions_dir %{_datadir}/fish/completions/
%endif

%if %{with bash_completion}
%if 0%{?suse_version} >= 1140
BuildRequires:  bash-completion
%else
BuildRequires:  bash
%endif
%endif

%if %{with zsh_completion}
BuildRequires:  zsh
%endif

%if 0%{?rhel}
BuildRequires:  yum
%endif

# for salt user and /etc directory structure
BuildRequires:  salt-master
Requires(pre):  salt-master

%description
Python 2.6 compatible salt library used for thin generation.

%prep
%setup -q -n salt-%{version}
cp %{S:1} .
cp %{S:5} ./.travis.yml
%patch1 -p1

# Do not apply this patch on RHEL 6
%if 0%{?rhel} > 6 || 0%{?suse_version}
%patch2 -p1
%endif

%patch3 -p1
%patch4 -p1

# This is SUSE-only patch
%if 0%{?suse_version}
%patch5 -p1
%endif

%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%if 0%{?rhel} == 6 || 0%{?suse_version} == 1110
%patch25 -p1
%patch26 -p1
%patch40 -p1
%endif
%if 0%{?rhel} == 6
%patch58 -p1
%patch59 -p1
%endif
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1

%build
%{__python} setup.py --with-salt-version=%{version} --salt-transport=both build
cp ./build/lib/salt/_version.py ./salt

%if %{with docs} && %{without builddocs}
# extract docs from the tarball
mkdir -p doc/_build
pushd doc/_build/
tar xfv %{S:3}
popd
%endif

%if %{with docs} && %{with builddocs}
## documentation
cd doc && make html && rm _build/html/.buildinfo && rm _build/html/_images/proxy_minions.png && cd _build/html && chmod -R -x+X *
%endif

%install
%{__python} setup.py --salt-transport=both install --prefix=%{_prefix} --root=%{buildroot} --install-lib=%{compatdir}/

mkdir -p %{buildroot}/etc/salt/master.d
%if 0%{?suse_version} >= 1500
install -m 644 %{S:7} %{buildroot}/etc/salt/master.d/py26-compat-salt.conf
%else
install -m 644 %{S:6} %{buildroot}/etc/salt/master.d
%endif

rm -rf %{buildroot}/usr/bin
rm -rf %{buildroot}/usr/share/man
find %{buildroot}%{compatdir}/ -name "*.pyc" | xargs rm

%post
rm -f /var/cache/salt/master/thin/version

%files
%defattr(-,root,root,-)
%dir %{_datadir}/susemanager
%config /etc/salt/master.d/py26-compat-salt.conf

%{compatdir}
%doc LICENSE AUTHORS README.rst HACKING.rst README.SUSE

%if %{with docs}
%files doc
%defattr(-,root,root)
%doc doc/_build/html
%endif

%changelog
* Mon Nov  2 2020 Pablo Suárez Hernández <pablo.suarezhernandez@suse.com>
- Properly validate eauth credentials and tokens on SSH calls made by Salt API
  (bsc#1178319) (bsc#1178362) (bsc#1178361)
  (CVE-2020-25592) (CVE-2020-17490) (CVE-2020-16846)
- Added:
  * fix-cve-2020-25592-and-add-tests-bsc-1178319.patch
* Fri Apr 17 2020 Pablo Suárez Hernández <pablo.suarezhernandez@suse.com>
- Do not make py26-compat-salt to require python-tornado on SLE15 (all SPs)
* Thu Mar 26 2020 Pablo Suárez Hernández <pablo.suarezhernandez@suse.com>
- Backport saltutil state module to 2016.11 codebase (bsc#1167556)
- Add new custom SUSE capability for saltutil state module
- Added:
  * backport-saltutil-state-module-to-2019.2-codebase-bs.patch
  * add-new-custom-suse-capability-for-saltutil-state-mo.patch
* Mon Jan 13 2020 Pablo Suárez Hernández <pablo.suarezhernandez@suse.com>
- Replace pycrypto with M2Crypto as dependency for SLE15+ (bsc#1165425)
* Thu Sep  5 2019 Pablo Suárez Hernández <pablo.suarezhernandez@suse.com>
- Get tornado dependency from the system on SLE12 (bsc#1149409)
- Changed:
  * py26-compat-salt.conf
* Thu Aug 29 2019 Jochen Breuer <jbreuer@suse.de>
- Catch SSLError for TLS 1.2 bootstraps with RES/RHEL6 and SLE11 (bsc#1147126)
- Added:
  * catch-sslerror-for-tls-1.2-bootstraps-with-res-rhel6.patch
* Wed May 29 2019 psuarezhernandez@suse.com
- Do not break repo files with multiple line values on yumpkg (bsc#1135360)
- Added:
  * do-not-break-repo-files-with-multiple-line-values-on.patch
* Mon May 27 2019 psuarezhernandez@suse.com
- Avoid syntax error on yumpkg module running on Python 2.6 (bsc#1136250)
- Added:
  * avoid-syntax-error-on-yumpkg-module-running-on-pytho.patch
* Tue Apr 30 2019 psuarezhernandez@suse.com
- Use ThreadPool from multiprocessing.pool to avoid leakins
  when calculating FQDNs
- Added:
  * use-threadpool-from-multiprocessing.pool-to-avoid-le.patch
* Mon Apr 29 2019 mdinca <mdinca@suse.de>
- Fix usermod options for SLE11 (bsc#1117017)
- Added:
  * fix-usermod-options-for-sle11-bsc-1117017-114.patch
* Mon Apr 29 2019 mdinca <mdinca@suse.de>
- Do not report patches as installed on RHEL systems when not all
  the related packages are installed (bsc#1128061)
- Added:
  * do-not-report-patches-as-installed-when-not-all-the-.patch
* Fri Apr 26 2019 pablo.suarezhernandez@suse.com
- Do not include "ordereddict" and "singledispatch" on the thin
  for Python 2.6 systems.
* Thu Apr 25 2019 psuarezhernandez@suse.com
- Fix paths for py26-compat dependencies on SLE15 and newer
* Tue Apr 23 2019 mdinca <mdinca@suse.de>
- Port optimization_order config parameter (bsc#1131423)
- Added:
  * add-optimization_order-config-option-with-default-va.patch
* Tue Apr 23 2019 mdinca <mdinca@suse.de>
- Use special tornado and msgpack-python compat packages on sles15sp1
  and greater in py26-compat-salt.conf (bsc#1131423)
- Add missing py26 thin dependencies
- Calculate the "FQDNs" grains in parallel to avoid long blocking (bsc#1129079)
- Added:
  * calculate-fqdns-in-parallel-to-avoid-blockings-bsc-1.patch
* Wed Apr  3 2019 Jochen Breuer <jbreuer@suse.de>
- Fix minion arguments assign via sysctl (bsc#1124290)
- Added:
  * fix-minion-arguments-assign-via-sysctl-bsc-1124290.patch
* Fri Jan 11 2019 pablo.suarezhernandez@suse.com
- Remove arch from name when pkg.list_pkgs is called with 'attr' (bsc#1114029)
- Added:
  * remove-arch-from-name-when-pkg.list_pkgs-is-called-w.patch
* Fri Oct 26 2018 pablo.suarezhernandez@suse.com
- Update Salt version to 2016.11.10
- Fix remote command execution and incorrect access control
  when using salt-api. (bsc#1113699) (CVE-2018-15751)
- Fix Directory traversal vulnerability when using salt-api.
  Allows an attacker to determine what files exist on
  a server when querying /run or /events. (bsc#1113698) (CVE-2018-15750)
- Modified:
  * adding-support-for-installing-patches-in-yum-dnf-exe.patch
  * security-fixes-cve-2017-14695-and-cve-2017-14696.patch
  * fix-setting-language-on-suse-systems.patch
  * fix-zypper.list_pkgs-to-be-aligned-with-pkg-state.patch
  * yumpkg-don-t-use-diff_attr-when-determining-install-.patch
  * fix-for-broken-jobs-jid-in-2016.11.4.patch
  * suppress-missing-fields-typeerror-exception-by-m2cry.patch
  * bugfix-the-logic-according-to-the-exact-described-pu.patch
  * backport-of-azurearm-from-salt-2018.3-to-opensuse-sa.patch
  * backport-46867-string-arg-normalization-bsc-1094960.patch
  * list_pkgs-add-parameter-for-returned-attribute-selec.patch
  * catching-error-when-pidfile-cannot-be-deleted.patch
  * fix-regressions-from-not-calling-load_args_and_kwarg.patch
  * fix-for-errno-0-resolver-error-0-no-error-bsc-108758.patch
  * fix-state-files-with-unicode-bsc-1074227.patch
  * fix-grain-for-os_family-on-suse-series.patch
  * add-other-attribute-to-gecos-fields-to-avoid-inconsi.patch
  * return-error-when-gid_from_name-and-group-does-not-e.patch
  * initialize-__context__-retcode-for-functions-handled.patch
  * feat-add-grain-for-all-fqdns.patch
  * add-clean_id-function-to-salt.utils.verify.py.patch
  * do-not-override-jid-on-returners-only-sending-back-t.patch
- Removed:
  * notify-systemd-synchronously-bsc-1053376.patch
  * use-home-to-get-the-user-home-directory-instead-usin.patch
  * rest_cherrypy-remove-sleep-call.patch
  * clean-up-change-attribute-from-interface-dict.patch
  * add-unit-test-for-skip-false-values-from-preferred_i.patch
  * revert-fix-augeas-module-so-shlex-doesn-t-strip-quot.patch
  * enable-with-salt-version-parameter-for-setup.py-scri.patch
  * multiprocessing-minion-option-documentation-fixes.patch
  * bugfix-jobs-scheduled-to-run-at-a-future-time-stay-p.patch
  * use-correct-grain-constants-for-timezone.patch
  * update-return-data-before-calling-returners.patch
  * bugfix-unable-to-use-127-as-hostname.patch
  * fixed-issue-with-parsing-of-master-minion-returns-wh.patch
* Mon Sep 17 2018 pablo.suarezhernandez@suse.com
- Fix wrong recurse behavior on for linux_acl.present (bsc#1106164)
- Adding backport for string arg normalization and fix for SUSE ES os
  grain detection (bsc#1094960)
- Added:
  * fix-wrong-recurse-behavior-on-for-linux_acl.present-.patch
  * fix-for-suse-expanded-support-detection.patch
  * backport-46867-string-arg-normalization-bsc-1094960.patch
* Wed Aug 29 2018 mc@suse.de
- Prepend current directory when path is just filename (bsc#1095942)
- Added:
  * prepend-current-directory-when-path-is-just-filename.patch
* Mon Jun 25 2018 mc@suse.de
- Handle packages with multiple version properly with zypper (bsc#1096514)
- Added:
  * fix-zypper.list_pkgs-to-be-aligned-with-pkg-state.patch
- Modified:
  * add-custom-suse-capabilities-as-grains.patch
* Mon Jun 25 2018 pablo.suarezhernandez@suse.com
- Fix file.get_diff regression in 2018.3 (bsc#1098394)
- Fix file.managed binary file utf8 error (bsc#1098394)
- Added:
  * porting-fix-diffing-binary-files-in-file.get_diff-bs.patch
  * fix-unboundlocalerror-in-file.get_diff.patch
* Thu Jun 21 2018 pablo.suarezhernandez@suse.com
- Add custom SUSE capabilities as Grains (bsc#1089526)
- Added:
  * add-custom-suse-capabilities-as-grains.patch
* Wed Jun 20 2018 pablo.suarezhernandez@suse.com
- Bugfix: state file.line warning (bsc#1093458)
- Enable '--with-salt-version' parameter for setup.py script
- Added:
  * enable-with-salt-version-parameter-for-setup.py-scri.patch
  * bugfix-state-file.line-warning-bsc-1093458-86.patch
* Fri Jun  8 2018 pablo.suarezhernandez@suse.com
- Add environment variable to know if yum is invoked from Salt (bsc#1057635)
- Added:
  * add-environment-variable-to-know-if-yum-is-invoked-f.patch
* Tue May 29 2018 jbreuer@suse.de
- Fix usage of salt.utils.which, that broke file.managed (bsc#1094546)
- Modified:
  * backport-of-azurearm-from-salt-2018.3-to-opensuse-sa.patch
* Fri May 25 2018 mc@suse.de
- require ssl_match_hostname module (bsc#1094661)
* Wed May 23 2018 pablo.suarezhernandez@suse.com
- Add 'other' attribute to GECOS fields to avoid inconsistencies with chfn
- Prevent zypper from parsing repo configuration from not .repo files (bsc#1094055)
- Collect all versions of installed packages on SUSE and RHEL systems (bsc#1089526)
- Update to saltstack:products
- Added:
  * add-all_versions-parameter-to-include-all-installed-.patch
  * prevent-zypper-from-parsing-repo-configuration-from-.patch
  * fixed-usage-of-ipaddress.patch
  * do-not-override-jid-on-returners-only-sending-back-t.patch
  * fix-for-ec2-rate-limit-failures.patch
  * update-return-data-before-calling-returners.patch
  * add-other-attribute-to-gecos-fields-to-avoid-inconsi.patch
* Wed Apr 25 2018 pablo.suarezhernandez@suse.com
- Fix minion scheduler to return a 'retcode' attribute (bsc#1089112)
- Added:
  * initialize-__context__-retcode-for-functions-handled.patch
* Sun Apr 22 2018 jbreuer@suse.de
- Fix for logging during network interface querying (bsc#1087581)
- Changed:
  * fix-for-errno-0-resolver-error-0-no-error-bsc-108758.patch
* Wed Apr 18 2018 pablo.suarezhernandez@suse.com
- Strip trailing commas on Linux user's GECOS fields (bsc#1089362)
- Added:
  * strip-trailing-commas-on-linux-user-gecos-fields.patch
* Tue Apr 17 2018 jbreuer@suse.de
- Backport of AzureARM from Salt 2018.3 to Salt 2016.11.4
  (bsc#1087342)
- Renamed patch to match the naming scheme
- Added:
  * backport-of-azurearm-from-salt-2018.3-to-opensuse-sa.patch
- Renamed:
  * disable-cron-logging-only-on-SLES11-systems-not-on-R.patch
  => disable-cron-logging-only-on-sles11-systems-not-on-r.patch
* Fri Apr 13 2018 bmaryniuk@suse.com
- Fix salt-api fails to return job ids (bsc#1087365)
- Changed:
  * fix-for-errno-0-resolver-error-0-no-error-bsc-108758.patch
- Added:
  * fix-regressions-from-not-calling-load_args_and_kwarg.patch
* Mon Apr  9 2018 jbreuer@suse.de
- Fix for [Errno 0] Resolver Error 0 (no error) (bsc#108758)
- Added:
  * fix-for-errno-0-resolver-error-0-no-error-bsc-108758.patch
* Fri Apr  6 2018 mc@suse.com
- package config for salt-master to generate py26 namespace in thin
* Fri Apr  6 2018 pablo.suarezhernandez@suse.com
- Add rsyslog rule to avoid salt-minion-watcher cron logs
  on RHEL6 (bsc#1090271)
- Added:
  * add-rsyslog-rule-to-avoid-salt-minion-watcher-cron-l.patch
* Fri Apr  6 2018 mantel@suse.de
- RHEL6 is using anacron, so logging cannot be disabled by starting
  entry with "-". Use only on SLES11 and cleanup RHEL6 systems that
  might already be affected by previous update (bsc#1088423)
- Added:
  * disable-cron-logging-only-on-SLES11-systems-not-on-R.patch
* Wed Mar 21 2018 mihai.dinca@suse.com
- Make module result usable in states module.run (bsc#1085635)
- Added:
  * make-module-result-usable-in-states-module.run-bsc-1.patch
* Wed Mar 21 2018 mihai.dinca@suse.com
- Fix Augeas module "stripped quotes" issue (bsc#1079398)
- Added:
  * revert-fix-augeas-module-so-shlex-doesn-t-strip-quot.patch
* Tue Mar 20 2018 michele.bologna@suse.com
- Fix logging with FQDNs
- Added:
  * fix-decrease-loglevel-when-unable-to-resolve-addr.patch
* Tue Mar 13 2018 mc@suse.com
- created a python 2.6 compatible salt library used for thin generation
* Wed Mar  7 2018 pablo.suarezhernandez@suse.com
- Explore 'module.run' state module output in depth to catch the
  "result" properly.
- Added:
  * explore-module.run-response-to-catch-the-result-in-d.patch
* Thu Feb 22 2018 pablo.suarezhernandez@suse.com
- Fix x509 unit test to run on 2016.11.4 version.
- Added:
  * fix-x509-unit-test-to-run-on-2016.11.4-version.patch
* Wed Feb 21 2018 bmaryniuk@suse.com
- Fix TypeError, thrown by M2Crypto on missing fields (bsc#1072973)
- Added:
  * suppress-missing-fields-typeerror-exception-by-m2cry.patch
* Fri Feb  9 2018 jbreuer@suse.de
- Added bsc#1068446 reference for bugfix-the-logic-according-to-the-exact-described-pu.patch
  in old changelog entry.
- Removed empty bsc entry for avoid-excessive-syslogging-by-watchdog-cronjob-58.patch
  This issue had no Bugzilla ticket.
* Wed Feb  7 2018 jbreuer@suse.de
- Fix state files with unicode (bsc#1074227)
- Added:
  * fix-state-files-with-unicode-bsc-1074227.patch
* Tue Jan 30 2018 pablo.suarezhernandez@suse.com
- catch ImportError for kubernetes.client import (bsc#1078001)
- Added:
  * catch-importerror-for-kubernetes.client-import.patch
* Mon Jan 29 2018 jbreuer@suse.de
- Fix epoch handling for Rhel 6 and 7
- Added:
  * yumpkg-don-t-use-diff_attr-when-determining-install-.patch
- Removed:
  * fix-for-wrong-version-processing.patch
* Tue Jan 23 2018 pablo.suarezhernandez@suse.com
- Allow Salt tests to run on Python 2.6 systems.
- Added:
  * allow-running-tests-on-python-2.6-systems.patch
* Tue Jan 23 2018 pablo.suarezhernandez@suse.com
- Fix zypper module to return UTC dates on 'pkg.list_downloaded'.
- Added:
  * bugfix-use-utc-date.patch
* Thu Jan 18 2018 bmaryniuk@suse.com
- Fix return value parsing when calling vm_state (bsc#1073618)
- Added:
  * setvcpus-setmem-fix-return-value-parsing-issue-when-.patch
* Wed Jan 17 2018 pablo.suarezhernandez@suse.com
- Fix 'user.present' when 'gid_from_name' is set but group
  does not exist.
- Added:
  * return-error-when-gid_from_name-and-group-does-not-e.patch
* Tue Jan 16 2018 pablo.suarezhernandez@suse.com
- Split only strings, if they are such (bsc#1072218)
- Fix for broken /jobs/<jid> in 2016.11.4
- Added:
  * fix-for-broken-jobs-jid-in-2016.11.4.patch
  * split-only-strings-if-they-are-such.patch
* Tue Jan  9 2018 pablo.suarezhernandez@suse.com
- Feat: add grain for all FQDNs (bsc#1063419)
- Fix "No service execution module loaded" issue (bsc#1065792)
- Added:
  * feat-add-grain-for-all-fqdns.patch
  * fix-bsc-1065792.patch
- Removed:
  * add-fqdns-grain.patch
* Wed Jan  3 2018 jbreuer@suse.de
- Removed unnecessary logging on shutdown (bsc#1050003)
  * Changed:
    catching-error-when-pidfile-cannot-be-deleted
* Wed Dec 27 2017 michele.bologna@suse.com
- Add grain for retrieving FQDNs (bsc#1063419)
  * Added:
    add-fqdns-grain.patch
* Mon Dec 11 2017 jbreuer@suse.de
- Older logrotate need su directive (bsc#1071322)
  * Added:
    older-logrotate-need-su-directive.patch
* Mon Dec 11 2017 jbreuer@suse.de
- Fix for wrong version processing during yum pkg install (bsc#1068566)
  * Added:
    fix-for-wrong-version-processing.patch
* Thu Dec  7 2017 mc@suse.com
- avoid excessive syslogging by watchdog cronjob
  * Added:
    avoid-excessive-syslogging-by-watchdog-cronjob-58.patch
- check pillar: fix the logic according to the exact described
  purpose of the function (bsc#1068446)
  * Added:
    bugfix-the-logic-according-to-the-exact-described-pu.patch
* Wed Oct 25 2017 jcavalheiro@suse.com
- Removed deprecation warning for beacon configuration using
  dictionaries (bsc#1041993)
- Added:
  * removes-beacon-configuration-deprecation-warning-48.patch
* Thu Oct 19 2017 bmaryniuk@suse.com
- Fixed beacons failure when pillar-based suppressing config-based.
  (bsc#1060230)
- Added:
  * activate-all-beacons-sources-config-pillar-grains.patch
* Wed Oct 11 2017 jbreuer@suse.de
- Re-added previously removed unit-test for bsc#1050003
- Changed:
  * catching-error-when-pidfile-cannot-be-deleted.patch
* Wed Oct 11 2017 bmaryniuk@suse.com
- Fixes for CVE-2017-14695 and CVE-2017-14696 (bsc#1062462)
- Added:
  * security-fixes-cve-2017-14695-and-cve-2017-14696.patch
* Tue Oct 10 2017 bmaryniuk@suse.com
- Add missing follow-up for CVE-2017-12791 (bsc#1053955)
- Fixed salt target-type field returns "String" for existing jids
  but an empty "Array" for non existing jids. (issue#1711)
- Added:
  * bugfix-always-return-a-string-list-on-unknown-job-ta.patch
  * escape-the-os.sep.patch
* Mon Oct  9 2017 bmaryniuk@suse.com
- Fixed minion resource exhaustion when many functions are being
  executed in parallel (bsc#1059758)
- Changed:
  * catching-error-when-pidfile-cannot-be-deleted.patch
- Added:
  * introduce-process_count_max-minion-configuration-par.patch
  * multiprocessing-minion-option-documentation-fixes.patch
  * revert-we-don-t-have-python-systemd-so-notify-can-t-.patch
- Removed:
  * revert-we-don-t-have-python-systemd-so-notify-can-t-work.patch
* Thu Oct  5 2017 pablo.suarezhernandez@suse.com
- Remove 'TasksTask' attribute from salt-master.service in older
  versions of systemd (bsc#985112)
* Wed Sep 27 2017 jbreuer@suse.de
- Fix for delete_deployment in Kubernetes module (bsc#1059291)
- Added:
  * fix-for-delete_deployment-in-kubernetes-module.patch
* Mon Sep 18 2017 jbreuer@suse.de
- Catching error when PIDfile cannot be deleted (bsc#1050003)
- Added:
  * catching-error-when-pidfile-cannot-be-deleted.patch
* Tue Sep 12 2017 pablo.suarezhernandez@suse.com
- Use $HOME to get the user home directory instead using '~' char (bsc#1042749)
- Added:
  * use-home-to-get-the-user-home-directory-instead-usin.patch
* Fri Sep  8 2017 jbreuer@suse.de
- Fixed patches for Kubernetes and YUM modules
- Updated:
  * list_pkgs-add-parameter-for-returned-attribute-selec.patch
  * introducing-the-kubernetes-module.patch
* Tue Sep  5 2017 jbreuer@suse.de
- Add patches to salt to support SUSE Manager scalability features
  (bsc#1052264)
- Added:
  * list_pkgs-add-parameter-for-returned-attribute-selec.patch
* Thu Aug 31 2017 jbreuer@suse.de
- Introducing the kubernetes module (bsc#1051948)
- Added:
  * introducing-the-kubernetes-module.patch
* Wed Aug 30 2017 jrenner@suse.com
- Revert "We don't have python-systemd, so notify can't work"
- Added:
  * revert-we-don-t-have-python-systemd-so-notify-can-t-work.patch
* Wed Aug 23 2017 brejoc@gmail.com
- Notify systemd synchronously via NOTIFY_SOCKET (bsc#1053376)
- Added:
  * notify-systemd-synchronously-bsc-1053376.patch
* Wed Aug 16 2017 pablo.suarezhernandez@suse.com
- Add clean_id function to salt.utils.verify.py
  (CVE-2017-12791, bsc#1053955)
- Added:
  * add-clean_id-function-to-salt.utils.verify.py.patch
* Mon Jul 17 2017 bmaryniuk@suse.com
- Added bugfix when jobs scheduled to run at a future time stay
  pending for Salt minions (bsc#1036125)
- Added:
  * bugfix-jobs-scheduled-to-run-at-a-future-time-stay-p.patch
* Tue Jun 20 2017 pablo.suarezhernandez@suse.com
- Adding procps as dependency. This provides "ps" and "pgrep" utils
  which are called from different Salt modules and also from new
  salt-minion watchdog.
* Thu Jun  8 2017 pablo.suarezhernandez@suse.com
- Adding a salt-minion watchdog for RHEL6 and SLES11 systems (sysV)
  to restart salt-minion in case of crashes during upgrade.
- Added:
  * adding-salt-minion-watchdog-for-sysv-systems-rhel6-a.patch
  * enables-salt-minion-watchdog-on-init.d-script-for-sy.patch
* Wed Jun  7 2017 mc@suse.com
- fix format error (bsc#1043111)
* Wed Jun  7 2017 mc@suse.com
- fix ownership for whole master cache directory (bsc#1035914)
* Tue Jun  6 2017 bmaryniuk@suse.com
- Bugfix: clean up `change` attribute from interface dict (upstream)
  Issue: https://github.com/saltstack/salt/issues/41461
  PR: 1. https://github.com/saltstack/salt/pull/41487
    2. https://github.com/saltstack/salt/pull/41533
  Added:
  * clean-up-change-attribute-from-interface-dict.patch
* Mon May 29 2017 bmaryniuk@suse.com
- Disable 3rd party runtime packages to be explicitly recommended.
  (bsc#1040886)
* Mon May 22 2017 bmaryniuk@suse.com
- Bugfix: orchestrate and batches returns false failed information
  https://github.com/saltstack/salt/issues/40635
  Added:
  * fixed-issue-with-parsing-of-master-minion-returns-wh.patch
* Sun May 21 2017 mc@suse.com
- speed-up cherrypy by removing sleep call
* Fri May 19 2017 mc@suse.com
- wrong os_family grains on SUSE - fix unittests (bsc#1038855)
* Thu May 18 2017 mc@suse.com
- fix setting the language on SUSE systems (bsc#1038855)
* Wed May 17 2017 bmaryniuk@suse.com
- Documentation refresh to 2016.11.4
* Wed May 17 2017 bmaryniuk@suse.com
- Update to 2016.11.4
  See https://docs.saltstack.com/en/develop/topics/releases/2016.11.4.html
  See https://docs.saltstack.com/en/develop/topics/releases/2016.11.3.html
  See https://docs.saltstack.com/en/develop/topics/releases/2016.11.2.html
  See https://docs.saltstack.com/en/develop/topics/releases/2016.11.1.html
  for full changelog
- Use SUSE specific salt-api.service (bsc#1039370)
- Bugfix: wrong os_family grains on SUSE (bsc#1038855)
- Bugfix: unable to use hostname for minion ID as '127' (upstream)
- Fix core grains constants for timezone (bsc#1032931)
- Add unit test for a skip false values from preferred IPs
  upstream patch
- Adding "yum-plugin-security" as required for RHEL 6
- Minor fixes on new pkg.list_downloaded
- Listing all type of advisory patches for Yum module
- Prevents zero length error on Python 2.6
- Fixes zypper test error after backporting
- raet protocol is no longer supported (bsc#1020831)
- Fix: move SSH data to the new home (bsc#1027722)
- Fix: /var/log/salt/minion fails logrotate (bsc#1030009)
- Fix: Result of master_tops extension is mutually overwritten
  (bsc#1030073)
- Allows to set 'timeout' and 'gather_job_timeout' via kwargs
- Allows to set custom timeouts for 'manage.up' and 'manage.status'
- Use salt's ordereddict for comparison (fixes failing tests)
- add special salt-minion.service file for RES7
- fix scripts for salt-proxy
- define with systemd for fedora and rhel >= 7 (bsc#1027240)
- add openscap module
- file.get_managed regression fix (upstream issues #39762)
- fix translate variable arguments if they contain hidden keywords
  (bsc#1025896)
- fix service handling for openSUSE
- added unit test for dockerng.sls_build dryrun
- added dryrun to dockerng.sls_build
- update dockerng minimal version requirements
- fix format error in error parsing
- keep fix for migrating salt home directory (bsc#1022562)
- Fix  salt pkg.latest raises exception if package is
  not available (bsc#1012999)
- Fix timezone: should be always in UTC (bsc#1017078)
- Fix timezone handling for rpm installtime (bsc#1017078)
- Increasing timeouts for running integrations tests
- Add buildargs option to dockerng.build module
- Disable custom rosters for Salt SSH via Salt API (bsc#1011800)
  More: https://github.com/saltstack/salt/pull/38596
- Fix error when missing ssh-option parameter
- readd yum notify plugin
- all kwargs to dockerng.create to provide all features to sls_build
  as well
- rename patches to get rid of the prefix numbers
- Added:
  * bugfix-unable-to-use-127-as-hostname.patch
  * fix-grain-for-os_family-on-suse-series.patch
  * use-correct-grain-constants-for-timezone.patch
  * search-the-entire-cache_dir-because-storage-paths-ch.patch
  * add-unit-test-for-skip-false-values-from-preferred_i.patch
  * add-a-salt-minion-service-control-file.patch
  * add-options-for-dockerng.patch
  * add-zypp-notify-plugin.patch
  * fixing-beacons.list-integration-test-failure.patch
  * fix-regression-in-file.get_managed-add-unit-tests.patch
  * fix-salt-summary-to-count-not-responding-minions-cor.patch
  * special-salt-minion.service-file-for-rhel7.patch
  * translate-variable-arguments-if-they-contain-hidden-.patch
- Renamed:
  * 0001-tserong-suse.com-We-don-t-have-python-systemd-so-not.patch
  => tserong-suse.com-we-don-t-have-python-systemd-so-not.patch
  * 0002-Run-salt-master-as-dedicated-salt-user.patch
  => run-salt-master-as-dedicated-salt-user.patch
  * 0003-Check-if-byte-strings-are-properly-encoded-in-UTF-8.patch
  => check-if-byte-strings-are-properly-encoded-in-utf-8.patch
  * 0004-do-not-generate-a-date-in-a-comment-to-prevent-rebui.patch
  => do-not-generate-a-date-in-a-comment-to-prevent-rebui.patch
  * 0009-Add-YUM-plugin.patch 0027-Add-YUM-plugin.patch
  => add-yum-plugin.patch
  * 0012-Run-salt-api-as-user-salt-bsc-990029.patch
  => run-salt-api-as-user-salt-bsc-990029.patch
  * 0020-Setting-up-OS-grains-for-SLES-Expanded-Support-SUSE-.patch
  => setting-up-os-grains-for-sles-expanded-support-suse-.patch
  * 0022-Change-travis-configuration-file-to-use-salt-toaster.patch
  => change-travis-configuration-file-to-use-salt-toaster.patch
  * 0036-Avoid-failures-on-SLES-12-SP2-because-of-new-systemd.patch
  => avoid-failures-on-sles-12-sp2-because-of-new-systemd.patch
  * 0042-Salt-ssh-ssh-option-param.patch
  => add-ssh-option-to-salt-ssh.patch
  * 0057-Adding-support-for-installing-patches-in-yum-dnf-exe.patch
  => adding-support-for-installing-patches-in-yum-dnf-exe.patch
- Removed:
  * 0005-Use-SHA256-hash-type-by-default.patch
  * 0006-Create-salt-proxy-instantiated-service-file.patch
  * 0007-Add-SUSE-Manager-plugin.patch
  * 0008-Fix-pkgrepo.managed-gpgkey-argument-bsc-979448.patch
  * 0009-Rewrite-minion-ID-generator-bsc-967803.patch
  * 0010-snapper-execution-module.patch
  * 0011-Fix-module-import-being-Py3-and-P2.6-compatible.patch
  * 0013-Bugfix-prevent-crash-if-python-dbus-module-is-instal.patch
  * 0014-Fix-some-unittests.patch
  * 0015-Check-for-single-quote-before-splitting-on-single-qu.patch
  * 0016-Unit-test-fixes-for-2015.8.7.patch
  * 0017-Fix-snapper_test-for-python26.patch
  * 0018-Integration-tests-fixes-for-2015.8.7.patch
  * 0019-Generate-Salt-Thin-with-configured-extra-modules.patch
  * 0021-acl.delfacl-fix-position-of-X-option-to-setfacl.patch
  * 0023-Adding-dist-upgrade-support-to-zypper-module.patch
  * 0024-Fix-open-ssh-bsc-1004723-upstream-issue-36966.patch
  * 0025-Including-resolver-params-for-Zypper-debug-solver.patch
  * 0026-fix-status-handling-in-sysv-init-scripts.patch
  * 0028-change-TIMEZONE-on-SUSE-systems-bsc-1008933.patch
  * 0029-Do-not-include-gpg-pubkey-packages-filtering-by-thei.patch
  * 0030-Extract-archive-into-existing-directory-add-overwrit.patch
  * 0031-Port-rsync-state-from-2016.3.patch
  * 0032-Support-remote-port-forwarding-with-salt-ssh.patch
  * 0033-Add-master_tops-support-in-salt-ssh.patch
  * 0034-Fix-pkg.latest_version-when-latest-already-installed.patch
  * 0035-salt-api-service-must-be-from-type-simple.patch
  * 0037-salt-minion-service-back-to-type-simple.patch
  * 0038-Successfully-exit-of-salt-api-child-processes-when-S.patch
  * 0039-Re-introducing-KillMode-process-for-salt-minion-syst.patch
  * 0040-Adding-Restart-on-failure-for-salt-minion-systemd-se.patch
  * 0041-add-try-restart-to-fix-autorestarting-on-SUSE-system.patch
  * 0043-Fixes-wrong-enabled-opts-for-yumnotify-plugin.patch
  * 0044-Add-general-sanitisers.patch
  * 0045-Fix-timezone-handling-for-rpm-installtime-bsc-101707.patch
  * 0046-Snapper-module-improvements.patch
  * 0047-Fix-issue-with-cp.push-36136.patch
  * 0048-Prevents-OSError-exception-in-case-path-doesn-t-exis.patch
  * 0049-OpenSCAP-module.patch
  * 0050-Fix-service-state-returning-stacktrace-bsc-1027044.patch
  * 0051-Allows-to-set-timeout-and-gather_job_timeout-via-kwa.patch
  * 0052-Don-t-send-passwords-after-shim-delimiter-is-found-3.patch
  * 0053-fix-race-condition-on-cache-directory-creation.patch
  * 0054-Merge-output-from-master_tops.patch
  * 0055-Adding-downloadonly-support-to-yum-dnf-module.patch
  * 0056-Makes-sure-gather_job_timeout-is-an-integer.patch
  * 0058-Adds-custom-timeout-and-gather_job_timeout-to-local_.patch
  * 0059-Add-SHELL-env-var-for-the-salt-api.service.patch
  * 0060-Fix-logrotate-for-minion-bsc-1030009-21.patch
* Thu May 11 2017 bmaryniuk@suse.com
- Bugfix: datetime should be returned always in UTC
- Added:
  * 0063-Bugfix-datetime-should-be-returned-always-in-UTC.patch
* Mon May  8 2017 bmaryniuk@suse.com
- Bugfix: scheduled state may cause crash while deserialising data
    on infinite recursion. (bsc#1036125)
- Added:
  * 0062-Bugfix-deserialising-crashes-in-the-recursive-loop-b.patch
* Tue May  2 2017 pablo.suarezhernandez@suse.com
- Enable yum to handle errata on RHEL 6: require yum-plugin-security
* Wed Apr 26 2017 pablo.suarezhernandez@suse.com
- Minor fixes on new pkg.list_downloaded
- Listing all type of advisory patches for Yum module
- Prevents zero length error on Python 2.6
- Fixes zypper test error after backporting
- Added:
  * 0061-Search-the-entire-CACHE_DIR-because-storage-paths-ch.patch
- Modified:
  * 0057-Adding-support-for-installing-patches-in-yum-dnf-exe.patch
* Mon Apr 17 2017 pablo.suarezhernandez@suse.com
- Refactoring on Zypper and Yum execution and state modules to allow
  installation of patches/errata.
- Added:
  * 0057-Adding-support-for-installing-patches-in-yum-dnf-exe.patch
- Removed:
  * 0057-Allows-using-downloadonly-in-a-pkg.installed-state.patch
* Wed Apr 12 2017 bmaryniuk@suse.com
- Fix log rotation permission issue (bsc#1030009)
- Use pkg/suse/salt-api.service by this package
- Removed:
  * 0059-Set-salt-api-shell-env.patch
- Added:
  * 0059-Add-SHELL-env-var-for-the-salt-api.service.patch
  * 0060-Fix-logrotate-for-minion-bsc-1030009-21.patch
* Tue Apr 11 2017 malbu@suse.com
- Patch to set SHELL env variable for the salt-api.service.
  Needed for salt-ssh ProxyCommand to work properly.
- Added:
  * 0059-Set-salt-api-shell-env.patch
* Mon Apr 10 2017 pablo.suarezhernandez@suse.com
- Fixes 'timeout' and 'gather_job_timeout' kwargs parameters
  for 'local_batch' client
- Added:
  * 0058-Adds-custom-timeout-and-gather_job_timeout-to-local_.patch
* Fri Apr  7 2017 bmaryniuk@suse.com
- Add missing bootstrap script for Salt Cloud (bsc#1032452)
* Tue Apr  4 2017 bmaryniuk@suse.com
- Fix: add missing /var/cache/salt/cloud directory (bsc#1032213)
* Fri Mar 31 2017 bmaryniuk@suse.com
- Added test case for race conditions on cache directory creation
- Modified:
  * 0053-fix-race-condition-on-cache-directory-creation.patch
* Thu Mar 30 2017 pablo.suarezhernandez@suse.com
- Adding "pkg.install downloadonly=True" support to yum/dnf
  execution module
- Makes sure "gather_job_timeout" is an Integer
- Adding "pkg.downloaded" state and support for installing
  patches/erratas
- Added:
  * 0055-Adding-downloadonly-support-to-yum-dnf-module.patch
  * 0056-Makes-sure-gather_job_timeout-is-an-integer.patch
  * 0057-Allows-using-downloadonly-in-a-pkg.installed-state.patch
* Wed Mar 29 2017 bmaryniuk@suse.com
- Fix: merge master_tops output
* Wed Mar 29 2017 moio@suse.com
- Fix: race condition on cache directory creation
- Added:
  * 0053-fix-race-condition-on-cache-directory-creation.patch
* Fri Mar 24 2017 bmaryniuk@suse.com
- Cleanup salt user environment preparation (bsc#1027722)
* Wed Mar 22 2017 pkazmierczak@suse.com
- Don't send passwords after shim delimiter is found (bsc#1019386)
- Add:
  * 0052-Don-t-send-passwords-after-shim-delimiter-is-found-3.patch
* Thu Mar 16 2017 pablo.suarezhernandez@suse.com
- Allows to set 'timeout' and 'gather_job_timeout' via kwargs
- Allows to set custom timeouts for 'manage.up' and 'manage.status'
- Add:
  * 0051-Allows-to-set-timeout-and-gather_job_timeout-via-kwa.patch
* Tue Mar  7 2017 mihai.dinca@suse.com
- Update systemd module unit tests (Update patch 0050)
* Sun Mar  5 2017 mc@suse.com
- define with system for fedora and rhel 7  (bsc#1027240)
* Fri Mar  3 2017 mihai.dinca@suse.com
- Fix service state returning stacktrace (bsc#1027044)
- Add:
  * 0050-Fix-service-state-returning-stacktrace-bsc-1027044.patch
* Tue Feb 21 2017 mihai.dinca@suse.com
- Update OpenSCAP Module patch
* Fri Feb 17 2017 mihai.dinca@suse.com
- OpenSCAP Module
- Added:
  * 0049-OpenSCAP-module.patch
* Wed Feb 15 2017 pablo.suarezhernandez@suse.com
- Prevents 'OSError' exception in case certain job cache path
  doesn't exist (bsc#1023535)
- Added:
  * 0048-Prevents-OSError-exception-in-case-path-doesn-t-exis.patch
* Mon Feb 13 2017 mihai.dinca@suse.com
- Backport: Fix issue with cp.push (#36136)
- Add:
  * 0047-Fix-issue-with-cp.push-36136.patch
* Tue Feb  7 2017 bmaryniuk@suse.com
- Fix salt-minion update on RHEL (bsc#1022841)
* Mon Feb  6 2017 pablo.suarezhernandez@suse.com
- Adding new functions to Snapper execution module.
- Added:
  * snapper-module-improvements.patch
* Thu Jan 26 2017 bmaryniuk@suse.com
- Fix invalid chars allowed for data IDs (bsc#1011304)
  Fix timezone: should be always in UTC (bsc#1017078)
  Add:
  * 0044-Add-general-sanitisers.patch
  * 0045-Fix-timezone-handling-for-rpm-installtime-bsc-101707.patch
* Wed Jan 25 2017 pablo.suarezhernandez@suse.com
- Fixes wrong "enabled" opts for yumnotify plugin
  Add:
  * 0043-Fixes-wrong-enabled-opts-for-yumnotify-plugin.patch
* Mon Jan  2 2017 malbu@suse.com
- ssh-option parameter for salt-ssh command.
  Added:
  * 0042-Salt-ssh-ssh-option-param.patch
* Tue Dec 20 2016 mc@suse.de
- minion should pre-require salt
- do not restart salt-minion in the salt package
- add try-restart to sys-v init scripts
  Add:
  * 0041-add-try-restart-to-fix-autorestarting-on-SUSE-system.patch
* Tue Dec 20 2016 pablo.suarezhernandez@suse.com
- Adding "Restart=on-failure" for salt-minion systemd service
  Add:
  * 0040-Adding-Restart-on-failure-for-salt-minion-systemd-se.patch
* Mon Dec 19 2016 pablo.suarezhernandez@suse.com
- Re-introducing "KillMode=process" for salt-minion systemd service
  Add:
  * 0039-Re-introducing-KillMode-process-for-salt-minion-syst.patch
* Wed Dec 14 2016 mihai.dinca@suse.com
- Successfully exit of salt-api child processes when SIGTERM is received
  Add:
  * 0038-Successfully-exit-of-salt-api-child-processes-when-S.patch
* Wed Dec 14 2016 mihai.dinca@suse.com
- Add new patches:
  * 0034-Fix-pkg.latest_version-when-latest-already-installed.patch
  * 0035-salt-api-service-must-be-from-type-simple.patch
  * 0036-Avoid-failures-on-SLES-12-SP2-because-of-new-systemd.patch
  * 0037-salt-minion-service-back-to-type-simple.patch
* Fri Dec  9 2016 mihai.dinca@suse.com
- Update to 2015.8.12
- Fix possible information leak due to revoked keys still being used.
  (bsc#1012398, CVE-2016-9639)
- inherited patches
    0001-tserong-suse.com-We-don-t-have-python-systemd-so-not.patch
    0002-Run-salt-master-as-dedicated-salt-user.patch
    0003-Check-if-byte-strings-are-properly-encoded-in-UTF-8.patch
- renamed patches
    0026-do-not-generate-a-date-in-a-comment-to-prevent-rebui.patch
  - > 0004-do-not-generate-a-date-in-a-comment-to-prevent-rebui.patch
    0036-Use-SHA256-hash-type-by-default.patch
  - > 0005-Use-SHA256-hash-type-by-default.patch
    0046-Add-SUSE-Manager-plugin.patch
  - > 0007-Add-SUSE-Manager-plugin.patch
    0048-Create-salt-proxy-instantiated-service-file.patch
  - > 0006-Create-salt-proxy-instantiated-service-file.patch
    0053-Fix-pkgrepo.managed-gpgkey-argument-bsc-979448.patch
  - > 0008-Fix-pkgrepo.managed-gpgkey-argument-bsc-979448.patch
    0059-Rewrite-minion-ID-generator-bsc-967803.patch
  - > 0009-Rewrite-minion-ID-generator-bsc-967803.patch
    0061-snapper-execution-module.patch
  - > 0010-snapper-execution-module.patch
    0063-Fix-module-import-being-Py3-and-P2.6-compatible.patch
  - > 0011-Fix-module-import-being-Py3-and-P2.6-compatible.patch
    0064-Run-salt-api-as-user-salt-bsc-990029.patch
  - > 0012-Run-salt-api-as-user-salt-bsc-990029.patch
    0067-Bugfix-prevent-crash-if-python-dbus-module-is-instal.patch
  - > 0013-Bugfix-prevent-crash-if-python-dbus-module-is-instal.patch
    0070-Fix-some-unittests.patch
  - > 0014-Fix-some-unittests.patch
    0071-Check-for-single-quote-before-splitting-on-single-qu.patch
  - > 0015-Check-for-single-quote-before-splitting-on-single-qu.patch
    0072-Unit-test-fixes-for-2015.8.7.patch
  - > 0016-Unit-test-fixes-for-2015.8.7.patch
    0073-Fix-snapper_test-for-python26.patch
  - > 0017-Fix-snapper_test-for-python26.patch
    0074-Integration-tests-fixes-for-2015.8.7.patch
  - > 0018-Integration-tests-fixes-for-2015.8.7.patch
    0075-Generate-Salt-Thin-with-configured-extra-modules.patch
  - > 0019-Generate-Salt-Thin-with-configured-extra-modules.patch
    0076-Setting-up-OS-grains-for-SLES-Expanded-Support-SUSE-.patch
  - > 0020-Setting-up-OS-grains-for-SLES-Expanded-Support-SUSE-.patch
    0077-acl.delfacl-fix-position-of-X-option-to-setfacl.patch
  - > 0021-acl.delfacl-fix-position-of-X-option-to-setfacl.patch
    0078-Change-travis-configuration-file-to-use-salt-toaster.patch
  - > 0022-Change-travis-configuration-file-to-use-salt-toaster.patch
    0079-Adding-dist-upgrade-support-to-zypper-module.patch
  - > 0023-Adding-dist-upgrade-support-to-zypper-module.patch
    0080-Fix-open-ssh-bsc-1004723-upstream-issue-36966.patch
  - > 0024-Fix-open-ssh-bsc-1004723-upstream-issue-36966.patch
    0081-Including-resolver-params-for-Zypper-debug-solver.patch
  - > 0025-Including-resolver-params-for-Zypper-debug-solver.patch
    0082-fix-status-handling-in-sysv-init-scripts.patch
  - > 0026-fix-status-handling-in-sysv-init-scripts.patch
- new patches from upstream
    0027-Add-YUM-plugin.patch
    0028-change-TIMEZONE-on-SUSE-systems-bsc-1008933.patch (bsc#1008933)
    0029-Do-not-include-gpg-pubkey-packages-filtering-by-thei.patch
    0030-Extract-archive-into-existing-directory-add-overwrit.patch
    0031-Port-rsync-state-from-2016.3.patch
    0032-Support-remote-port-forwarding-with-salt-ssh.patch
    0033-Add-master_tops-support-in-salt-ssh.patch
- upstreamed patches
    0004-Fix-pkg.latest-prevent-crash-on-multiple-package-ins.patch
    0005-Fix-package-status-filtering-on-latest-version-and-i.patch
    0006-add_key-reject_key-do-not-crash-w-Permission-denied-.patch
    0007-Force-kill-websocket-s-child-processes-faster-than-d.patch
    0008-Fix-types-in-the-output-data-and-return-just-a-list-.patch
    0009-The-functions-in-the-state-module-that-return-a-retc.patch
    0010-add-handling-for-OEM-products.patch
    0011-improve-doc-for-list_pkgs.patch
    0012-implement-version_cmp-for-zypper.patch
    0013-pylint-changes.patch
    0014-Check-if-rpm-python-can-be-imported.patch
    0015-call-zypper-with-option-non-interactive-everywhere.patch
    0016-write-a-zypper-command-builder-function.patch
    0017-Fix-crash-with-scheduler-and-runners-31106.patch
    0018-unify-behavior-of-refresh.patch
    0019-add-refresh-option-to-more-functions.patch
    0020-simplify-checking-the-refresh-paramater.patch
    0021-do-not-change-kwargs-in-refresh-while-checking-a-val.patch
    0022-fix-argument-handling-for-pkg.download.patch
    0023-Initial-Zypper-Unit-Tests-and-bugfixes.patch
    0024-proper-checking-if-zypper-exit-codes-and-handling-of.patch
    0025-adapt-tests-to-new-zypper_check_result-output.patch
    0027-make-suse-check-consistent-with-rh_service.patch
    0028-fix-numerical-check-of-osrelease.patch
    0029-Make-use-of-checksum-configurable-defaults-to-MD5-SH.patch
    0030-Bugfix-on-SLE11-series-base-product-reported-as-addi.patch
    0031-Only-use-LONGSIZE-in-rpm.info-if-available.-Otherwis.patch
    0032-Add-error-check-when-retcode-is-0-but-stderr-is-pres.patch
    0033-fixing-init-system-dectection-on-sles-11-refs-31617.patch
    0034-Fix-git_pillar-race-condition.patch
    0035-Fix-the-always-false-behavior-on-checking-state.patch
    0037-Force-sort-the-RPM-output-to-ensure-latest-version-o.patch
    0038-fix-sorting-by-latest-version-when-called-with-an-at.patch
    0039-Prevent-metadata-download-when-getting-installed-pro.patch
    0040-Check-if-EOL-is-available-in-a-particular-product-bs.patch
    0041-Bugfix-salt-key-crashes-if-tries-to-generate-keys-to.patch
    0042-align-OS-grains-from-older-SLES-with-current-one-bsc.patch
    0043-Prevent-crash-if-pygit2-package-is-requesting-re-com.patch
    0044-Unblock-Zypper.-Modify-environment.patch
    0045-Bugfix-Restore-boolean-values-from-the-repo-configur.patch
    0047-Old-style-proxymodules-need-to-be-setup-earlier-in-m.patch
    0049-Prevent-several-minion-processes-on-the-same-machine.patch
    0050-checksum-validation-when-zypper-pkg.download.patch
    0051-unit-tests-for-rpm.checksum-and-zypper.download.patch
    0052-jobs.exit_success-allow-to-check-if-a-job-has-execut.patch
    0054-fix-groupadd-module-for-sles11-systems.patch
    0055-Backport-31164-and-31364-32474.patch
    0056-Move-log-message-from-INFO-to-DEBUG.patch
    0057-fix-salt-summary-to-count-not-responding-minions-cor.patch
    0058-Getting-the-os-grain-from-CPE_NAME-inside-etc-os-rel.patch
    0060-Bugfix-return-boolean-only-for-isbase-and-installed-.patch
    0062-Add-realpath-to-lvm.pvdisplay-and-use-it-in-vg_prese.patch
    0065-fix-beacon-list-to-include-all-beacons-being-process.patch
    0066-Fix-continuous-minion-restart-if-a-dependency-wasn-t.patch
    0068-Add-ignore_repo_failure-option-to-suppress-zypper-s-.patch
    0069-Remove-zypper-s-raise-exception-if-mod_repo-has-no-a.patch
* Mon Nov 28 2016 kkaempf@suse.com
- Splitted non-Linux and other external platform modules
  to 'salt-other' sub-package.
* Mon Nov 28 2016 kkaempf@suse.com
- Switch package group from System/Monitoring to System/Management
* Sun Nov  6 2016 mc@suse.com
- fix exist codes of sysv init script (bsc#999852)
  Add:
  * 0082-fix-status-handling-in-sysv-init-scripts.patch
* Mon Oct 31 2016 pablo.suarezhernandez@suse.com
- Including resolution parameters in the Zypper debug-solver call
  during a dry-run dist-upgrade.
  Add:
  * 0081-Including-resolver-params-for-Zypper-debug-solver.patch
* Tue Oct 25 2016 bmaryniuk@suse.com
- Fix Salt API crash via salt-ssh on empty roster (bsc#1004723)
  Add:
  * 0080-Fix-open-ssh-bsc-1004723-upstream-issue-36966.patch
* Wed Oct 19 2016 pablo.suarezhernandez@suse.com
- Adding 'dist-upgrade' support to zypper module (FATE#320559)
  Add:
  * 0079-Adding-dist-upgrade-support-to-zypper-module.patch
* Mon Oct 17 2016 mihai.dinca@suse.com
- Copy .travis.yml from git commit ea63e793567ba777e47dc766a4f88edfb037a02f
  Add:
  * travis.yml
- Change travis configuration file to use salt-toaster
  Add:
  * travis.yml
  * 0078-Change-travis-configuration-file-to-use-salt-toaster.patch
* Thu Oct 13 2016 mihai.dinca@suse.com
- acl.delfacl: fix position of -X option to setfacl (bsc#1004260)
  Add:
  * 0077-acl.delfacl-fix-position-of-X-option-to-setfacl.patch
* Tue Oct 11 2016 mc@suse.com
- fix generated shebang in scripts on SLES-ES 7 (bsc#1004047)
* Thu Oct  6 2016 mc@suse.de
- add update-documentation.sh to specfile
* Wed Oct  5 2016 mihai.dinca@suse.com
- Setting up OS grains for SLES-ES (SLES Expanded Support platform)
  Add:
  * 0076-Setting-up-OS-grains-for-SLES-Expanded-Support-SUSE-.patch
* Tue Oct  4 2016 Michele.Bologna@suse.com
- Move salt home directory to /var/lib/salt (bsc#1002529)
- Adjust permissions on home directory
- Adjust pre-install script to correctly move existing salt users' home directory
  salt user cannot write in his own home directory (/srv/salt) because
  it is owned by user `root`.
  This prevents salt from correctly save ssh known hosts in ~/.ssh/
  and breaks salt-ssh bootstrapping.
* Tue Sep 27 2016 bmaryniuk@suse.com
- Updated html.tar.bz2 documentation tarball.
- Generate Salt Thin with configured extra modules (bsc#990439)
  Add:
  * 0075-Generate-Salt-Thin-with-configured-extra-modules.patch
* Tue Sep 13 2016 pablo.suarezhernandez@suse.com
- Unit and integration tests fixes for 2015.8.7
  Add:
  * 0072-Unit-test-fixes-for-2015.8.7.patch
  * 0073-Fix-snapper_test-for-python26.patch
  * 0074-Integration-tests-fixes-for-2015.8.7.patch
* Fri Sep  2 2016 pablo.suarezhernandez@suse.com
- Prevent pkg.install failure for expired keys (bsc#996455)
  Add:
  * 0071-Check-for-single-quote-before-splitting-on-single-qu.patch
* Mon Aug 29 2016 bmaryniuk@suse.com
- Required D-Bus and generating machine ID
* Fri Aug 26 2016 mc@suse.de
- add a macro to check if the docs should be build or the static
  tarball should be used
* Wed Aug 24 2016 mihai.dinca@suse.com
- Fix a couple of failing unittests
  * 0070-Fix-some-unittests.patch
* Tue Aug 23 2016 bmaryniuk@suse.com
- Helper script for updating documentation tarball.
  Added:
  * update-documentation.sh
* Tue Aug 16 2016 mihai.dinca@suse.com
- Fix python-jinja2 requirements in rhel
* Tue Aug 16 2016 bmaryniuk@suse.com
- Fix pkg.installed refresh repo failure (bsc#993549)
  Fix salt.states.pkgrepo.management no change failure (bsc#990440)
  Add:
  * 0068-Add-ignore_repo_failure-option-to-suppress-zypper-s-.patch
  * 0069-Remove-zypper-s-raise-exception-if-mod_repo-has-no-a.patch
* Thu Aug 11 2016 bmaryniuk@suse.com
- Prevent snapper module crash on load if no DBus is
  available in the system (bsc#993039)
  Add:
  * 0067-Bugfix-prevent-crash-if-python-dbus-module-is-instal.patch
* Thu Aug 11 2016 bmaryniuk@suse.com
- Prevent continuous restart, if a dependency wasn't installed
  (bsc#991048)
  Add:
  * 0066-Fix-continuous-minion-restart-if-a-dependency-wasn-t.patch
* Wed Aug  3 2016 pablo.suarezhernandez@suse.com
- Fix beacon list to include all beacons being process
  Add:
  * 0065-fix-beacon-list-to-include-all-beacons-being-process.patch
* Fri Jul 29 2016 mc@suse.de
- Run salt-api as user salt like the master (bsc#990029)
  Add:
  * 0064-Run-salt-api-as-user-salt-bsc-990029.patch
* Fri Jul 22 2016 dmacvicar@suse.de
- Revert patch Minion ID generation (bsc#967803)
  Removes:
  * 0059-Rewrite-minion-ID-generator-bsc-967803.patch
* Wed Jul 20 2016 bmaryniuk@suse.com
- Fix broken inspector due to accidentally
  missed commit (bsc#989798)
  Add:
  * 0063-Fix-module-import-being-Py3-and-P2.6-compatible.patch
* Wed Jul 20 2016 bmaryniuk@suse.com
- Set always build salt-doc package.
* Tue Jul 19 2016 pablo.suarezhernandez@suse.com
- Bugfix: lvm.vg_present does not recognize PV with certain LVM
    filter settings (bsc#988506)
  Add:
  * 0062-Add-realpath-to-lvm.pvdisplay-and-use-it-in-vg_prese.patch
* Mon Jul 18 2016 pablo.suarezhernandez@suse.com
- Backport: Snapper module for Salt.
  Add:
  * 0061-snapper-execution-module.patch
* Fri Jul 15 2016 bmaryniuk@suse.com
- Bugfix: pkg.list_products on "registerrelease" and "productline"
    returns boolean.False if empty (bsc#989193, bsc#986019)
  Add:
  * 0060-Bugfix-return-boolean-only-for-isbase-and-installed-.patch
* Fri Jun 24 2016 bmaryniuk@suse.com
- Rewrite Minion ID generation (bsc#967803)
  Add:
  * 0059-Rewrite-minion-ID-generator-bsc-967803.patch
* Wed Jun 22 2016 pablo.suarezhernandez@suse.com
- Bugfix: Fixed behavior for SUSE OS grains (bsc#970669)
  Bugfix: Salt os_family does not detect SLES for SAP (bsc#983017)
  Add:
  * 0058-Getting-the-os-grain-from-CPE_NAME-inside-etc-os-rel.patch
* Tue Jun 21 2016 mc@suse.de
- Move log message from INFO to DEBUG (bsc#985661)
  Add:
  0056-Move-log-message-from-INFO-to-DEBUG.patch
- fix salt --summary to count not responding minions correctly
  (bsc#972311)
  Add:
  * 0057-fix-salt-summary-to-count-not-responding-minions-cor.patch
* Tue Jun 14 2016 tserong@suse.com
- Fix memory leak on custom execution module sheduled jobs (bsc#983512)
  Add:
  * 0055-Backport-31164-and-31364-32474.patch
* Thu Jun  9 2016 pablo.suarezhernandez@suse.com
- fix groupadd module for sles11 systems (bsc#978150)
  Add:
  * 0054-fix-groupadd-module-for-sles11-systems.patch
* Wed Jun  1 2016 mihai.dinca@suse.com
- Fix pkgrepo.managed gpgkey argument doesn't work (bsc#979448)
  Add:
  * 0053-Fix-pkgrepo.managed-gpgkey-argument-bsc-979448.patch
* Fri May 27 2016 pablo.suarezhernandez@suse.com
- Package checksum validation for zypper pkg.download
  Add:
  * 0050-checksum-validation-when-zypper-pkg.download.patch
  * 0051-unit-tests-for-rpm.checksum-and-zypper.download.patch
- Check if a job has executed and returned successfully
  Add:
  * 0052-jobs.exit_success-allow-to-check-if-a-job-has-execut.patch
* Mon May 23 2016 bmaryniuk@suse.com
- Remove option -f from startproc (bsc#975733)
  Add:
  * 0049-Prevent-several-minion-processes-on-the-same-machine.patch
* Mon May 23 2016 bmaryniuk@suse.com
- Changed Zypper's plugin. Added Unit test and related to that
  data (bsc#980313).
  Update:
  * 0046-Add-SUSE-Manager-plugin.patch
  Delete (not needed anymore):
  * 0049-Alter-the-event-name.patch
* Tue May 17 2016 bmaryniuk@suse.com
- Zypper plugin: alter the generated event name on package set
  change.
  Add:
  * 0049-Alter-the-event-name.patch
* Thu May 12 2016 tserong@suse.com
- Fix file ownership on master keys and cache directories during upgrade
  (handles upgrading from salt 2014, where the daemon ran as root, to 2015
  where it runs as the salt user, bsc#979676).
* Wed May 11 2016 pablo.suarezhernandez@suse.com
- salt-proxy .service file created (bsc#975306)
  Add:
  * 0048-Create-salt-proxy-instantiated-service-file.patch
* Wed May 11 2016 pablo.suarezhernandez@suse.com
- Prevent salt-proxy test.ping crash (bsc#975303)
  Add:
  * 0047-Old-style-proxymodules-need-to-be-setup-earlier-in-m.patch
* Wed May 11 2016 bmaryniuk@suse.com
- Fix shared directories ownership issues.
* Mon May  9 2016 bmaryniuk@suse.com
- Add Zypper plugin to generate an event,
  once Zypper is used outside the Salt infrastructure
  demand (bsc#971372).
  Add:
  * 0046-Add-SUSE-Manager-plugin.patch
* Fri May  6 2016 bmaryniuk@suse.com
- Restore boolean values from the repo configuration
  Fix priority attribute (bsc#978833)
  Add:
  * 0045-Bugfix-Restore-boolean-values-from-the-repo-configur.patch
* Wed May  4 2016 bmaryniuk@suse.com
- Unblock-Zypper. (bsc#976148)
  Modify-environment. (bsc#971372)
  Add:
  * 0044-Unblock-Zypper.-Modify-environment.patch
* Wed Apr 20 2016 bmaryniuk@suse.com
- Prevent crash if pygit2 package is requesting re-compilation.
  Add:
  * 0043-Prevent-crash-if-pygit2-package-is-requesting-re-com.patch
* Mon Apr 18 2016 mc@suse.de
- align OS grains from older SLES with current one (bsc#975757)
  Add:
  * 0042-align-OS-grains-from-older-SLES-with-current-one-bsc.patch
* Thu Apr 14 2016 bmaryniuk@suse.com
- Bugfix: salt-key crashes if tries to generate keys
  to the directory w/o write access (bsc#969320)
  Add:
  * 0041-Bugfix-salt-key-crashes-if-tries-to-generate-keys-to.patch
* Tue Apr 12 2016 bmaryniuk@suse.com
- Check if EOL is available in a particular product (bsc#975093)
  Add:
  * 0040-Check-if-EOL-is-available-in-a-particular-product-bs.patch
* Tue Apr  5 2016 mc@suse.com
- fix building with docs on SLE11
* Tue Apr  5 2016 mc@suse.com
- Prevent metadata download when getting installed products
  Add:
  * 0039-Prevent-metadata-download-when-getting-installed-pro.patch
* Tue Apr  5 2016 kkaempf@suse.com
- Add statically built docs.
* Mon Apr  4 2016 mc@suse.com
- fix sorting by latest package
  Add:
  * 0038-fix-sorting-by-latest-version-when-called-with-an-at.patch
* Sat Apr  2 2016 mc@suse.com
- ensure pkg.info_installed report latest package version
  (bsc#972490)
  Add:
  * 0037-Force-sort-the-RPM-output-to-ensure-latest-version-o.patch
* Thu Mar 17 2016 bmaryniuk@suse.com
- Use SHA256 by default in master, minion and proxy (bsc#955373)
  Add:
  * 0036-Use-SHA256-hash-type-by-default.patch
* Wed Mar 16 2016 bmaryniuk@suse.com
- Fix state structure compilation
  Add:
  * 0035-Fix-the-always-false-behavior-on-checking-state.patch
- Fix git_pillar race condition
  Add:
  * 0034-Fix-git_pillar-race-condition.patch
* Sat Mar 12 2016 mc@suse.com
- fix detection of base products in SLE11
  * 0030-Bugfix-on-SLE11-series-base-product-reported-as-addi.patch
- fix rpm info for SLE11
  * 0031-Only-use-LONGSIZE-in-rpm.info-if-available.-Otherwis.patch
  * 0032-Add-error-check-when-retcode-is-0-but-stderr-is-pres.patch
- fix init system detection for SLE11
  * 0033-fixing-init-system-dectection-on-sles-11-refs-31617.patch
* Fri Mar 11 2016 bmaryniuk@suse.com
- Re-add corrected patch:
  0029-Make-use-of-checksum-configurable-defaults-to-MD5-SH.patch
* Wed Mar  9 2016 kkaempf@suse.com
- Make checksum configurable (upstream still wants md5, we
  suggest sha256). bsc#955373
  Add:
  0029-Make-use-of-checksum-configurable-defaults-to-MD5-SH.patch
* Fri Mar  4 2016 tampakrap@opensuse.org
- Fix the service state / module on SLE11.
  Add:
  * 0027-make-suse-check-consistent-with-rh_service.patch
  * 0028-fix-numerical-check-of-osrelease.patch
* Fri Mar  4 2016 mc@suse.de
- Prevent rebuilds in OBS by not generating a date as a comment in
  a source file
  Add: 0026-do-not-generate-a-date-in-a-comment-to-prevent-rebui.patch
* Fri Feb 26 2016 mc@suse.de
- Add better checking for zypper exit codes and simplify evaluation
  of the zypper error messages.
  Add: 0024-proper-checking-if-zypper-exit-codes-and-handling-of.patch
- Adapt unit tests
  Add: 0025-adapt-tests-to-new-zypper_check_result-output.patch
* Fri Feb 26 2016 bmaryniuk@suse.com
- Add initial pack of Zypper's Unit tests.
  Use XML output in list_upgrades.
  Bugfix: upgrade_available crashes when only one package specified
  Purge is not using "-u" anymore
  Add:
  * 0023-Initial-Zypper-Unit-Tests-and-bugfixes.patch
* Tue Feb 23 2016 mc@suse.de
- fix argument handling of pkg.download
  Add: 0022-fix-argument-handling-for-pkg.download.patch
* Mon Feb 22 2016 mc@suse.de
- unify behavior of zypper refresh in salt
  Add: 0018-unify-behavior-of-refresh.patch
    0019-add-refresh-option-to-more-functions.patch
    0020-simplify-checking-the-refresh-paramater.patch
    0021-do-not-change-kwargs-in-refresh-while-checking-a-val.patch
* Sat Feb 20 2016 mc@suse.de
- Fix crash with scheduler and runners
  Add: 0017-Fix-crash-with-scheduler-and-runners-31106.patch
* Fri Feb 19 2016 mc@suse.de
- Call zypper always with --non-interactive
  Add:
  * 0015-call-zypper-with-option-non-interactive-everywhere.patch
  * 0016-write-a-zypper-command-builder-function.patch
* Fri Feb 19 2016 mc@suse.de
- require rpm-python on SUSE for zypper support
* Thu Feb 18 2016 mc@suse.de
- fix state return code
  Add: 0009-The-functions-in-the-state-module-that-return-a-retc.patch
- add handling of OEM products to pkg.list_products
  Add: 0010-add-handling-for-OEM-products.patch
- improve doc for list_pkgs
  Add: 0011-improve-doc-for-list_pkgs.patch
- implement pkg.version_cmp in zypper.py
  Add:
  * 0012-implement-version_cmp-for-zypper.patch
  * 0013-pylint-changes.patch
  * 0014-Check-if-rpm-python-can-be-imported.patch
* Wed Feb 17 2016 aboe76@gmail.com
- Update to 2015.8.7
  this is a small update to fix some regressions
  see https://docs.saltstack.com/en/latest/topics/releases/2015.8.7.html
* Thu Feb 11 2016 bmaryniuk@suse.com
- Booleans should not be strings from XML, add Unix ticks time and
  format result in a list of maps.
  Add:
  * 0008-Fix-types-in-the-output-data-and-return-just-a-list-.patch
* Thu Feb 11 2016 bmaryniuk@suse.com
- Stop salt-api daemon faster (bsc#963322)
  Add:
  * 0007-Force-kill-websocket-s-child-processes-faster-than-d.patch
* Wed Feb 10 2016 dmacvicar@suse.de
- Do not crash on salt-key reject/delete consecutive calls.
  Add:
  * 0006-add_key-reject_key-do-not-crash-w-Permission-denied-.patch
* Mon Feb  8 2016 kkaempf@suse.com
- Update to 2015.8.5
  Security fixes:
  * CVE-2016-1866: Improper handling of clear messages on the
    minion remote code execution (boo#965403)
  See https://docs.saltstack.com/en/latest/topics/releases/2015.8.5.html
  Dropped patches (all upstream):
  * 0003-List-products-consistently-across-all-SLES-systems.patch
  * 0004-Add-missing-return-data-to-scheduled-jobs.patch
  * 0005-Fix-RPM-issues-with-the-date-time-and-add-package-at.patch
  * 0006-Bugfix-info_available-does-not-work-correctly-on-SLE.patch
  Renamed patches:
  * 0007-Check-if-byte-strings-are-properly-encoded-in-UTF-8.patch
  - > 0003-Check-if-byte-strings-are-properly-encoded-in-UTF-8.patch
  * 0008-Fix-pkg.latest-prevent-crash-on-multiple-package-ins.patch
  - > 0004-Fix-pkg.latest-prevent-crash-on-multiple-package-ins.patch
  * 0009-Fix-package-status-filtering-on-latest-version-and-i.patch
  - > 0005-Fix-package-status-filtering-on-latest-version-and-i.patch
- Update to 2015.8.4
  See https://docs.saltstack.com/en/latest/topics/releases/2015.8.4.html
* Wed Jan 27 2016 bmaryniuk@suse.com
- Fix latest version available comparison and implement epoch
  support in Zypper module.
  Add:
  * 0009-Fix-package-status-filtering-on-latest-version-and-i.patch
* Wed Jan 27 2016 bmaryniuk@suse.com
- Update patch from opensuse to upstream version.
  Update:
  * 0008-Fix-pkg.latest-prevent-crash-on-multiple-package-ins.patch
* Tue Jan 26 2016 bmaryniuk@suse.com
- Fix dependencies to Salt subpackages requiring release along the
  version.
* Mon Jan 25 2016 bmaryniuk@suse.com
- Fix pkg.latest crash.
- Fix pkg.latest SLS ID bug, when pkgs empty list is passed,
  but SLS ID still treated as a package name.
  Add:
  * 0008-Fix-pkg.latest-prevent-crash-on-multiple-package-ins.patch
* Wed Jan 20 2016 bmaryniuk@suse.com
- Drop:
  * -0004-zypper-check-package-header-content-for-valid-utf-8.patch
- Rename:
  * -0004-zypper-check-package-header-content-for-valid-utf-8.patch
    +0004-Add-missing-return-data-to-scheduled-jobs.patch
  * -0005-Add-missing-return-data-to-scheduled-jobs.patch
    +0004-Add-missing-return-data-to-scheduled-jobs.patch
  * -0006-Fix-RPM-issues-with-the-date-time-and-add-package-at.patch
    +0005-Fix-RPM-issues-with-the-date-time-and-add-package-at.patch
  * -0007-Bugfix-info_available-does-not-work-correctly-on-SLE.patch
    +0006-Bugfix-info_available-does-not-work-correctly-on-SLE.patch
- Add:
  * 0007-Check-if-byte-strings-are-properly-encoded-in-UTF-8.patch
* Wed Jan 20 2016 kkaempf@suse.com
- Rename use-forking-daemon.patch to
  0001-tserong-suse.com-We-don-t-have-python-systemd-so-not.patch
- Rename use-salt-user-for-master.patch to
  0002-Run-salt-master-as-dedicated-salt-user.patch
- Rename 1efe484309a5c776974e723f3da0f5181f4bdb86.patch to
  0003-List-products-consistently-across-all-SLES-systems.patch
- Rename zypper-utf-8.patch to
  0004-zypper-check-package-header-content-for-valid-utf-8.patch
- Rename salt-2015.8-schedule-ret.patch to
  0005-Add-missing-return-data-to-scheduled-jobs.patch
- Rename salt-2015.8-pkg-zypper-attr-filtering.patch to
  0006-Fix-RPM-issues-with-the-date-time-and-add-package-at.patch
- Rename salt-2015.8-zypper-info.patch to
  0007-Bugfix-info_available-does-not-work-correctly-on-SLE.patch
* Fri Jan 15 2016 dmacvicar@suse.de
- Fix zypper module info_available on SLE-11
  * add salt-2015.8-zypper-info.patch
  * https://github.com/saltstack/salt/pull/30384
- zypper/pkg: add package attributes filtering
  * add salt-2015.8-pkg-zypper-attr-filtering.patch
  * https://github.com/saltstack/salt/pull/30267
- Remove obsoleted patches and fixes:
  * 0001-Add-rpm.minimal_info-fix-rpm.info.patch
  * 0002-Reduce-information-returned-from-pkg.info_installed.patch
  * Remove require on glibc-locale (bsc#959572)
* Wed Jan 13 2016 dmacvicar@suse.de
- Add missing return data to scheduled jobs
  * add salt-2015.8-schedule-ret.patch for
  * https://github.com/saltstack/salt/pull/30246
* Mon Dec 21 2015 kkaempf@suse.com
- Update zypper-utf-8.patch for Python 2.6
* Thu Dec 17 2015 kkaempf@suse.com
- require glibc-locale (bsc#959572)
* Tue Dec 15 2015 kkaempf@suse.com
- Report epoch and architecture of installed packages
  0001-Add-rpm.minimal_info-fix-rpm.info.patch
- pkg.info_installed exceeds the maximum event size, reduce the
  information to what's actually needed
  0002-Reduce-information-returned-from-pkg.info_installed.patch
* Wed Dec  9 2015 kkaempf@suse.com
- Filter out bad UTF-8 strings in package data (bsc#958350)
  zypper-utf-8.patch
* Tue Dec  1 2015 aboe76@gmail.com
- Updated to salt 2015.8.3 bugfix release
- remove the following patches because upstream merged them:
  - 4b9302d79455d6a586b7cad1d7990cb22e7bc62e.patch
  - os_grain.patch
  - zypper_pkgrepo.patch
- more details at: https://docs.saltstack.com/en/latest/topics/releases/2015.8.3.html
* Tue Dec  1 2015 bmaryniuk@suse.com
- added 1efe484309a5c776974e723f3da0f5181f4bdb86.patch:
  reimplements pkg.list_products that potentially may be broken in
  a future releases of SLES.
* Mon Nov 30 2015 mrueckert@suse.de
- added 4b9302d79455d6a586b7cad1d7990cb22e7bc62e.patch:
  fixes a regression introduced in 2015.8.2, which was actually
  holding back the release. Downgrade is not an option as we need
  the leap fixes.
* Thu Nov 26 2015 mrueckert@suse.de
- it shouldnt be >= 1110 but just > 1110
* Wed Nov 25 2015 mrueckert@suse.de
- require pmtools on sle11 to get dmidecode
* Fri Nov 20 2015 mrueckert@suse.de
- update use-salt-user-for-master.patch:
  First step to make the syndic also run as salt user.
* Fri Nov 13 2015 aboe76@gmail.com
- Updated to bugfix release 2015.8.2
- os_grain.patch fix the "os" grain on SLES11SP4
- zypper_pkgrepo.patch fix the priority and humanname pkgrepo args for the
  zypper backend
  for more details:
  https://docs.saltstack.com/en/2015.8/topics/releases/2015.8.2.html
* Thu Oct 15 2015 mrueckert@suse.de
- update to 2015.8.1
  - Add support for ``spm.d/*.conf`` configuration of SPM
    (:issue:`27010`)
  - Fix ``proxy`` grains breakage for non-proxy minions
    (:issue:`27039`)
  - Fix global key management for git state
  - Fix passing http auth to ``util.http`` from ``state.file``
    (:issue:`21917`)
  - Fix ``multiprocessing: True`` in windows (on by default`)
  - Add ``pkg.info`` to pkg modules
  - Fix name of ``serial`` grain (this was accidentally renamed in
    2015.8.0`)
  - Merge config values from ``master.d``/``minion.d`` conf files
    (rather than flat update`)
  - Clean grains cache on grains sync (:issue:`19853`)
  - Remove streamed response for fileclient to avoid HTTP
    redirection problems (:issue:`27093`)
  - Fixed incorrect warning about ``osrelease`` grain
    (:issue:`27065`)
  - Fix authentication via Salt-API with tokens (:issue:`27270`)
  - Fix winrepo downloads from https locations (:issue:`27081`)
  - Fix potential error with salt-call as non-root user
    (:issue:`26889`)
  - Fix global minion provider overrides (:issue:`27209`)
  - Fix backward compatibility issues for pecl modules
  - Fix Windows uninstaller to only remove ``./bin``, ``salt*``,
    ``nssm.exe``, ``uninst.exe`` (:issue:`27383`)
  - Fix misc issues with mongo returner.
  - Add sudo option to cloud config files (:issue:`27398`)
  - Fix regression in RunnerClient argument handling
    (:issue:`25107`)
  - Fix ``dockerng.running`` replacing creation hostconfig with
    runtime hostconfig (:issue:`27265`)
  - Fix dockerng.running replacing creation hostconfig with runtime
    hostconfig (:issue:`27265`)
  - Increased performance on boto asg/elb states due to
    ``__states__`` integration
  - Windows minion no longer requires powershell to restart
    (:issue:`26629`)
  - Fix x509 module to support recent versions of OpenSSL
    (:issue:`27326`)
  - Some issues with proxy minions were corrected.
- drop salt-2015.8-backports-susemanager.diff: included in update
- guard raet buildrequires with bcond_with raet and comment out the
  recommends for salt-raet.
* Mon Oct 12 2015 tampakrap@opensuse.org
- remove pygit2 global recommends, it is only needed in the master
- remove git-core, pygit2 should pull it as a dependency
- add a (currently disabled) %%check
* Mon Oct 12 2015 toddrme2178@gmail.com
- Add salt-2015.8-backports-susemanager.diff
  Returns detailed information about a package
* Mon Oct 12 2015 dmacvicar@suse.de
- ifdef Recommends to build on RHEL based distros
- use _initddir instead of _sysconfdir/init.d as
  it works on both platforms.
* Mon Oct 12 2015 dmacvicar@suse.de
- allow to disable docs in preparation for building
  on other platforms without all dependencies.
* Mon Oct 12 2015 dmacvicar@suse.de
- python-libnacl, python-ioflo are _not_ required to build the
  package. They are anyways requires of python-raet, which is
  also not required to build the package.
* Sat Oct 10 2015 mrueckert@suse.de
- merge (build)requires/recommends with requirements/*txt and
  setup.py
* Fri Oct  9 2015 mrueckert@suse.de
- add raet subpackage which will pull all requires for it and
  provides config snippets to enable it for the minion and master.
* Fri Oct  9 2015 mrueckert@suse.de
- add tmpfiles.d file
* Fri Oct  9 2015 dmacvicar@suse.de
- Remove requires on python-ioflo and python-libnacl
  they will be pulled by python-raet,
  which is optional.
* Fri Oct  9 2015 dmacvicar@suse.de
- python-raet is optional, so make it a Recommends
* Fri Oct  9 2015 dmacvicar@suse.de
- update backports patch from 2015.8 branch
* Wed Oct  7 2015 mrueckert@suse.de
- update use-forking-daemon.patch:
  the original intention was to get rid of the python systemd
  dependency. for this we do not have daemonize the whole process.
  just switching to simple mode is enough.
* Wed Oct  7 2015 mrueckert@suse.de
- drop fdupes:
  1. it broke python byte code handling
  2. the only part of the package which would really benefit from
    it would be the doc package. but given we only install the
    files via %%doc, we can not use it for that either.
- reenable completions on distros newer than sle11
- do not use _datarootdir, use _datadir instead.
* Wed Oct  7 2015 mrueckert@suse.de
- package all directories in /var/cache/salt and /etc/salt and
  have permissions set for non root salt master
- update use-salt-user-for-master.patch:
  - also patch the logrotate file to include the su option
* Tue Oct  6 2015 mrueckert@suse.de
- remove duplicated recommends
- never require pygit2 and git. the master can run fine without.
  always use recommends
* Tue Oct  6 2015 tampakrap@opensuse.org
- cleanup dependencies:
  - remove a lot of unneeded buildrequires
  - fdupes not present on SLE10
  - python-certifi needed on SLE11
  - python-zypp not needed any more
  - python-pygit2 is not a global requirement
  - convert python-pysqlite to recommends as it is not available on python <=2.7
- sles_version -> suse_version
- %%exclude the cloud/deploy/*.sh scripts to fix build issue on SLE11
* Mon Oct  5 2015 tampakrap@opensuse.org
- Remove python-PyYAML from the dependencies list, as python-yaml is the same
- Build the -completion subpackages in SLE11 as well
- Add salt-proxy (by dmacvicar@suse.de)
- Create salt user/group only in the -master subpkg
* Sat Oct  3 2015 infroma@gmail.com
- Fix typo in use-forking-daemon.patch, that prevented daemon loading
* Thu Oct  1 2015 toddrme2178@gmail.com
- Fix typo in Requires
* Tue Sep 29 2015 toddrme2178@gmail.com
- Cleanup requirements
* Wed Sep 23 2015 aboe76@gmail.com
- New Major release 2015.8.0
  for more details:
  http://docs.saltstack.com/en/latest/topics/releases/2015.8.0.html
- Cleaned the spec file with spec-cleaner
- Added the use-salt-user-for-master.patch see README.SUSE
- Updated the files ownership with salt user
- removed m2crypto depency
* Tue Sep 22 2015 infroma@gmail.com
- Removed fish dependency for fish completions.
* Tue Sep 22 2015 infroma@gmail.com
- Added fish completions.
* Mon Sep 21 2015 tampakrap@opensuse.org
- Support SLE11SP{3,4}, where the M2Crypto package is named python-m2crypto
* Tue Aug 18 2015 aboe76@gmail.com
- Updated to Bugfix release 2015.5
  for more details:
  https://github.com/saltstack/salt/blob/develop/doc/topics/releases/2015.5.5.rst
- Add prereq, for user creation.
- Add creation of salt user in preparation of running the salt-master daemon
  as non-root user salt.
  https://bugzilla.opensuse.org/show_bug.cgi?id=939831
- Add README.SUSE with explanation and how to.
* Mon Jul 20 2015 bwiedemann@suse.com
- only require git-core to not pull in git-web and gitk
* Wed Jul  8 2015 aboe76@gmail.com
- New Bugfix release 2015.5.3
  for more details:
  http://docs.saltstack.com/en/latest/topics/releases/2015.5.3.html
* Thu Jun  4 2015 aboe76@gmail.com
- New Bugfix release 2015.5.2
  for more details:
  http://docs.saltstack.com/en/latest/topics/releases/2015.5.2.html
* Sat May 23 2015 aboe76@gmail.com
- New Bugfix release 2015.5.1
  salt.runners.cloud.action() has changed the fun keyword argument to func.
  Please update any calls to this function in the cloud runner.
  for more details:
  http://docs.saltstack.com/en/latest/topics/releases/2015.5.1.html
* Fri May 15 2015 aboe76@gmail.com
- Removed python-pssh depency not needed anymore.
* Wed May  6 2015 aboe76@gmail.com
- Major release 2015.5.0 Lithium
- update to 2015.5.0
  The 2015.5.0 feature release of Salt is focused on hardening Salt
  and mostly on improving existing systems. A few major additions
  are present, primarily the new Beacon system. Most enhancements
  have been focused around improving existing features and
  interfaces.
  As usual the release notes are not exhaustive and primarily
  include the most notable additions and improvements. Hundreds of
  bugs have been fixed and many modules have been substantially
  updated and added.
  See especially the warning right on the top regarding
  python_shell=False.
  For all details see
  http://docs.saltstack.com/en/latest/topics/releases/2015.5.0.html
- RPM Package changes:
- add some versions to the buildrequires to match the 2
  requirements files from the tarball
- Moved the depencencies to main salt package
  except where they are specific for the package
- Changed python-request dependency,only needed on salt-cloud
- Added python-tornado dependency for http.py
- Fixed zsh_completion in tarball.
- Fixed salt-api requirements to require python-cherrypy
- Fixed salt-cloud requiments to require salt-master
* Sun Apr 19 2015 aboe76@gmail.com
- New Bugfix release 2014.7.5
  Changes:
  + Fixed a key error bug in salt-cloud
  + Updated man pages to better match documentation
  + Fixed bug concerning high CPU usage with salt-ssh
  + Fixed bugs with remounting cvfs and fuse filesystems
  + Fixed bug with alowing requisite tracking of entire sls files
  + Fixed bug with aptpkg.mod_repo returning OK even if apt-add-repository fails
  + Increased frequency of ssh terminal output checking
  + Fixed malformed locale string in localmod module
  + Fixed checking of available version of package when accept_keywords were changed
  + Fixed bug to make git.latest work with empty repositories
  + Added **kwargs to service.mod_watch which removes warnings about enable and __reqs__ not being supported by the function
  + Improved state comments to not grow so quickly on failed requisites
  + Added force argument to service to trigger force_reload
  + Fixed bug to andle pkgrepo keyids that have been converted to int
  + Fixed module.portage_config bug with appending accept_keywords
  + Fixed bug to correctly report disk usage on windows minion
  + Added the ability to specify key prefix for S3 ext_pillar
  + Fixed issues with batch mode operating on the incorrect number of minions
  + Fixed a bug with the proxmox cloud provider stacktracing on disk definition
  + Fixed a bug with the changes dictionary in the file state
  + Fixed the TCP keep alive settings to work better with SREQ caching
  + Fixed many bugs within the iptables state and module
  + Fixed bug with states by adding fun, state, and unless to the state runtime internal keywords listing
  + Added ability to eAuth against Active Directory
  + Fixed some salt-ssh issues when running on Fedora 21
  + Fixed grains.get_or_set_hash to work with multiple entries under same key
  + Added better explanations and more examples of how the Reactor calls functions to docs
  + Fixed bug to not pass ex_config_drive to libcloud unless it's explicitly enabled
  + Fixed bug with pip.install on windows
  + Fixed bug where puppet.run always returns a 0 retcode
  + Fixed race condition bug with minion scheduling via pillar
  + Made efficiency improvements and bug fixes to the windows installer
  + Updated environment variables to fix bug with pygit2 when running salt as non-root user
  + Fixed cas behavior on data module -- data.cas was not saving changes
  + Fixed GPG rendering error
  + Fixed strace error in virt.query
  + Fixed stacktrace when running chef-solo command
  + Fixed possible bug wherein uncaught exceptions seem to make zmq3 tip over when threading is involved
  + Fixed argument passing to the reactor
  + Fixed glibc caching to prevent bug where salt-minion getaddrinfo in dns_check() never got updated nameservers
  Known Issues:
  + In multimaster mode, a minion may become temporarily unresponsive if modules or pillars are refreshed at the
  same time that one or more masters are down. This can be worked around by setting 'auth_timeout' and 'auth_tries'
  down to shorter periods.
* Mon Mar 30 2015 aboe76@gmail.com
- New Bugfix Release 2014.7.4
- Updated patch use-forking-daemon.patch
- fix salt-zsh-completion conflicts
  + Multi-master minions mode no longer route fileclient operations asymetrically.
  This fixes the source of many multi-master bugs where the minion would
  become unrepsonsive from one or more masters.
  + Fix bug wherein network.iface could produce stack traces.
  + net.arp will no longer be made available unless arp is installed on the
  system.
  + Major performance improvements to Saltnado
  + Allow KVM module to operate under KVM itself or VMWare Fusion
  + Various fixes to the Windows installation scripts
  + Fix issue where the syndic would not correctly propogate loads to the master
  job cache.
  + Improve error handling on invalid /etc/network/interfaces file in salt
  networking modules
  + Fix bug where a reponse status was not checked for in fileclient.get_url
  + Enable eauth when running salt in batch mode
  + Increase timeout in Boto Route53 module
  + Fix bugs with Salt's 'tar' module option parsing
  + Fix parsing of NTP servers on Windows
  + Fix issue with blockdev tuning not reporting changes correctly
  + Update to the latest Salt bootstrap script
  + Update Linode salt-cloud driver to use either linode-python or
  apache-libcloud
  + Fix for s3.query function to return correct headers
  + Fix for s3.head returning None for files that exist
  + Fix the disable function in win_service module so that the service is
  disabled correctly
  + Fix race condition between master and minion when making a directory when
  both daemons are on the same host
  + Fix an issue where file.recurse would fail at the root of an svn repo
  when the repo has a mountpoint
  + Fix an issue where file.recurse would fail at the root of an hgfs repo
  when the repo has a mountpoint
  + Fix an issue where file.recurse would fail at the root of an gitfs repo
  when the repo has a mountpoint
  + Add status.master capability for Windows.
  + Various fixes to ssh_known_hosts
  + Various fixes to states.network bonding for Debian
  + The debian_ip.get_interfaces module no longer removes nameservers.
  + Better integration between grains.virtual and systemd-detect-virt and
  virt-what
  + Fix traceback in sysctl.present state output
  + Fix for issue where mount.mounted would fail when superopts were not a part
  of mount.active (extended=True). Also mount.mounted various fixes for Solaris
  and FreeBSD.
  + Fix error where datetimes were not correctly safeguarded before being passed
  into msgpack.
  + Fix file.replace regressions.  If the pattern is not found, and if dry run is False,
  and if `backup` is False, and if a pre-existing file exists with extension `.bak`,
  then that backup file will be overwritten. This backup behavior is a result of how `fileinput`
  works. Fixing it requires either passing through the file twice (the
  first time only to search for content and set a flag), or rewriting
  `file.replace` so it doesn't use `fileinput`
  + VCS filreserver fixes/optimizations
  + Catch fileserver configuration errors on master start
  + Raise errors on invalid gitfs configurations
  + set_locale when locale file does not exist (Redhat family)
  + Fix to correctly count active devices when created mdadm array with spares
  + Fix to correctly target minions in batch mode
  + Support ssh:// urls using the gitfs dulwhich backend
  + New fileserver runner
  + Fix various bugs with argument parsing to the publish module.
  + Fix disk.usage for Synology OS
  + Fix issue with tags occurring twice with docker.pulled
  + Fix incorrect key error in SMTP returner
  + Fix condition which would remount loopback filesystems on every state run
  + Remove requsites from listens after they are called in the state system
  + Make system implementation of service.running aware of legacy service calls
  + Fix issue where publish.publish would not handle duplicate responses gracefully.
  + Accept Kali Linux for aptpkg salt execution module
  + Fix bug where cmd.which could not handle a dirname as an argument
  + Fix issue in ps.pgrep where exceptions were thrown on Windows.
- Known Issues:
  + In multimaster mode, a minion may become temporarily unresponsive
  if modules or pillars are refreshed at the same time that one
  or more masters are down. This can be worked around by setting
  'auth_timeout' and 'auth_tries' down to shorter periods.
* Thu Feb 12 2015 aboe76@gmail.com
- New Bugfix release 2014.7.2:
- fix package bug with fdupes.
- keep sle 11 sp3 support.
  + Fix erroneous warnings for systemd service enabled check (issue 19606)
  + Fix FreeBSD kernel module loading, listing, and persistence kmod (issue 197151, issue 19682)
  + Allow case-sensitive npm package names in the npm state. This may break behavior
  for people expecting the state to lowercase their npm package names for them.
  The npm module was never affected by mandatory lowercasing. (issue 20329)
  + Deprecate the activate parameter for pip.install for both the module and the state.
  If bin_env is given and points to a virtualenv, there is no need to activate that virtualenv
  in a shell for pip to install to the virtualenv.
  + Fix a file-locking bug in gitfs (issue 18839)
* Thu Jan 15 2015 aboe76@gmail.com
- New Bugfix release 2014.7.1:
  + Fixed gitfs serving symlinks in file.recurse states (issue 17700)
  + Fixed holding of multiple packages (YUM) when combined with version pinning (issue 18468)
  + Fixed use of Jinja templates in masterless mode with non-roots fileserver backend (issue 17963)
  + Re-enabled pillar and compound matching for mine and publish calls. Note that pillar globbing is still disabled for those modes, for security reasons. (issue 17194)
  + Fix for tty: True in salt-ssh (issue 16847)
- Needed to provide zsh completion because of the tarball missing the zsh completion script.
- Removed man salt.1.gz file from salt-master because upstream removed it.
- Added man salt.7.gz to salt-master package
* Mon Nov  3 2014 aboe76@gmail.com
- Updated to Major Release 2014.7.0
- added python-zipp as depency
- added recommend python-pygit2, this is the preferred gitfs backend of saltstack
- added zsh-completion package
- Removed Patch fix-service-py-version-parsing-sles.patch already fixed in this package
- Removed Patch pass-all-systemd-list-units.patch already fixed in this package
- Removed Patch disable-service-py-for-suse-family.patch already fixed in this package
- Removed Patch allow-systemd-units-no-unit-files.patch already fixed in this package
- Removed Patch allow-systemd-parameterized-services.patch already fixed in this package
- More information at: http://docs.saltstack.com/en/latest/topics/releases/2014.7.0.html
- SALT SSH ENHANCEMENTS:
  + Support for Fileserver Backends
  + Support for Saltfile
  + Ext Pillar
  + No more sshpass needed
  + Pure Python Shim
  + Custom Module Delivery
  + CP module Support
  + More Thin Directory Options
  - Salt State System enhancements:
  + New Imperative State Keyword "Listen"
  + New Mod Aggregate Runtime Manipulator
  + New Requisites: onchanges and onfail
  + New Global onlyif and unless
  + Use names to expand and override values
  - Salt Major Features:
  + Improved Scheduler Additions
  + Red Hat 7 Support
  + Fileserver Backends in Salt-call
  + Amazon Execution Modules in salt-cloud
  + LXC Runner Enhancements
  + Next Gen Docker Management
  + Peer System Performance Improvements
  + SDB Encryption at rest for configs
  + GPG Renderer encrypted pillar at rest
  + OpenStack Expansions
  + Queues System external queue systems into Salt events
  + Multi Master Failover Additions
  + Chef Execution Module
  - salt-api Project Merge
  + Synchronous and Asynchronous Execution of Runner and Wheel Modules
  + rest_cherrypy Additions
  + Web Hooks
  - Fileserver Backend Enhancements:
  + New gitfs Features
  + Pygit2 and Dulwich support
  + Mountpoints support
  + New hgfs Features
  + mountpoints support
  + New svnfs Features:
    + mountpoints
  + minionfs Featuressupport
    + mountpoints
  - New Salt Modules:
  + Oracle
  + Random
  + Redis
  + Amazon Simple Queue Service
  + Block Device Management
  + CoreOS etcd
  + Genesis
  + InfluxDB
  + Server Density
  + Twilio Notifications
  + Varnish
  + ZNC IRC Bouncer
  + SMTP
  - NEW RUNNERS:
  + Map/Reduce Style
  + Queue
  - NEW EXTERNAL PILLARS:
  + CoreOS etcd
  - NEW SALT-CLOUD PROVIDERS:
  + Aliyun ECS Cloud
  + LXC Containers
  + Proxmox (OpenVZ containers & KVM)
- DEPRECATIONS:
  + Salt.modules.virtualenv_mod
* Thu Oct 16 2014 aboe76@gmail.com
- Updated to 2014.1.13 a bugfix release on 2014.1.12
  + fix module run exit code (issue 16420)
  + salt cloud Check the exit status code of scp before assuming it has failed. (issue 16599)
* Fri Oct 10 2014 aboe76@gmail.com
  ff
- Updated to 2014.1.12 a bugfix release on 2014.1.11
  + Fix scp_file always failing (which broke salt-cloud) (issue 16437)
  + Fix regression in pillar in masterless (issue 16210, issue 16416, issue 16428)
* Wed Sep 10 2014 aboe76@gmail.com
- Updated to 2014.1.11 is another bugfix release for 2014.1.0. Changes include:
  + Fix for minion_id with byte-order mark (BOM) (issue 12296)
  + Fix runas deprecation in at module
  + Fix trailing slash befhavior for file.makedirs_ (issue 14019)
  + Fix chocolatey path (issue 13870)
  + Fix git_pillar infinite loop issues (issue 14671)
  + Fix json outputter null case
  + Fix for minion error if one of multiple masters are down (issue 14099)
  + Updated the use-forking-daemon.patch with the right version
* Mon Aug 18 2014 tserong@suse.com
- Fix service.py version parsing for SLE 11
  + Added fix-service-py-version-parsing-sles.patch
* Tue Aug 12 2014 tserong@suse.com
- Remove salt-master's hard requirement for git and python-GitPython on SLE 12
* Wed Aug  6 2014 tserong@suse.com
- Ensure salt uses systemd for services on SLES
  + Added disable-service-py-for-suse-family.patch
* Mon Aug  4 2014 aboe76@gmail.com
- RPM spec update
  + added service_add_pre function
* Fri Aug  1 2014 aboe76@gmail.com
- Updated to 2014.1.10:
  + Version 2014.1.9 contained a regression which caused inaccurate Salt version
  detection, and thus was never packaged for general release.  This version
  contains the version detection fix, but is otherwise identical to 2014.1.9.
  + Version 2014.1.8 contained a regression which caused inaccurate Salt version
  detection, and thus was never packaged for general release.  This version
  contains the version detection fix, but is otherwise identical to 2014.1.8.
* Wed Jul 30 2014 aboe76@gmail.com
- Updated to 2014.1.8:
  + Ensure salt-ssh will not continue if permissions on a temporary directory are not correct.
  + Use the bootstrap script distributed with Salt instead of relying on an external resource
  + Remove unused testing code
  + Ensure salt states are placed into the .salt directory in salt-ssh
  + Use a randomized path for temporary files in a salt-cloud deployment
  + Clean any stale directories to ensure a fresh copy of salt-ssh during a deployment
* Thu Jul 24 2014 tserong@suse.com
- Allow salt to correctly detect services provided by init scripts
  + Added allow-systemd-units-no-unit-files.patch
  + Added allow-systemd-parameterized-services.patch
  + Added pass-all-systemd-list-units.patch
- Move systemd service file fix to patch, add PIDFile parameter (this
  fix is applicable for all SUSE versions, not just 12.3)
  + Added use-forking-daemon.patch
* Wed Jul 23 2014 aboe76@gmail.com
- Improve systemd service file fix for 12.3
  Use forking instead of Simple and daemonize salt-master process
* Sat Jul 19 2014 aboe76@gmail.com
- Fixed bug in opensuse 12.3 systemd file
  systemd 198 doesn't have python-systemd binding.
- Disabled testing on SLES
* Thu Jul 10 2014 aboe76@gmail.com
- Update to 2014.7
  This release was a hotfix release for the regression listed above which was present in the 2014.1.6
- Fix batch mode regression (issue 14046)
* Wed Jul  9 2014 aboe76@gmail.com
- Updated to 2014.1.6
- Fix extra iptables --help output (Sorry!) (issue 13648, issue 13507, issue 13527, issue 13607)
- Fix mount.active for Solaris
- Fix support for allow-hotplug statement in debian_ip network module
- Add sqlite3 to esky builds
- Fix jobs.active output (issue 9526)
- Fix the virtual grain for Xen (issue 13534)
- Fix eauth for batch mode (issue 9605)
- Fix force-related issues with tomcat support (issue 12889)
- Fix KeyError when cloud mapping
- Fix salt-minion restart loop in Windows (issue 12086)
- Fix detection of service virtual module on Fedora minions
- Fix traceback with missing ipv4 grain (issue 13838)
- Fix issue in roots backend with invalid data in mtime_map (issue 13836)
- Fix traceback in jobs.active (issue 11151)
* Wed Jun 11 2014 aboe76@gmail.com
- Updated to 2014.1.5
- Add function for finding cached job on the minion
- Fix for minion caching jobs when master is down
- Bump default `syndic_wait` to 5 to fix syndic-related problems
  (issue 12262)
- Fix false positive error in logs for `makeconf` state (issue 9762)
- Fix for extra blank lines in `file.blockreplace` (issue 12422)
- Use system locale for ports package installations
- Fix for `cmd_iter`/`cmd_iter_no_block` blocking issues (issue 12617)
- Fix traceback when syncing custom types (issue 12883)
- Fix cleaning directory symlinks in `file.directory`
- Add performance optimizations for `saltutil.sync_all` and
  `state.highstate`
- Fix possible error in `saltutil.running`
- Fix for kmod modules with dashes (issue 13239)
- Fix possible race condition for Windows minions in state module reloading
  (issue 12370)
- Fix bug with roster for `passwd`s that are loaded as non-string objects
  (issue 13249)
- Keep duplicate version numbers from showing up in `pkg.list_pkgs` output
- Fixes for Jinja renderer, timezone mod`module
  <salt.modules.timezone>`/mod`state <salt.states.timezone>` (issue 12724)
- Fix timedatectl parsing for systemd>=210 (issue 12728)
- Removed the deprecated external nodes classifier (originally accessible by
  setting a value for external_nodes in the master configuration file).  Note
  that this functionality has been marked deprecated for some time and was
  replaced by the more general doc`master tops <topics/master_tops>` system.
- More robust escaping of ldap filter strings.
- Fix trailing slash in conf_master`gitfs_root` causing files not to be
  available (issue 13185)
* Tue Jun 10 2014 aboe76@gmail.com
- added bash completion package
* Mon May  5 2014 aboe76@gmail.com
- Updated to 2014.1.4
  - Fix setup.py dependency issue (issue 12031)
  - Fix handling for IOErrors under certain circumstances (issue 11783 and issue 11853)
  - Fix fatal exception when `/proc/1/cgroup` is not readable (issue 11619)
  - Fix os grains for OpenSolaris (issue 11907)
  - Fix `lvs.zero` module argument pass-through (issue 9001)
  - Fix bug in `debian_ip` interaction with `network.system` state (issue 11164)
  - Remove bad binary package verification code (issue 12177)
  - Fix traceback in solaris package installation (issue 12237)
  - Fix `file.directory` state symlink handling (issue 12209)
  - Remove `external_ip` grain
  - Fix `file.managed` makedirs issues (issue 10446)
  - Fix hang on non-existent Windows drive letter for `file` module (issue 9880)
  - Fix salt minion caching all users on the server (issue 9743)
* Thu Apr 17 2014 aboe76@gmail.com
- Updated to 2014.1.3
  - Fix username detection when su'ed to root on FreeBSD (issue 11628)
  - Fix minionfs backend for file.recurse states
  - Fix 32-bit packages of different arches than the CPU arch, on 32-bit RHEL/CentOS (issue 11822)
  - Fix bug with specifying alternate home dir on user creation (FreeBSD) (issue 11790)
  - Don’t reload site module on module refresh for MacOS
  - Fix regression with running execution functions in Pillar SLS (issue 11453)
  - Fix some modules missing from Windows installer
  - Don’t log an error for yum commands that return nonzero exit status on non-failure (issue 11645)
  - Fix bug in rabbitmq state (issue 8703)
  - Fix missing ssh config options (issue 10604)
  - Fix top.sls ordering (issue 10810 and issue 11691)
  - Fix salt-key --list all (issue 10982)
  - Fix win_servermanager install/remove function (issue 11038)
  - Fix interaction with tokens when running commands as root (issue 11223)
  - Fix overstate bug with find_job and **kwargs (issue 10503)
  - Fix saltenv for aptpkg.mod_repo from pkgrepo state
  - Fix environment issue causing file caching problems (issue 11189)
  - Fix bug in __parse_key in registry state (issue 11408)
  - Add minion auth retry on rejection (issue 10763)
  - Fix publish_session updating the encryption key (issue 11493)
  - Fix for bad AssertionError raised by GitPython (issue 11473)
  - Fix debian_ip to allow disabling and enabling networking on Ubuntu (issue 11164)
  - Fix potential memory leak caused by saved (and unused) events (issue 11582)
  - Fix exception handling in the MySQL module (issue 11616)
  - Fix environment-related error (issue 11534)
  - Include psutil on Windows
  - Add file.replace and file.search to Windows (issue 11471)
  - Add additional file module helpers to Windows (issue 11235)
  - Add pid to netstat output on Windows (issue 10782)
  - Fix Windows not caching new versions of installers in winrepo (issue 10597)
  - Fix hardcoded md5 hashing
  - Fix kwargs in salt-ssh (issue 11609)
  - Fix file backup timestamps (issue 11745)
  - Fix stacktrace on sys.doc with invalid eauth (issue 11293)
  - Fix git.latest with test=True (issue 11595)
  - Fix file.check_perms hardcoded follow_symlinks (issue 11387)
  - Fix certain pkg states for RHEL5/Cent5 machines (issue 11719)
- Packaging:
  - python-psutil depencies (more functional modules out of the box)
  - python-yaml depencies (more functional modules out of the box)
  - python-requests depencies (salt-cloud)
* Wed Mar 19 2014 aboe76@gmail.com
- Updated to 2014.1.1 Bug Fix release
- temporarily disabled integration check after consult with Upstream
* Thu Feb 20 2014 aboe76@gmail.com
- Updated to 2014.1.0 Major Release
- features:
  - 2014.1.0 is the first release to follow the new date-based release naming system.
  - Salt Cloud Merged into Salt
  - Google Compute Engine support is added to salt-cloud.
  - Salt Virt released
  - Docker Integration
  - IPv6 Support for iptables State/Module
  - GitFS Improvements
  - MinionFS
  - saltenv
  - Grains Caching
  - Improved Command Logging Control
  - PagerDuty Support
  - Virtual Terminal
  - Proxy Minions
- bugfixes:
  - Fix mount.mounted leaving conflicting entries in fstab (:issue:`7079`)
  - Fix mysql returner serialization to use json (:issue:`9590`)
  - Fix ZMQError: Operation cannot be accomplished in current state errors (:issue:`6306`)
  - Rbenv and ruby improvements
  - Fix quoting issues with mysql port (:issue:`9568`)
  - Update mount module/state to support multiple swap partitions (:issue:`9520`)
  - Fix archive state to work with bsdtar
  - Clarify logs for minion ID caching
  - Add numeric revision support to git state (:issue:`9718`)
  - Update master_uri with master_ip (:issue:`9694`)
  - Add comment to Debian mod_repo (:issue:`9923`)
  - Fix potential undefined loop variable in rabbitmq state (:issue:`8703`)
  - Fix for salt-virt runner to delete key on VM deletion
  - Fix for salt-run -d to limit results to specific runner or function (:issue:`9975`)
  - Add tracebacks to jinja renderer when applicable (:issue:`10010`)
  - Fix parsing in monit module (:issue:`10041`)
  - Fix highstate output from syndic minions (:issue:`9732`)
  - Quiet logging when dealing with passwords/hashes (:issue:`10000`)
  - Fix for multiple remotes in git_pillar (:issue:`9932`)
  - Fix npm installed command (:issue:`10109`)
  - Add safeguards for utf8 errors in zcbuildout module
  - Fix compound commands (:issue:`9746`)
  - Add systemd notification when master is started
  - Many doc improvements
- packaging:
  - source tarball includes all packaging files in pkg folder.
  - fixed rpmlint errors about duplicates.
  - fixed rpmlint errors about non executables scripts.
* Sat Jan 25 2014 aboe76@gmail.com
- Updated to 0.17.5 a bugfix release for 0.17.0:
* Thu Dec 12 2013 aboe76@gmail.com
- Updated to  0.17.4 which is another bugfix release for 0.17.0:
  - Fix some jinja render errors (issue 8418)
  - Fix file.replace state changing file ownership (issue 8399)
  - Fix state ordering with the PyDSL renderer (issue 8446)
  - Fix for new npm version (issue 8517)
  - Fix for pip state requiring name even with requirements file (issue 8519)
  - Add sane maxrunning defaults for scheduler (issue 8563)
  - Fix states duplicate key detection (issue 8053)
  - Fix SUSE patch level reporting (issue 8428)
  - Fix managed file creation umask (issue 8590)
  - Fix logstash exception (issue 8635)
  - Improve argument exception handling for salt command (issue 8016)
  - Fix pecl success reporting (issue 8750)
  - Fix launchctl module exceptions (issue 8759)
  - Fix argument order in pw_user module
  - Add warnings for failing grains (issue 8690)
  - Fix hgfs problems caused by connections left open (issue 8811 and issue 8810)
  - Fix installation of packages with dots in pkg name (issue 8614)
  - Fix noarch package installation on CentOS 6 (issue 8945)
  - Fix portage_config.enforce_nice_config (issue 8252)
  - Fix salt.util.copyfile umask usage (issue 8590)
  - Fix rescheduling of failed jobs (issue 8941)
  - Fix conflicting options in postgres module (issue 8717)
  - Fix ps modules for psutil >= 0.3.0 (issue 7432)
  - Fix postgres module to return False on failure (issue 8778)
  - Fix argument passing for args with pound signs (issue 8585)
  - Fix pid of salt CLi command showing in status.pid output (issue 8720)
  - Fix rvm to run gem as the correct user (issue 8951)
  - Fix namespace issue in win_file module (issue 9060)
  - Fix masterless state paths on windows (issue 9021)
  - Fix timeout option in master config (issue 9040)
* Thu Nov 21 2013 speilicke@suse.com
- Add bugzilla for solved issues
* Fri Nov 15 2013 aboe76@gmail.com
- dropped python-urllib3 depency not in factory yet.
  only needed with saltstack helium and higher
* Thu Nov 14 2013 aboe76@gmail.com
- Updated to salt 0.17.2 Bugfix Release:
  - Add ability to delete key with grains.delval (issue 7872)
  - Fix possible state compiler stack trace (issue 5767)
  - Fix grains targeting for new grains (issue 5737)
  - Fix bug with merging in git_pillar (issue 6992)
  - Fix print_jobs duplicate results
  - Fix possible KeyError from ext_job_cache missing option
  - Fix auto_order for - names states (issue 7649)
  - Fix regression in new gitfs installs (directory not found error)
  - Fix fileclient in case of master restart (issue 7987)
  - Try to output warning if CLI command malformed (issue 6538)
  - Fix --out=quiet to actually be quiet (issue 8000)
  - Fix for state.sls in salt-ssh (issue 7991)
  - Fix for MySQL grants ordering issue (issue 5817)
  - Fix traceback for certain missing CLI args (issue 8016)
  - Add ability to disable lspci queries on master (issue 4906)
  - Fail if sls defined in topfile does not exist (issue 5998)
  - Add ability to downgrade MySQL grants (issue 6606)
  - Fix ssh_auth.absent traceback (issue 8043)
  - Fix ID-related issues (issue 8052, issue 8050, and others)
  - Fix for jinja rendering issues (issue 8066 and issue 8079)
  - Fix argument parsing in salt-ssh (issue 7928)
  - Fix some GPU detection instances (issue 6945)
  - Fix bug preventing includes from other environments in SLS files
  - Fix for kwargs with dashes (issue 8102)
  - Fix apache.adduser without apachectl (issue 8123)
  - Fix issue with evaluating test kwarg in states (issue 7788)
  - Fix regression in salt.client.Caller() (issue 8078)
  - Fix bug where cmd.script would try to run even if caching failed (issue 7601)
  - Fix for mine data not being updated (issue 8144)
  - Fix a Xen detection edge case (issue 7839)
  - Fix version generation for when it's part of another git repo (issue 8090)
  - Fix _handle_iorder stacktrace so that the real syntax error is shown (issue 8114 and issue 7905)
  - Fix git.latest state when a commit SHA is used (issue 8163)
  - Fix for specifying identify file in git.latest (issue 8094)
  - Fix for --output-file CLI arg (issue 8205)
  - Add ability to specify shutdown time for system.shutdown (issue 7833)
  - Fix for salt version using non-salt git repo info (issue 8266)
  - Add additional hints at impact of pkgrepo states when test=True (issue 8247)
  - Fix for salt-ssh files not being owned by root (issue 8216)
  - Fix retry logic and error handling in fileserver (related to issue 7755)
  - Fix file.replace with test=True (issue 8279)
  - Add flag for limiting file traversal in fileserver (issue 6928)
  - Fix for extra mine processes (issue 5729)
  - Fix for unloading custom modules (issue 7691)
  - Fix for salt-ssh opts (issue 8005 and issue 8271)
  - Fix compound matcher for grains (issue 7944)
  - Add dir_mode to file.managed (issue 7860)
  - Improve traceroute support for FreeBSD and OS X (issue 4927)
  - Fix for matching minions under syndics (issue 7671)
  - Improve exception handling for missing ID (issue 8259)
  - Add configuration option for minion_id_caching
  - Fix open mode auth errors (issue 8402)
* Sun Nov 10 2013 aboe76@gmail.com
- In preparation of salt Helium all requirements of salt-cloud
  absorbed in salt
* Fri Nov  1 2013 aboe76@gmail.com
- Added salt-doc package with html documentation of salt
* Thu Oct 31 2013 aboe76@gmail.com
- Disabled salt unit test, new test assert value not in 0.17.1
* Mon Oct 21 2013 aboe76@gmail.com
- Updated requirements python-markupsafe required for salt-ssh
* Fri Oct 18 2013 p.drouand@gmail.com
- Don't support sysvinit and systemd for the same system; add conditionnal
  macros to use systemd only on systems which support it and sysvinit
  on other systems
* Thu Oct 17 2013 aboe76@gmail.com
- Updated to salt 0.17.1 bugfix release (bnc#849205, bnc#849204, bnc#849184):
  - Fix symbolic links in thin.tgz (:issue:`7482`)
  - Pass env through to file.patch state (:issue:`7452`)
  - Service provider fixes and reporting improvements (:issue:`7361`)
  - Add --priv option for specifying salt-ssh private key
  - Fix salt-thin's salt-call on setuptools installations (:issue:`7516`)
  - Fix salt-ssh to support passwords with spaces (:issue:`7480`)
  - Fix regression in wildcard includes (:issue:`7455`)
  - Fix salt-call outputter regression (:issue:`7456`)
  - Fix custom returner support for startup states (:issue:`7540`)
  - Fix value handling in augeas (:issue:`7605`)
  - Fix regression in apt (:issue:`7624`)
  - Fix minion ID guessing to use socket.getfqdn() first (:issue:`7558`)
  - Add minion ID caching (:issue:`7558`)
  - Fix salt-key race condition (:issue:`7304`)
  - Add --include-all flag to salt-key (:issue:`7399`)
  - Fix custom grains in pillar (part of :issue:`5716`, :issue:`6083`)
  - Fix race condition in salt-key (:issue:`7304`)
  - Fix regression in minion ID guessing, prioritize socket.getfqdn() (:issue:`7558`)
  - Cache minion ID on first guess (:issue:`7558`)
  - Allow trailing slash in file.directory state
  - Fix reporting of file_roots in pillar return (:issue:`5449` and :issue:`5951`)
  - Remove pillar matching for mine.get (:issue:`7197`)
  - Sanitize args for multiple execution modules
  - Fix yumpkag mod_repo functions to filter hidden args (:issue:`7656`)
  - Fix conflicting IDs in state includes (:issue:`7526`)
  - Fix mysql_grants.absent string formatting issue (:issue:`7827`)
  - Fix postgres.version so it won't return None (:issue:`7695`)
  - Fix for trailing slashes in mount.mounted state
  - Fix rogue AttributErrors in the outputter system (:issue:`7845`)
  - Fix for incorrect ssh key encodings resulting in incorrect key added (:issue:`7718`)
  - Fix for pillar/grains naming regression in python renderer (:issue:`7693`)
  - Fix args/kwargs handling in the scheduler (:issue:`7422`)
  - Fix logfile handling for file://, tcp:// and udp:// (:issue:`7754`)
  - Fix error handling in config file parsing (:issue:`6714`)
  - Fix RVM using sudo when running as non-root user (:issue:`2193`)
  - Fix client ACL and underlying logging bugs (:issue:`7706`)
  - Fix scheduler bug with returner (:issue:`7367`)
  - Fix user management bug related to default groups (:issue:`7690`)
  - Fix various salt-ssh bugs (:issue:`7528`)
  - Many various documentation fixes
* Thu Oct  3 2013 aboe76@gmail.com
- Updated init files to be inline with fedora/rhel packaging upstream
* Mon Sep 30 2013 aboe76@gmail.com
- Cleaned up spec file:
- Unit testing can be done on all distributions
* Sat Sep 28 2013 aboe76@gmail.com
- Updated package following salt package guidelins:
  https://github.com/saltstack/salt/blob/develop/doc/topics/conventions/packaging.rst
- activated salt-testing for unit testing salt before releasing rpm
- updated docs
- added python-xml as dependency
* Thu Sep 19 2013 aboe76@gmail.com
- Updated 0.17.0 Feature Release
  Major features:
  - halite (web Gui)
  - salt ssh (remote execution/states over ssh) with its own package
  - Rosters (list system targets not know to master)
  - State Auto Order (state evaluation and execute in order of define)
  - state.sls Runner (system orchestration from within states via master)
  - Mercurial Fileserver Backend
  - External Logging Handlers (sentry and logstash support)
  - Jenkins Testing
  - Salt Testing Project (testing libraries for salt)
  - StormPath External Authentication support
  - LXC Support (lxc support for salt-virt)
  - Package dependencies reordering:
  * salt-master requires python-pyzmq, and recommends python-halite
  * salt-minion requires python-pyzmq
  * salt-ssh requires sshpass
  * salt-syndic requires salt-master
  Minor features:
  - 0.17.0 release wil be last release for 0.XX.X numbering system
    Next release will be <Year>.<Month>.<Minor>
* Sat Sep  7 2013 aboe76@gmail.com
- Update 0.16.4 bugfix release:
  - Multiple documentation improvements/additions
  - Added the osfinger and osarch grains
  - Fix bug in :mod:`hg.latest <salt.states.hg.latest>` state
  that would erroneously delete directories (:issue:`6661`)
  - Fix bug related to pid not existing for
  :mod:`ps.top <salt.modules.ps.top>` (:issue:`6679`)
  - Fix regression in :mod:`MySQL returner <salt.returners.mysql>`
  (:issue:`6695`)
  - Fix IP addresses grains (ipv4 and ipv6) to include all addresses
  (:issue:`6656`)
  - Fix regression preventing authenticated FTP (:issue:`6733`)
  - Fix :mod:`file.contains <salt.modules.file.contains>` on values
  YAML parses as non-string (:issue:`6817`)
  - Fix :mod:`file.get_gid <salt.modules.file.get_gid>`,
  :mod:`file.get_uid <salt.modules.file.get_uid>`, and
  :mod:`file.chown <salt.modules.file.chown>` for broken symlinks
  (:issue:`6826`)
  - Fix comment for service reloads in service state (:issue:`6851`)
* Fri Aug  9 2013 aboe76@gmail.com
- Update 0.16.3 bugfix release:
  - Fixed scheduler config in pillar
  - Fixed default value for file_recv master config option
  - Fixed missing master configuration file parameters
  - Fixed regression in binary package installation on 64-bit systems
  - Fixed stackgrace when commenting a section in top.sls
  - Fixed state declarations not formed as a list message.
  - Fixed infinite loop on minion
  - Fixed stacktrace in watch when state is 'prereq'
  - Feature: function filter_by to grains module
  - Feature: add new "osfinger" grain
* Sat Aug  3 2013 aboe76@gmail.com
- Fixed regression bug in salt 0.16.2
  - Newly installed salt-minion doesn't create
    /var/cache/salt/minion/proc
  - fix let package create this directory
    next version of Salt doesn't need this.
* Fri Aug  2 2013 aboe76@gmail.com
- Updated to salt 0.16.2
  - gracefully handle lsb_release data when it is enclosed in quotes
  - fixed pillar load from master config
  - pillar function pillar.item and pillar.items instead of pillar.data
  - fixed traceback when pillar sls is malformed
  - gracefully handle quoted publish commands
  - publich function publish.item and publish.items instead of publish.data
  - salt-key usage in minionswarm script fixed
  - minion random reauth_delay added to stagger re-auth attempts.
  - improved user and group management
  - improved file management
  - improved package management
  - service management custom initscripts support
  - module networking hwaddr renamed to be in line with other modules
  - fixed traceback in bridge.show
  - fixed ssh know_hosts and auth.present output.
  for more information: http://docs.saltstack.com/topics/releases/0.16.2.html
* Mon Jul 29 2013 aboe76@gmail.com
- removed not needed requirements:
  Requires(pre): /usr/sbin/groupadd
  Requires(pre): /usr/sbin/useradd
  Requires(pre): /usr/sbin/userdel
* Mon Jul 29 2013 aboe76@gmail.com
- Updated to salt 0.16.1
  - Bugfix release
  - postgresql module Fixes #6352.
  - returner fixes Fixes issue #5518
  - http authentication issues fixed  #6356
  - warning of deprecation runas in favor of user
- more information at https://github.com/saltstack/salt/commits/v0.16.1
* Fri Jul  5 2013 aboe76@gmail.com
- Updated init files, rc_status instead of rc status.
* Tue Jul  2 2013 aboe76@gmail.com
- Update to salt 0.16.0 final
  - Multi-Master capability
  - Prereq, the new requisite
  - Peer system improvement
  - Relative Includes
  - More state Output Options
  - Improved Windows Support
  - Multi Targets for pkg.removed, pgk.purged States
  - Random Times in cron states
  - Confirmation Prompt on Key acceptance on master
- full changelog details: http://docs.saltstack.com/topics/releases/0.16.0.html
* Sat Jun 22 2013 aboe76@gmail.com
- Updated to salt 0.16.0RC
- New Features in 0.16.0:
  - Multi-Master capability
  - Prereq, the new requisite
  - Peer system improvement
  - Relative Includes
  - More state Output Options
  - Improved Windows Support
  - Multi Targets for pkg.removed, pgk.purged States
  - Random Times in cron states
  - Confirmation Prompt on Key acceptance on master
- full changelog details: http://docs.saltstack.com/topics/releases/0.16.0.html
* Wed Jun 12 2013 aboe76@gmail.com
- Updated init files from upstream, so init files are the same for
  fedora/redhat/centos/debian/suse
- Removed salt user and daemon.conf file, so package is in line
  with upstream packages fedora/centos/debian.
* Sun Jun  2 2013 aboe76@gmail.com
- minor permission fix on salt config files to fix external auth
* Sat Jun  1 2013 aboe76@gmail.com
- Service release 0.15.3
  showstoppers from 0.15.2:
  - mine fix cross validity.
  - redhat package issue
  - pillar refresh fix
* Wed May 29 2013 aboe76@gmail.com
- Service release 0.15.2
  xinetd service name not appended
  virt-module uses qemu-img
  publish.publish returns same info as salt-master
  updated gitfs module
* Mon May 27 2013 aboe76@gmail.com
- Fixed salt-master config file not readable by user 'salt'
* Mon May 27 2013 aboe76@gmail.com
- Updated package spec: security enhancement.
  added system user salt to run salt-master under privileged user 'salt'
  added config dirs, master.d/minion.d/syndic.d to add config files.
  added salt-daemon.conf were salt user is specified under salt-master.
* Sun May 12 2013 aboe76@gmail.com
- Updated package spec, for systemd unit files
  according to how systemd files needs to be packaged
- added logrotate on salt log files
- fixed rpmlint complain about reload function in init files
* Wed May  8 2013 aboe76@gmail.com
- Updated to salt 0.15.1
- bugfix release.
- fixes suse service check
* Sat May  4 2013 aboe76@gmail.com
- Updated to salt 0.15.0
  Major update:
  - salt mine function
  - ipv6 support
  - copy files from minions to master
  - better template debugging
  - state event firing
  - major syndic updates
  - peer system updates
  - minion key revokation
  - function return codes
  - functions in overstate
  - Pillar error reporting
  - Cached State Data
  - Monitoring states
- Read http://docs.saltstack.com/topics/releases/0.15.0.html for more information
- improved init files overwrite with /etc/default/salt
* Tue Apr 23 2013 aboe76@gmail.com
- Updated init files:
- removed probe/reload/force reload
  this isn't supported
* Sun Apr 14 2013 aboe76@gmail.com
- Updated init files
* Sun Apr 14 2013 aboe76@gmail.com
- Updated to 0.14.1 bugfix release:
- some major fixes for the syndic system,
- fixes to file.recurse and external auth and
- fixes for windows
* Thu Apr 11 2013 aboe76@gmail.com
- Updated salt init files with option -d to really daemonize it
* Sat Mar 23 2013 aboe76@gmail.com
- Updated to 0.14.0
  MAJOR FEATURES:
  - Salt - As a Cloud Controller
  - Libvirt State
  - New get Functions
* Tue Mar 19 2013 aboe76@gmail.com
- Updated to 0.13.3
  Last Bugfixes release before 0.14.0
* Wed Mar 13 2013 aboe76@gmail.com
- Updated 0.13.2
  Bugfixes release (not specified)
* Mon Feb 25 2013 aboe76@gmail.com
- Updated spec file, postun removal of init.d files
* Sat Feb 16 2013 aboe76@gmail.com
- Updated to Salt 0.13.1 bugfixes:
- Fix #3693 (variable ref'ed before assignment)
- Fix stack trace introduced with
- Updated limit to be escaped like before and after.
- Import install command from setuptools if we use them.
- Fix user info not displayed correctly when group doesn't map cleanly
- fix bug: Client.cache_dir()
- Fix #3717
- Fix #3716
- Fix cmdmod.py daemon error
- Updated test to properly determine homebrew user
- Fixed whitespace issue
* Thu Feb 14 2013 aboe76@gmail.com
- Updated to salt 0.13.0
* Wed Jan 30 2013 aboe76@gmail.com
- Updated Suse Copyright in Spec-file
* Mon Jan 28 2013 toddrme2178@gmail.com
- Cleanup spec file
* Sat Jan 26 2013 aboe76@gmail.com
- split syndic from master in separate package
* Tue Jan 22 2013 aboe76@gmail.com
- updated to salt 0.12.1 bugfix release
* Wed Jan 16 2013 aboe76@gmail.com
- uploaded to salt 1.12.0