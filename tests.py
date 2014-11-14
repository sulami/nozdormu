#!/usr/bin/env python3
# coding: utf-8

import sys
import unittest
from unittest.mock import Mock

import titus.main
from titus.batch import BenchBatch
from titus.loader import BenchLoader
from titus.suite import BenchSuite

class BatchMock(BenchBatch):
    """Serve as a mock to load a batch from a module"""
    def bench_something(self):
        pass

class MainTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_main_bench_running(self):
        with self.assertRaises(SystemExit) as e:
            titus.main.main(module=sys.modules[__name__])
        self.assertEqual(0, e.exception.code)

class LoaderTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_load_from_module(self):
        b = BenchLoader()
        benchs = b.loadFromModule(sys.modules[__name__])
        for b in benchs:
            self.assertEqual(type(b), BenchSuite)

if __name__ == '__main__':
    unittest.main()

