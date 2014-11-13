#!/usr/bin/env python3
# coding: utf-8

from sys import exit
from time import time
from types import FunctionType

from loader import BenchLoader
from runner import BenchRunner

class BenchProgram:
    """This program loads and runs the tests"""

    def __init__(self, benchLoader=BenchLoader, benchRunner=BenchRunner):
        self.benchLoader = benchLoader()
        self.benchRunner = benchRunner()
        self.runBenchs()

    def runBenchs(self):
        result = self.benchRunner.run()
        exit(result)

main = BenchProgram

if __name__ == '__main__':
    main()

