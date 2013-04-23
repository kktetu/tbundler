#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

required = []
if sys.version_info >= (2, 7):
    required.append('termcolor')

setup(
        name             = "tbundler",
        version          = "0.0.5",
        description      = "Package Bundler to resolve dependencies",
        author           = 'Daehyub "appframe" KKtetu',
        author_email     = "appframe@gmail.com",
        url              = "http://www.google.co.jp/",
        download_url     = "http://www.google.jp/appframe/tbundler",
        packages         = find_packages(),
        install_requires = required,
        entry_points     = {
            'console_scripts': [
                'tbundler=tbundler.runner:run'
            ]
        },
        classifiers      = [
            "Development Status :: 1 - Planning",
            "Environment :: Web Environment",
            "Framework :: google",
            "License :: Other/Proprietary License",
            "Programming Language :: Python :: 2.7",
            "Topic :: Software Development :: Libraries :: Python Modules"
        ]
)
