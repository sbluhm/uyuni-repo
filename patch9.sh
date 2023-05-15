# Fixes waiting for merge:

# Waiting for new python3-urlgrapper release (< 4.1.0-2)
sed -i "1860s#self.fo = open(self.filename, 'r')#self.fo = open(self.filename, 'rb')#" /usr/lib/python3.9/site-packages/urlgrabber/grabber.py

# fix without patch yet:
# Required whilst reworking folders
ln -s /var/lib/susemanager /srv/susemanager

# Adding debug info
#sed -i '/log_level_logfile/d' /etc/salt/master.d/logging.conf ||:
#echo "log_level_logfile: trace" >> /etc/salt/master.d/logging.conf


#Update Java Softlinks for Taskomatik und Tomcat:
ln -s /usr/share/tomcat/bin/tomcat-juli.jar /usr/share/java/tomcat/tomcat-juli.jar


echo "Java RHN logging in /usr/share/tomcat/webapps/rhn/WEB-INF/classes/log4j2.xml"

#Fehlende Logs "Show Tomcat Logs in der Gui bringt sonst einen Fehler"
touch /var/log/rhn/rhn_salt_remote_commands.log
chown tomcat:tomcat /var/log/rhn/rhn_salt_remote_commands.log
touch /var/log/rhn/rhn_web_ui.log
chown tomcat:tomcat /var/log/rhn/rhn_web_ui.log
touch /var/log/rhn/rhn_web_frontend.log
chown tomcat:tomcat /var/log/rhn/rhn_web_frontend.log



#ln -s /var/lib/tftpboot /srv/tftpboot

# New patches. should probably symlink in /usr/share/jar instead of lib folders
#ln -s /usr/share/java/glassfish-jaxb-api.jar /usr/share/tomcat/webapps/rhn/WEB-INF/lib/glassfish-jaxb-api.jar
#ln -s /usr/share/java/glassfish-jaxb-api.jar /usr/share/spacewalk/taskomatic/glassfish-jaxb-api.jar
