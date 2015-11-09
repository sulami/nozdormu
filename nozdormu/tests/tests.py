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
    def output(self, arg):
        pass # be silent

class MainTestCase(unittest.TestCase):
    def test_main_bench_running(self):
        nozdormu.main(benchRunner=SilentRunner)

class LoaderTestCase(unittest.TestCase):
    def test_load_from_module(self):
        b = BenchLoader()
        benchs = b.loadFromModule(sys.modules[__name__])
        for b in benchs.benchs:
            self.assertEqual(b.__class__, BenchSuite)

class BatchTestCase(unittest.TestCase):
    def setUp(self):
        b = BenchLoader()
        self.benchs = b.loadFromModule(sys.modules[__name__])

    def test_min_runtime(self):
        r = SilentRunner()
        r.run(self.benchs)
        results = r.results
        self.assertTrue(r.results) # Make sure the array is not empty.
        batch = results[0]
        self.assertEqual(batch['batch'], 'BatchMock')
        for b in batch['results']:
            self.assertTrue(b['runs'] >= 16)
            self.assertTrue(b['time'] * b['runs'] >= 0.001)

class UtilTestCase(unittest.TestCase):
    def setUp(self):
        from nozdormu.util import format_time
        self.f = format_time

    def test_format_time(self):
        self.assertEqual(self.f(1.3e-8), '13ns')
        self.assertEqual(self.f(1.3e-5), '13μs')
        self.assertEqual(self.f(1.3e-2), '13ms')
        self.assertEqual(self.f(0.3), '300ms')
        self.assertEqual(self.f(1.3), '1s')

if __name__ == '__main__':
    unittest.main()

