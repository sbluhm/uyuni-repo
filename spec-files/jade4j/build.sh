#!/bin/bash
set -xe
PROJECT_PREFIX=`readlink -e .`
cd src/jade4j-1.0.7
alias mvn='$PROJECT_PREFIX/kit/apache-maven-3.2.5/bin/mvn -Dmaven.repo.local=$PROJECT_PREFIX/kit/m2 --settings $PROJECT_PREFIX/kit/m2/settings.xml --strict-checksums -o'
# Some unit tests would fail otherwise
export LANG=en_US.UTF-8
mvn package
