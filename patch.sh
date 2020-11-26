curl https://raw.githubusercontent.com/uyuni-project/uyuni/master/schema/spacewalk/spacewalk-schema-upgrade > /usr/bin/spacewalk-schema-upgrade
curl https://raw.githubusercontent.com/uyuni-project/uyuni/master/spacewalk/setup/bin/spacewalk-setup  > /usr/bin/spacewalk-setup
curl https://raw.githubusercontent.com/uyuni-project/uyuni/master/java/conf/default/rhn_taskomatic_daemon.conf  > /usr/share/rhn/config-defaults/rhn_taskomatic_daemon.conf
curl https://raw.githubusercontent.com/uyuni-project/uyuni/master/spacewalk/setup/share/tomcat.java_opts  > /usr/share/spacewalk/setup/tomcat.java_opts
dnf install glassfish-annotation-api glassfish-jaxb hibernate3
#ln -s /usr/share/java/mchange-commons/mchange-commons-java.jar mchange-commons-java.jar
#ln -s /usr/share/java/slf4j/slf4j-simple.jar slf4j-simple.jar 
