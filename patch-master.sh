# Fixes waiting for merge:
## Waiting for new python3-urlgrapper release (< 4.1.0-2)
sed -i "1860s#self.fo = open(self.filename, 'r')#self.fo = open(self.filename, 'rb')#" /usr/lib/python3.9/site-packages/urlgrabber/grabber.py


# fix without patch yet:
## Required whilst reworking folders
ln -s /var/lib/susemanager /srv/susemanager
## Issue 72 to be fixed
chown root:apache /var/log/rhn
chmod 770 /var/log/rhn
##
sed -i 's#/usr/bin/openssl genrsa -out %s 2048#/usr/bin/openssl genrsa -traditional -out %s 2048#' /usr/lib/python3.9/site-packages/certs/rhn_ssl_tool.py
mkdir /usr/share/java/javassist/
ln -s /usr/share/java/javassist.jar /usr/share/java/javassist/javassist.jar
##
sed -i '/ca-certificates.service/d'  /usr/lib/systemd/system/uyuni-check-database.service
echo "ExecStartPre=/usr/bin/update-ca-trust" >> /usr/lib/systemd/system/uyuni-check-database.service
systemctl daemon-reload
##
sed -i 's/yum_src/yum_dnf_src/' /usr/lib/python3.9/site-packages/spacewalk/satellite_tools/repo_plugins/uln_src.py
## PR8031
curl https://raw.githubusercontent.com/sbluhm/uyuni/fixULN/python/spacewalk/satellite_tools/repo_plugins/yum_dnf_src.py > /usr/lib/python3.9/site-packages/spacewalk/satellite_tools/repo_plugins/yum_dnf_src.py
## Workaround: Replace empty certificate file. Might have to be done regularly or even after setup
cp /var/www/html/pub/RHN-ORG-TRUSTED-SSL-CERT /usr/share/susemanager/salt/certs/RHN-ORG-TRUSTED-SSL-CERT



# Adding debug info
#sed -i '/log_level_logfile/d' /etc/salt/master.d/logging.conf ||:
#echo "log_level_logfile: trace" >> /etc/salt/master.d/logging.conf
echo "Java RHN logging in /usr/share/tomcat/webapps/rhn/WEB-INF/classes/log4j2.xml"

if [[ ! $(hostname -f)  =~ \. ]]; then echo -e "\n\n\n";echo '--> !!!WARNING!!! Set the a fully qualified hostname via "hostnamectl set-hostname <FQDN>" first !!! <--'; echo -e "\n\n\n";fi
