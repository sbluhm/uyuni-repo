set -e
LANGPACK=glibc-langpack-de # UPDATE THIS TO THE LANGPACK OF YOUR CHOICE!
dnf clean all
dnf -y update
dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm $LANGPACK # Installing EPEL and language pack
setenforce 0 # disabling SELinux for this session.
sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config # permanently disabling SELinux

REPO_SOURCE=https://download.opensuse.org/repositories/systemsmanagement:/Uyuni:/Master

dnf -y config-manager --set-enabled powertools # required for dependencies
rpm --import https://build.opensuse.org/projects/systemsmanagement:Uyuni:Master/public_key
dnf -y config-manager --add-repo ${REPO_SOURCE}/AlmaLinux_8/
dnf -y config-manager --add-repo ${REPO_SOURCE}:/Other/AlmaLinux_8/
dnf -y config-manager --add-repo ${REPO_SOURCE}:/Other:/EL/AlmaLinux_8/
#zypper ar https://download.opensuse.org/repositories/systemsmanagement:/Uyuni:/Master/images/repo/Uyuni-Server-POOL-$(arch)-Media1/ uyuni-server-devel

dnf -y module enable postgresql:13 javapackages-tools cobbler pki-deps
dnf -y module disable satellite-5-client rhn-tools # Don't use Spacewalk packages.

NEWPACKAGES=$(curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/new-packages.txt)  # let's get packages that are waiting to be merged
dnf -y install patterns-uyuni_server $NEWPACKAGES
#zypper in patterns-uyuni_server

curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/root/setup_env.sh > /root/setup_env.sh
curl https://raw.githubusercontent.com/sbluhm/uyuni-repo/master/patch.sh | bash # Installs current fixes

# Start the installation of the server now:
/usr/lib/susemanager/bin/mgr-setup -s
set +e

