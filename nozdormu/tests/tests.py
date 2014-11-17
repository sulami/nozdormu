#!/usr/bin/env python3
# coding: utf-8

import sys
import unittest

import nozdormu.main
from nozdormu.batch import BenchBatch
from nozdormu.loader import BenchLoader
from nozdormu.suite import BenchSuite
from nozdormu.runner import BenchRunner

class BatchMock(BenchBatch):
    """Serve as a mock to load a batch from a module"""
    def bench_something(self):
        pass
    def bench_something_else(self):
        pass

class SilentRunner(BenchRunner):
    def output(self, str):
        pass # be silent

class MainTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_main_bench_running(self):
        nozdormu.main(benchRunner=SilentRunner)

class LoaderTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_load_from_module(self):
        b = BenchLoader()
        benchs = b.loadFromModule(sys.modules[__name__])
        for b in benchs.benchs:
            self.assertEqual(type(b), BenchSuite)

class UtilTestCase(unittest.TestCase):
    def setUp(self):
        from nozdormu.util import format_time
        self.f = format_time

    def test_format_time(self):
        self.assertEqual(self.f(1.3e-8), '13ns')
        self.assertEqual(self.f(1.3e-5), '13μs')
        self.assertEqual(self.f(1.3e-2), '13ms')

if __name__ == '__main__':
    unittest.main()

