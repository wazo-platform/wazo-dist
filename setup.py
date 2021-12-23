#!/usr/bin/env python3
# Copyright 2014-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup
from setuptools import find_packages

setup(
    name='wazo-dist',
    version='1.0',
    description='Wazo repository sources manager',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'wazo-dist = wazo_dist.main:main',
        ],
    },
)
