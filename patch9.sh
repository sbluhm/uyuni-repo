# Fixes waiting for merge:
## Waiting for new python3-urlgrapper release (< 4.1.0-2)
sed -i "1860s#self.fo = open(self.filename, 'r')#self.fo = open(self.filename, 'rb')#" /usr/lib/python3.9/site-packages/urlgrabber/grabber.py
## BZ2188218: Update Java Softlinks for Taskomatik und Tomcat:
ln -s /usr/share/tomcat/bin/tomcat-juli.jar /usr/share/java/tomcat/tomcat-juli.jar


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

## post script does not run: https://github.com/sbluhm/uyuni/blob/77c4ee91387b297d23d18e3d90a3b07bf1502082/spacewalk/setup/spacewalk-setup.spec#L194
CURRENT_DATE=$(date +"%Y-%m-%dT%H:%M:%S.%3N")
cp /etc/tomcat/server.xml /etc/tomcat/server.xml.$CURRENT_DATE
xsltproc /usr/share/spacewalk/setup/server.xml.xsl /etc/tomcat/server.xml.$CURRENT_DATE > /etc/tomcat/server.xml


# Adding debug info
#sed -i '/log_level_logfile/d' /etc/salt/master.d/logging.conf ||:
#echo "log_level_logfile: trace" >> /etc/salt/master.d/logging.conf
echo "Java RHN logging in /usr/share/tomcat/webapps/rhn/WEB-INF/classes/log4j2.xml"

