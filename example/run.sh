#!/bin/sh
set -e
root=$(dirname $(readlink -f $0))

adroit -d debian:stretch -r $root base
adroit -d debian:stretch -r $root fail2ban

adroit -d centos:7 -r $root base
adroit -d centos:7 -r $root fail2ban
