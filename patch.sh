dnf -y install \
	https://download.copr.fedorainfracloud.org/results/sbluhm/uyuni-server/epel-8-x86_64/01867280-spacewalk-config/spacewalk-config-4.2.2-1.el8.noarch.rpm

# java=tomcat libs, java-config=taskomatic conf, taskomatic=taskomatic libs, setup=tomcat conf

# Workaround as http is not working.
sed -i 's#http://localhost#https://localhost#' /usr/bin/spacewalk-setup

# Fixes waiting for merge:
