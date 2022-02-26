#dnf -y install \

# Fixes waiting for merge:
# PR4623
curl https://raw.githubusercontent.com/sbluhm/uyuni/fix-4614/backend/server/importlib/headerSource.py -o /usr/lib/python3.6/site-packages/spacewalk/server/importlib/headerSource.py

# Waiting for new python3-urlgrapper release (< 4.1.0-2)
sed -i "1860s#self.fo = open(self.filename, 'r')#self.fo = open(self.filename, 'rb')#" /usr/lib/python3.6/site-packages/urlgrabber/grabber.py

# fix without patch yet:
# Required whilst reworking folders
ln -s /var/lib/susemanager /srv/susemanager

# not sure if any patches are still required. seems to work without.
echo "bootloaders_dir: '/usr/share/syslinux'" >> /etc/cobbler/settings.yaml
#cobbler sync
#/usr/share/cobbler/bin/mkgrub.sh # <-- should be this instead of cobbler sync. Code currently to be refactored and doesnt work anyways so only keeping for reference.
#mkgrub tftp boots result in Failed to load libutil.c32 and menu.c32

# Adding debug info
echo "log_level_logfile: trace" >> /etc/salt/master.d/logging.conf

# Random hack waiting to be fixed. Some Merge broke folders.
#mkdir -p /etc/pki/trust/
#ln -s /etc/pki/ca-trust/source/anchors /etc/pki/trust/anchors ||:
##sed -i 's#report_db_sslrootcert = /etc/pki/trust/anchors/RHN-ORG-TRUSTED-SSL-CERT#report_db_sslrootcert = /etc/pki/ca-trust/source/anchors/RHN-ORG-TRUSTED-SSL-CERT#' /usr/share/rhn/config-defaults/rhn.conf
chmod a+w /var/log/rhn -R
#sed -i 's#CA_CERT=/etc/pki/trust/anchors/RHN-ORG-TRUSTED-SSL-CERT#CA_CERT=/etc/pki/ca-trust/source/anchors/RHN-ORG-TRUSTED-SSL-CERT#' /usr/bin/uyuni-setup-reportdb
#sed -i 's#report-db-ca-cert=/etc/pki/trust/anchors/RHN-ORG-TRUSTED-SSL-CERT#report-db-ca-cert=/etc/pki/ca-trust/source/anchors/RHN-ORG-TRUSTED-SSL-CERT#' /usr/lib/susemanager/bin/mgr-setup
# test if above is fixed for issue sbluhm/71 (via https://github.com/uyuni-project/uyuni/pull/4868)

