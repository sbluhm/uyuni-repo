# Fixes waiting for merge:
## Waiting for new python3-urlgrapper release (< 4.1.0-2)
sed -i "1860s#self.fo = open(self.filename, 'r')#self.fo = open(self.filename, 'rb')#" /usr/lib/python3.9/site-packages/urlgrabber/grabber.py
## BZ2188218: Update Java Softlinks for Taskomatik und Tomcat:
ln -s /usr/share/tomcat/bin/tomcat-juli.jar /usr/share/java/tomcat/tomcat-juli.jar

# fix without patch yet:
## Required whilst reworking folders
ln -s /var/lib/susemanager /srv/susemanager
## Debian user rights fix
curl https://raw.githubusercontent.com/sbluhm/uyuni/rhnconf-users/python/spacewalk/satellite_tools/repo_plugins/deb_src.py > /usr/lib/python3.9/site-packages/spacewalk/satellite_tools/repo_plugins/deb_src.py
# Log files not created after setup
touch /var/log/rhn/rhn_salt_remote_commands.log
chown tomcat:tomcat /var/log/rhn/rhn_salt_remote_commands.log
touch /var/log/rhn/rhn_web_ui.log
chown tomcat:tomcat /var/log/rhn/rhn_web_ui.log
touch /var/log/rhn/rhn_web_frontend.log
chown tomcat:tomcat /var/log/rhn/rhn_web_frontend.log

# Adding debug info
#sed -i '/log_level_logfile/d' /etc/salt/master.d/logging.conf ||:
#echo "log_level_logfile: trace" >> /etc/salt/master.d/logging.conf
#echo "Java RHN logging in /usr/share/tomcat/webapps/rhn/WEB-INF/classes/log4j2.xml"

