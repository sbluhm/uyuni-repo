set -e
if [ "$1" = "install" ]; then
  echo "Installing Uyuni"
  curl -s https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/install.sh | bash >> /var/log/uyuni-system-test.log
fi




# This script executes an Uyuni System test after a basic installation (no company/user set up).

echo "Create First User (don't check certificate)"
curl -s 'https://localhost/rhn/newlogin/CreateFirstUser.do' --insecure --data-raw 'submitted=true&orgName=Clacee&login=admin&desiredpassword=admin&desiredpasswordConfirm=admin&email=uyuni-admin%40example.com&prefix=+&firstNames=Uyuni&lastName=Administrator'

# Store credentials
spacecmd -u admin -p admin -- whoami 2>> /var/log/uyuni-system-test.log

# Create Repositories, Channels and Activation Keys
/usr/bin/spacewalk-common-channels -u admin -p admin -k unlimited '*' 2>> /var/log/uyuni-system-test.log

echo "Synchronise Base channel"
# Base needs to sync first or kickstart sync will get stuck
spacecmd -- softwarechannel_syncrepos almalinux8-x86_64 2>> /var/log/uyuni-system-test.log

echo "Create kickstartable tree"
#Update repo url as mirrorlinks do not support kickstart syncs
spacecmd -- repo_updateurl "External - AlmaLinux 8 (aarch64)" http://ftp.gwdg.de/pub/linux/almalinux/8/BaseOS/x86_64/os/ 2>> /var/log/uyuni-system-test.log
spacecmd -- softwarechannel_syncrepos almalinux8-x86_64 --sync-kickstart 2>> /var/log/uyuni-system-test.log

echo "Synchronise Autosetup repo dependency (AppStream)"
spacecmd -- softwarechannel_syncrepos almalinux8-x86_64-appstream 2>> /var/log/uyuni-system-test.log 
spacecmd -- softwarechannel_syncrepos almalinux8-uyuni-client-x86_64  2>> /var/log/uyuni-system-test.log


echo "Configure Activation key"
spacecmd -- activationkey_addentitlements 1-almalinux8-x86_64 ansible_control_node 2>> /var/log/uyuni-system-test.log
spacecmd -- activationkey_addentitlements 1-almalinux8-x86_64 container_build_host 2>> /var/log/uyuni-system-test.log
spacecmd -- activationkey_addentitlements 1-almalinux8-x86_64 monitoring_entitled 2>> /var/log/uyuni-system-test.log
spacecmd -- activationkey_addentitlements 1-almalinux8-x86_64 osimage_build_host 2>> /var/log/uyuni-system-test.log
spacecmd -- activationkey_addentitlements 1-almalinux8-x86_64 virtualization_host 2>> /var/log/uyuni-system-test.log

echo "Configure Autosetup distribution"
echo "Waiting for kickstart to be synchronised..."
until $( spacecmd -- distribution_update "External_-_AlmaLinux_8_aarch64" "-p /var/spacewalk/rhn/kickstart/1/External_-_AlmaLinux_8_aarch64" "-b almalinux8-x86_64" "-t rhel_8" 2>> /var/log/uyuni-system-test.log );
do
	sleep 60;
done;
echo "Kickstart synchronised"
spacecmd -- kickstart_create "-n almalinux8-x86_64" "-d External_-_AlmaLinux_8_aarch64" "-p admin" "-v none" 2>> /var/log/uyuni-system-test.log

echo "Waiting for Appstream channel to be synchronised..."
dnf -yq install tftp

while [ `ps -A | grep repo | wc -l` > 1 ] ;
do
        sleep 60;
done;
echo "Done. Lets create the bootstrap repo"

mgr-create-bootstrap-repo -c almalinux-8-x86_64-uyuni >> /var/log/uyuni-system-test.log ||:
#sed -i 's/AppStream,//g' /var/spacewalk/rhn/kickstart/1/almalinux8-x86_64/.treeinfo

# Test cobbler files
#dnf -yq install tftp
tftp localhost <<'EOF'
get pxelinux.0
get ldlinux.c32
get pxelinux.cfg/default
get menu.c32
get libutil.c32
EOF

echo "# Somehow Autoinstall profile only works if distribution is manually saved"

echo "Done"

set +e
