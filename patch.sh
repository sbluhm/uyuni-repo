dnf -y install \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01852572-spacewalk-java/spacewalk-java-4.2.5-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01852572-spacewalk-java/spacewalk-java-config-4.2.5-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01852572-spacewalk-java/spacewalk-taskomatic-4.2.5-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01852646-spacewalk-setup/spacewalk-setup-4.2.3-1.el8.noarch.rpm \
        https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01864414-spacewalk-admin/spacewalk-admin-4.2.2-1.el8.noarch.rpm \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01864472-uyuni-base/uyuni-base-common-4.2.1-1.x86_64.rpm

# java=tomcat libs, java-config=taskomatic conf, taskomatic=taskomatic libs, setup=tomcat conf

# Workaround as http is not working.
chown root:apache /etc/rhn
sed -i 's#http://localhost#https://localhost#' /usr/bin/spacewalk-setup

# Fixes waiting for merge:
