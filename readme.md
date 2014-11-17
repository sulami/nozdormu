# Nozdormu

Python benchmarking for humans and dragons.

### Features

* Unittest-style benchmark setup (TestCase -> BenchBatch)
* `setUp`/`tearDown` are excluded from timing
* Precise even for very fast benchmarks by running them for at least 1ms
* Benchmarks in a batch are run interleaved to reduce jitter
* Saves results into json file to use as baseline for future runs

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
        pass

if __name__ == '__main__':
    nozdormu.main()
```

yields

```
Starting benchmark session

  Running Batch: MyBenchBatch
    bench_one: 0.00024ms (0.01s / 40839 runs) (new)
    bench_two: 0.00024ms (0.01s / 41834 runs) (-0.0ms)
  Batch finished, time: 0.09s

  Running Batch: MyOtherBenchBatch
    bench_three: 0.1s (+0.014ms)
  Batch finished, time: 0.1s

Benchmarking finished
2 batches, 3 benchmarks
total time: 0.19s
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

