#dnf -y install \

# Unclear what to do with these packages. Will keep them here for now:
dnf -y install py26-compat-tornado py26-compat-msgpack-python # will be added to requirements later


# Fixes waiting for merge:

# cobbler fix for AlmaLinux/Rocky Linux.
# Uyuni will start shipping cobbler 3.3. EPEL 8 must be updated with upstream 3.2
curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/cobbler/utils.py > /usr/lib/python3.6/site-packages/cobbler/utils.py
curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/cobbler/distro_signatures.json > /var/lib/cobbler/distro_signatures.json

# https://github.com/SUSE/smdba/pull/49
curl https://raw.githubusercontent.com/sbluhm/smdba/dev-eladaption/src/smdba/postgresqlgate.py > /usr/lib/python3.6/site-packages/smdba/postgresqlgate.py

# https://github.com/uyuni-project/uyuni/pull/3994
dnf -y install https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/02348230-susemanager/susemanager-4.3.0-0.x86_64.rpm https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/02348230-susemanager/susemanager-tools-4.3.0-0.x86_64.rpm
