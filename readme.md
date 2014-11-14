# Titus

Python benchmarking for humans.

### Features

* Unittest-style benchmark setup (TestCase -> BenchBatch)
* `setUp`/`tearDown` are excluded from timing
* Precise even for very fast benchmarks by running them for at least 1ms
* Benchmarks in a batch are run interleaved to reduce jitter

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

with some Cucumber-inpsired colouring if your terminal supports that.

