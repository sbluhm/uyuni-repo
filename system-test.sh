set -e
if [ "$1" = "install" ]; then
  echo "Installing Uyuni"
  curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/install.sh | bash
fi




# This script executes an Uyuni System test after a basic installation (no company/user set up).

echo "Create First User (don't check certificate)"
curl 'https://localhost/rhn/newlogin/CreateFirstUser.do' --insecure --data-raw 'submitted=true&orgName=Clacee&login=admin&desiredpassword=admin&desiredpasswordConfirm=admin&email=uyuni-admin%40example.com&prefix=+&firstNames=Uyuni&lastName=Administrator'

# Store credentials
spacecmd -u admin -p admin -- whoami

echo "Add AlmaLinux repositories"
spacecmd -- repo_create --name "almalinux8-baseos-x86_64" --url "https://rsync.repo.almalinux.org/almalinux/8/BaseOS/x86_64/os/"
spacecmd -- repo_create --name "almalinux8-appstream-x86_64" --url "https://rsync.repo.almalinux.org/almalinux/8/AppStream/x86_64/os/"
spacecmd -- repo_create --name "almalinux8-powertools-x86_64" --url "https://rsync.repo.almalinux.org/almalinux/8/PowerTools/x86_64/os/"
spacecmd -- repo_create --name "rhel8-epel-x86_64" --url "https://mirror.dogado.de/fedora-epel/8/Everything/x86_64/"
spacecmd -- repo_create --name "el8-uyuni-client-tools-x86_64" --url "https://download.opensuse.org/repositories/systemsmanagement:/Uyuni:/Stable:/EL8-Uyuni-Client-Tools/EL_8/"


echo "Add Channel structure"
spacecmd -- softwarechannel_create -n "AlmaLinux 8 (x86_64)" -l "almalinux8-x86_64" -s "AlmaLinux 8 (x86_64)"
spacecmd -- softwarechannel_create -n "AlmaLinux 8 BaseOS (x86_64)" -l "almalinux8-baseos-x86_64" -s "AlmaLinux 8 BaseOS (x86_64)" -p "almalinux8-x86_64"
spacecmd -- softwarechannel_create -n "AlmaLinux 8 AppStream (x86_64)" -l "almalinux8-appstream-x86_64" -s "AlmaLinux 8 Appstream (x86_64)" -p "almalinux8-x86_64"
spacecmd -- softwarechannel_create -n "AlmaLinux 8 PowerTools (x86_64)" -l "almalinux8-powertools-x86_64" -s "AlmaLinux 8 PowerTools (x86_64)" -p "almalinux8-x86_64"
spacecmd -- softwarechannel_create -n "EL 8 Uyuni Client Tools (x86_64)" -l "el8-uyuni-client-tools-x86_64" -s "EL 8 Uyuni Client Tools (x86_64)" -p "almalinux8-x86_64"
spacecmd -- softwarechannel_create -n "RHEL8 EPEL (x86_64)" -l "rhel8-epel-x86_64" -s "RHEL8 EPEL (x86_64)" -p "almalinux8-x86_64"

echo "Configure channels"
spacecmd -- softwarechannel_addrepo almalinux8-baseos-x86_64 almalinux8-baseos-x86_64
spacecmd -- softwarechannel_addrepo almalinux8-appstream-x86_64 almalinux8-appstream-x86_64
spacecmd -- softwarechannel_addrepo almalinux8-powertools-x86_64 almalinux8-powertools-x86_64
spacecmd -- softwarechannel_addrepo el8-uyuni-client-tools-x86_64 el8-uyuni-client-tools-x86_64
spacecmd -- softwarechannel_addrepo rhel8-epel-x86_64 rhel8-epel-x86_64

echo "Synchronise Base channel"
# disable below to see if necessary.
#spacecmd -- softwarechannel_syncrepos almalinux8-baseos-x86_64

echo "Create kickstartable tree"
spacecmd -- softwarechannel_syncrepos almalinux8-baseos-x86_64 --sync-kickstart

echo "Synchronise Autosetup repo dependency (AppStream)"
spacecmd -- softwarechannel_syncrepos almalinux8-appstream-x86_64
spacecmd -- softwarechannel_syncrepos el8-uyuni-client-tools-x86_64

echo "Configure Autosetup distribution"
until $( spacecmd -- distribution_update "almalinux8-baseos-x86_64" "-p /var/spacewalk/rhn/kickstart/1/almalinux8-baseos-x86_64" "-b almalinux8-baseos-x86_64" "-t rhel_8" );
do
	sleep 60;
done;
spacecmd -- kickstart_create "-n almalinux8-x86_64" "-d almalinux8-baseos-x86_64" "-p admin" "-v none"
echo "Done"

set +e
