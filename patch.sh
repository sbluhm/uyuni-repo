dnf -y install \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01852572-spacewalk-java/spacewalk-java-4.2.5-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01852572-spacewalk-java/spacewalk-java-config-4.2.5-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01852572-spacewalk-java/spacewalk-taskomatic-4.2.5-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01851669-uyuni-base/uyuni-base-common-4.2.2-1.x86_64.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01851669-uyuni-base/uyuni-base-server-4.2.2-1.x86_64.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01851668-spacewalk-admin/spacewalk-admin-4.2.2-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01851667-perl-Satcon/perl-Satcon-4.2.1-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01852268-spacewalk-setup/spacewalk-setup-4.2.3-1.el8.noarch.rpm

chown :apache /etc/rhn


# Workaround as http is not working.
sed -i 's#http://localhost#https://localhost#' /usr/bin/spacewalk-setup

# Fix waiting for merge:
sed -i 's/--add-modules java.annotation,com.sun.xml.bind//' /usr/share/spacewalk/setup/tomcat.java_opts 
sed -i 's/--add-modules java.annotation,com.sun.xml.bind//' /etc/sysconfig/tomcat
