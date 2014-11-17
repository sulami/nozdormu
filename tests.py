#!/usr/bin/env python3
# coding: utf-8

import sys
import unittest

import nozdormu.main
from nozdormu.batch import BenchBatch
from nozdormu.loader import BenchLoader
from nozdormu.suite import BenchSuite

class BatchMock(BenchBatch):
    """Serve as a mock to load a batch from a module"""
    def bench_something(self):
        pass
    def bench_something_else(self):
        pass

class MainTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_main_bench_running(self):
        nozdormu.main()

class LoaderTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_load_from_module(self):
        b = BenchLoader()
        benchs = b.loadFromModule(sys.modules[__name__])
        for b in benchs.benchs:
            self.assertEqual(type(b), BenchSuite)

if __name__ == '__main__':
    unittest.main()

