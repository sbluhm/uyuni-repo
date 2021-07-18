#dnf -y install \
#


# Fixes waiting for merge:
#PR3980
ln -sf /var/www/html/pub/RHN-ORG-TRUSTED-SSL-CERT /usr/share/susemanager/salt/certs/RHN-ORG-TRUSTED-SSL-CERT

# cobbler fix for AlmaLinux/Rocky Linux.
curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/cobbler/utils.py > /usr/lib/python3.6/site-packages/cobbler/utils.py
curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/cobbler/distro_signatures.json > /var/lib/cobbler/distro_signatures.json

# https://github.com/SUSE/smdba/pull/49
curl https://raw.githubusercontent.com/sbluhm/smdba/dev-eladaption/src/smdba/postgresqlgate.py > /usr/lib/python3.6/site-packages/smdba/postgresqlgate.py
