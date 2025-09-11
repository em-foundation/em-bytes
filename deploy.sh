#! /bin/sh

VERS=$(cat VERSION-*)
VERS_FULL=$(echo VERSION-*)

release_repo() {
    git add --all
    git commit -a -m 'RELEASE'
    git tag $VERS_FULL
    git push
    git push --tags
}

pushd build/docs
release_repo
popd
release_repo
