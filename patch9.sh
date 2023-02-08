#dnf -y install \

# Fixes waiting for merge:

# Waiting for new python3-urlgrapper release (< 4.1.0-2)
#sed -i "1860s#self.fo = open(self.filename, 'r')#self.fo = open(self.filename, 'rb')#" /usr/lib/python3.9/site-packages/urlgrabber/grabber.py

# fix without patch yet:
# Required whilst reworking folders
ln -s /var/lib/susemanager /srv/susemanager

# not sure if any patches are still required. seems to work without.
#sed -i '/bootloaders_dir/d' /etc/cobbler/settings.yaml ||:
#echo "bootloaders_dir: '/usr/share/syslinux'" >> /etc/cobbler/settings.yaml
#cobbler sync
#/usr/share/cobbler/bin/mkgrub.sh # <-- should be this instead of cobbler sync. Code currently to be refactored and doesnt work anyways so only keeping for reference.
#mkgrub tftp boots result in Failed to load libutil.c32 and menu.c32

# Adding debug info
#sed -i '/log_level_logfile/d' /etc/salt/master.d/logging.conf ||:
#echo "log_level_logfile: trace" >> /etc/salt/master.d/logging.conf

# Random hack waiting to be fixed.
#chmod a+w /var/log/rhn -R

mkdir /usr/share/java/glassfish-jaxb
ln -s /usr/share/java/jaxb/jaxb-runtime.jar /usr/share/java/glassfish-jaxb/jaxb-runtime.jar
ln -s /usr/share/java/jaxb/txw2.jar /usr/share/java/glassfish-jaxb/txw2.jar
ln -s /usr/share/java/jaxb-istack-commons/istack-commons-runtime.jar /usr/share/java/istack-commons-runtime.jar
#mkdir /usr/share/java/byte-buddy
#ln -s /usr/share/java/byte-buddy.jar /usr/share/java/byte-buddy/
ln -sf /usr/share/java/c3p0/c3p0.jar /usr/share/java/hibernate_jdbc_cache.jar



#Update Java Softlinks for Taskomatik und Tomcat:
#mkdir /usr/share/java/glassfish-jaxb
#ln -s  /usr/share/java/jaxb/jaxb-runtime.jar /usr/share/java/glassfish-jaxb/jaxb-core.jar
#ln -s /usr/share/java/jaxb/jaxb-runtime.jar /usr/share/java/glassfish-jaxb/jaxb-runtime.jar
#ln -s /usr/share/java/jaxb/txw2.jar /usr/share/java/glassfish-jaxb/txw2.jar
ln -s /usr/share/tomcat/bin/tomcat-juli.jar /usr/share/java/tomcat/tomcat-juli.jar

ln -s /usr/share/java/istack-commons-runtime.jar /usr/share/spacewalk/taskomatic
ln -s /usr/share/java/istack-commons-runtime.jar /usr/share/tomcat/webapps/rhn/WEB-INF/lib

# Fix postgresql service (Credit Hubert Hoffmann)
ln -s /usr/pgsql-14/bin/initdb /usr/bin/initdb

perl -spi -e 's|/var/lib/pgsql/data|/var/lib/pgsql/14/data|' /usr/share/perl5/vendor_perl/Spacewalk/Setup.pm
perl -spi -e 's|service postgresql |service postgresql-14 |' /usr/share/perl5/vendor_perl/Spacewalk/Setup.pm

perl -spi -e 's|/var/lib/pgsql/data|/var/lib/pgsql/14/data|g' /usr/lib/susemanager/bin/mgr-setup
perl -spi -e 's|systemctl --quiet enable postgresql|systemctl --quiet enable postgresql-14|' /usr/lib/susemanager/bin/mgr-setup
perl -spi -e 's|systemctl start postgresql|systemctl start postgresql-14|' /usr/lib/susemanager/bin/mgr-setup
perl -spi -e 's|systemctl restart postgresql|systemctl restart postgresql-14|' /usr/lib/susemanager/bin/mgr-setup

perl -spi -e 's|systemctl start postgresql|systemctl start postgresql-14|' /usr/bin/uyuni-setup-reportdb
perl -spi -e 's|postgresql-setup initdb|postgresql-14-setup initdb|' /usr/bin/uyuni-setup-reportdb
perl -spi -e 's|systemctl \$1 postgresql|systemctl \$1 postgresql-14|' /usr/bin/uyuni-setup-reportdb
perl -spi -e 's|/var/lib/pgsql/data|/var/lib/pgsql/14/data|' /usr/bin/uyuni-setup-reportdb

perl -spi -e 's|/var/lib/pgsql/data|/var/lib/pgsql/14/data|' /usr/bin/uyuni-sort-pg_hba

perl -spi -e 's|/var/lib/pgsql/data|/var/lib/pgsql/14/data|g' /usr/sbin/spacewalk-startup-helper
perl -spi -e 's|/var/lib/pgsql/data|/var/lib/pgsql/14/data|g' /usr/sbin/spacewalk-service



echo "Java RHN logging in /usr/share/tomcat/webapps/rhn/WEB-INF/classes/"
rm -f /usr/share/tomcat/webapps/rhn/WEB-INF/lib/glassfish-jaxb_jaxb-core.jar

#es kommt zu einer Java Exception mit Version 2.9.0
#mv /usr/share/java/google-gson /usr/share/java/google-gson.bak
#cp -frp google-gson /usr/share/java/
dnf -y install https://download.opensuse.org/distribution/openSUSE-stable/repo/oss/noarch/google-gson-2.8.5-3.2.6.noarch.rpm
rm -f /usr/share/tomcat/webapps/rhn/WEB-INF/lib/google-gson_google-gsongson-extras.jar

#Das Packet wird bei der Installation nicht installiert, daher manuel nachgeliefert
dnf -y install python3-websockify

#Es kommt sonst zu Java Exceptions
rpm -e woodstox-core-6.2.3-17.51.noarch --nodeps
dnf -y install woodstox

#Fehlende Logs "Show Tomcat Logs in der Gui bringt sonst einen Fehler"
touch /var/log/rhn/rhn_salt_remote_commands.log
chown tomcat:tomcat /var/log/rhn/rhn_salt_remote_commands.log
touch /var/log/rhn/rhn_web_ui.log
chown tomcat:tomcat /var/log/rhn/rhn_web_ui.log
touch /var/log/rhn/rhn_web_frontend.log
chown tomcat:tomcat /var/log/rhn/rhn_web_frontend.log

