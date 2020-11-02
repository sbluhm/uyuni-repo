#!/bin/bash
set -xe
PROJECT_PREFIX=`readlink -e .`
cp -r kit/* /tmp
cd src/ical4j-ical4j-3.0.18
export GRADLE_USER_HOME=/tmp/gradle
./gradlew --offline --project-cache-dir /tmp/gradle-project clean build -x test -x javadoc