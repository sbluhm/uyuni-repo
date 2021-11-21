dnf provides \
	apache-commons-daemon \
	apache-commons-el \
	apache-commons-fileupload \
	apache-commons-validator \
	apache-portlet-1_0-api \
	dom4j \
	geronimo-jta \
	icu4j \
	jakarta-commons-discovery \
	jaxen \
	joda-convert \
	joda-time \
	maven-javadoc-plugin \
	mod_wsgi \
	openslp-server \
	protobuf-java \
	python-certifi \
	python-futures \
	python-m2crypto \
	python-zmq \
	python2-msgpack \
	python2-pycurl \
	python2-simplejson \
	python2-singledispatch \
	python2-tornado \
	python2-typing \
	"python3-psycopg2 >= 2.8.4" \
	"python3-pyyaml >= 5.1" \
	servletapi4 \
	servletapi5 \
	"tomcat > 1" \
	unix2_chkpwd \


echo "icu4j - Enabling the module can cause requirement conflicts with other modules so this package is provided separately. Build only requirement for nutch-core."
echo "jaxen - Build required by velocity-tools. Stock jaxen does not seem to work."
