#!/bin/bash

tag=$(sed -n 's/^Version:\s\(.*\)$/\1/p' ./*.spec | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
url=https://github.com/babel/babel/
subpackage=$(sed -n 's/^.global packagename\s\(.*\)$/\1/p' ./*.spec | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')

echo "*** Working on [$subpackage] version [$tag] *** "

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    echo Cleaning up...
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)

pushd "$tmp"
git clone $url
cd babel
subdir=packages/${subpackage}
if [ -d "${subdir}/test" ]; then
  git archive --prefix='test/' --format=tar refs/tags/v${tag}:${subdir}/test/ \
      |  bzip2 > "$pwd"/${subpackage}-tests-${tag}.tar.bz2
elif [ -d "${subdir}/tests" ]; then
  git archive --prefix='tests/' --format=tar refs/tags/v${tag}:${subdir}/tests/ \
      |  bzip2 > "$pwd"/${subpackage}-tests-${tag}.tar.bz2
else
  echo "No test directory found for tag ${gittag}"
fi
if [ -d "${subdir}/src" ]; then
  git archive --prefix='src/' --format=tar refs/tags/v${tag}:${subdir}/src/ \
      | bzip2 > "$pwd"/${subpackage}-src-${tag}.tar.bz2
fi
if [ -d "${subdir}/scripts" ]; then
  git archive --prefix='scripts/' --format=tar refs/tags/v${tag}:${subdir}/scripts/ \
      | bzip2 > "$pwd"/${subpackage}-scripts-${tag}.tar.bz2
fi
popd
