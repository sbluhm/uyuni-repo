#dnf -y install \

# Unclear what to do with these packages. Will keep them here for now:
dnf -y install py26-compat-tornado py26-compat-msgpack-python # will be added to requirements later


# Fixes waiting for merge:

# cobbler fix for AlmaLinux/Rocky Linux.
# Uyuni will start shipping cobbler 3.3. EPEL 8 must be updated with upstream 3.2
curl https://raw.githubusercontent.com/cobbler/cobbler/release32/cobbler/utils.py > /usr/lib/python3.6/site-packages/cobbler/utils.py
curl https://raw.githubusercontent.com/cobbler/cobbler/release32/config/cobbler/distro_signatures.json > /var/lib/cobbler/distro_signatures.json

# https://github.com/SUSE/smdba/pull/49
# Waiting for release and integration into OBS
curl https://raw.githubusercontent.com/SUSE/smdba/master/src/smdba/postgresqlgate.py > /usr/lib/python3.6/site-packages/smdba/postgresqlgate.py

