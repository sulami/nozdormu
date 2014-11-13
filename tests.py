#!/usr/bin/env python3
# coding: utf-8

from unittest import TestCase, main

from titus import Timer

class TimingTestCase(TestCase):
    def test_simple_test(self):
        class Toast(Timer):
            pass

        t = Toast()
        t.run()
        self.assertIn('0.00', t.results()) # This should run fast

if __name__ == '__main__':
    main()

