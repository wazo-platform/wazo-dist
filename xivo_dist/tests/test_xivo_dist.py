# -*- coding: utf-8 -*-

# Copyright 2014-2018 The Wazo Authors  (see the AUTHORS file)
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

    def test_generate_sources(self):
        host = 'mirror.example.org'
        path = '/foobar/'
        distribution = 'xivo-five'

        sources = xivo_dist.generate_sources(distribution, host, path)

        self._assert_sources(sources, 'http://mirror.example.org/foobar/', distribution)

    def test_given_named_distribution_when_distribution_is_archive_then_false(self):
        distribution = 'xivo-dev'

        is_archive = xivo_dist.distribution_is_archive(distribution)

        self.assertFalse(is_archive)

    def test_given_unnamed_distribution_when_distribution_is_archive_then_true(self):
        distribution = 'xivo-ftw'

        is_archive = xivo_dist.distribution_is_archive(distribution)

        self.assertTrue(is_archive)

    def test_given_main_repo_when_determine_path_then_debian(self):
        path = xivo_dist.determine_path('some-distro', '/some-path/', main_repo=True, archive_repo=False)

        self.assertEqual(path, '/debian/')

    def test_given_archive_repo_when_determine_path_then_archive(self):
        path = xivo_dist.determine_path('some-distro', '/some-path/', main_repo=False, archive_repo=True)

        self.assertEqual(path, '/archive/')

    def test_given_custom_path_when_determine_path_then_custom(self):
        path = xivo_dist.determine_path('some-distro', '/some-path/', main_repo=False, archive_repo=False)

        self.assertEqual(path, '/some-path/')

    def test_given_named_distribution_when_determine_path_then_debian(self):
        path = xivo_dist.determine_path('phoenix', custom_path=None, main_repo=False, archive_repo=False)

        self.assertEqual(path, '/debian/')

    def test_given_unnamed_distribution_when_determine_path_then_archive(self):
        path = xivo_dist.determine_path('some-distro', custom_path=None, main_repo=False, archive_repo=False)

        self.assertEqual(path, '/archive/')

    def _assert_sources(self, sources, mirror_uri, distribution):
        expected_sources = textwrap.dedent("""
            # {distrib}
            deb {mirror_uri} {distrib} main
            # deb-src {mirror_uri} {distrib} main
        """).format(mirror_uri=mirror_uri, distrib=distribution)

        return self.assertEqual(sources, expected_sources)
