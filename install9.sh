set -e
if [ "$1" = "force" ]; then
  echo "Continue on error"
  set +e
fi

DISTRIBUTION_ID="$(source /etc/os-release && echo ${ID})"
case ${DISTRIBUTION_ID} in
    centos|rhel|almalinux|rocky|ol)    DISTRIBUTION_ID='RHEL';;
    *)                        echo 'Not RHEL. Using SUSE Logic'
esac

if [ "$DISTRIBUTION_ID" = RHEL ] ; then

    subscription-manager attach ||:
    LANGPACK=glibc-langpack-de # UPDATE THIS TO THE LANGPACK OF YOUR CHOICE!
    dnf clean all
    dnf -y update
    dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm $LANGPACK # Installing EPEL and language pack
    setenforce 0 # disabling SELinux for this session.
    sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config ||: # permanently disabling SELinux
else
    sudo zypper update
fi


if [ "$DISTRIBUTION_ID" = RHEL ] ; then
    REPO_SOURCE=https://download.opensuse.org/repositories/home:/sbluhm:/branches:/systemsmanagement:/Uyuni:/Master
    dnf -y config-manager --set-enabled codeready-builder-beta-for-rhel-9-x86_64-rpms # required for dependencies
    rpm --import ${REPO_SOURCE}/CentOS-9_Stream/repodata/repomd.xml.key
    dnf -y config-manager --add-repo ${REPO_SOURCE}/CentOS-9_Stream/
    dnf -y config-manager --add-repo ${REPO_SOURCE}:/Other/CentOS-9_Stream/
    dnf -y config-manager --add-repo ${REPO_SOURCE}:/Other:/EL/CentOS-9_Stream/
    dnf -y copr enable sbluhm/python-packages-dnf
else
    sudo zypper ar https://download.opensuse.org/repositories/systemsmanagement:/Uyuni:/Master/images/repo/Uyuni-Server-POOL-$(arch)-Media1/ uyuni-server-devel
    sudo zypper ref
fi

if [ "$DISTRIBUTION_ID" = RHEL ] ; then
    NEWPACKAGES=$(curl -s https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/new-packages9.txt)  # let's get packages that are waiting to be merged
    dnf -y install patterns-uyuni_server $NEWPACKAGES  --exclude="uyuni-el9-javabuildrequirements"
    curl -s https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/patch9.sh | bash # Installs current fixes
else
    zypper in patterns-uyuni_server
fi

curl -s https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/root/setup_env.sh > /root/setup_env.sh

# Start the installation of the server now:
/usr/lib/susemanager/bin/mgr-setup -s
set +e

