for package in \
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
	openslp \
	protobuf \
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
	python3-psycopg2 \
	python3-pyyaml \
	servletapi4 \
	servletapi5 \
	tomcat \
	unix2_chkpwd \
	; do
	if [ `dnf list $package | grep $package | wc -l` == 1 ]; then echo $package;beep;fi;done

