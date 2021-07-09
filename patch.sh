#dnf -y install \
#


# Fixes waiting for merge:

# cobbler fix for AlmaLinux/Rocky Linux.
curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/cobbler/utils.py > /usr/lib/python3.6/site-packages/cobbler/utils.py
curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/cobbler/distro_signatures.json > /var/lib/cobbler/distro_signatures.json
