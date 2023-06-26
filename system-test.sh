set -ex
export LOG=/var/log/uyuni-system-test.log
echo "Output will be logged to $LOG"

if [ "$1" = "force" ]; then
  echo "Continue on error"
  set +e
fi

if [ "$1" = "install" ]; then
# Use curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/system-test.sh | bash -s -- install
  echo "Installing Uyuni (low verbosity)"
  curl -s https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/install9.sh | bash >> $LOG
  echo "Testing for broken Symlinks"
  find /usr/share/tomcat/webapps/rhn/WEB-INF/lib -xtype l
  find /usr/share/spacewalk/taskomatic/ -xtype l
  /usr/lib/susemanager/bin/mgr-setup -s
fi





# This script executes an Uyuni System test after a basic installation (no company/user set up).

echo "Create First User (don't check certificate)"
curl -s 'https://localhost/rhn/newlogin/CreateFirstUser.do' --insecure --data-raw 'submitted=true&orgName=Clacee&login=admin&desiredpassword=admin&desiredpasswordConfirm=admin&email=uyuni-admin%40example.com&prefix=+&firstNames=Uyuni&lastName=Administrator'

# Store credentials
spacecmd -u admin -p admin -- whoami 2>> /var/log/uyuni-system-test.log

# Create Repositories, Channels and Activation Keys
/usr/bin/spacewalk-common-channels -u admin -p admin -k unlimited -a x86_64 'almalinux9' 2>> /var/log/uyuni-system-test.log
## AppStream is not required for EL9 (I believe)
/usr/bin/spacewalk-common-channels -u admin -p admin -k unlimited -a x86_64 'almalinux9-uyuni-client' 2>> /var/log/uyuni-system-test.log
/usr/bin/spacewalk-common-channels -u admin -p admin -k unlimited -a x86_64 'almalinux9-appstream' 2>> /var/log/uyuni-system-test.log

echo "Synchronise Base channel with kickstart"
# The next line might fail if done late/early as Uyuni will start autosyncing
spacecmd -- softwarechannel_syncrepos almalinux9-x86_64 --sync-kickstart 2>> /var/log/uyuni-system-test.log


echo "Configure Activation key"
spacecmd -- activationkey_addentitlements 1-almalinux9-x86_64 ansible_control_node 2>> /var/log/uyuni-system-test.log
spacecmd -- activationkey_addentitlements 1-almalinux9-x86_64 container_build_host 2>> /var/log/uyuni-system-test.log
spacecmd -- activationkey_addentitlements 1-almalinux9-x86_64 monitoring_entitled 2>> /var/log/uyuni-system-test.log
spacecmd -- activationkey_addentitlements 1-almalinux9-x86_64 osimage_build_host 2>> /var/log/uyuni-system-test.log
spacecmd -- activationkey_addentitlements 1-almalinux9-x86_64 virtualization_host 2>> /var/log/uyuni-system-test.log

if [[ ! $(which tftpd) ]]; then
dnf -yq install tftp
fi

echo "Configure Autosetup distribution"
echo "Waiting for kickstart to be synchronised..."
until $( spacecmd -- kickstart_create "-n almalinux9-x86_64" "-d External_-_AlmaLinux_9_x86_64" "-p admin" "-v none" 2>> /var/log/uyuni-system-test.log );
do
	if [[ $(spacecmd -- kickstart_create '-n almalinux9-x86_64' '-d External_-_AlmaLinux_9_x86_64' '-p admin' '-v none' 2>&1 | grep "Autoinstallation label already exists:") ]]; then 
		echo "Autoinstallation label already exists. Continuing"
		break
	fi;
	PID=$(ps -ef | grep -m 1 spacewalk-repo | tr -s ' ' | cut -d ' ' -f2)
	tail --pid $PID  -f /var/log/rhn/reposync/*.log
	sleep 60;
done;

echo "Adding child channels to kickstart base channel"
spacecmd -- kickstart_addchildchannels almalinux9-x86_64 almalinux9-uyuni-client-x86_64
spacecmd -- kickstart_addchildchannels almalinux9-x86_64  almalinux9-x86_64-appstream 

echo "mgr-create-bootstrap-repo"
mgr-create-bootstrap-repo -c almalinux-9-x86_64-uyuni >> $LOG

# Test cobbler files
tftp localhost <<'EOF'
get pxelinux.0
get ldlinux.c32
get pxelinux.cfg/default
get menu.c32
get libutil.c32
EOF

echo "Done"

set +e
