#!/usr/bin/env python3
# coding: utf-8

import unittest
from unittest.mock import Mock

import titus.main

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.runner = Mock()
        self.runner.run = Mock(return_value=False)

    def test_main(self):
        try:
            titus.main.main(benchRunner=self.runner)
        except SystemExit:
            # main exits with return code
            pass

if __name__ == '__main__':
    unittest.main()

