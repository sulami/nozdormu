from sys import exit
from time import time
from types import FunctionType

from titus.loader import BenchLoader
from titus.runner import BenchRunner

class BenchProgram:
    """This program loads and runs the tests"""

    def __init__(self, benchLoader=BenchLoader, benchRunner=BenchRunner):
        self.benchLoader = benchLoader
        self.benchRunner = benchRunner
        self.run()

    def run(self):
        self.result = self.benchRunner.run()
        exit(self.result)

main = BenchProgram

