#!/usr/bin/env python3
# coding: utf-8

import unittest
from unittest.mock import Mock

import titus.main

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.runner = Mock()
        self.runner.run = Mock(return_value=0)
        self.loader = Mock()

    def test_main_bench_running(self):
        with self.assertRaises(SystemExit) as e:
            titus.main.main(benchLoader=self.loader, benchRunner=self.runner)
        self.assertEqual(0, e.exception.code)

class LoaderTestCase(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()

