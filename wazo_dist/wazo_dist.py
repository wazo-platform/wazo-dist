#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014-2019 The Wazo Authors  (see the AUTHORS file)
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
SOURCE_LIST_PATH = '/etc/apt/sources.list.d/wazo-dist.list'
NAMED_DISTRIBUTIONS = [
    'xivo-five',
    'xivo-dev',
    'xivo-rc',
    'wazo-dev',
    'wazo-rc',
    'phoenix',
    'wazo-dev-stretch',
    'wazo-rc-stretch',
    'phoenix-stretch',
    'pelican-stretch',
]
DEB_SOURCE_CONTENT = """
# {distrib}
deb http://{host}{path} {distrib} main
# deb-src http://{host}{path} {distrib} main
"""


def main():
    args = parse_args()
    path = determine_path(args.distribution, args.path, args.archive_repo, args.main_repo)
    distribution_sources = generate_sources(args.distribution, args.host, path)
    write_source_list(distribution_sources)


def parse_args():
    parser = argparse.ArgumentParser('wazo-dist')
    parser.add_argument('--host', default=DEFAULT_HOST)

    group = parser.add_mutually_exclusive_group()
    parser.add_argument('--path')
    group.add_argument('-a', '--archive-repo', action='store_true', help='Use archive repository')
    group.add_argument('-m', '--main-repo', action='store_true', help='Use main repository')

    parser.add_argument('distribution', help='Switch sources to given distribution')

    return parser.parse_args()


def write_source_list(distribution_sources):
    with open(SOURCE_LIST_PATH, 'w') as source_file:
        source_file.write(distribution_sources)


def generate_sources(distribution, host, path):
    deb_source = DEB_SOURCE_CONTENT.format(host=host, path=path, distrib=distribution)

    return deb_source


def determine_path(distribution, custom_path, archive_repo, main_repo):
    if main_repo:
        return '/debian/'
    if archive_repo:
        return '/archive/'
    if custom_path:
        return custom_path
    if distribution_is_archive(distribution):
        return '/archive/'

    return '/debian/'


def distribution_is_archive(distribution):
    if distribution in NAMED_DISTRIBUTIONS:
        return False
    return True


if __name__ == "__main__":
    main()
