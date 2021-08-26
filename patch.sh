#dnf -y install \

# Unclear what to do with these packages. Will keep them here for now:
dnf -y install py26-compat-tornado py26-compat-msgpack-python # will be added to requirements later


# Fixes waiting for merge:
# Cobbler setup fix #4166 
curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/tmp/rhn.conf > /usr/share/rhn/config-defaults/rhn.conf


# cobbler fix for AlmaLinux/Rocky Linux.
# Uyuni will start shipping cobbler 3.3. EPEL 8 must be updated with upstream 3.2
curl https://raw.githubusercontent.com/cobbler/cobbler/release32/cobbler/utils.py > /usr/lib/python3.6/site-packages/cobbler/utils.py
curl https://raw.githubusercontent.com/cobbler/cobbler/release32/config/cobbler/distro_signatures.json > /var/lib/cobbler/distro_signatures.json


