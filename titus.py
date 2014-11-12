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

    def __init__(self, func, setup=None, teardown=None):
        det = lambda f: (f if type(f) in (list, tuple)
                           else [f] if type(f) is FunctionType
                           else None)
        self.func = det(func)
        self.setup = det(setup)
        self.teardown = det(teardown)

    def __repr__(self):
        return 'Timer object for {}'.format(self.func)

    def __run__(self):
        """Actually run functions and time them"""
        if self.setup:
            [f() for f in self.setup]
        self.start = time()
        for i in range(self.counts):
            [f() for f in self.func]
        self.stop = time()
        if self.teardown:
            [f() for f in self.teardown]

    def __timer__(self):
        """Calculate the time needed"""
        return self.stop - self.start

    def run(self):
        """Run the benchmark until it takes long enough"""
        self.counts = 1
        self.__run__()
        while self.__timer__() < 0.001:
            self.counts *= 2
            self.__run__()

    def output(self):
        """Return human-readable output"""
        return ('{} seconds for {} runs ({} seconds per run)'.format(
                round(self.__timer__(), 3), self.counts,
                round(self.__timer__() / self.counts, 5)))

