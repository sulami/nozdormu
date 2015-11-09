import sys

if sys.version_info.major == 2:
    from types import ClassType as batchType
else:
    batchType = type

from nozdormu.batch import BenchBatch
from nozdormu.suite import BenchSuite

class BenchLoader:
    """Load a batch of benchmarks and return them"""

    def __init__(self, benchSuite=BenchSuite):
        self.suiteClass = benchSuite

    def loadFromModule(self, module):
        """Get all batches from a module and all benchs from a batch"""
        benchs = []
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, batchType) and issubclass(obj, BenchBatch):
                benchs.append(self.loadFromBatch(obj))
        return self.suiteClass(benchs)

    def loadFromBatch(self, batch):
        """Get all benchs from a batch and return a loaded suite"""
        isbench = lambda name: name.startswith('bench')
        benchNames = list(filter(isbench, dir(batch)))
        suite = self.suiteClass(map(batch, benchNames))
        suite.batch=batch
        return suite

