from six import string_types
from sys import exit
from time import time
from types import FunctionType

from nozdormu.loader import BenchLoader
from nozdormu.runner import BenchRunner

class BenchProgram:
    """This program loads and runs the tests"""

    module = None # For testing purposes

    def __init__(self, module='__main__', benchLoader=BenchLoader,
                 benchRunner=BenchRunner):
        self.benchLoader = benchLoader
        self.benchRunner = benchRunner
        if isinstance(module, string_types):
            self.module = __import__(module)
            for part in module.split('.')[1:]:
                self.module = getattr(self.module, part)
        self.load()
        self.run()

    def load(self):
        loader = self.benchLoader()
        self.bench = loader.loadFromModule(self.module)

    def run(self):
        runner = self.benchRunner()
        self.result = runner.run(self.bench)

main = BenchProgram

