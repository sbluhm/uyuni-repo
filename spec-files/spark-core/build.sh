#!/bin/bash
set -xe
PROJECT_PREFIX=`readlink -e .`
cd src/spark-2.7.2/
$PROJECT_PREFIX/kit/apache-maven-3.3.9/bin/mvn -Dmaven.repo.local=$PROJECT_PREFIX/kit/m2 --settings $PROJECT_PREFIX/kit/m2/settings.xml --strict-checksums -o package -DskipTests=true -Dmaven.javadoc.skip=true -B -V
