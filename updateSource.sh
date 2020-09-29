#!/bin/bash
topdir=$(pwd)
version=1.6.0
rm -rf pytorch-${version}
git clone --recursive https://github.com/pytorch/pytorch pytorch-${version}
cd pytorch-${version}
git checkout v${version}
git submodule sync
git submodule update --init --recursive
rm -rf .git
cd ${topdir}
tar -cjf pytorch-${version}-include-submodules.tar.bz2 pytorch-${version}
