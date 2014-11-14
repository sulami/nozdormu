class BenchRunner:
    """The standard runner for a BenchSuite"""

    def run(self, suite):
        """
        Run the tests interleaved until all tests are finished, runs
        them grouped by batch (1-1, 1-2, 1-1, 1-2, ..., 2-1, 2-2, ...)
        """
        for batch in suite:
            benchsRunning = [b for b in batch]
            while len(benchsRunning) >= 1:
                for bench in benchsRunning:
                    if bench.totalTime < 0.001:
                        bench.count += 1
                        bench.run()
                    else:
                        benchsRunning.remove(bench)
                        print(str(bench), bench.results())

