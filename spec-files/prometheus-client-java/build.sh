#!/bin/bash
set -xe
PROJECT_PREFIX=`readlink -e .`
cd src/client_java-parent-0.3.0
$PROJECT_PREFIX/kit/apache-maven-3.3.9/bin/mvn -Dmaven.repo.local=$PROJECT_PREFIX/kit/m2 --settings $PROJECT_PREFIX/kit/m2/settings.xml --strict-checksums -o --projects simpleclient,simpleclient_common,simpleclient_hotspot,simpleclient_servlet,simpleclient_hibernate,simpleclient_httpserver install
