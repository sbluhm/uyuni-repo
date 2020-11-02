#!/bin/bash
set -xe
cp -r kit/* /tmp
cd src/hibernate-orm-5.3.7
export GRADLE_USER_HOME=/tmp/gradle
# work around the following error:
# java.lang.reflect.InaccessibleObjectException: Unable to make static com.sun.xml.bind.v2.model.nav.ReflectionNavigator com.sun.xml.bind.v2.model.nav.ReflectionNavigator.getInstance() accessible: module com.sun.xml.bind does not "opens com.sun.xml.bind.v2.model.nav" to unnamed module @66f87784
# sources: https://stackoverflow.com/a/41265267 https://docs.gradle.org/4.8.1/userguide/build_environment.html#sec:configuring_jvm_memory https://docs.gradle.org/4.8.1/userguide/gradle_daemon.html#sec:disabling_the_daemon
export JAVA_OPTS="--add-opens com.sun.xml.bind/com.sun.xml.bind.v2.model.nav=ALL-UNNAMED"
./gradlew --project-cache-dir /tmp/gradle-project --offline -Dorg.gradle.daemon=false clean build -x test -x javadoc -x documentation:aggregateJavadocs -x release:distTar -x release:distZip
