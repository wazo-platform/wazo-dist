#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import fnmatch
import os

from setuptools import setup
from setuptools import find_packages


setup(
    name='xivo-dist',
    version='1.0',
    description='XiVO repository sources manager',
    author='Avencall',
    author_email='dev@avencall.com',
    url='https://github.com/wazo-pbx/xivo-dist',
    packages=find_packages(),
    scripts=['bin/xivo-dist'],
)
