# Nozdormu

Python benchmarking for humans and dragons.

### Features

* Unittest-style benchmark setup (TestCase -> BenchBatch)
* `setUp`/`tearDown` are excluded from timing
* Precise even for very fast benchmarks by running them for at least 1ms
  or 16 times, whichever takes longer
* Benchmarks in a batch are run interleaved to reduce jitter from random load
* Uses manual GC to prevent it from interfering with the benchmarks
* Saves results into json file to use as baseline for future runs and compares
  the results automatically

### Requirements

* Python 3.2+

### Usage example

```python
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

```

yields

```
Starting benchmark session

  Running Batch: AnActualBenchBatch
    bench_random_addition: 0.15365ms (0.002s / 16 runs) (-0.010ms / 6.4%)
    bench_list_creation: 0.00779ms (0.001s / 129 runs) (-0.001ms / 1.0%)
    bench_import_math: 0.00105ms (0.001s / 954 runs) (-0.000ms / 1.7%)
  Batch finished, time: 0.01s

  Running Batch: MyBenchBatch
    bench_one: 0.00026ms (0.001s / 3897 runs) (new)
    bench_two: 0.00026ms (0.001s / 3900 runs) (new)
  Batch finished, time: 0.01s

Benchmarking finished
2 batches, 5 benchmarks
total time: 0.02s
```

with some Cucumber-inspired colouring if your terminal supports that.

### Usage

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

### Acknowledgements

Ideas and inspiration by:

* Python's unittest
* GRB's readygo
* Cucumber

