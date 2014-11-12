#!/usr/bin/env python3
# coding: utf-8

from unittest import TestCase, main

from titus import Timer

def a():
    pass

def b():
    pass

class TimingTestCase(TestCase):
    def test_single_function(self):
        t = Timer(a)
        t.run()
        self.assertIn('0.00', t.output()) # This should run fast

    def test_multiple_functions(self):
        t = Timer([a, b]) # List
        t.run()
        self.assertIn('0.00', t.output())

        t = Timer((a, b)) # Tuple
        t.run()
        self.assertIn('0.00', t.output())

    def test_setup_function(self):
        t = Timer(a, setup=b)
        t.run()
        self.assertIn('0.00', t.output())

    def test_exit_function(self):
        t = Timer(a, exit=b)
        t.run()
        self.assertIn('0.00', t.output())

    def test_setup_exit(self):
        t = Timer(a, setup=b, exit=b)
        t.run()
        self.assertIn('0.00', t.output())

if __name__ == '__main__':
    main()

