#!/usr/bin/env bash

# suggestion from: 
# https://gist.github.com/slavafomin/08670ec0c0e75b500edbaa5d43a5c93c

git pull "$@" &&
  git submodule sync --recursive &&
  git submodule update --init --recursive