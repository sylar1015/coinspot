#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name="pycoinspot",
    version="0.1.0",
    author="Liang.Sun",
    author_email="sylar1015@qq.com",
    description="coinspot api,works for both python2 & python3",
    long_description=open("README.md").read(),
    license="MIT",
    url="https://github.com/sylar1015/coinspot",
    packages=['coinspot'],
    install_requires=[
        "requests",
        ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)