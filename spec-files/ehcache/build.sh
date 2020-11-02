#!/bin/bash
set -xe
PROJECT_PREFIX=`readlink -e .`
cd src/ehcache-2.10.1
$PROJECT_PREFIX/kit/apache-maven-3.2.5/bin/mvn -Dmaven.repo.local=$PROJECT_PREFIX/kit/m2 --settings $PROJECT_PREFIX/kit/m2/settings.xml --strict-checksums -o package -DskipTests=true --projects ehcache-core
