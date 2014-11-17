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

class MyOtherBenchBatch(nozdormu.BenchBatch):
    def bench_three(self):
        from time import sleep
        sleep(.1)

if __name__ == '__main__':
    nozdormu.main()
```

yields

```
Starting benchmark session

  Running Batch: MyBenchBatch
    bench_two: 0.00073ms (0.001s / 1375 runs) (new)
    bench_one: 0.00072ms (0.001s / 1388 runs) (-0.0ms)
  Batch finished, time: 1.6s

  Running Batch: MyOtherBenchBatch
    bench_three: 100.18411ms (1.603s / 16 runs) (+0.039ms)
  Batch finished, time: 1.64s

Benchmarking finished
2 batches, 3 benchmarks
total time: 3.23s
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

