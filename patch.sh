#dnf -y install \
#

# Workaround as http is not working.
#sed -i 's#http://localhost#https://localhost#' /usr/bin/spacewalk-setup
sed -i /VirtualHost/d /etc/httpd/conf.d/cobbler.conf

# Fixes waiting for merge:

# reposync workaround until DNF works
#dnf -y install zypper
