class BenchRunner:
    """The standard runner for a BenchSuite"""

    def run(self, suite):
        """Run the tests and return success status"""
        for batch in suite:
            for bench in batch:
                bench.run()
                print(str(bench), bench.results())
        return 0

