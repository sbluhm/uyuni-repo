#dnf -y install \
#

# Workaround as http is not working.
sed -i 's#http://localhost#https://localhost#' /usr/bin/spacewalk-setup

# Fixes waiting for merge:
