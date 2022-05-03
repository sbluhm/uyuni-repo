#dnf -y install \

# Fixes waiting for merge:

# Waiting for new python3-urlgrapper release (< 4.1.0-2)
sed -i "1860s#self.fo = open(self.filename, 'r')#self.fo = open(self.filename, 'rb')#" /usr/lib/python3.9/site-packages/urlgrabber/grabber.py

# fix without patch yet:
# Required whilst reworking folders
ln -s /var/lib/susemanager /srv/susemanager

# not sure if any patches are still required. seems to work without.
sed -i 'bootloaders_dir/d' /etc/cobbler/settings.yaml ||:
echo "bootloaders_dir: '/usr/share/syslinux'" >> /etc/cobbler/settings.yaml
#cobbler sync
#/usr/share/cobbler/bin/mkgrub.sh # <-- should be this instead of cobbler sync. Code currently to be refactored and doesnt work anyways so only keeping for reference.
#mkgrub tftp boots result in Failed to load libutil.c32 and menu.c32

# Adding debug info
sed -i '/log_level_logfile/d' /etc/salt/master.d/logging.conf ||:
echo "log_level_logfile: trace" >> /etc/salt/master.d/logging.conf

# Random hack waiting to be fixed.
#chmod a+w /var/log/rhn -R

ln -s /usr/share/java/jaxb/jaxb-runtime.jar /usr/share/java/glassfish-jaxb/jaxb-runtime.jar
ln -s /usr/share/java/jaxb/txw2.jar /usr/share/java/glassfish-jaxb/txw2.jar
ln -s /usr/share/java/jaxb-istack-commons/istack-commons-runtime.jar /usr/share/java/istack-commons-runtime.jar

