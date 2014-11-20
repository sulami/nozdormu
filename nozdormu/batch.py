import gc
import sys

if sys.platform == 'win32':
    from time import clock as time
else:
    from time import time

from nozdormu.util import format_time

class BenchBatch:
    """This class contains benchmark to run"""

    def __init__(self, methodName):
        self.totalTime = 0.0
        self.count = 0
        self.methodName = methodName
        try:
            self.method = getattr(self, self.methodName)
        except:
            raise ImportError('Failed to load {}'.format(self.methodName))

    def __repr__(self):
        return self.methodName

    def run(self):
        """Peform setup/run method/teardown and time it"""
        # Manual GC
        gc.collect()

        # Warm up
        self.setUp()
        self.method()
        self.tearDown()

        # Timed run
        self.setUp()
        start = time()
        self.method()
        self.totalTime += time() - start
        self.tearDown()

        self.count += 1

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def exact(self):
        """Return the raw time per execution"""
        return self.totalTime / self.count

    def results(self):
        """Return human-readable output"""
        return '{} ({} / {} runs)'.format(format_time(self.exact()),
                format_time(self.totalTime), self.count)

