#!/bin/bash
set -xe
PROJECT_PREFIX=`readlink -e .`
cd src/pgjdbc-ng-0.8.3
alias ant='$PROJECT_PREFIX/kit/apache-ant-1.9.7/bin/ant'
alias mvn='$PROJECT_PREFIX/kit/apache-maven-3.3.9/bin/mvn -Dmaven.repo.local=$PROJECT_PREFIX/kit/m2 --settings $PROJECT_PREFIX/kit/m2/settings.xml --strict-checksums -o'
alias gradlew='./gradlew --gradle-user-home=$PROJECT_PREFIX/kit/gradle-home --offline'
gradlew assemble
