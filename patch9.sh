# Fixes waiting for merge:
## Waiting for new python3-urlgrapper release (< 4.1.0-2)
sed -i "1860s#self.fo = open(self.filename, 'r')#self.fo = open(self.filename, 'rb')#" /usr/lib/python3.9/site-packages/urlgrabber/grabber.py
## BZ2188218: Update Java Softlinks for Taskomatik und Tomcat:
ln -s /usr/share/tomcat/bin/tomcat-juli.jar /usr/share/java/tomcat/tomcat-juli.jar
## BZ2224420: OpenJDK 11.0.20.0.8-1 does not include tzdata-java-2023c-1 [rhel-9, openjdk-11]
dnf -y install tzdata-java-2023c


# fix without patch yet:
## Required whilst reworking folders
ln -s /var/lib/susemanager /srv/susemanager
## Issue 72 to be fixed
chown root:apache /var/log/rhn
chmod 770 /var/log/rhn
##
sed -i 's#/usr/bin/openssl genrsa -out %s 2048#/usr/bin/openssl genrsa -traditional -out %s 2048#' /usr/lib/python3.9/site-packages/certs/rhn_ssl_tool.py

# Adding debug info
#sed -i '/log_level_logfile/d' /etc/salt/master.d/logging.conf ||:
#echo "log_level_logfile: trace" >> /etc/salt/master.d/logging.conf
echo "Java RHN logging in /usr/share/tomcat/webapps/rhn/WEB-INF/classes/log4j2.xml"

