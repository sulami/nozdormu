from sys import exit
from time import time
from types import FunctionType

from titus.loader import BenchLoader
from titus.runner import BenchRunner

class BenchProgram:
    """This program loads and runs the tests"""

    def __init__(self, module='__main__', benchLoader=BenchLoader,
                 benchRunner=BenchRunner):
        self.benchLoader = benchLoader
        self.benchRunner = benchRunner
        self.module = module
        self.load()
        self.run()

    def load(self):
        loader = self.benchLoader()
        self.bench = loader.loadFromModule(self.module)

    def run(self):
        runner = self.benchRunner()
        self.result = runner.run(self.bench)
        exit(self.result)

main = BenchProgram

