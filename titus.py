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

    def __init__(self):
        self.__total__ = 0.0
        self.__load__()

    def __repr__(self):
        return 'Timer object for {}'.format(self.func)

    def __run__(self):
        """Actually run functions and time them"""
        for i in range(self.counts):
            self.setUp()
            start = time()
            for b in self.__benchmarks__:
                print(b) # TODO call the functions
            self.__total__ += time() - start
            self.tearDown()

    def __load__(self):
        isvalid = lambda attr: attr.startswith('bench')
        self.__benchmarks__ = list(filter(isvalid, dir(self)))

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        """Run the benchmark until it takes long enough"""
        self.counts = 1
        self.__run__()
        while self.__total__ < 0.001:
            self.__total__ = 0.0
            self.counts *= 2
            self.__run__()

    def exact(self):
        """Return the raw time per execution"""
        return self.__total__ / self.counts

    def results(self):
        """Return human-readable output"""
        return ('{} seconds for {} runs ({} milliseconds per run)'.format(
                round(self.__total__, 3), self.counts,
                round(self.exact() * 1000, 5)))

