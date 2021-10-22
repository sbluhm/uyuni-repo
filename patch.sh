#dnf -y install \

# Unclear what to do with these packages. Will keep them here for now:
dnf -y install py26-compat-tornado py26-compat-msgpack-python # will be added to requirements later


# Fixes waiting for merge:


# fix without patch yet:
ln -s /etc/cobbler/settings.yaml /etc/cobbler/settings

echo "bootloaders_dir: '/usr/share/syslinux'" >> /etc/cobbler/settings.yaml
#cobbler sync
# /usr/share/cobbler/bin/mkgrub.sh # <-- should be this instead of cobbler sync. Code currently to be refactored and doesnt work anyways so only keeping for reference.

# Adding debug info
echo "log_level_logfile: trace" >> /etc/salt/master.d/logging.conf

