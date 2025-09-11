#! /bin/sh

rm -rf docs/shelf
mkdir docs/shelf
cp docs/shelf-index.md docs/shelf/index.md

pushd ../emscript-content/workspace > /dev/null
emscript-dev markdown -p em.core -o ../../emscript/emscript-docs/docs/shelf
emscript-dev markdown -p ti.cc23xx -o ../../emscript/emscript-docs/docs/shelf
popd > /dev/null
