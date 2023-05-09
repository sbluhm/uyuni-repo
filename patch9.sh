#dnf -y install \

# Fixes waiting for merge:

# Waiting for new python3-urlgrapper release (< 4.1.0-2)
sed -i "1860s#self.fo = open(self.filename, 'r')#self.fo = open(self.filename, 'rb')#" /usr/lib/python3.9/site-packages/urlgrabber/grabber.py

# fix without patch yet:
# Required whilst reworking folders
ln -s /var/lib/susemanager /srv/susemanager

# Adding debug info
#sed -i '/log_level_logfile/d' /etc/salt/master.d/logging.conf ||:
#echo "log_level_logfile: trace" >> /etc/salt/master.d/logging.conf

# Random hack waiting to be fixed.
#chmod a+w /var/log/rhn -R

#ln -sf /usr/share/java/c3p0/c3p0.jar /usr/share/java/hibernate_jdbc_cache.jar



#Update Java Softlinks for Taskomatik und Tomcat:
ln -s /usr/share/tomcat/bin/tomcat-juli.jar /usr/share/java/tomcat/tomcat-juli.jar


echo "Java RHN logging in /usr/share/tomcat/webapps/rhn/WEB-INF/classes/"

#es kommt zu einer Java Exception mit Version 2.9.0
#mv /usr/share/java/google-gson /usr/share/java/google-gson.bak
#cp -frp google-gson /usr/share/java/
#dnf -y install https://download.opensuse.org/distribution/openSUSE-stable/repo/oss/noarch/google-gson-2.8.5-3.2.6.noarch.rpm
#rm -f /usr/share/tomcat/webapps/rhn/WEB-INF/lib/google-gson_google-gsongson-extras.jar

#PR6961
dnf -y install python3-websockify


#Fehlende Logs "Show Tomcat Logs in der Gui bringt sonst einen Fehler"
touch /var/log/rhn/rhn_salt_remote_commands.log
chown tomcat:tomcat /var/log/rhn/rhn_salt_remote_commands.log
touch /var/log/rhn/rhn_web_ui.log
chown tomcat:tomcat /var/log/rhn/rhn_web_ui.log
touch /var/log/rhn/rhn_web_frontend.log
chown tomcat:tomcat /var/log/rhn/rhn_web_frontend.log



ln -s /var/lib/tftpboot /srv/tftpboot

# New patches. should probably symlink in /usr/share/jar instead of lib folders
#rm -f /usr/share/tomcat/webapps/rhn/WEB-INF/lib/google-gson_google-gsongson-codegen.jar
ln -s /usr/share/java/glassfish-jaxb-api.jar /usr/share/tomcat/webapps/rhn/WEB-INF/lib/glassfish-jaxb-api.jar
ln -s /usr/share/java/glassfish-jaxb-api.jar /usr/share/spacewalk/taskomatic/glassfish-jaxb-api.jar
