#!/usr/bin/env python3
# coding: utf-8

from time import time

class Timer:
    """
    Timer class to use for benchmarking

    Runs the supplied function (or a list/tuple of functions) as many
    as needed until the total time exceeds 1ms. The functions are run
    interleaved (1,2,3,1,2,3,...) to minimize jitter.
    """

    def __init__(self, func):
        self.func = func if type(func) in (list, tuple) else [func]

    def __repr__(self):
        return 'Timer object for {}'.format(self.func)

    def __run__(self):
        self.start = time()
        for i in range(self.counts):
            [f() for f in self.func]
        self.stop = time()

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
        """Print human-readable output"""
        print('{} seconds for {} runs ({} seconds per run)'.format(
              round(self.__timer__(), 3), self.counts,
              round(self.__timer__() / self.counts, 5)))

