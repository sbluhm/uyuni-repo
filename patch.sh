dnf -y install \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01852212-spacewalk-java/spacewalk-java-4.2.5-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01852212-spacewalk-java/spacewalk-java-config-4.2.5-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01851669-uyuni-base/uyuni-base-common-4.2.2-1.x86_64.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01851669-uyuni-base/uyuni-base-server-4.2.2-1.x86_64.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01851668-spacewalk-admin/spacewalk-admin-4.2.2-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01851667-perl-Satcon/perl-Satcon-4.2.1-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01852268-spacewalk-setup/spacewalk-setup-4.2.3-1.el8.noarch.rpm

chown :apache /etc/rhn

# Tomcat/rhn
ln -s /usr/share/java/jaxb-api.jar /var/lib/tomcat/webapps/rhn/WEB-INF/lib/jaxb-api.jar
ln -s /usr/share/java/istack-commons/istack-commons-runtime.jar /var/lib/tomcat/webapps/rhn/WEB-INF/lib/istack-commons-runtime.jar
ln -s /usr/share/java/glassfish-jaxb/jaxb-runtime.jar /var/lib/tomcat/webapps/rhn/WEB-INF/lib/jaxb-runtime.jar
ln -s /usr/share/java/glassfish-jaxb/jaxb-core.jar /var/lib/tomcat/webapps/rhn/WEB-INF/lib/jaxb-core.jar
ln -s /usr/share/java/glassfish-jaxb/txw2.jar /var/lib/tomcat/webapps/rhn/WEB-INF/lib/txw2.jar

# Taskomatic
ln -s /usr/share/java/jaxb-api.jar /usr/share/spacewalk/taskomatic/jaxb-api.jar
ln -s /usr/share/java/istack-commons/istack-commons-runtime.jar /usr/share/spacewalk/taskomatic/istack-commons-runtime.jar
ln -s /usr/share/java/glassfish-jaxb/jaxb-runtime.jar /usr/share/spacewalk/taskomatic/jaxb-runtime.jar
ln -s /usr/share/java/glassfish-jaxb/jaxb-core.jar /usr/share/spacewalk/taskomatic/jaxb-core.jar

# Search
#no jaxb required.

# Workaround as http is not working.
sed -i 's#http://localhost#https://localhost#' /usr/bin/spacewalk-setup
