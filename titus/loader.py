from titus.batch import BenchBatch

class BenchLoader:
    """Load a batch of benchmarks and return them"""

    def __init__(self):
        pass

    def loadFromModule(self, module):
        """Get all batches from a module and all benchs from a batch"""
        benchs = []
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and issubclass(obj, BenchBatch):
                benchs.append(self.loadfromBatch(obj))
        return benchs

    def loadFromBatch(self, module):
        isbench = lambda name: name.startswith('bench')
        # self.__benchmarks__ = list(map(Benchmark, list(filter(isvalid, dir(self)))))

