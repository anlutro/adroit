#!/bin/sh
set -e
root=$(dirname $(readlink -f $0))

adroit -l debug -d debian:stretch -r $root base unbound
adroit -l debug -d centos:7 -r $root base unbound
