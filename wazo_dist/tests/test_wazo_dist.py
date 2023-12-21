# Copyright 2014-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import textwrap
import unittest

from wazo_dist import main as wazo_dist


class TestXivoDist(unittest.TestCase):
    def test_generate_sources(self):
        host = 'mirror.example.org'
        path = '/foobar/'
        distribution = 'xivo-five'

        sources = wazo_dist.generate_sources(distribution, host, path)

        self._assert_sources(sources, 'http://mirror.example.org/foobar/', distribution)

    def test_given_named_distribution_when_distribution_is_archive_then_false(self):
        distribution = 'xivo-dev'

        is_archive = wazo_dist.distribution_is_archive(distribution)

        self.assertFalse(is_archive)

    def test_given_unnamed_distribution_when_distribution_is_archive_then_true(self):
        distribution = 'xivo-ftw'

        is_archive = wazo_dist.distribution_is_archive(distribution)

        self.assertTrue(is_archive)

    def test_given_main_repo_when_determine_path_then_debian(self):
        path = wazo_dist.determine_path(
            'some-distro', '/some-path/', main_repo=True, archive_repo=False
        )

        self.assertEqual(path, '/debian/')

    def test_given_archive_repo_when_determine_path_then_archive(self):
        path = wazo_dist.determine_path(
            'some-distro', '/some-path/', main_repo=False, archive_repo=True
        )

        self.assertEqual(path, '/archive/')

    def test_given_custom_path_when_determine_path_then_custom(self):
        path = wazo_dist.determine_path(
            'some-distro', '/some-path/', main_repo=False, archive_repo=False
        )

        self.assertEqual(path, '/some-path/')

    def test_given_named_distribution_when_determine_path_then_debian(self):
        path = wazo_dist.determine_path(
            'phoenix', custom_path=None, main_repo=False, archive_repo=False
        )

        self.assertEqual(path, '/debian/')

    def test_given_unnamed_distribution_when_determine_path_then_archive(self):
        path = wazo_dist.determine_path(
            'some-distro', custom_path=None, main_repo=False, archive_repo=False
        )

        self.assertEqual(path, '/archive/')

    def _assert_sources(self, sources, mirror_uri, distribution):
        expected_sources = textwrap.dedent(
            """
            # {distrib}
            deb {mirror_uri} {distrib} main
            # deb-src {mirror_uri} {distrib} main
        """
        ).format(mirror_uri=mirror_uri, distrib=distribution)

        return self.assertEqual(sources, expected_sources)
