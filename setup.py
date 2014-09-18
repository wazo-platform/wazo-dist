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

from distutils.core import setup


def is_package(path):
    is_test_module = fnmatch.fnmatch(path, '*tests')
    return not is_test_module

packages = [p for p, _, _ in os.walk('xivo_dist') if is_package(p)]


setup(
    name='xivo-dist',
    version='1.0',
    description='XiVO repository sources manager',
    author='Avencall',
    author_email='dev@avencall.com',
    url='https://github.com/xivo-pbx/xivo-dist',
    packages=packages,
    scripts=['bin/xivo-dist'],
)
