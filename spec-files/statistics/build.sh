#!/bin/bash
set -xe
PROJECT_PREFIX=`readlink -e .`
cd src/statistics-1.0.2
$PROJECT_PREFIX/kit/apache-maven-3.2.5/bin/mvn -Dmaven.repo.local=$PROJECT_PREFIX/kit/m2 --settings $PROJECT_PREFIX/kit/m2/settings.xml --strict-checksums -o package
