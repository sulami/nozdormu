#!/usr/bin/env python3
# coding: utf-8

from unittest import TestCase, main

from titus import Timer

class TimingTestCase(TestCase):
    def test_emtpy(self):
        class Toast(Timer):
            pass

        t = Toast()
        t.run()
        self.assertIn('0.00', t.results()) # This should run fast

    def test_simple(self):
        class Toast(Timer):
            def bench_blub(self):
                print('blub')

        t = Toast()
        t.run()
        self.assertIn('0.00', t.results()) # This should run fast

if __name__ == '__main__':
    main()

