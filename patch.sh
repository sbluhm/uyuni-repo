#dnf -y install \

# Unclear what to do with these packages. Will keep them here for now:
#dnf -y install py26-compat-tornado py26-compat-msgpack-python # will be added to requirements later
# Required for salt-ssh (for now) and SLES11SP4 LTSS 


# Fixes waiting for merge:
# PR4773
curl https://raw.githubusercontent.com/uyuni-project/uyuni/7ae9763328b9916edf798c7f9d189abd11d2827e/spacewalk/certs-tools/mgr_ssl_cert_setup.py -o /usr/lib/python3.6/site-packages/certs/mgr_ssl_cert_setup.py

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
mkdir -p /etc/pki/trust/
ln -s /etc/pki/ca-trust/source/anchors /etc/pki/trust/anchors ||:
echo "/usr/bin/update-ca-trust extract" > /usr/sbin/update-ca-certificates
chmod a+x /usr/sbin/update-ca-certificates
##sed -i 's#report_db_sslrootcert = /etc/pki/trust/anchors/RHN-ORG-TRUSTED-SSL-CERT#report_db_sslrootcert = /etc/pki/ca-trust/source/anchors/RHN-ORG-TRUSTED-SSL-CERT#' /usr/share/rhn/config-defaults/rhn.conf

systemctl stop firewalld ||:
systemctl disable firewalld ||:
