# Titus

Python benchmarking for humans.

### Features

* Unittest-style benchmark setup (TestCase -> BenchBatch)
* `setUp`/`tearDown` are excluded from timing
* Precise even for very fast benchmarks by running them for at least 1ms
* Benchmarks in a batch are run interleaved to reduce jitter


### Requirements

* Python 3.2+
* `six`

### Usage example

```python
import titus

class MyBenchBatch(titus.BenchBatch):
    def bench_one(self):
        pass

    def bench_two(self):
        pass

class MyOtherBenchBatch(titus.BenchBatch):
    def bench_three(self):
        pass

if __name__ == '__main__':
    titus.main()
```

yields

```
Starting benchmark session

  Running Batch: MyBenchBatch
    bench_one: 0.001 seconds for 3026 runs (0.00033 milliseconds per run)
    bench_two: 0.001 seconds for 3027 runs (0.00033 milliseconds per run)
  Batch finished, time: 0.01s

  Running Batch: MyOtherBenchBatch
    bench_three: 0.001 seconds for 3173 runs (0.00032 milliseconds per run)
  Batch finished, time: 0.01s

Benchmarking finished
2 batches, 3 benchmarks
total time: 0.01s
```

with some Cucumber-inspired colouring if your terminal supports that.

### Usage

As you can see above, there are few things for you to do. The general structure
is very similar to unittests. First `import titus`, then subclass
`titus.BenchBatch` as often as you need to. Each batch can hold as many
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

