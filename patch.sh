#dnf -y install \

# Unclear what to do with these packages. Will keep them here for now:
dnf -y install py26-compat-tornado py26-compat-msgpack-python # will be added to requirements later

# https://bugzilla.redhat.com/show_bug.cgi?id=2010567
dnf -y install https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/02876112-cobbler/cobbler-3.2.2-1.el8.noarch.rpm


# Fixes waiting for merge:
# Cobbler setup fix #4166 
curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/tmp/rhn.conf > /usr/share/rhn/config-defaults/rhn.conf


# cobbler fix for AlmaLinux/Rocky Linux.
# Uyuni will start shipping cobbler 3.3. EPEL 8 must be updated with upstream 3.2
sed -i 's/("red hat", "redhat", "scientific linux", "fedora", "centos", "virtuozzo")/("red hat", "redhat", "scientific linux", "fedora", "centos", "virtuozzo", "almalinux", "rocky linux")/' /usr/lib/python3.6/site-packages/cobbler/utils.py
sed -i 's/redhat|sl|slf|centos|oraclelinux|vzlinux/redhat|sl|slf|centos|oraclelinux|vzlinux|almalinux|rocky/' /var/lib/cobbler/distro_signatures.json


# fix without patch yet:
echo "bootloaders_dir: '/usr/share/syslinux'" >> /etc/cobbler/settings
# /usr/share/cobbler/bin/mkgrub.sh # <-- should be this instead of cobbler sync. Code currently to be refactored and doesnt work anyways so only keeping for reference.

# Adding debug info
echo "log_level_logfile: trace" > /etc/salt/master.d/logging.conf

