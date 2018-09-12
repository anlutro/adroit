#!/bin/sh
set -e
root=$(dirname $(readlink -f $0))

adroit -l debug -d debian:stretch -r $root base
adroit -l debug -d debian:stretch -r $root fail2ban

adroit -l debug -d centos:7 -r $root base
adroit -l debug -d centos:7 -r $root fail2ban
