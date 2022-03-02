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

# Oracle Linux only patch until cobbler 3.3
curl https://raw.githubusercontent.com/sbluhm/cobbler/2f85610c9865ed3f393e1e441eeab952d4de7d18/cobbler/utils.py -o /usr/lib/python3.6/site-packages/cobbler/utils.py

# Random hack waiting to be fixed. Some Merge broke folders.
chmod a+w /var/log/rhn -R
sed -i 's#report-db-ca-cert=/etc/pki/trust/anchors/RHN-ORG-TRUSTED-SSL-CERT#report-db-ca-cert=/etc/pki/ca-trust/source/anchors/RHN-ORG-TRUSTED-SSL-CERT#' /usr/lib/susemanager/bin/mgr-setup

