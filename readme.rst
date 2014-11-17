Nozdormu
========

Python benchmarking for humans and dragons.

Features
--------

- Unittest-style benchmark setup (TestCase -> BenchBatch)
- `setUp`/`tearDown` are excluded from timing
- Precise even for very fast benchmarks by running them for at least 1ms
  or 16 times, whichever takes longer
- Timing down to the nanosecond
- Benchmarks in a batch are run interleaved to reduce jitter from random load
- Manual GC to prevent interference with the benchmarks
- Results are saved into a human-readable json file and used as baseline for
  future tests
- Just a few milliseconds overhead

Requirements
------------

- Python 3.2+

Sorry, Python 2 will *not* work, that is just how it is.

Usage example
-------------

.. code:: python
    import nozdormu

    class MyBenchBatch(nozdormu.BenchBatch):
        def bench_one(self):
            pass

        def bench_two(self):
            pass

    class AnActualBenchBatch(nozdormu.BenchBatch):
        def setUp(self):
            import random
            self.r = random

        def bench_list_creation(self):
            l = []
            for i in range(100):
                l.append(i)

        def bench_random_addition(self):
            l = []
            for i in range(100):
                l.append(self.r.randint(0, 100))

        def bench_import_math(self):
            import math

    if __name__ == '__main__':
        nozdormu.main()


yields

::
    Starting benchmark session

      Running Batch: AnActualBenchBatch
        bench_random_addition: 152μs (2ms / 16 runs) (-6μs / 3.6%)
        bench_list_creation: 8μs (1ms / 127 runs) (-85ns / 1.1%)
        bench_import_math: 954ns (1ms / 1049 runs) (new)
      Batch finished, time: 12ms

      Running Batch: MyBenchBatch
        bench_one: 236ns (1ms / 4243 runs) (-13ns / 5.4%)
        bench_two: 232ns (1ms / 4305 runs) (-6ns / 2.7%)
      Batch finished, time: 9ms

    Benchmarking finished
    2 batches, 5 benchmarks
    total time: 23ms

with some Cucumber-inspired colouring if your terminal supports that.

Usage
-----

As you can see above, there are few things for you to do. The general structure
is very similar to unittests. First `import nozdormu`, then subclass
`nozdormu.BenchBatch` as often as you need to. Each batch can hold as many
benchmarks as you need it to.

To get executed, benchmarks have to start with 'bench' (like unittests have to
start with 'test'), and just like in unittests, you can override the class
methods `setUp` and `tearDown` for preparations and/or mocking. Both these
functions are run before and after each benchmark execution and will be
excluded from the benchmark timing (but included in the total time).

Benchmarks that take less than 1ms will be executed repeatedly until they
accumulate at least 1ms of total runtime. This happens on a per-batch basis
and the benchmarks of a batch will rotate until they all ran long enough. This
should reduce jitter from other system load for these extremely fast
benchmarks.

Acknowledgements
----------------

Ideas and inspiration by:

- Python's unittest
- GRB's readygo
- Cucumber

