#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014-2016 The Wazo Authors  (see the AUTHORS file)
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

import argparse

DEFAULT_HOST = 'mirror.wazo.community'
SOURCE_LIST_PATH = '/etc/apt/sources.list.d/xivo-dist.list'
NAMED_DISTRIBUTIONS = ['xivo-five', 'xivo-dev', 'xivo-rc', 'wazo-dev', 'wazo-rc', 'phoenix']
DEB_SOURCE_CONTENT = """
# {distrib}
deb http://{host}{path} {distrib} main
# deb-src http://{host}{path} {distrib} main
"""


def main():
    args = parse_args()
    distribution_sources = generate_sources(args.distribution, args.host, args.path)
    write_source_list(distribution_sources)


def parse_args():
    parser = argparse.ArgumentParser('xivo-dist')
    parser.add_argument('--host', default=DEFAULT_HOST)
    parser.add_argument('--path')
    parser.add_argument('distribution', help='switch sources to given distribution')

    return parser.parse_args()


def write_source_list(distribution_sources):
    fh = open(SOURCE_LIST_PATH, 'w')
    fh.write(distribution_sources)
    fh.close()


def generate_sources(distribution, host, path):
    if path is None:
        if distribution_is_archive(distribution):
            path = '/archive/'
        else:
            path = '/debian/'

    deb_source = DEB_SOURCE_CONTENT.format(host=host, path=path, distrib=distribution)

    return deb_source


def distribution_is_archive(distribution):
    if distribution in NAMED_DISTRIBUTIONS:
        return False
    return True


if __name__ == "__main__":
    main()
