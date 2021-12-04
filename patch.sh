#dnf -y install \

# Unclear what to do with these packages. Will keep them here for now:
dnf -y install py26-compat-tornado py26-compat-msgpack-python # will be added to requirements later


# Fixes waiting for merge:

# fix without patch yet:

# not sure if any patches are still required. seems to work without.
echo "bootloaders_dir: '/usr/share/syslinux'" >> /etc/cobbler/settings.yaml
#cobbler sync
#/usr/share/cobbler/bin/mkgrub.sh # <-- should be this instead of cobbler sync. Code currently to be refactored and doesnt work anyways so only keeping for reference.
#mkgrub tftp boots result in Failed to load libutil.c32 and menu.c32

# Adding debug info
echo "log_level_logfile: trace" >> /etc/salt/master.d/logging.conf

