# Titus

Python benchmarking for humans.

### Features

* Benchmarking of n functions (n >= 1)
* n setup/teardown functions which are not included in the timing (n >= 0)
* Very precise timing by running functions at least 1ms long
* Reduced jitter by interlacing function run

### Usage example

    from titus import Timer
    
    def func():
        return 1 + 1
    
    t = Timer(func)
    t.run()
    print(t.output())

yields

    0.002 seconds for 1024 runs (0.0 seconds per run)

