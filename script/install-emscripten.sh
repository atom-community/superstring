#!/usr/bin/env bash

set -e

EMSCRIPTEN_DOWNLOAD_URL='https://codeload.github.com/emscripten-core/emsdk/tar.gz/1.39.16'
EMSDK_PATH="./emsdk-1.39.16/emsdk"

if [ ! -f $EMSDK_PATH ]; then
  echo 'Downloading emscripten SDK installer...'
  curl $EMSCRIPTEN_DOWNLOAD_URL | tar xz
fi

echo 'Installing emscripten SDK...'

$EMSDK_PATH update
$EMSDK_PATH list --old
$EMSDK_PATH install emscripten-1.37.9
$EMSDK_PATH activate emscripten-1.37.9
