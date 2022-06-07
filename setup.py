# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="universal-packages",
    version="0.0.2",
    description="CLI tool to sync brew <-> deb packages. It creates intermediate representation for both package managers",
    license="MIT",
    author="Jacke",
    packages=find_packages(),
    install_requires=["click==8.1.3; python_version >= '3.7'", 'commonmark==0.9.1', "pygments==2.12.0; python_version >= '3.6'", 'pyyaml==6.0', 'rich==12.4.4', 'typer==0.4.1'



],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
    ]
)