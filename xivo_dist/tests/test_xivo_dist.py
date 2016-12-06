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

import textwrap
import unittest
from xivo_dist import xivo_dist


class TestXivoDist(unittest.TestCase):

    def setUp(self):
        self.host = 'mirror.wazo.community'
        self.path = None

    def test_given_prod_distribution_when_generate_sources_then_prod_debian_source(self):
        distribution = 'xivo-five'

        sources = xivo_dist.generate_sources(distribution, self.host, self.path)

        self._assert_sources(sources, 'http://mirror.wazo.community/debian/', distribution)

    def test_given_unnamed_distribution_when_generate_sources_then_archive_source(self):
        distribution = 'xivo-forever'

        sources = xivo_dist.generate_sources(distribution, self.host, self.path)

        self._assert_sources(sources, 'http://mirror.wazo.community/archive/', distribution)

    def test_generate_sources_explicit_path(self):
        self.path = '/foobar/'
        distribution = 'xivo-five'

        sources = xivo_dist.generate_sources(distribution, self.host, self.path)

        self._assert_sources(sources, 'http://mirror.wazo.community/foobar/', distribution)

    def test_generate_sources_explicit_host(self):
        self.host = 'mirror.example.org'
        distribution = 'xivo-five'

        sources = xivo_dist.generate_sources(distribution, self.host, self.path)

        self._assert_sources(sources, 'http://mirror.example.org/debian/', distribution)

    def test_given_named_distribution_when_distribution_is_archive_then_false(self):
        distribution = 'xivo-dev'

        is_archive = xivo_dist.distribution_is_archive(distribution)

        self.assertFalse(is_archive)

    def test_given_unnamed_distribution_when_distribution_is_archive_then_true(self):
        distribution = 'xivo-ftw'

        is_archive = xivo_dist.distribution_is_archive(distribution)

        self.assertTrue(is_archive)

    def _assert_sources(self, sources, mirror_uri, distribution):
        expected_sources = textwrap.dedent("""
            # {distrib}
            deb {mirror_uri} {distrib} main
            # deb-src {mirror_uri} {distrib} main
        """).format(mirror_uri=mirror_uri, distrib=distribution)

        return self.assertEqual(sources, expected_sources)
