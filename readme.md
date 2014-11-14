# Titus

Python benchmarking for humans.

### Features

* Benchmarking of n functions (n >= 1)
* n setup/teardown functions which are not included in the timing (n >= 0)
* Very precise timing by running functions at least 1ms long
* Reduced jitter by interlacing function run

### Usage example

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

yields

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

with some Cucumber-inpsired colouring if your terminal supports that.

