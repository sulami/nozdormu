#!/usr/bin/env python3
# coding: utf-8

from time import time
from types import FunctionType

class Timer:
    """
    Timer class to use for benchmarking

    Runs the supplied function (or a list/tuple of functions) as many
    as needed until the total time exceeds 1ms. The functions are run
    interleaved (1,2,3,1,2,3,...) to minimize jitter.

    Optionally supllied setup and teardown function(s/lists/tuples) are
    run without timing.
    """

    def __init__(self, func, setUp=None, tearDown=None):
        det = lambda f: (f if type(f) in (list, tuple)
                           else [f] if type(f) is FunctionType
                           else None)
        self.func = det(func)
        self.setUp = det(setUp)
        self.tearDown = det(tearDown)
        self.total = 0.0

    def __repr__(self):
        return 'Timer object for {}'.format(self.func)

    def __run__(self):
        """Actually run functions and time them"""
        for i in range(self.counts):
            if self.setUp:
                [f() for f in self.setUp]
            start = time()
            [f() for f in self.func]
            self.total += time() - start
            if self.tearDown:
                [f() for f in self.tearDown]

    def run(self):
        """Run the benchmark until it takes long enough"""
        self.counts = 1
        self.__run__()
        while self.total < 0.001:
            self.total = 0.0
            self.counts *= 2
            self.__run__()

    def output(self):
        """Return human-readable output"""
        return ('{} seconds for {} runs ({} seconds per run)'.format(
                round(self.total, 3), self.counts,
                round(self.total / self.counts, 5)))

