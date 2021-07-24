#dnf -y install \
#


# Fixes waiting for merge:

# cobbler fix for AlmaLinux/Rocky Linux.
curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/cobbler/utils.py > /usr/lib/python3.6/site-packages/cobbler/utils.py
curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/cobbler/distro_signatures.json > /var/lib/cobbler/distro_signatures.json

# https://github.com/SUSE/smdba/pull/49
curl https://raw.githubusercontent.com/sbluhm/smdba/dev-eladaption/src/smdba/postgresqlgate.py > /usr/lib/python3.6/site-packages/smdba/postgresqlgate.py

# https://github.com/uyuni-project/uyuni/pull/3988
dnf -y install https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/02347846-spacewalk-selinux/spacewalk-selinux-2.8.6-1.el8.noarch.rpm
