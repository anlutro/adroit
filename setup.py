#!/usr/bin/env python

import os
import setuptools

# allow setup.py to be ran from anywhere
os.chdir(os.path.dirname(os.path.abspath(__file__)))

setuptools.setup(
    name="adroit",
    version="0.4",
    license="GPL-3.0",
    description="Ansible Docker Role Testing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Andreas Lutro",
    author_email="anlutro@gmail.com",
    url="https://github.com/anlutro/adroit",
    packages=setuptools.find_packages(include=("adroit", "adroit.*")),
    entry_points={"console_scripts": ["adroit=adroit.cli:main"]},
)
