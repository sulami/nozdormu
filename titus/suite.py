class BenchSuite:
    """A suite that houses benchmarks"""

    def __init__(self, benchs=()):
        self.benchs = benchs

    def __repr__(self):
        return 'BenchSuite: '+ str(self.benchs)

